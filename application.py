from flask import Flask, render_template, request	
import os
import sys
from werkzeug.utils import secure_filename
application = Flask(__name__)


@application.route("/register_mainmenu", methods=['GET','POST'])
def reg_register_mainmenu():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    return render_template("/register_mainmenu.html", data=data, image_file=image_file.filename) 
#나중에 view_mainmenu와 image_file=image_file.filename 으로 바꾸고 추가해야 함.   , image_file=image_file.filename

@application.route("/view_mainmenu", methods=['GET','POST'])
def reg_view_mainmenu():    
# #    image_file=request.files["file"]
# #    image_file.save("static/image/{}".format(image_file.filename))
#	if request.method=='POST':
        result=request.form
        return render_template("view_mainmenu.html")
#후기~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
@application.route("/write_review", methods=['GET','POST'])
def reg_write_review():
#    image_file=request.files["file"]
#    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    return render_template("/view_review.html", data=data)

@application.route("/view_review", methods=['GET','POST'])
def reg_view_review():
        result=request.form
        return render_template("view_review.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
    
    
