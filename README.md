## Programs's description
This web app is a basic chat room app.

# How to launch the program
Follow the following steps: 

* Make sure that you are using python3, and have a virtual environment running python3. 

* In order to create a virtual environment, type in the following command: `virtualenv yourvirtualenvname`

* Use the following command to access your virtual environment: `source yourvirtualenvname/bin/activate`

* Now that you are in your virtual environment, make sure that you are in your project directory

* Install the requirements.txt by running this command: `pip install -r requirements.txt`, this will install all module
you need to run your application.

* In the terminal run the following command:
`python manage.py migrate`, and run `python manage.py runserver` to launch your application, then start development
server at `http://127.0.0.1:8000/` in your browser.

* In order to have access to the administration of the application, you should create a super user, to do that
type in the following command: `python manage.py createsuperuser`, then you will be prompted to enter a username, email and 
password.
