import mysql.connector

def execute_query(query, fetch=True):
    """
    Connects to MySQL, executes a query, and fetches results if needed.

    :param query: SQL query to execute.
    :param fetch: Set to True to fetch results (for SELECT queries).
    :return: Query result if fetch=True, else None.
    """
    try:
        # Connect to MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="Customer"
        )
        mycursor = mydb.cursor()

        # Execute query
        mycursor.execute(query)

        # Fetch results if needed
        if fetch:
            result = mycursor.fetchall()
        else:
            mydb.commit()  # Commit for INSERT/UPDATE/DELETE
            result = None

        # Close connection
        mycursor.close()
        mydb.close()

        return result

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def showalldata():
    customers = execute_query("SELECT * FROM CUST")
    for customer in customers:
        print(customer)


def insertdata():
    insert_query = "INSERT INTO CUST (id, name) VALUES (3, 'John Doe')"
    execute_query(insert_query, fetch=False)
    print("Record inserted successfully!")


def update_data():
    update_query = "UPDATE CUST SET name='Jane Doe' WHERE id=3"
    execute_query(update_query, fetch=False)
    print("Record updated successfully!")

def deletedata(id):
    delete_query = "DELETE FROM CUST WHERE id="+str(id)
    execute_query(delete_query, fetch=False)
    print("Record deleted successfully!")

