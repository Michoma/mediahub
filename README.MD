### Media HUB 
media sharing platform that has role based access 
- teacher role - manage assigned student content  , media uploads
- student role - share media uploads 
- admin role - overseeing all content and managing the platform 

### Tools of use 
- django 
- python libraries (ready made snippets for a specific job)
   - pillow : media transactions in python frameworks (absolute media url ,  )
   - cloudinary : media storage and also url access generation (url -> save to database for an upload)
   - python-decouple : media tasks 

### Apps in projects
  - accounts : authentication and authorization (signups, login , forgot password)
  - media_assets : uploads tasks , displays , updates 

### steps 
- install the libraries : 
   pip install libraryname
   pip install -r requirements.txt
- create our apps
- configure our project settings 
     - register our apps  
     - register cloudinary (give the cloudinary configs)
     - register a custom authentication process 
     - emails registry 

### Authentication and Authorization  (accounts app)
Authentication = identity identification, who are you ? 
Authorization = access priviledges - role based authorization , token based authorization 

1. Create our custom user model - models.py
2. Extend the integrated form captures - forms.py
3. Create the views action for registration and login , logout and profile view , 
custompasswordresetview , custompasswordresetconfirmview - views.py
4. Register the views actions as URL route - urls.py 
5. Register the models for admin to use and manage content on - admin.py
6. Register the apps url to the projects urls = project/urls.py
7. Create the templates 
   - create a templates folder - within the app 
   - create a global templates folder - register it's configuration in the settings.py file 
8. Make databases migrations and then populate the templates 
   python manage.py makemigrations 
   python manage.py migrate

### Template creation
1. Configuration level file : base.html 
   - Defining your blocks : title , extra_css , content (most important) , footer, extra_js
   - Linking to global stylesheet / style lib. (bootstrap)
   - Link to global js files 

### Configuring our environmental variables
1. Create a .env file for development purposes -  store your info as a reference



### MPESA INTERGRATI














