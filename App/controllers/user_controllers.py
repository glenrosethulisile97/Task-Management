from flask import Flask, url_for, redirect, Response, request, render_template,flash, jsonify
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity,get_jwt
from..models.user import User


def AdminSignup():
   
   
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Validate email format
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not (email_regex, email):
            flash('Invalid email format. Please try again.', 'error')
            return jsonify

        # Check if user already exists
        signupdetails = {'username': username, 'email': email, 'password': password}
        if not User.create_user(signupdetails):
            flash('Email or username already exists. Please try again with different credentials.', 'error')
            return jsonify

        # Redirect to login page or homepage after successful signup
        return jsonify

    # Render the signup form template if it's a GET request
    return jsonify

def signup():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

       # Validate email format
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not (email_regex, email):
            flash('Invalid email format. Please try again.', 'error')
            return jsonify


          # Check if user already exists
        signupdetails = {'username': username, 'email': email, 'password': password}
        if not User.create_user(signupdetails):
            flash('Email or username already exists. Please try again with different credentials.', 'error')
            return jsonify
          
# Redirect to login page or homepage after successful signup
        return jsonify

    # Render the signup form template if it's a GET request
    return jsonify


