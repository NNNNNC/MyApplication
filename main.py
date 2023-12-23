




from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] == 'localhost'
app.config['MYSQL_USER'] == 'root'
app.config['MYSQL_PASSWORD'] == '09102001nico'
app.config['MYSQL_DB'] == 'mydb'

mysql = MySQL(app)


@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("select * from customers")
    customers = cur.fetchall()

    return render_template('index.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True)
