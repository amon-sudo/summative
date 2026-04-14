from flask import Blueprint, request, session
from server.controllers.note_controller import (
    create_note,
    get_notes,
    update_note,
    delete_note
)

note_bp = Blueprint("notes", __name__)



# CREATE NOTE

@note_bp.route("", methods=["POST"])
def create():
    print("CREATE NOTE HIT")
    return create_note(request.json)



# GET NOTES (PAGINATION)

@note_bp.route("", methods=["GET"])
def get_all():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    return get_notes(page, per_page)



# UPDATE NOTE

@note_bp.route("/<int:note_id>", methods=["PATCH"])
def update(note_id):
    return update_note(note_id, request.json)



# DELETE NOTE

@note_bp.route("/<int:note_id>", methods=["DELETE"])
def delete(note_id):
    return delete_note(note_id)