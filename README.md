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

### Step 3: Define Homepage and Detail Views

1. **Create the Views**:

Open `blog/views.py`. Add the following code:

```python
from django.shortcuts import render, get_object_or_404
from .models import Post

# Homepage view to list posts
def post_list(request):
    posts = Post.objects.all().order_by('-created')  # Fetch posts ordered by creation date
    return render(request, 'blog/post_list.html', {'posts': posts})

# Detail view for a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetch post by primary key or return 404
    return render(request, 'blog/post_detail.html', {'post': post})
```

**Set Up URLs**:

Create a file named `urls.py` inside the `blog` app directory.

Add the following code:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Homepage URL
    path('<int:pk>/', views.post_detail, name='post_detail'),  # Detail page URL
]
```

Update the `myblog/urls.py` file to include the `blog` app URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include the blog app's URLs
]
```

**Create Templates**:

Inside the `blog` app, create a folder named `templates`, and within it, a folder named `blog`.

```bash
mkdir -p blog/templates/blog
python manage.py runserver
```

**Homepage Template**: `blog/templates/blog/post_list.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Blog Homepage</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <ul>
        {% for post in posts %}
            <li>
                <a href="{{ post.id }}/">{{ post.title }}</a> 
                ({{ post.created|date:"Y-m-d H:i" }})
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Detail Page Template**: `blog/templates/blog/post_detail.html`:
     
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.created|date:"Y-m-d H:i" }}</p>
    <p>{{ post.content }}</p>
    <a href="/">Back to Homepage</a>
</body>
</html>
```

**Test the Views**:

Run the server. Visit the homepage at `http://127.0.0.1:8000/`. There are no posts yet, all you will see is `Blog Posts`.

### Step 4: Add Sample Posts Through the Admin Panel

**Log In to the Admin Panel**:

Open the admin panel in your browser: `http://127.0.0.1:8000/admin`.

Use the superuser credentials you created earlier during `createsuperuser`.

**Add Posts**:

In the admin panel, locate the `Post` model under the `Blog` section. After adding posts, visit `http://127.0.0.1:8000/`. The homepage should now list the two posts.

### Step 5: Add routes for the homepage ( / ) and detail pages ( /post/<id>/ ). 



### Create a base.html template for a consistent layout with a header, footer, and {% block content %}.

### Extend base.html for the homepage to list post titles linking to detail pages.

### Extend base.html for the detail page to display the post's title and content.

### Use the admin panel to create sample posts.

### And finnally run the development server and verify.The hompage should display list of posts And clicking a title navigates to the corresponding detail page.
