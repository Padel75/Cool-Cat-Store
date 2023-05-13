# Add your database informations
class Config:
    MYSQL_HOST: str = ''
    MYSQL_USER: str = ''
    MYSQL_PASSWORD: str = ''
    MYSQL_DB: str = ''
    MYSQL_PORT: int = 0
    DATABASE_COMMANDS_FILE: str = 'infrastructure/commandes.sql'
    TOKEN_DB: str = 'GLO2005_TP_TOKENS'
