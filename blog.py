from flask import Flask , render_template ,flash,redirect,url_for,session,logging,request
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
import data_acces
from werkzeug.security import generate_password_hash,check_password_hash
import pyodbc
from classes import User_db
import data_acces
from functools import wraps








class LoginForm(Form):
    username = StringField("Kullanıcı Adı",validators=[validators.length(min=3),validators.DataRequired()])
    sifre= PasswordField("Şifrenizi Giriniz",validators=[validators.DataRequired("Lütfen Şifrenizi Giriniz")])





app = Flask(__name__)
app.secret_key = "mustiler463"



con_str2 = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-QVEIDUC;'
        'DATABASE=zen;'
        'Trusted_Connection=yes;'




)
con_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=sql.athena.domainhizmetleri.com;'
        'DATABASE=mustaf11_Stok_Demo;'
        'UID=mustaf11_sencan;'
        'PWD=Mustiler463!'



)



con = pyodbc.connect(con_str)






cursor = con.cursor()



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            
            return redirect(url_for("login"))
    return decorated_function







@app.route("/login", methods = ["GET","POST"])

def login():
    form = LoginForm(request.form)
    
    if request.method == "POST":
        t_username = form.username.data
        t_password = form.sifre.data
        if data_acces.validate(t_username, t_password):
            session["logged_in"] = True
            session["username"] = t_username
            flash("Giriş Başarılı","success")
            return redirect(url_for("private"))   
        else:
            return redirect(url_for("login"))
             
        
    else:
        flash("Hatalı Giriş","danger")
        return render_template("login.html", form = form)

@app.route("/logout") 
def logout():
    session.clear()
    return redirect(url_for("index")) 

@app.route("/")

def index():
    return render_template("index.html")




@app.route("/about_deneme")
def about():
    return render_template("about_deneme.html")


@app.route("/opinions")
def opinions():
    return render_template("opinions.html")


@app.route("/private")
@login_required
def private():
    cursor.execute("SELECT * FROM Stok_demo ")
    data = cursor.fetchall()
    return render_template("private.html",products = data)
    

    


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":     
        name = request.form['isim']
        count = request.form['adet']
        quer= "INSERT INTO Stok_demo (Ürün_Adı,Ürün_Sayısı) VALUES('"+name+"','"+count+"')"
        print(quer)
        cursor.execute(quer)
        con.commit()
        flash("Yeni ürün eklendi")
        return redirect(url_for('private'))
    else:
        return redirect(url_for("login"))





@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Ürün Silindi")
    cursor.execute("DELETE FROM Stok_demo WHERE Ürün_Barkodu= ? ",id_data)
    cursor.commit()
    return redirect(url_for('private'))







@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['isim']
        count = request.form['adet']
        cursor.execute("UPDATE Stok_demo SET Ürün_Sayısı=? WHERE Ürün_adı = ? ",count,name)
        cursor.commit()
        flash("Ürün Güncellendi")
        return redirect(url_for('private'))



if __name__ == "__main__":
    app.run(debug=True)
 
