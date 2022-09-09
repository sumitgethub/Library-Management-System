# Library-management-system

####### Inportant #######
Admin login id
email = admin@gmail.com
password = admin

#PROJECT SETUP

1 activate vertualenv = source venv/bin/activate

2 intall all requirement = pip3 install -r requirements.txt

3 run project = python3 manage.py runserver

4 admin-pannel = http://127.0.0.1:8000/admin/

username = admin
email = admin@gmail.com
password = admin

#Api-Endpoint

#Admin-module

register_admin = http://127.0.0.1:8000/user/register/

its give you a access token and refresh token

login_admin = http://127.0.0.1:8000/user/login/ its give you a access token and refresh token

#Book-module

get-book = http://127.0.0.1:8000/app/api/

about this api = show all book

post-book = http://127.0.0.1:8000/app/api/

In post api you can create your Book you need to add your access token remember your id is admin id its mandatory

ex:- {
    "title" : "Python",
    
    "subtitle" : "Modern Python",
    
    "author" : "Admin"
}

edit-book = http://127.0.0.1:8000/app/api/1/ # 1 is book id

In edit book you pass your jwt token and #book_id and what you want to change 

ex:- {

    "title" : "Django-updated"
}


delete-book = http://127.0.0.1:8000/app/api/1/ # 1 is book id

pass your book_id and access token


#work on this module

1 first i create a custom user

2 then i add jwt authantication

3 then i crete book application

#how this all are work

first you create your id in #registration Api its give you a access token and a refresh token

and go to admin pannel and update any user to admin and then #login api you only see your book 

if your token or user is not admin ,if you are admin then you

perform #create book api #edit book api #delete book api
