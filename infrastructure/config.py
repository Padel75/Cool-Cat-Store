# Add your database informations
class Config:
    MYSQL_HOST: str = 'localhost'
    MYSQL_USER: str = 'root'
    MYSQL_PASSWORD: str = 'MDP'
    MYSQL_DB: str = 'GLO2005_TP'
    MYSQL_PORT: int = 1433
    DATABASE_COMMANDS_FILE: str = '../infrastructure/commandes.sql'