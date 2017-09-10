from flasgger import swag_from
from flask import Blueprint, jsonify, request


from server.user.models import *

user = Blueprint('user', __name__)


@user.route('/save',methods=['POST'])
@swag_from("api/user_save.yml",methods=['POST'])
def user_login():
    isErr = False;
    try:
        User.objects.create(username=request.get_json()['username'],
                            password=request.get_json()['password']);
    except:
        isErr = True

    if isErr:
        return json.dumps({"err": "-1", "message": "parameters invalid"})
    else:
        return User.objects.filter(username='Alan').to_json();


@user.route('/<id>/')
@swag_from("api/user.yml")
def user_info(id):
    print(id)
    return User.objects.filter(_id = id).to_json()


