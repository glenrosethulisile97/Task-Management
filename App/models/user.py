from flask_bcrypt import Bcrypt

class dealers:

  
    def create_user(signupdetails):
        existing_user = dealers.find_user_by_username_or_email(signupdetails['username'], signupdetails['email'])
        if existing_user:
            return False  # User already exists
        else:
            # Insert the new user into the database
           # db.signup.insert_one(signupdetails)
            return True  # User created successfully

  
    def find_user_by_username_or_email(username, email):
        return# db.signup.find_one({'$or': [{'username': username}, {'email': email}]})

  
    def find_user_by_username_and_password(username, password):
        return #db.signup.find_one({'username': username, 'password': password})

 
    def get_user_by_email(email):
        return #db.signup.find_one({'email': email})
    
    def authenticate(username, password):
        user = dealers.query.filter_by(username=username).first()
        if user and dealers.check_password_hash(user.password, password):
            return user
        return None
    


    
    
    
    