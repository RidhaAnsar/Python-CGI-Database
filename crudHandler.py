#!C:\xampp\htdocs\sample\newDb\venv\Scripts\python.exe

import cgi
import cgitb
import MySQLdb

cgitb.enable()
try:
    myDb = MySQLdb.connect(host="localhost",user="root",password="",db="test")
    myCursor = myDb.cursor()

    form = cgi.FieldStorage()
    item = form.getvalue('item')
    quantity = form.getvalue('quantity')
   
    sql = "INSERT INTO items (name,qnt)VALUES(%s,%s)"
    myCursor.execute(sql,(item,quantity))
    myDb.commit()

    read = "SELECT * FROM items"
    myCursor.execute(read)
    rows = myCursor.fetchall()
    print("Content-type:text/html")
    print()
    print('''<!DOCTYPE html>
            <html lang='en'>
                <head>
                    <meta charset='UTF-8'>
                    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                    <title>Success</title>
                </head>
                <body>
            ''')
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}<br>")

    print('''
              <a href='crud.html'>back</a>
            </body>
            </html>''')


except Exception as e:
    print(e)
finally:
    myDb.close()

