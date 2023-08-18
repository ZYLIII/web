from flask import Flask,request,session，jsonify
from settings import *
from models import *
from utils import *
import traceback

app = Flask(__name__,static_folder="",static_url_path="")
app.config.from_object(MySQLConfig)
with app.app_context():
	db.init_app(app)
	db.create_all()


@app.before_request
def before():
	try:
		data = json.loads(request.get_data(as_text=True))
		request.form = data
	except:
		pass
	url = request.path #request URL now
	passUrl = WHITE_NAME_LIST
	if url in passUrl:
		pass 
	elif "static" in url:
		pass
	elif "/api/goods/detail/" in url:
		pass 
	else:
		_id = session.get("_id",None)
		if not _id:
			return result(203,{"info":"not login"})
		else:
			pass 

#login port user&admin
@app.route("/api/login",methods=["POST","GET"])
def login():

	if request.method == "POST":
		account = request.form["account"]
		password = request.form["password"]
		password = md5(password)
		_type = request.form["type"]
		if _type == "admin":
			admin = Admin.query.filter_by(account=account).first()
			if admin:
				if admin.password == password:
					session["_id"] = admin._id
					admin.loginTime = getNowDataTime()
					db.session.commit()
					return result(200)
				else:
					return result(202,{"info":"Wrong P password"})
			else:
				return result(201,{"info":"No this admin info"})
		else:
			user = User.query.filter_by(account=account).first()
			if user:
				if user.password==password:
					session["_id"] = user._id
					user.loginTime = getNowDataTime()
					db.session.commit()
					return result(200)
				else:
					return result(202,{"info":"Wrong Password"})
			else:
				return result(201,{"info":"No this user information"})
	if request.method == "GET":
		return result()

#exit system
@app.route("/api/quit",methods=["POST"])
def quit():
	if request.method == "POST":
		_id = session["_id"]
		_type = request.form["type"]
		if _type == "admin":
			admin = Admin.query.get(_id)
			admin.logoutTime = getNowDataTime()
		else:
			user = User.query.get(_id)
			user.logoutTime = getNowDataTime()
		del session["_id"]
		return result(200)

#normal register port
@app.route("/api/regist",methods=["POST"])
def regist():
	if request.method=="POST":
		try:
			account = request.form["account"]
			password = request.form["password"]
			password = md5(password)
			user = User(account=account,password=password)
			try:
				db.session.add(user)
				db.session.commit()
			except:
				return result(205,{"info":"Has been registered"})
			user = User.query.filter_by(account=account).first()
			court = Court(user_id=user._id)
			db.session.add(court)
			db.session.commit()
			session["_id"] = user._id 
			return result(200)
		except:
			return result(502,{"info":"error data"})

from flask import Flask, request, jsonify

app = Flask(__name__)

# Obtain personal information
@app.route("/api/self/information", methods=["GET"])
def get_self_information():
    sId = session['_id']
    informations = Information.query.filter_by(user_id=sId)
    data = [info.__dict__ for info in informations]
    for info in data:
        del info["_sa_instance_state"]
    return jsonify(status=200, information=data)

# Delete information
@app.route("/api/information/delete", methods=["DELETE"])
def delete_information():
    _id = request.form["id"]
    Information.query.filter_by(_id=_id).delete()
    db.session.commit()
    return jsonify(status=200)

# Add personal information
@app.route("/api/self/information/add", methods=["POST"])
def add_self_information():
    sId = session['_id']
    data = {
        "province": request.form["province"],
        "town": request.form["town"],
        "county": request.form["county"],
        "detail": request.form["detail"],
        "user_id": sId
    }
    information = Information(**data)
    db.session.add(information)
    db.session.commit()
    return jsonify(status=200)

# Add information
@app.route("/api/information/add", methods=["POST"])
def add_information():
    data = {
        "province": request.form["province"],
        "town": request.form["town"],
        "county": request.form["county"],
        "detail": request.form["detail"],
    }
    information = Information(**data)
    db.session.add(information)
    db.session.commit()
    return jsonify(status=200)

# Obtain all information
@app.route("/api/information", methods=["GET"])
def get_all_information():
    informations = Information.query.filter_by(user_id=None)
    data = {"data": [info.__dict__ for info in informations]}
    for info in data["data"]:
        del info["_sa_instance_state"]
    return jsonify(status=200, **data)



if __name__ == '__main__':
	app.run(host="172.0.0.1")

