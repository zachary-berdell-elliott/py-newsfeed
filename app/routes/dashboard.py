from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
  posts = (
    db.query(Post)
    .filter(Post.user_id == session.get('user_id'))
    .order_by(Post.created_at.desc())
    .all()
  )

  return render_template(
    'dashboard.html',
    post=posts,
    loggedIn=session.get('loggedIn')
  )

@bp.route('/edit/<id>')
def edit(id):
  return render_template(
    'edit-post.html',
    loggedIn=session.get('loggedIn')
  )