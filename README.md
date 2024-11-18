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

### Step 2: Create a Post Model

**Define the Model**:

Open `blog/models.py`.

Add the following `Post` model:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

**Field Explanation**:

   - `title`: A `CharField` for the post title with a maximum length of 200 characters.
   - `content`: A `TextField` for the post's body.
   - `created`: A `DateTimeField` that automatically sets the current timestamp when a post is created.



**Make Migrations**:

Run the following command to generate migration files for the `Post` model:
     
```bash
python manage.py makemigrations
python manage.py migrate
```

**Verify**:

Run the server again to ensure everything works:

```bash
python manage.py runserver
```

**Test the Model in the Admin Interface**:

Register the model in `blog/admin.py` by adding:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Create a superuser if you haven't already:

```bash
python manage.py createsuperuser
python manage.py runserver
```

Log in to the admin interface at `http://127.0.0.1:8000/admin` and check if the `Post` model appears.










### Register the Post model in the admin and create a superuser to manage posts.

### Define a homepage view to list posts and a detail view to show individual posts.

### Add routes for the homepage ( / ) and detail pages ( /post/<id>/ ). 

### Create a base.html template for a consistent layout with a header, footer, and {% block content %}.

### Extend base.html for the homepage to list post titles linking to detail pages.

### Extend base.html for the detail page to display the post's title and content.

### Use the admin panel to create sample posts.

### And finnally run the development server and verify.The hompage should display list of postsAnd clicking a title navigates to the corresponding detail page.
