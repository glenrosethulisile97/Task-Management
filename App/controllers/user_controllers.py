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
        
        
          
       

    



