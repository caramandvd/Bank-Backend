from flask import Flask, request, jsonify
from controller.app_controller import AppController
from model.repository.users_repository import UsersRepository

app = Flask(__name__)


@app.route('/api/v1/create_user', methods=['POST'])
def create_user():
    if request.method == 'POST':
        # date = request.get_json()
        user_id = request.json['user_id']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']
        address = request.json['address']
        phone_number = request.json['phone_number']
        username = request.json['username']
        user_password_hash = request.json['password']

        AppController(UsersRepository()).add_user(user_id=user_id,
                               first_name=first_name,
                               last_name=last_name,
                               email=email,
                               address=address,
                               phone_number=phone_number,
                               username=username,
                               user_password_hash=user_password_hash)

        return jsonify({
            'response': "User: " + user_id + "; " + first_name + "; " + last_name + "; " + email + "; " + address + "; "
                        + phone_number + "; "})

if __name__ == '__main__':
    app.run(debug=True)
