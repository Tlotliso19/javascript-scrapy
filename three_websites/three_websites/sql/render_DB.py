import psycopg2
import os

SUPABASE_URL = 'postgresql://postgres.ltxefuhyxlyhezlvdned:tlotliso101@aws-0-eu-west-2.pooler.supabase.com:6543/postgres'
connection_string = SUPABASE_URL

def connection_DB(connection_string):
    try:
        conn = psycopg2.connect(connection_string)
        print("✅ Connected")
        return conn, conn.cursor()
    except psycopg2.Error as e:
        print("❌ Connection Error:", e)
        return None, None

def clean_up(connection_string):
    print("🔧 Running clean_up()")
    conn, cursor = connection_DB(connection_string)
    if cursor:
        try:
            cursor.execute("SELECT tablename FROM pg_tables WHERE schemaname = 'public';")
            tables = cursor.fetchall()
            for table in tables:
                cursor.execute(f'DROP TABLE IF EXISTS "{table[0]}" CASCADE;')
                print(f"Dropped: {table[0]}")
            conn.commit()
        except Exception as e:
            print("❌ Error dropping tables:", e)
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    clean_up(connection_string)
    print("✅ done done done")


