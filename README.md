# Django project for learning proposal
- Based on the book "Django 4 By Example, Fourth Edition" by Antonio Melé
- Building a Blog Application
- https://github.com/PacktPublishing/Django-4-by-example

## Commands
1. python -m venv .venv
2. .venv\scripts\activate
3. python -m pip install Django==5.0.2
4. python.exe -m pip install --upgrade pip
5. pip freeze > requirements.txt
6. django-admin startproject mysite .
7. python manage.py migrate
8. python manage.py runserver
9. python manage.py startapp blog

## Observations
- Dot end at the command "django-admin startproject mysite ." to not create folder inside folder. Keep root folder. 

## Project Files
### manage.py
- No editing.
- Command-line to interact with the project.
### mysite/
#### __init__.py
#### asgi.py
#### settings.py
##### DEBUG
- If True, Django will display detailed error pages.
- Set it to False in Production environment.
- Never deploy a site into production with DEBUG turned on because you will expose sensitive project-related data.
##### ALLOWED_HOST
- Only used in production. 
- Domain, host to serve Django.
##### INSTALLED_APPS
- Applications are active.
##### MIDDLEWARE
- List middleware to be executed.
##### ROOT_URLCONF
- Root URL patterns
##### DATABASES
- Dictionary of settings database. 
- Require a default database, SQLITE default configuration.
##### LANGUAGE_CODE
- Default language code.
##### USE_TZ
- Activate or deactivate timezone.
#### urls.py
#### wsgi.py

## App Files and Folders
### apps.py
- main configuration of the blog application
### admin.py
- [Admin objects](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#modeladmin-objects)

## To study
- [Design philosophies](https://docs.djangoproject.com/en/5.0/misc/design-philosophies/)
- Multiple environments and different configurations files
- Not Using delete cascading. How to implement other solution: [ForeignKey.on_delete](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.on_delete)
- [Template language](https://docs.djangoproject.com/en/5.0/ref/templates/language/)
--  template tags, template variables, and template filters



## Concepts
### Project
- Django installation with some settings.
- Website, which contains several applications, such as a blog, wiki, or forum, that can also be used by other Django projects.
### Application
- Group of models, views, templates, and URLs.
### MTV (Model-Template-View)
#### Model

#### Template
#### View
#### URLs
#### Migrations
#### Template
- {% tag %}
- {{ variable }}
- {{ variable|filter }}



## Request Response Flow 
- Figure 1.1 
```mermaid
    flowchart TD
        A[Web Browser] --> 
```
