# Tech Blog

A simple tech blog built with Django.

## Installation

	Ensure you have Python 3.8 or later installed.

## Clone the repository to your local machine:

	git clone https://github.com/yourusername/techblog.git

## Navigate to the project directory

	cd techblog

## Install the required packages

	pip install -r requirements.txt

##Setting Up the Database

	Before running the app, you need to set up the database:

	python manage.py makemigrations
	python manage.py migrate

## Create a superuser to access the Django admin interface:

	python manage.py createsuperuser
	Running the Application

## Start the development server:

	python manage.py runserver

	You can access the application at http://127.0.0.1:8000/.
	The Django admin site is accessible at http://127.0.0.1:8000/admin/.

## Features

	Create, edit, and delete blog posts via the Django admin site.
	View a list of all blog posts on the home page.
