import sys
from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()
  
  try:
    #Creates a new user
    newUser = User(
        username = data['username'],
        email = data['email'],
        password = data['password']
    )

    # Saves user to the database
    db.add(newUser)
    db.commit()
  except:
    print(sys.exc_info()[0])

    #Sends user error message and rollsback db
    db.rollback()
    return jsonify(message = 'Signup failed'), 500

  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True
  return jsonify(id = newUser.id)