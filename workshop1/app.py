from flask import (Flask, render_template, request, redirect, session, url_for) 
from flask_mysqldb import MySQL
import math
from geopy.geocoders import Nominatim
import geopy.distance

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'workshop1'
mysql = MySQL(app)

app.secret_key = 'abcdefghijklmnopqrstuvwxyz'

@app.before_first_request
def awalan():
    session['loged'] = False

@app.route('/')
@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/logout')
def logout():
    session.pop('username',None)
    session.pop('iduser',None)
    session['loged'] = False
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT IdUser FROM user_accounts WHERE username=%s",(username,))
        iduser = cursor.fetchall()
        if cursor.execute(' SELECT * FROM user_accounts WHERE username=%s or password=%s ', (username, password)):
            if cursor.execute(' SELECT * FROM user_accounts WHERE username=%s and password=%s ', (username, password)):
                session['loged'] = True
                session['username'] = username
                session['iduser'] = iduser
                return redirect(url_for('home'))
            elif cursor.execute(' SELECT * FROM user_accounts WHERE username=%s ', (username,)):
                return render_template('login.html', msg="Wrong password", username=username)
            else:
                return render_template('login.html', msg="Wrong password and username", username=username)
        else:
            return render_template('login.html', msg="Wrong password and username", username=username)
    else:
        return render_template('login.html')


@app.route('/home')
def home():
    cond = session['loged']
    if cond == True:
        iduser = session['iduser']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM product_details ORDER BY dates DESC LIMIT 10")
        rv = cur.fetchall()
        cur.execute("SELECT * FROM user_accounts WHERE IdUser=%s",(iduser,))
        us = cur.fetchall()
        cur.close()
        return render_template('home.html', data=rv,user=us)
    else:
        return render_template('nicetry.html')


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
            cur.execute(" INSERT INTO user_accounts (Name,idUser,Username,Email,Alamat,NoHP,Birthdate,Password,registration_date) VALUES(%s, FLOOR(RAND()*(9999-1000+1))+1000,%s,%s,%s,%s,%s,%s,now()) ",
                        (name, username, email, alamat, nohp, birthdate, password))
            mysql.connection.commit()
            cur.execute(" INSERT INTO cart VALUES (FLOOR(RAND()*(99999-10000+1))+10000,(SELECT IdUser FROM user_accounts WHERE username = %s))",(username,))
            mysql.connection.commit()
        mysql.connection.commit()
        return render_template('login.html')
    else:
        return render_template('register.html')


@app.route('/forget password', methods=['POST', 'GET'])
def forget_password():
    return render_template('forget_password.html')


@app.route('/details/<string:id_data>', methods=["GET"])
def details(id_data):
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM product_details JOIN user_accounts ON product_details.IdUser=user_accounts.IdUser WHERE product_name=%s", 
        (id_data,))
    det = cur.fetchall()
    return render_template('details.html', det=det)

@app.route('/detailprofile', methods=["GET"])
def detailsprofile():
    iduser = session['iduser']
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM user_accounts WHERE IdUser=%s", (iduser,))
    det = cur.fetchall()
    return render_template('detailprofile.html',user=det)

@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    nama = request.form['nama']
    alamat = request.form['alamat']
    email = request.form['email']
    hp = request.form['hp']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE user_accounts SET Name=%s, Alamat=%s, Email=%s, NoHP=%s WHERE Username=%s",
                (nama, alamat, email, hp, id_data,))
    mysql.connection.commit()
    return redirect(url_for('detailprofile'))

@app.route('/updateitem', methods=["POST"])
def updateitem():
    id_data = request.form['id']
    nama = request.form['nama']
    harga = request.form['harga']
    berat = request.form['berat']
    desc = request.form['desc']
    link = request.form['foto']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE product_details SET product_name=%s, price=%s, weight=%s, description=%s,photo=%s WHERE IdProduct=%s",
                (nama, harga, berat, desc,link, id_data,))
    mysql.connection.commit()
    return redirect(url_for('prodlist'))

@app.route('/prodlist', methods=["GET"])
def prodlist():
    iduser = session['iduser']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product_details WHERE IdUser=%s ORDER BY product_name ASC",
                (iduser,))
    item = cur.fetchall()
    cur.execute("SELECT * FROM user_accounts WHERE IdUser=%s",
                (iduser,))
    user=cur.fetchall()
    cur.close()
    return render_template('productlist.html',item=item,user=user)

@app.route('/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM product_details WHERE idProduct=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('prodlist'))

@app.route('/simpan',methods=["POST"])
def simpan():
    id_data = request.form['id']
    uname = request.form['uname']
    link = request.form['foto']
    nama = request.form['nama']
    harga = request.form['harga']
    berat = request.form['berat']
    desc = request.form['deskripsi']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO product_details VALUES (FLOOR(RAND()*(99999-10000+1))+10000,%s,%s,now(),%s,%s,%s,0,%s,%s,0)",
                (id_data,uname,link,nama,harga,berat,desc,))
    mysql.connection.commit()
    return redirect(url_for('prodlist'))

