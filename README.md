# {{ Sistema de Controle de Portaria | SFurnas - Portaria }}

# Introduction

The goal of this project is to provide a minimalistic django project template for access control on premises, which has the basic requirements and can be improved.

Template is written with django 4.0.5 and python 3.10.4 in mind.

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/Hulgo/django_portaria.git
    $ cd django_portaria
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver