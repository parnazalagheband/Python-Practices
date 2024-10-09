import sqlite3
conn=sqlite3.connect("database.db")
my_cursor =conn.cursor()
   
id=int(input("Pleae enter id: "))
name=input("Please enter  name: ")
mobile_number=input("Please enter  mobile_number: ")
phone_number=input("Please enter phone_number: ")
email=input("Please enter email: ")
my_cursor.execute(f"INSERT INTO persons(id, name, phone_number, mobile_number, email) VALUES({id}, '{name}', '{phone_number}', '{mobile_number}','{email}' )")
conn.commit()
conn.close()



    
    
id2=int(input("Enter the id you want to delete: "))
my_cursor.execute("DELETE FROM persons WHERE id ==2")
conn.commit()
conn.close()