from flask_jwt_extended import JWTManager as JWT
from flask_jwt_extended import (
    get_jwt,
    get_jwt_identity,
    create_access_token,
    set_access_cookies,
)
from flask import Flask
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from datetime import timedelta, datetime, timezone
import os
import bcrypt
from infrastructure.config import Config
from infrastructure.database.user_database import UserDatabase


class TokenManager:
    def __init__(self, app: Flask):
        self.app: Flask = app
        self.__set_app_configurations()
        self.connection = mysql.connector.connect(
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            host=Config.MYSQL_HOST,
            port=Config.MYSQL_PORT,
        )
        self.__init_db()
        jwt: JWT = JWT(app)
        self.jwt: JWT = jwt

        # called when a protected endpoint is accessed
        @jwt.token_in_blocklist_loader
        def check_if_token_is_revoked(_jwt_header: dict, jwt_payload: dict) -> bool:
            jti: str = jwt_payload["jti"]
            token_in_redis: tuple = self.__get_token_from_blocklist(jti)
            return token_in_redis is not None

        @jwt.user_identity_loader
        def user_identity_loader(user: dict) -> str:
            id: str = user["id"]
            username: str = user["username"]
            password: str = user["password"]
            return f"{id}:{username}:{password}"

        @jwt.user_lookup_loader
        def user_identity_loader(_jwt_header: dict, jwt_data: dict) -> dict | None:
            identity: str = jwt_data["sub"]
            id, username, password = identity.split(":")
            if id is None or username is None or password is None:
                return None
            user_database: UserDatabase = UserDatabase()
            user_id: int = user_database.get_user_id(username)
            if user_id is None or user_id != int(id):
                return None
            encrypted_user_password: str = user_database.get_user_password(username)
            if encrypted_user_password is None or not bcrypt.checkpw(
                password.encode("utf-8"), encrypted_user_password.encode("utf-8")
            ):
                return None
            return id

        @app.after_request
        def refresh_expiring_jwts(response):
            try:
                expiration_time = get_jwt()["exp"]
                now = datetime.now(timezone.utc)
                target_timestamp = datetime.timestamp(now + timedelta(minutes=20))
                if target_timestamp > expiration_time:
                    access_token = create_access_token(identity=get_jwt_identity())
                    set_access_cookies(response, access_token)
                return response
            except (RuntimeError, KeyError):
                return response

    def __set_app_configurations(self) -> None:
        self.app.config["SECRET_KEY"] = os.environ.get(
            "FLASK_SECRET_KEY", "supersekrit"
        )
        self.app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    def __init_db(self) -> None:
        cursor: MySQLCursor = self.connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.TOKEN_DB}")
        cursor.execute(f"USE {Config.TOKEN_DB}")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS token_blocklist (token VARCHAR(255) PRIMARY KEY, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        )
        cursor.close()
        self.connection.commit()
        return

    def __get_token_from_blocklist(self, token: str) -> tuple | None:
        cursor: MySQLCursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM token_blocklist WHERE token = '{token}'")
        token_in_blocklist = cursor.fetchone()
        cursor.close()
        return token_in_blocklist

    def add_token_to_blocklist(self, token: str) -> None:
        self.__removed_expired_tokens()
        cursor: MySQLCursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO token_blocklist (token) VALUES ('{token}')")
        cursor.close()
        self.connection.commit()
        return

    def __removed_expired_tokens(self) -> None:
        expiration_time: timedelta = self.app.config["JWT_ACCESS_TOKEN_EXPIRES"]
        expiration_time_in_seconds: float = expiration_time.total_seconds()
        interval: str = f"INTERVAL {expiration_time_in_seconds} SECOND"
        cursor = self.connection.cursor()
        cursor.execute(
            f"DELETE FROM token_blocklist WHERE created_at < NOW() - {interval}"
        )
        cursor.close()
        self.connection.commit()
        return
