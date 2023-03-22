from flask import Flask, request, jsonify
from controller.app_controller import AppController
from model.repository.users_repository import UsersRepository
from model.repository.users_transaction_repository import UsersTransactionsRepository

app = Flask(__name__)

user_repository = UsersRepository()
app_ctrl = AppController(user_repository)


@app.route('/api/v1/create_user', methods=['POST'])
def create_user():
    req_json = request.json
    if request.method == 'POST':
        user_id = req_json['user_id']
        first_name = req_json['first_name']
        last_name = req_json['last_name']
        email = req_json['email']
        address = req_json['address']
        phone_number = req_json['phone_number']
        username = req_json['username']
        user_password_hash = req_json['password']

        app_ctrl.add_user(user_id=user_id,
                          first_name=first_name,
                          last_name=last_name,
                          email=email,
                          address=address,
                          phone_number=phone_number,
                          username=username,
                          user_password_hash=user_password_hash)

        return {"response": {"user_id": user_id,
                             "first_name": first_name,
                             "last_name": last_name,
                             "email": email,
                             "address": address,
                             "phone_number": phone_number
                             }}


@app.route('/api/v1/get_user_contact_transactions', methods=['GET'])
def get_user_contact_transactions():
    req_json = request.json
    user_transactions_repository = UsersTransactionsRepository()
    app_ctrl_transactions = AppController(user_transactions_repository)
    if request.method == 'GET':
        user_id = req_json['user_id']

        response = app_ctrl_transactions.get_last_transactions_by_user_id(user_id)

        return jsonify({
            'The latest transactions for the user': response
        })


if __name__ == '__main__':
    app.run(debug=True)
