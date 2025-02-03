import psycopg2
from urllib.parse import urlparse

connection_string = "postgresql://erik_user:vJnjEibIrqr3BkvAwmjcZdbUiFi4oXfK@dpg-ctuh0f8gph6c73eqljrg-a.oregon-postgres.render.com/erik"


# Parse the connection string
url = urlparse(connection_string)

# Extract components
db_config = {
    "host": url.hostname,
    "port": url.port,
    "database": url.path[1:],  # Skip the leading "/"
    "user": url.username,
    "password": url.password,
}

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Example: Test the connection
    cursor.execute("SELECT version();")
    print("PostgreSQL version:", cursor.fetchone())

except psycopg2.Error as e:
    print("Error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()