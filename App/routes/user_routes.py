from flask import Blueprint
from ..controllers import user_controllers


app = Blueprint ('user',__name__)

app.route("/signup", methods = ['POST'])(user_controllers.signup)



