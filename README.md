# ProyectoCoder

Coder mi primer proyecto

# URL DEL FORMULARIO  
http://127.0.0.1:8000/v2/pentrega/

# URL DEL FORMULARIO SEARCH
http://127.0.0.1:8000/v2/search/


# Primer entrega MODELS

ruta : carpeta proyectocoder  > carpeta Pentrega  > file models.py


# Primer entrega FOMRULARIO VISTA

ruta: carpeta proyectocoder  > carpeta Pentrega  > file views.py


# Primer entrega FOMRULARIO URLS

ruta: carpeta proyectocoder  > carpeta v2  > file urls.py


# Primer entrega FOMRULARIO HTML

ruta: carpeta proyectocoder  > carpeta templates  > carpeta v2 > index.html


# Primer entrega FOMRULARIO SEARCH VISTA

ruta: carpeta proyectocoder  > carpeta Pentrega  > file views.py


# Primer entrega FOMRULARIO SEARCH URLS

ruta: carpeta proyectocoder  > carpeta v2  > file urls.py


# Primer entrega FOMRULARIO SEARCH HTML

ruta: carpeta proyectocoder  > carpeta templates  > carpeta v2 > search.html

































[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy proyectocoder

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.
