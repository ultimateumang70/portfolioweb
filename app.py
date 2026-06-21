from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from pathlib import Path
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'ultimateumang70-secure-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload folder if it doesn't exist
Path(app.config['UPLOAD_FOLDER']).mkdir(parents=True, exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

db = SQLAlchemy(app)

# OAuth setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'}
)

# Database Models
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    likes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Post {self.title}>'

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=6)
    return render_template('posts.html', posts=posts)

@app.route('/create-post', methods=['GET', 'POST'])
def create_post():
    # Restrict to admin Gmail
    if session.get('email') != "your_admin@gmail.com":
        flash("Only admin can create posts!", "danger")
        return redirect(url_for('home'))

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        image_file = request.files.get('image')
        
        if not title or not content:
            flash('Title and content are required!', 'danger')
            return redirect(url_for('create_post'))
        
        image_filename = None
        if image_file and image_file.filename:
            if allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                filename = f"{datetime.utcnow().timestamp()}_{filename}"
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_filename = filename
            else:
                flash('Only image files are allowed (png, jpg, jpeg, gif, webp)', 'danger')
                return redirect(url_for('create_post'))
        
        new_post = Post(title=title, content=content, image_filename=image_filename)
        db.session.add(new_post)
        db.session.commit()
        
        flash('Post created successfully!', 'success')
        return redirect(url_for('posts'))
    
    return render_template('create_post.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)

@app.route('/post/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    db.session.commit()
    flash('Post liked!', 'success')
    return redirect(url_for('view_post', post_id=post_id))

@app.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    # Restrict delete to admin Gmail
    if session.get('email') != "your_admin@gmail.com":
        flash("Only admin can delete posts!", "danger")
        return redirect(url_for('home'))

    post = Post.query.get_or_404(post_id)
    if post.image_filename:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], post.image_filename))
        except OSError:
            pass
    
    db.session.delete(post)
    db.session.commit()
    
    flash('Post deleted!', 'success')
    return redirect(url_for('posts'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        flash(f'Thanks {name}! Your message has been received.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# --- Login / Logout Routes ---
@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()
    session['email'] = user_info['email']

    if session['email'] == "your_admin@gmail.com":
        flash("Admin login successful!", "success")
    else:
        flash("Logged in, but not admin.", "info")

    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('email', None)
    flash("Logged out!", "success")
    return redirect(url_for('home'))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=False)
