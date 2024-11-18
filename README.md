# Django Blog Example

Create a blog with a homepage to list posts and detail pages for each post using Django and template inheritance.

## Steps

### Step 1: Create a Django Project and an App

**Create the Django Project and App**:

```bash
python -m venv venv
pip install django
django-admin startproject myblog
cd myblog
python manage.py startapp blog
```

**Add the App to `INSTALLED_APPS`**:
   
Open the `myblog/settings.py` file.

Find the `INSTALLED_APPS` list and add `'blog',` to it:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Add this line
]
```

**Verify the Setup**:

Run the development server to ensure everything is working so far:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser. It should show the Django "It worked!" page.

### Create a Post model with fields for title, content, and created and run migrations.

### Register the Post model in the admin and create a superuser to manage posts.

### Define a homepage view to list posts and a detail view to show individual posts.

### Add routes for the homepage ( / ) and detail pages ( /post/<id>/ ). 

### Create a base.html template for a consistent layout with a header, footer, and {% block content %}.

### Extend base.html for the homepage to list post titles linking to detail pages.

### Extend base.html for the detail page to display the post's title and content.

### Use the admin panel to create sample posts.

### And finnally run the development server and verify.The hompage should display list of postsAnd clicking a title navigates to the corresponding detail page.
