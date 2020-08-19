# blog_app

Installation Instructions
Clone the project.

$ git clone https://github.com/zymrytekabashi/blog_app.git
cd intro the project directory

$ cd blog_project
Create a new virtual environment using Python 3.6.4 and activate it.

$ python -m venv env
$ source env/bin/activate
Install dependencies from requirements.txt:

(env)$ pip install -r requirements.txt
Migrate the database.

(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(Optionally) load sample fixtures that will populate the database with a handful of users and tweeters.


Run the local server via:

(env)$ python manage.py runserver
Done!
The local application will be available at http://localhost:8000
