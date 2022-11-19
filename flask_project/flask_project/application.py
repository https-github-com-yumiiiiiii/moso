from flask import Flask, render_template, request
from database import DBhandler
import sys
application = Flask(__name__)

DB=DBhandler()


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/login")
def login():
    return render_template("login.html")

@application.route("/signup")
def signup():
    return render_template("signup.html")

@application.route("/register_restaurant")
def register_restaurant():
    return render_template("register_restaurant.html")

@application.route("/register_mainmenu")
def register_mainmenu():
    return render_template("register_mainmenu.html")

@application.route("/view_restaurantlist")
def view_restaurantlist():
    return render_template("view_restaurantlist.html")

@application.route("/map")
def map():
    return render_template("map.html")

@application.route("/recommend")
def recommend():
    return render_template("recommend.html")

@application.route("/mypage")
def mypage():
    return render_template("mypage.html")


@application.route("/result", methods=['GET','POST'])
def result():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    return render_template("result.html",data=data,image_file=image_file.filename)




# ~~~~~~~~유미~~~~~~메인메뉴~~~~~~
@application.route("/view_mainmenu", methods=['GET','POST'])
def view_mainmenu():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    if DB.insert_mainmenu(data['menu_name'], data, image_file.filename)
        return render_template("view_mainmenu.html", data=data, image_file=image_file.filename) 
    else
        return "Mainmenu name is already exist!"



#후기~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@application.route("/write_review")
def write_review():
    return render_template("write_review.html")
    


@application.route("/view_review", methods=['GET','POST'])
def view_review():
    # image_file=request.files["file"]
    # image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    return render_template("view_review.html",data=data)

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug = True)
