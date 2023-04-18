# Add your database informations
class Config:
    MYSQL_HOST: str = 'localhost'
    MYSQL_USER: str = 'root'
    MYSQL_PASSWORD: str = '0'
    MYSQL_DB: str = 'GLO2005_TP'
    MYSQL_PORT: int = 3306
    DATABASE_COMMANDS_FILE: str = 'infrastructure/commandes.sql'
    TOKEN_DB: str = 'GLO2005_TP_TOKENS'
