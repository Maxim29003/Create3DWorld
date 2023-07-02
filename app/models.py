from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
  #  avatar = db.Column(db.String(100), nullable=False)
 #   models = db.relationship("Model3D", back_populates="user")

    def get_id(self):
        return str(self.id)


#class Model3D(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
   # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   # name_3d_model = db.Column(db.String(100), nullable=False)
  #  file_3d_model = db.Column(db.String(100), nullable=False)
    #user = db.relationship("User", back_populates='models')
