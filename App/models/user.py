from flask_bcrypt import Bcrypt
from .. import mongo

class dealers:
    def create_new(signupdetails):
        return mongo.db.user.insert_one(signupdetails)