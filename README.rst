eGRID
=====

technical assessment

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/cookiecutter/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: MIT

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

API endpoints
--------------
PLANTS
^^^^^^
* list all plants 
::
   
  GET /api/plants/ 
  
 
**Parameters**

``PSTATABB: state code``

``limit: number or results limit`` 


* get plant details 
::
 
 GET /api/plants/{id} 
 

STATES
^^^^^^
* list all states 
::

    /api/states/

* get state details 
::

    GET /api/state/{id}  



Basic Commands
--------------

Populate the database with egrid dataset 
^^^^^^^^^^^^^^^^^^^^^

* after setting up dev environnement, you will need to migrate and populate the database, use this commands::

    $ python manage.py migrate
    $ python manage.py populate_db

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy egrid

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Deployment
----------

The following details how to deploy this application.

Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html

Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html
