from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User(db.Model):

	__tablename__ = "user"
	__table_args__ = {'mysql_collate':'utf8_general_ci'}

	_id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30))
	account = db.Column(db.String(11),unique=True)
	password = db.Column(db.String(64))
	avatar = db.Column(db.String(256))
	age = db.Column(db.Integer)
	idCard = db.Column(db.String(18))
	gneder = db.Column(db.String(2))
	createTime = db.Column(db.DateTime)
	loginTime = db.Column(db.DateTime)
	logoutTime = db.Column(db.DateTime)
	balance = db.Column(db.Float(10),default=0)

	vip = db.Column(db.Integer,db.ForeignKey("vip._id"))

	def __repr__(self):
		return "User:%s"%self.name

goodsCourt = db.Table("goodsCourt",
	db.Column("goods_id",db.Integer,db.ForeignKey("goods._id")),
	db.Column("court_id",db.Integer,db.ForeignKey("court._id"))
	)

class Court(db.Model):

	__tablename__ = "court"
	__table_args__ = {'mysql_collate':'utf8_general_ci'}
	_id = db.Column(db.Integer,primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user._id'))
	number = db.Column(db.Integer,default=0)#记录商品种类
	goods = db.relationship("Goods",secondary=goodsCourt,backref=db.backref("court",lazy="dynamic"),lazy="dynamic")


class Address(db.Model):

	__tablename__ = "address"
	__table_args__ = {'mysql_collate':'utf8_general_ci'}
	_id = db.Column(db.Integer,primary_key=True)
	province = db.Column(db.String(18))
	town = db.Column(db.String(18))
	county = db.Column(db.String(18))
	detail = db.Column(db.String(200))
	user_id = db.Column(db.Integer,db.ForeignKey("user._id"))

	def __repr__(self):
		return "Address:%s"%self.detail


class Admin(db.Model):

	__tablename__ = "admin"
	__table_args__ = {'mysql_collate':'utf8_general_ci'}
	_id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30))
	account = db.Column(db.String(11))
	password = db.Column(db.String(64))
	createTime = db.Column(db.DateTime)
	loginTime = db.Column(db.DateTime)
	logoutTime = db.Column(db.DateTime)
	level = db.Column(db.Integer,default=0)

	def __repr__(self):
		return "Admin:%s"%self.name 
