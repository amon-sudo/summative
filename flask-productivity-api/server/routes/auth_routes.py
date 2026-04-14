from flask import Blueprint, request
from server.controllers.auth_controller import (
    signup_user,
    login_user,
    logout_user,
    get_current_user
)

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    print("REAL SIGNUP HIT")
    return signup_user(request.json)


@auth_bp.route("/login", methods=["POST"])
def login():
    return login_user(request.json)


@auth_bp.route("/logout", methods=["DELETE"])
def logout():
    return logout_user()


@auth_bp.route("/check_session", methods=["GET"])
def check_session():
    return get_current_user()