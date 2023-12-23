




from flask import Flask, render_template, request, redirect, url_for
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
    cur.close()
    return render_template('index.html', customers=customers)

@app.route("/add", methods=['POST'])
def add():
    if request.method == 'POST':
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        email = request.form['email']
        phone_number = request.form['phone_number']
        town_city = request.form['town_city']
        country = request.form['country']
        cur = mysql.connection.cursor()
        cur.execute("insert into customers (first_name,middle_name,last_name,gender,email,phone_number,town_city,country) values (%s,%s,%s,%s,%s,%s,%s,%s)", (first_name,middle_name,last_name,gender,email,phone_number,town_city,country))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
