from flask import session
from server.models import User
from server.extensions import db



# SIGNUP LOGIC

def signup_user(data):
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "Username and password required"}, 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return {"error": "Username already exists"}, 409

    new_user = User(username=username)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    session["user_id"] = new_user.id

    return new_user.to_dict(), 201



# LOGIN LOGIC

def login_user(data):
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return {"error": "Invalid credentials"}, 401

    session["user_id"] = user.id

    return user.to_dict(), 200



# LOGOUT LOGIC

def logout_user():
    session.pop("user_id", None)
    return {"message": "Logged out successfully"}, 200



# CHECK SESSION LOGIC

def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    user = User.query.get(user_id)

    if not user:
        return {"error": "User not found"}, 404

    return user.to_dict(), 200