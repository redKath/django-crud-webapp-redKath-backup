# django-crud-webapp-redKath
django-crud-webapp-redKath created by GitHub Classroom

### **CRUD Application**  (***Create, Read, Update and Delete***)

This is a fairly simple CRUD application with added features of:
- Login Authentication 
- Export to PDF option


The application is an activity log maker. 
![Image of Sample Screenshot of the Application](crud_app/media/Snapshot.png)

Users are required to login before able to create an activity log.

Follow these steps to setup the crud_app project:
 1. Clone the repository in your machine.
 2. Create your virtual environment.
 3. Pip install requirements.txt. (For this project, you only have 2 additional packages to install)
 4. Issue a migrate command.  
 ```python 
 python manage.py migrate
 ```
 5. Create your own superuser. 
 ```python 
 python manage.py createsuperuser
 ```
 6. Then issue the makemigrations command.
 ```python
 python manage.py makemigrations crud_app
 ```
 7. Lastly, migrate your changes.
 ```python 
 python manage.py migrate
 ```
 
 
If you have not encountered any error in the setup, you can now start the development server by issuing the command:
```
python manage.py runserver
```
Once the server is up and running you can now view the project by visiting localhost:8000 in your browser. In this project the default database in django is utilized so you need not any configurations in the database to run it. However, if you prefer to customized your database, you may do so.

Using your credentials as a superuser, you must need to login first before using the app. You can also register a new account if you prefer not to use your superuser accoutn.

After a successful login, you can click the Activity log and start using the CRUD application.

Redkath signing off :
> Happy coding everyone! All the love. :grin::relieved:
