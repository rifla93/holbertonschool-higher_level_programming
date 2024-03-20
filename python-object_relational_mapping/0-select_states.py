import MySQLdb

def get_states(username, password, db_name):
    try:
        # Establish a connection to the MySQL server
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name)

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Execute the query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

        # Close the cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    username = "your_mysql_username"
    password = "your_mysql_password"
    db_name = "hbtn_0e_0_usa"

    get_states(username, password, db_name)
