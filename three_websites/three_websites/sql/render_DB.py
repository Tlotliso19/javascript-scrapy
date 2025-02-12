import psycopg2
from urllib.parse import urlparse
import os

connection_string ="postgresql://postgres:BSwtGv4AvaKvoYJD@quarterly-prominent-seagull.data-1.use1.tembo.io:5432/postgres"
#= os.getenv("DATABASE_URL")


import psycopg2

def connection_DB(connection_string):
    """ Connects to PostgreSQL and returns (conn, cursor) """
    try:
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()
        return conn, cursor
    except psycopg2.Error as e:
        print("Error:", e)
        return None, None

def clean_up(connection_string):
    """ Drops all tables in the public schema """
    conn, cursor = connection_DB(connection_string)

    if cursor:
        try:
            # Fetch all table names
            cursor.execute("""
                SELECT tablename FROM pg_tables 
                WHERE schemaname = 'public'
            """)
            tables = cursor.fetchall()  # Fetch all table names
            table_list = [table[0] for table in tables]  # Convert to a list
            
            # Drop each table safely
            for table in table_list:
                cursor.execute(f'DROP TABLE IF EXISTS "{table}" CASCADE;')

            conn.commit()  # Commit the transaction
            print("All tables dropped successfully.")

        except psycopg2.Error as e:
            print("Error:", e)
            conn.rollback()  # Rollback in case of an error
        
        finally:
            cursor.close()
            conn.close()

# Example usage

clean_up(connection_string)

print('done done done')


