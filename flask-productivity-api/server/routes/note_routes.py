from flask import Blueprint

note_bp = Blueprint("notes", __name__)

@note_bp.route("", methods=["GET"])
def get_notes():
    return {"message": "notes route works"}