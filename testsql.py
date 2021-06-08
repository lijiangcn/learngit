import sqlite3

conn=sqlite3.connect('test.db')
print('open database successfully')
cursor=conn.cursor()
cursor.execute("CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR(50),SALARY REAL);")
cursor.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(1,'PAUL',32,'TEXAS',15000.00);")
cursor.execute("INSERT INTO COMPANY VALUES(2,'ALLEN',25,'NORWAY',20000.00);")
cursor.execute("SELECT * FROM COMPANY;")

results=cursor.fetchall()
for row in results:
    print(row)

cursor.close()
conn.commit()
conn.close()


