# Passing  OTL to user email account for inviting him in exam

## 1) Copy the code in the django server

## 2) Prepare some users' account as directed in https://github.com/amardrylab/django_adduser.git

## 3) Load your questions in qbank table of the database.

    ./manage.py shell
    >>>from otl.qp import loadquestion
    >>>loadquestion("otl/qp.dat")

## 4) Prepare your question paper in question table from qbank.

    >>>from otl.qp import createtemplate
    >>>createtemplate()

## 5) Move the generated file in template folder

    cd ..
    mv question.html template/

## 6) Run the following commands for sending emails request
    ./manage.py shell
    >>>from otl.qp import send_otl_email
    >>>send_otl_email()
    >>>exit()

## 7) Run the server


    ./manage.py runserver

## 8) Open any user account and click the link

## 9) After receiving all the answers send the results by executing the following commands

    ./manage.py shell
    >>>from otl.qp import send_result
    >>>send_result()
    >>>exit()
