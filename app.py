from flask import Flask,request,session
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
#obain personal address
@app.route("/api/self/address",methods=["GET"])
def self_address():
	if request.method == "GET":
		sId = session['_id']
		addresses = Address.query.filter_by(user_id=sId)
		data = []
		for address in addresses:
			address = address.__dict__
			del address["_sa_instance_state"]
			data.append(address)
		return result(200,{"address":data})

#delete address
@app.route("/api/address/delete",methods=["DELETE"])
def address_delete():
	if request.method=="DELETE":

		_id = request.form["id"]
		Address.query.filter_by(_id=_id).delete()
		db.session.commit()
		return result(200)

#user personal address add
@app.route("/api/self/address/add",methods=["POST"])
def self_address_add():
	if request.method=="POST":
		sId = session['_id']
		form = request.form
		data = {
			"province":form["province"],
			"town":form["town"],
			"county":form["county"],
			"detail":form["detail"],
			"user_id":sId
		}
		address = Address(**data)
		db.session.add(address)
		db.session.commit()
		return result(200)
#address add
@app.route("/api/address/add",methods=["POST"])
def address_add():
	if request.method=="POST":

		form = request.form
		data = {
			"province":form["province"],
			"town":form["town"],
			"county":form["county"],
			"detail":form["detail"],
		}
		address = Address(**data)
		db.session.add(address)
		db.session.commit()
		return result(200)

#obain all address info port
@app.route("/api/address")
def address():
	if request.method == "GET":

		addresses = Address.query.filter_by(user_id=None)
		data = dict()
		data["data"]=[]
		for address in addresses:
			dic = address.__dict__
			del dic["_sa_instance_state"]
			data["data"].append(dic) 
		return result(200,data)



if __name__ == '__main__':
	app.run(host="172.0.0.1")

