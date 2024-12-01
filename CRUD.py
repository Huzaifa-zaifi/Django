import psycopg2
import os
from tabulate import tabulate

# Creating connection with database
conn = psycopg2.connect(
    database = 'Python',
    host = 'localhost',
    user = 'postgres',
    password = 'root',
    port = 5454
)
cur = conn.cursor()

inp = 0
while(True):
    print("Welcome to my CRUD application. Choose from following options")
    print("1: ADD\n2: Show\n3: Update\n4: Delete\n5: Exit\n")
    inp = int(input("Your choice: "))
    os.system("cls")
    # Adding the record
    if(inp == 1):
        id = int(input("Enter your id: "))
        name = input("Enter student name: ")
        marks = int(input("Enter your marks: "))
        cur.execute("INSERT INTO data (\"id\",\"name\", \"marks\") VALUES (%s,%s, %s)", (id,name, marks))
        conn.commit()
        print("Student has been added")

    # Showing all the records stored in database
    elif(inp == 2):
        cur.execute("Select * from data")
        d = cur.fetchall()
        
        r= []
        for i in d:
            record = [
                [i[0],i[1],i[2]]               
                
            ]
            r = r + record
            
        head = ["Id","Name","Marks"]
        print(tabulate(r, headers=head, tablefmt="grid"))
        
    # Updating the record
    elif(inp == 3):
        uid = int(input("Enter the id you want to update: "))
        n = input("Enter updated name: ")
        m = int(input("Enter updated marks: "))
        cur.execute("Update data set \"name\" = %s, \"marks\" = %s where \"id\" = %s",(n,m,uid))
        conn.commit()
        print("Successfully Updated")
    
    # Deleting the record
    elif(inp == 4):
        dname = int(input("Enter the id you want to delete: "))
        cur.execute("Delete from data where \"id\" = %s",(dname,))
        conn.commit()
        print(f"Deleted user with id: {dname}")
    elif(inp > 4 or inp < 1):
        break



# We are using 'os' module to clear screen after every choice and 'tabulate' to visualize all record in table format