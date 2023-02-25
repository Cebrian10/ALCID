import pyodbc

class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    debug = True  
    server = 'ALDAIR'
    database = 'proy_flask'
    username = 'Cebrian10'
    password = 'lizmariham507'

    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            f'SERVER={server};'
                            f'DATABASE={database};'
                            f'UID={username};'
                            f'PWD={password}')

config={
    'development':DevelopmentConfig
}