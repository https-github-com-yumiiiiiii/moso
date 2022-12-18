from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import DBhandler
import sys
import hashlib
import os
import math
import json
application = Flask(__name__)
application.secret_key = os.urandom(24)
DB = DBhandler()

@application.route("/")
def index():
    return render_template("index.html")
    #return redirect(url_for('view_restaurantlist'))


@application.route("/login")
def login():
    return render_template("login.html")

@application.route("/login_confirm", methods=['POST'])
def login_user():
    id_=request.form['id']
    pw=request.form['password']
    pw_hash=hashlib.sha256(pw.encode('utf-8')).hexdigest()
    if DB.find_user(id_, pw_hash):
        session['id']=id_
#        data = DB.get_restaurant_byname(str(id_))
#        print("####data:",data)
#        return render_template('index.html', data=data)
        return redirect(url_for('index'))
    else: 
        flash('Wrond ID or PW!')
        return render_template('login.html')
    
@application.route("/logout")
def logout_user():
    session.clear()
    return redirect(url_for('index'))

@application.route("/signup")
def signup():
    return render_template("signup.html")

#회원가입
@application.route("/signup_post", methods=['POST'])
def register_user():
    data=request.form
    pw=request.form['password']
    pw_hash=hashlib.sha256(pw.encode('utf-8')).hexdigest()
    if DB.insert_user(data, pw_hash):
        return render_template('login.html')
    else:
        flash('user id already exist!')
        return render_template('signup.html')

@application.route("/register_restaurant")
def register_restaurant():
    return render_template("register_restaurant.html")

@application.route("/view_restaurantlist")
def view_restaurantlist():
    page=request.args.get("page",0,type=int)
    category=request.args.get("category","all")
    limit=4
    
    category=request.args.get("category","all")
    limit=4

    start_idx=limit*(page)
    end_index=limit*(page+1)

    if category=="all":
        data=DB.get_restaurants()
    else:
        data=DB.get_restaurants_bycategory(category)

    tot_count=len(data)

    print("category",category,tot_count)

    if tot_count <= limit:
        data=dict(list(data.items())[:tot_count])
    else:
        data=dict(list(data.items())[start_idx:end_index])

    data=dict(sorted(data.items(),key=lambda x: x[1]['name'], reverse=False))
    print(data)

    page_count = len(data)
    print(tot_count,page_count)

    return render_template("view_restaurantlist.html", datas=data.items(), total=tot_count, limit=limit, page=page,
                          page_count=math.ceil(tot_count/4), category=category)

@application.route("/map")
def map():
    data=DB.get_maps()
    return render_template("map.html", datas=data.items())



# def view_restaurantlist():
#     page=request.args.get("page",0,type=int)
#     limit=4

#     start_idx=limit*(page-1)
#     end_index=limit*page
#     data=DB.get_restaurants()
#     tot_count=len(data)
#     data=dict(list(data.items())[start_idx:end_index])

#     return render_template("view_restaurantlist.html", datas=data.items(), 
#                            total=int(tot_count), limit=limit, page=page, page_count=int((tot_count/4)+1))


@application.route("/recommend")
def recommend():
    result = DB.random_recommend()
    return render_template("recommend.html",result=result)

@application.route("/mypage/<id_>/")
def mypage(id_):
    data=DB.get_user_byname(str(id_))
#    data2=DB.get_bookmark_byuser(str(id_))
    return render_template("mypage.html", datas=data)


#@application.route("/food_list", methods=['GET','POST'])
#def food_list():
#    page=request.args.get("page",0,type=int)
#    limit=3
#    start_idx=limit*page
#    end_idx=limit*(page+1)
#    data=DB.get_mainmenus()
#    tot_count=len(data)
#    data=dict(list(data.items())[start_idx:end_idx])
#    return render_template("food_list.html", datas=data.items(), total=int(tot_count),
#                               limit=limit, page=page, page_count=int((tot_count/3)+1)) 

@application.route("/view_mainmenulist/<name>/")
def view_mainmenulist(name):
    data = DB.get_food_byname(str(name))
    tot_count=len(data)
    res_name=name

    page=request.args.get("page",0,type=int)
    limit=4
    start_idx=limit*page
    end_index=limit*(page+1)

    data2=DB.get_food_byname(str(name))[start_idx:end_index]
    new_dict={}
    for k,v in enumerate(data2):
            new_dict[k]=v


    print("##data:", data)

    return render_template("view_mainmenulist.html",  datas=new_dict.items(), name=res_name,
                           total=int(tot_count), limit=limit, page=page, page_count=int((tot_count/4)+1))



@application.route("/view_reviewlist/<name>/")
def view_reviewlist(name):
    data = DB.get_review_byname(str(name))
    tot_count=len(data)
    
    res_name=name
    page=request.args.get("page",0,type=int)
    limit=4
    start_idx=limit*page
    end_index=limit*(page+1)

    data2=DB.get_review_byname(str(name))[start_idx:end_index]
    new_dict={}
    for k,v in enumerate(data2):
            new_dict[k]=v
            
    print("##data:", data)
    
    return render_template("view_reviewlist.html", datas=new_dict.items(), name=res_name,
                           total=int(tot_count), limit=limit, page=page, page_count=int((tot_count/4)+1))

    
@application.route("/result_mainmenu", methods=['GET','POST'])    
def result_mainmenu():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    if DB.insert_mainmenu(data['menu_name'], data, image_file.filename):
        return render_template("result_mainmenu.html",data=data,image_file=image_file.filename)
    else:
        return "Mainmenu name is already exist!"
    
@application.route("/write_review", methods=['GET','POST'])
def write_review():
    data=request.form
    return render_template("write_review.html", data=data)

@application.route("/result_review", methods=['GET','POST'])
def result_review():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form    
    if DB.insert_review(data['write'],data,image_file.filename):
        return render_template("result_review.html",data=data,image_file=image_file.filename)
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
    if DB.get_avgrate_byname(str(name)):
        avg_rate=DB.get_avgrate_byname(str(name))
        return render_template("view_one_restaurant.html",data=data, avg_rate=avg_rate)
    else:
        return render_template("view_one_restaurant.html",data=data, avg_rate=0)
    


# @application.route("/bookmark/<id_>/<name>/", methods=['GET','POST'])
# def bookmark(id_, name):                        
#     data = DB.get_restaurant_byname(str(name))
#     avg_rate=DB.get_avgrate_byname(str(name))
#     if DB.insert_bookmark(id_, name):
#         return render_template("view_one_restaurant.html", data=data, avg_rate=avg_rate)
#     else:
#         return "RESTAURANT NAME ALREADY EXISTS!"
    

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug = True)
    application.secret_key = 'super secret key'
    application.config['SESSION_TYPE'] = 'filesystem'
    
    
