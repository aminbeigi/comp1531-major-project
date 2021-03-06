import sys
from json import dumps
from flask import Flask, request, send_from_directory
from flask_cors import CORS
from src.error import InputError
from src import config
from src.auth import auth_register_v1
from src.auth import auth_login_v1
from src.channels import channels_create_v1

from src.routes.dm_http import dm_blueprint
from src.routes.auth_http import auth_blueprint
from src.routes.clear_http import clear_blueprint
from src.routes.channels_http import channels_blueprint
from src.routes.channel_http import channel_blueprint
from src.routes.user_http import user_blueprint
from src.routes.message_http import message_blueprint
from src.routes.admin_http import admin_blueprint
from src.routes.users_http import users_blueprint
from src.routes.notifications_http import notifications_blueprint
from src.routes.standup_http import standup_blueprint

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__,static_url_path='/static/')
### Register routes ###
APP.register_blueprint(auth_blueprint)
APP.register_blueprint(clear_blueprint)
APP.register_blueprint(channels_blueprint)
APP.register_blueprint(channel_blueprint)
APP.register_blueprint(user_blueprint)
APP.register_blueprint(message_blueprint)
APP.register_blueprint(dm_blueprint)
APP.register_blueprint(admin_blueprint)
APP.register_blueprint(users_blueprint)
APP.register_blueprint(notifications_blueprint)
APP.register_blueprint(standup_blueprint)
#######################
CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)

# Example
@APP.route("/echo", methods=['GET'])
def echo():
    data = request.args.get('data')
    if data == 'echo':
	    raise InputError(description='Cannot echo "echo"')
    return dumps({
        'data': data
    })

@APP.route("/message/send/v2", methods=['POST'])
def message_send():
    return dumps({
    })

@APP.route("/message/edit/v2", methods=['PUT'])
def message_edit():
    return dumps({
    })

@APP.route("/message/remove/v1", methods=['DELETE'])
def message_remove():
    return dumps({
    })

@APP.route("/message/share/v1", methods=['POST'])
def message_share():
    return dumps({
    })

@APP.route("/message/senddm/v1", methods=['POST'])
def message_send_dm():
    return dumps({
    })

@APP.route("/user/profile/v2", methods=['GET'])
def user_profile():
    return dumps({
    })

@APP.route("/user/profile/setname/v2", methods=['PUT'])
def user_profile_set_name():
    return dumps({
    })

@APP.route("/user/profile/setemail/v2", methods=['PUT'])
def user_profile_set_email():
    return dumps({
    })

@APP.route("/user/profile/sethandle/v1", methods=['PUT'])
def user_profile_set_handle():
    return dumps({
    })

@APP.route("/users/all/v1", methods=['GET'])
def users_all():
    return dumps({
    })

@APP.route("/search/v2", methods=['GET'])
def search():
    return dumps({
    })
'''
@APP.route("/admin/user/remove/v1", methods=['DELETE'])
def admin_user_remove():
    return dumps({
    })

@APP.route("/admin/userpermission/change/v1", methods=['POST'])
def admin_user_permission_change():
    return dumps({
    })
'''
@APP.route("/notifications/get/v1", methods=['GET'])
def notification_get():
    return dumps({
    })

@APP.route('/static/photo/<path:path>')
def send_js(path):
    return send_from_directory('', path)

if __name__ == "__main__":
    APP.run(port=config.port) # Do not edit this port
