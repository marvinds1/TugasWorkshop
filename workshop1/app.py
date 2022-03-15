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
    return render_template('home.html', computers=rv)

@app.route('/simpan',methods=["POST"])
def simpan():
    link = request.form['linkfoto']
    nama = request.form['nama']
    harga = request.form['harga']
    beli = request.form['beli']
    berat = request.form['berat']
    desc = request.form['deskripsi']
    rate = request.form['rating']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO product_details VALUES (NULL, now(), %s,%s,%s,%s,%s,%s,%s)",(link,nama,harga,beli,berat,desc,rate,))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    nama = request.form['nama']
    harga = request.form['harga']
    berat = request.form['berat']
    desc = request.form['desc']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE product_details SET product_name=%s, price=%s, weight=%s, description=%s WHERE num=%s", (nama,harga,berat,desc,id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM product_details WHERE product_name=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/details', methods=["POST"])
def details():
    id_data = request.form['id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT product_details WHERE product_name=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)