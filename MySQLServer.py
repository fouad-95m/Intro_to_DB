import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish connection to MySQL server (replace user, password, and host accordingly)
        connection = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost'  # or use '127.0.0.1'
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Incorrect username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Close cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
