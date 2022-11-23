from flask import Flask, render_template, request
from database import DBhandler
import sys
application = Flask(__name__)
DB = DBhandler()

@application.route("/")
def index():
    return render_template("index.html")
    #return redirect(url_for('view_restaurantlist'))


@application.route("/login")
def login():
    return render_template("login.html")

@application.route("/signup")
def signup():
    return render_template("signup.html")

@application.route("/register_restaurant")
def register_restaurant():
    return render_template("register_restaurant.html")

@application.route("/view_restaurantlist")
def view_restaurantlist():
    page=request.args.get("page",0,type=int)
    limit=4
    
    start_idx=limit*(page-1)
    end_index=limit*page
    data=DB.get_restaurants()
    tot_count=len(data)
    data=dict(list(data.items())[start_idx:end_index])
    
    return render_template("view_restaurantlist.html", datas=data.items(), 
                           total=int(tot_count), limit=limit, page=page, page_count=int((tot_count/4)+1))

@application.route("/map")
def map():
    return render_template("map.html")

@application.route("/recommend")
def recommend():
    return render_template("recommend.html")

@application.route("/mypage")
def mypage():
    return render_template("mypage.html")

@application.route("/view_one_restaurant")
def view_one_restaurant():
    return render_template("view_one_restaurant.html")

@application.route("/view_mainmenu", methods=['GET','POST'])
def view_mainmenu():
    global idx
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    
    if DB.insert_mainmenu(data['menu_name'], data, image_file.filename):
        return render_template("view_mainmenu.html", data=data, image_path="image/"+image_file.filename) 
    else:
        return "Mainmenu name is already exist!"
    
@application.route("/write_review")
def write_review():
    return render_template("write_review.html")

@application.route("/view_review", methods=['GET','POST'])
def view_review():
    # image_file=request.files["file"]
    # image_file.save("static/image/{}".format(image_file.filename))
    data=request.form    
    if DB.insert_review(data['write'],data):
        return render_template("view_review.html",data=data)
    else:
        return "YOUR REVIEW ALREADY EXISTS!"



@application.route("/result", methods=['GET','POST'])
def result():
    global idx
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    
    if DB.insert_restaurant(data['name'],data,image_file.filename):
        return render_template("result.html",data=data,image_path="image/"+image_file.filename)
    else:
        return "RESTAURANT NAME ALREADY EXISTS!"
    
@application.route("/register_mainmenu", methods=['GET','POST'])
def register_mainmenu():
    global idx
    data=request.form
    print(data)
    return render_template("register_mainmenu.html",data=data)


@application.route("/view_one_restaurant/<name>/")
def view_restaurant_detail(name):
    data = DB.get_restaurant_byname(str(name))
    print("####data:",data)
    return render_template("view_one_restaurant.html",data=data)

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug = True)
