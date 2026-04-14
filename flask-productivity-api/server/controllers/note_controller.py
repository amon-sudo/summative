from flask import session
from server.models import Note
from server.extensions import db



# CREATE NOTE

def create_note(data):
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return {"error": "Title and content required"}, 400

    note = Note(title=title, content=content, user_id=user_id)

    db.session.add(note)
    db.session.commit()

    return note.to_dict(), 201



# GET NOTES (PAGINATION)

def get_notes(page, per_page):
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    query = Note.query.filter_by(user_id=user_id)

    paginated = query.paginate(page=page, per_page=per_page, error_out=False)

    return {
        "notes": [note.to_dict() for note in paginated.items],
        "total": paginated.total,
        "page": paginated.page,
        "pages": paginated.pages
    }, 200



# UPDATE NOTE

def update_note(note_id, data):
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    note = Note.query.filter_by(id=note_id, user_id=user_id).first()

    if not note:
        return {"error": "Note not found"}, 404

    if "title" in data:
        note.title = data["title"]

    if "content" in data:
        note.content = data["content"]

    db.session.commit()

    return note.to_dict(), 200



# DELETE NOTE

def delete_note(note_id):
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    note = Note.query.filter_by(id=note_id, user_id=user_id).first()

    if not note:
        return {"error": "Note not found"}, 404

    db.session.delete(note)
    db.session.commit()

    return {"message": "Note deleted"}, 200