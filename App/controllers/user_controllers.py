from flask import Flask, url_for, redirect, Response, request, render_template,flash, jsonify
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity,get_jwt
from..models.user import dealers
from bson.objectid import ObjectId 




def signup():
    if request.method == 'POST':
        # Extract form data
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        
        signupdetails = {'username': username, 'email': email, 'password': password}
        dealers.create_new(signupdetails)
        
        return jsonify({"message": "successfully signup"})
    

def login():
    if request.method == 'POST':
        signupdetails = { 
            'username': request.json.get('username'),
            'password': request.json.get('password')
        }

        # Assuming you have a function to handle the login logic
        dealers.create_new(signupdetails)
        
        return jsonify({"message": "successfully logged in"})

    return jsonify({"message": "method not allowed"}), 405

    # else:
    #   return jsonify({'message': 'Login Failed'}), 401


    # # Extract the user ID from the JWT
    # user_id = get_jwt_identity()
    # user = User.query.filter_by(id=user_id).first()

    # # Check if user exists
    # if user:
    #     return jsonify({'message': 'User found', 'name': user.name})
    # else:
    #     return jsonify({'message': 'User not found'}), 404

        
        
          
       

    



