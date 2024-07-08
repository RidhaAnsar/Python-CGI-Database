#!C:\xampp\htdocs\sample\newDb\venv\Scripts\python.exe

import cgi
import cgitb
import MySQLdb

cgitb.enable()
try:
    myDb = MySQLdb.connect(host="localhost",user="root",password="",db="test")
    myCursor = myDb.cursor()

    form = cgi.FieldStorage()
    id = form.getvalue('id')
    name = form.getvalue('name')

    sql = "INSERT INTO user VALUES(%s,%s)"
    myCursor.execute(sql,(id,name))
    myDb.commit()
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
                    <h1>SUCCESS</h1>
                    <a href='index.html'>back</a>
                </body>
                </html>''')
except Exception as e:
    print(e)
finally:
    myDb.close()

