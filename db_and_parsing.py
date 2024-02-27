import psycopg2

def create_database_table(connection, nameDB):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS {nameDB} (
                    ID SERIAL PRIMARY KEY,
                    Data_length INTEGER,
                    Length INTEGER,
                    Name VARCHAR(255),
                    RusName VARCHAR(255),
                    Scalling VARCHAR(255),
                    Range VARCHAR(255),
                    SPN VARCHAR(255)
                )
            """)
        connection.commit()
        print("Table created successfully!")
    except Exception as ex:
        print("[INFO] Error while creating table:", ex)

def data_for_podkluchenie_k_bd(host, nameDB, login, password):
    connection = None
    try:
        connection = psycopg2.connect(host=host, user=login, password=password, database=nameDB, options="-c client_encoding=latin1")
        create_database_table(connection)
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION();")
            db_version = cursor.fetchone()
            print("Database version:", db_version)
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL:", ex)
    finally:
        if connection:
            connection.close()

# Пример использования функции
#data_for_podkluchenie_k_bd("your_host", "your_database_name", "your_username", "your_password")

