import pymysql

# Function to create a MySQL database connection
def create_connection():
    try:
        # Create a connection to the MySQL database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='password',
            database='cs518',
            port=3306
        )
        print('Connected to MySQL database')
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL database: {e}")
        raise e

# Example usage
# connection = create_connection()
