from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
  db = get_db()
  posts = (
    db.query(Post)
    .filter(Post.user_id == session.get('user_id'))
    .order_by(Post.created_at.desc())
    .all()
  )

  return render_template(
    'dashboard.html',
    loggedIn=session.get('loggedIn'),
    posts=posts
  )

@bp.route('/edit/<id>')
def edit(id):
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  return render_template(
    'edit-post.html',
    loggedIn=session.get('loggedIn'),
    post=post
  )