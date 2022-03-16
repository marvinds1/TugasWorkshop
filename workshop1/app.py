from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'workshop1'
mysql = MySQL(app)

app.secret_key = 'abcdefghijklmnopqrstuvwxyz'


@app.route('/')
@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/logout')
def logout():
    session['loggedin'] = False
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        if cursor.execute(' SELECT * FROM user_accounts WHERE username=%s or password=%s ', (username, password)):
            if cursor.execute(' SELECT * FROM user_accounts WHERE username=%s and password=%s ', (username, password)):
                account = cursor.fetchone()
                session['loggedin'] = True
                session['id'] = account[0]
                session['name'] = account[1]
                session['username'] = account[3]
                return redirect('/home1')
            elif cursor.execute(' SELECT * FROM user_accounts WHERE username=%s ', (username,)):
                return render_template('login.html', msg="Wrong password", username=username)
            else:
                return render_template('login.html', msg="Wrong password and username", username=username)
        else:
            return render_template('login.html', msg="Wrong password and username", username=username)
    else:
        return render_template('login.html')


@app.route('/home1')
def home1():
    if session['loggedin']:
        return redirect('/home')
    else:
        return f"Please login in"


@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product_details ORDER BY dates DESC LIMIT 10")
    rv = cur.fetchall()
    cur.close()
    return render_template('home.html', data=rv)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        alamat = request.form['alamat']
        nohp = request.form['nohp']
        birthdate = request.form['birthdate']
        password = request.form['password']
        cur = mysql.connection.cursor()
        if cur.execute(" SELECT * FROM user_accounts WHERE Email=%s or Username=%s ", (email, username)):
            if cur.execute(" SELECT * FROM user_accounts WHERE Email=%s and Username=%s ", (email, username)):
                return render_template('register.html', msg="Email and Username already taken", name=name)
            elif cur.execute(" SELECT * FROM user_accounts WHERE email=%s ", (email,)):
                return render_template('register.html', msg="Email already registered,try another email", name=name, username=username)
            elif cur.execute(" SELECT * FROM user_accounts WHERE username=%s ", (username,)):
                return render_template('register.html', msg="Username already exists,try another username", name=name, email=email)
        else:
            cur.execute(" INSERT INTO user_accounts (Name,Username,Email,Alamat,NoHP,Birthdate,Password,registration_date) VALUES(%s,%s,%s,%s,%s,%s,%s,now()) ",
                        (name, username, email, alamat, nohp, birthdate, password))
        mysql.connection.commit()
        return render_template('login.html')
    else:
        return render_template('register.html')


@app.route('/forget password', methods=['POST', 'GET'])
def forget_password():
    return render_template('forget_password.html')


"""@app.route('/simpan', methods=["POST"])
def simpan():
    link = request.form['linkfoto']
    nama = request.form['nama']
    harga = request.form['harga']
    beli = request.form['beli']
    berat = request.form['berat']
    desc = request.form['deskripsi']
    rate = request.form['rating']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO product_details VALUES (NULL, now(), %s,%s,%s,%s,%s,%s,%s)",
                (link, nama, harga, beli, berat, desc, rate,))
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
    cur.execute("UPDATE product_details SET product_name=%s, price=%s, weight=%s, description=%s WHERE num=%s",
                (nama, harga, berat, desc, id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))


@app.route('/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM product_details WHERE product_name=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))


@app.route('/details/<string:id_data>', methods=["GET"])
def details(id_data):
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM product_details WHERE product_name=%s", (id_data,))
    det = cur.fetchall()
    return render_template('details.html', det=det)
"""

if __name__ == '__main__':
    app.run(debug=True)
