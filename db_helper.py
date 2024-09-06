import mysql.connector
# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="food_restaurant"
)

def insert_order_item(food_item, quantity, order_id):
    try:
        cursor = connection.cursor()

        # Calling the stored procedure
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))

        # Committing the changes
        connection.commit()

        # Closing the cursor
        cursor.close()

        print("Order item inserted successfully!")
        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")
        # Rollback changes if necessary
        connection.rollback()
        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback changes if necessary
        connection.rollback()
        return -1

def get_total_order_price(order_id):
     cursor = connection.cursor()

     # Executing the SQL query to get the total order price

     query = f"SELECT get_total_order_price({order_id})"
     cursor.execute(query)

     # Fetching the result
     result = cursor.fetchone()[0]

     # closing the cursor
     cursor.close()

     return result

def get_next_order_id():
     
     cursor = connection.cursor()

     # Executing the SQL query to get next available order_id

     query = "Select MAX(order_id) from orders"
     cursor.execute(query)

     ## fetching the result
     result = cursor.fetchone()[0]

     # closing the cursor

     cursor.close()

     # Returning the next available order_id

     if result is None:
          return 1
     else:
          return result + 1
     

def insert_order_tracking(order_id, status):
     cursor = connection.cursor()

     ## Inserting the record into the order-tracking table
     insert_query = "INSERT INTO order_tracking(order_id, status) VALUES (%s, %s)"
     cursor.execute(insert_query, (order_id, status))

     connection.commit()

     cursor.close()


    




def get_order_status(order_id: int):
        
        
        
        cursor = connection.cursor()

        # Execute SQL query to select status based on order_id
        query = ("SELECT status FROM order_tracking WHERE order_id = %s")
        cursor.execute(query, (order_id,))

        # Fetch the status
        status = cursor.fetchone()
        print("Status from database:", status)  # Debug print
        if status is not None:
            print("Status:", status[0])
        else:
            print("No status found for order ID:", order_id)
        cursor.close()

        if status is not None:
            return status[0]
        else:
            return None

    
            
            