@app.route('/cart')
def cart():
    iduser = session['iduser']
    cur = mysql.connection.cursor()
    cur.execute("SELECT DISTINCT IdUser FROM detail_cart RIGHT JOIN product_details ON \
        detail_cart.IdProduct=product_details.IdProduct WHERE IdCart=(SELECT IdCart FROM cart WHERE IdUser = %s);",(iduser,))
    sellerID = cur.fetchall()
    cartlist = []
    for seller in sellerID:
        curUser = seller
        cur.execute("SELECT * FROM detail_cart RIGHT JOIN product_details ON \
        detail_cart.IdProduct=product_details.IdProduct WHERE IdCart=(SELECT IdCart FROM cart WHERE IdUser = %s) AND IdUser = %s;", (iduser,curUser))
        cart=cur.fetchall()
        cartlist.append(cart)
    realcart = tuple(cartlist)
    return render_template('cart.html',cart=realcart)

@app.route('/addCart', methods=["POST"])
def addCart():
    iduser = session['iduser']
    id_data = request.form['id']
    quantity = request.form['items']
    cur = mysql.connection.cursor()
    if cur.execute("UPDATE product_details SET stock=stock-%s WHERE IdProduct = %s AND stock>=%s;", (quantity, id_data, quantity,)):
        cur.execute("INSERT INTO detail_cart VALUES (FLOOR(RAND()*(99999-10000+1))+10000, \
            (SELECT IdCart FROM cart WHERE IdUser = %s), %s,%s)",
                    (iduser, id_data, quantity,))
        mysql.connection.commit()
        return redirect(url_for('cart'))
    else:
        cur.execute(
            "SELECT * FROM product_details JOIN user_accounts ON \
                product_details.IdUser=user_accounts.IdUser WHERE IdProduct=%s", (id_data,))
        det = cur.fetchall()
        return render_template('details.html', msg="Stock tidak mencukupi", det=det)

@app.route('/hapuscart/<string:id_data>', methods=["GET"])
def hapuscart(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT amount FROM detail_cart WHERE IdDetailCart=%s", (id_data,))
    qt=cur.fetchall()
    cur.execute("UPDATE product_details SET stock=stock+%s \
        WHERE IdProduct = (SELECT IdProduct From detail_cart WHERE IdDetailCart=%s);", (qt,id_data,))
    cur.execute("DELETE FROM detail_cart WHERE IdDetailCart=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('cart'))

def findDistance(lokasi):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(lokasi)
    print(getLoc.address)
    Latitude = getLoc.latitude
    Longitude = getLoc.longitude
    coords = (Latitude, Longitude)
    return coords

def setPrice(distance):
    harga = distance * 50
    if harga<5000:
        return 5000
    else:
        harga = harga / 1000
        harga = math.ceil(harga)
        harga = harga*1000
        return harga

@app.route("/checkout", methods=["POST"])
def checkout():
    iduser = session['iduser']
    idowner = request.form['id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM detail_cart RIGHT JOIN product_details ON \
        detail_cart.IdProduct=product_details.IdProduct WHERE IdCart=(SELECT IdCart FROM cart WHERE IdUser = %s) AND IdUser = %s;", (iduser,idowner))
    cart=cur.fetchall()
    cur.execute("SELECT SUM(amount * product_details.price) FROM detail_cart RIGHT JOIN product_details ON \
        detail_cart.IdProduct=product_details.IdProduct WHERE IdCart=(SELECT IdCart FROM cart WHERE IdUser = %s) AND IdUser = %s;", (iduser,idowner))
    sum=cur.fetchall()
    cur.execute("SELECT Alamat FROM user_accounts WHERE IdUser=%s",(iduser,))
    buyer=cur.fetchall()
    cur.execute("SELECT Alamat FROM user_accounts WHERE IdUser=%s",(idowner,))
    seller=cur.fetchall()
    mysql.connection.commit()
    cur.execute("SELECT * FROM courier WHERE 1")
    kurir=cur.fetchall()
    coords_1 = findDistance(str(buyer[0][0]))
    coords_2 = findDistance(str(seller[0][0]))
    coords = (geopy.distance.geodesic(coords_1, coords_2).km)
    ongkir = setPrice(coords)
    totalharga=int(sum[0][0]) + ongkir
    mysql.connection.commit()
    return render_template('checkout.html', cart=cart, sum=sum, ongkir=ongkir, total=totalharga,kurir=kurir)


if __name__ == '__main__':
    app.run(debug=True)
