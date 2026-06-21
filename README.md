# My Portfolio Website

A beautiful, responsive portfolio website built with Flask where you can showcase your work, create community posts, and share images.

## Features

✨ **Key Features:**
- 🏠 Beautiful home page with hero section
- 👤 About page to tell your story
- 📝 Create, view, and manage community posts
- 🖼️ Upload images with your posts
- ❤️ Like system for posts
- 📱 Fully responsive design (mobile & desktop)
- ✉️ Contact page for visitors to reach out
- 🎨 Modern UI with gradient design

## Requirements

- Python 3.7+
- Flask 2.3.3
- Flask-SQLAlchemy 3.0.5
- Werkzeug 2.3.7

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ultimateumang70/portfolioweb.git
cd portfolioweb
```

### 2. Create a Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
portfolioweb/
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── portfolio.db          # SQLite database (auto-created)
├── static/
│   └── uploads/         # User uploaded images
├── templates/
│   ├── base.html        # Base template
│   ├── home.html        # Home page
│   ├── about.html       # About page
│   ├── posts.html       # Posts listing
│   ├── create_post.html # Create post form
│   ├── view_post.html   # Single post view
│   ├── contact.html     # Contact page
│   ├── 404.html         # 404 error page
│   └── 500.html         # 500 error page
└── README.md            # This file
```

## How to Use

### Creating a Post
1. Navigate to "Create Post" from the navigation menu
2. Fill in the post title and content
3. Optionally upload an image (PNG, JPG, JPEG, GIF, WebP)
4. Click "Publish Post"

### Viewing Posts
1. Go to "Posts" to see all community posts
2. Click "Read More" on any post to see the full content
3. Like posts by clicking the heart icon

### Customizing Your Portfolio

Edit these files to personalize your portfolio:

**Home Page:** `templates/home.html`
**About Page:** `templates/about.html`
**Contact Info:** `templates/contact.html`

Update the hero section and intro text to match your style!

## Deployment Options

### Option 1: Render.com (Recommended)
1. Push your code to GitHub
2. Go to [render.com](https://render.com)
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Set runtime to Python 3.10
6. Set start command to `gunicorn app:app`
7. Deploy!

### Option 2: PythonAnywhere
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Create an account
3. Upload your files
4. Configure a web app with Flask
5. Done!

### Option 3: Railway.app
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repository
3. Railway will auto-detect Flask
4. Deploy with one click!

## Adding Your Custom Domain

After deployment, add your custom domain:
1. Register a domain (GoDaddy, Namecheap, etc.)
2. Update your hosting provider's DNS settings
3. Point your domain to your deployed site

## Customization Tips

### Change Colors
Edit the CSS variables in `templates/base.html`:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --light-bg: #f7fafc;
}
```

### Update Social Links
Find these in `templates/base.html`, `templates/about.html`, and `templates/contact.html`:
```html
<a href="#" class="text-white me-3"><i class="fab fa-twitter"></i></a>
```

Replace `#` with your actual social media URLs.

### Add Email Notifications
The contact form is ready for email integration. Add a service like:
- SendGrid
- Mailgun
- Gmail SMTP

## Database

The application uses SQLite for database storage. The database is automatically created when you first run the app.

To reset the database, simply delete `portfolio.db` and restart the app.

## Security Notes

⚠️ **Before deploying to production:**
1. Change the `SECRET_KEY` in `app.py` to a strong random string
2. Set `debug=False` in the Flask configuration
3. Use environment variables for sensitive data
4. Enable HTTPS on your hosting provider

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Make sure you've activated your virtual environment and installed requirements:
```bash
pip install -r requirements.txt
```

### Issue: "Address already in use"
**Solution:** Change the port in `app.py`:
```python
app.run(debug=True, port=5001)
```

### Issue: Uploaded images not showing
**Solution:** Ensure the `static/uploads/` folder exists and has write permissions

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.

## Support

Need help? Check out:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

**Happy coding! 🚀**

Built with ❤️ by Your Name
