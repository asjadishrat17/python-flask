import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", db="shop")
mycursor = mydb.cursor()


@app.route('/', methods=['GET', 'POST'])
def index():
    #mydb = mysql.connector.connect(host="localhost", user="root", passwd="",db="shop")
    #mycursor = mydb.cursor()
    #mycursor.execute("select * from shop")
    #result = mycursor.fetchall()

    #for row in result:
     #   print(row)
    return render_template('home.html')

@app.route('/about')
def about():
     return render_template('about.html')

@app.route('/web/<string:insert>')
def add(insert):
    #mycursor.execute('''insert into shop (user_name,password) values(%s,'1234');''',(insert))
    #mycursor.execute('''insert into shop (user_name,password) values(insert,insert''')
    password=1234
    query = ('INSERT INTO shop'
             '(user_name, password)'
             'VALUES (%s, %s)')
    value = (insert, password)
    mycursor.execute(query, value)

    #mysql.connection.commit;
    mydb.commit()
    mycursor.close()
    mydb.close()
    return render_template('about.html')

if __name__=='__main__': 
    app.run(debug=True)