#### Installation
    pip install requirements.txt

#### Making migrations
    python manage.py makemigrations
    python manage.py migrate
    
####Generating faker data
    python reports_faker.py

#### Running tests
    python manage.py test

#### Starting app
    python manage.py runserver
   

Docker case:
-------------

#### Installation
    docker-compose build

#### Making migrations
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    
## Generating faker data
    docker-compose run web python reports_faker.py
    
#### Running tests
    docker-compose run web python manage.py test
    
#### Starting app
    docker-compose up
   
