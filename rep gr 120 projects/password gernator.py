import random
import sqlite3


#db
conn =sqlite3.connect('personal_p_db.db')
c= conn.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS data (input text primary key, attached_sting TEXT)''')
def save_data(input_data,attached_sting):
  try:
    c.execute('INSERT INFO data VALUES (?, ?)',(input_data,attached_sting))
    conn.commit()
    print("Data saved successfully!")
  except sqlite3.Error as e:
    print("Error saveing data",e)
def get_attached_sting(input_data):
  try:
    c.execute('Select attached_string From Data Where input = ?',(input_data))
    result=c.fetchone()
    if result:
      return result[0]  
    else:
      return "No attached sting found"
  except sqlite3.Error as e:
    print("Error retriveing data:",e)

#example use case 
save_data("input 1","attached string 1")
save_data("input 1","attached sting 2 ")

print(get_attached_sting("input 1"))


'''
# geration 
charater_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtstuvwxyz1234567890!@#$%^&*()[];:,.<>?"

#for i 
'''