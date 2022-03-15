from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'workshop1'
mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product_details ORDER BY dates DESC LIMIT 10")
    rv = cur.fetchall()
    cur.close()
    return render_template('home.html', data=rv)

@app.route('/details/<string:id_data>', methods=["GET"])
def details(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product_details WHERE product_name=%s", (id_data,))
    det = cur.fetchall()
    return render_template('details.html', det=det)

if __name__ == '__main__':
    app.run(debug=True)