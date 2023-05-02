from flask import Blueprint, make_response, jsonify, request
from flask.views import MethodView
from project.server.models.auth_td import Users
from project.server import db

class Registration(MethodView):
    def post(self):
        post_data = request.get_json()
        
        try:
            user = Users(
                email = post_data.get('email'),
                password = post_data.get('password'),
                confirmed=False
            )
            db.session.add(user)
            db.session.commit()
                
            resp = {
                'status':'success',
                'message': 'user successfully registered',
            }
            return make_response(jsonify(resp)), 200
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401


reg_view = Registration.as_view('registration_api')
auth_blueprint = Blueprint('auth', __name__)
auth_blueprint.add_url_rule(
    '/register',
    view_func=reg_view,
    methods=['POST']
)