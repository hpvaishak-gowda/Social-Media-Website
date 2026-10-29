#  Social Media Website

A social media web application built using **Python and Django** that allows users to share posts, upload images, interact with content through likes, and view posts shared by other users.

## Features

* **User Authentication** — User registration, login, and logout.
* **Create Posts** — Upload images with captions.
* **Home Feed** — View posts shared by users.
* **Like Posts** — Like posts and view their like counts.
* **User Profiles** — View user profiles and profile pictures.
* **Media Management** — Upload and display profile pictures and post images.
* **Responsive Interface** — A user interface built using HTML, CSS, and Bootstrap.
* **Database Integration** — Store user profiles, posts, captions, and like counts.

## 🛠️ Tech Stack

| Technology   | Purpose                  |
| ------------ | ------------------------ |
| Python       | Backend programming      |
| Django       | Web framework            |
| SQLite       | Database                 |
| HTML5        | Page structure           |
| CSS3         | Styling                  |
| Bootstrap    | Responsive UI components |
| JavaScript   | Frontend interactions    |
| Font Awesome | Icons                    |

## Project Structure

```text
Social-Media-Website/
│
├── media/
│   ├── profile_images/
│   └── post_images/
│
├── socialmedia/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── userauth/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── main.html
│   └── modal.html
│
├── manage.py
├── db.sqlite3
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository


git clone <https://github.com/hpvaishak-gowda/Social-Media-Website.git>


Navigate into the project directory:


cd Social-Media-Website


### 2. Create a Virtual Environment


python -m venv venv


### 3. Activate the Virtual Environment

**Windows:**


venv\Scripts\activate


**macOS/Linux:**


source venv/bin/activate


### 4. Install Dependencies

Install Django and Pillow, which Django uses for image processing.


pip install django pillow


If you have a `requirements.txt` file, you can install all project dependencies using:


pip install -r requirements.txt


### 5. Apply Database Migrations


python manage.py makemigrations
python manage.py migrate


### 6. Create a Superuser (Optional)

To access the Django administration panel:


python manage.py createsuperuser


### 7. Start the Development Server


python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/

## Media Configuration

The project uses Django's media configuration to store uploaded images.

Add the following settings to `settings.py`:

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


During development, configure `urls.py` to serve media files:


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )


Uploaded images are stored in the media directory, including profile pictures and post images.

## Database Models

The application includes two primary models:

* **Profile:** Stores user profile information, including profile pictures, biography, and location.
* **Post:** Stores post details, including the username, uploaded image, caption, creation date, and number of likes.

### Future Improvements

* Add comments and replies to posts.
* Implement follow and unfollow functionality.
* Add a personalized news feed.
* Improve profile editing and account settings.
* Add search functionality for users and posts.
* Implement notifications for likes and other interactions.
* Improve mobile responsiveness and interface design.

## Learning Outcomes

Through this project, I practiced:

* Building web applications using Django.
* Implementing user authentication.
* Creating Django models and working with SQLite.
* Handling image uploads and media files.
* Using Django templates and template inheritance.
* Implementing database operations through Django ORM.
* Integrating frontend technologies with a Python backend.

##  Author

**Vaishak HP**

Aspiring Python Backend Developer, passionate about building web applications and learning backend technologies.

## License

This project is intended for educational and learning purposes.


### System Design 

## System Design

The application follows a client-server architecture, with Django handling backend logic, SQLite storing application data, and HTML, CSS, JavaScript, and Bootstrap providing the frontend interface.

### Architecture


                 ┌──────────────────────┐
                 │       User           │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Frontend Interface │
                 │ HTML, CSS, Bootstrap│
                 │     JavaScript       │
                 └──────────┬───────────┘
                            │ HTTP Requests
                            ▼
                 ┌──────────────────────┐
                 │    Django Backend   │
                 │     URLs & Views    │
                 │ Authentication      │
                 │ Business Logic      │
                 └──────────┬───────────┘
                            │
                 ┌──────────┴───────────┐
                 ▼                      ▼
       ┌──────────────────┐   ┌──────────────────┐
       │  SQLite Database │   │   Media Storage  │
       │ Users, Profiles, │   │ Profile Pictures │
       │ Posts and Likes  │   │   Post Images    │
       └──────────────────┘   └──────────────────┘


### Main Components

* **Frontend:** Provides the interface for creating posts, uploading images, viewing the feed, and liking posts.
* **Django Backend:** Processes HTTP requests, handles authentication, validates input, and manages application logic.
* **Database:** Stores user profiles, post information, captions, and like counts.
* **Media Storage:** Stores uploaded profile pictures and post images.
* **Django Admin:** Provides an administrative interface for managing application data.

### Data Flow

1. A user interacts with the frontend.
2. The browser sends an HTTP request to the Django application.
3. Django processes the request and interacts with the database or media storage.
4. Django returns an HTTP response.
5. The browser displays the resulting page and images.
