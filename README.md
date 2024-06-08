# Milestone Project 4(PP4) - 1link-event-management-system
![All devices](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/screenshots/combine.png)

[View the live project here.](https://event-management-system-3014bff26c17.herokuapp.com/)

1link-event-management-system is a platform to manage events, allowing users to create, view, edit, and delete events. It can have features like user registration, event booking, and ticket management.

## Table of Contents
* [Introduction](#introduction)

* [UX](#ux) 
    - User Stories
        -  First Time Visitor Goals
        -  Returning and Frequent Visitor Goals
        -  Site Administrator Goals  
* [Layout](#layout)

    - Design
        - Colour scheme
        - Typography
        - Images
    - Wireframes
        - Discrepancy with Original Ideas
        - Links to Wireframes
* [Features](#features)
    - Responsivity
    - Interactive Elements
    - Features to add in future

* [Technologies Used](#technologies-used) 
    - Languages Used
    - Frameworks, Libraries and Programs Used  

* [Testing](#testing)
    - Testing User Stories from User Experience (UX) Section
    - Further Testing
    - Unresolved Bugs 

* [Deployment](#deployment)

* [Credits](#credits)

# Introduction

1link-event-management-system is a platform to manage events, allowing users to create, view, edit, and delete events. It can have features like user registration, event booking.

Beside being able to view pages like the home page, menu and the contact page, users are also able to create an account, sign in, avail of the event booking feature and view bookings, which unregistered users don't have access to. Through the booking and the view booking navbar link users can access all their previous bookings, edit and delete them. Site user administrators have access to all bookings and all create, edit and delete functionalities.
The site has been designed to be fully responsive on desktop, laptop, tablet and mobile devices.


# UX

-   ### User stories 

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the business.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        3. As a First Time Visitor, I want to sign up for a user account to access restricted content.
        4. As a First Time Visitor, I want to create a event booking, view booking details, and learn what changes I can make on created bookings.
        5. As a First Time Visitor, I want to sign out of my user account at the end of the session to keep my account related details safe.
        

    -   #### Returning and Frequent Visitor Goals

        1. As a Returning and Frequent Visitor, I want to sign into my user account.
        2. As a Returning and Frequent Visitor, I want to create a event booking, view my current and previous event details, and alternatively edit them or delete them.
        3. As a Returning and Frequent visitor I want to like the restaurant services.
        4. As a Returning and Frequent Visitor, I want to sign out of my account at the end of the session to keep my account safe.

    -   #### Site Administrator Goals
        1. As a Site Administrator I would like to be able to create, view, edit and delete events.
        2. As a Site Administrator I would like to be able to create, view, edit and delete UserGroups.
        3. As a Site Administrator I would like to be able to create, view, edit and delete Users.
        
        
# Layout
-   ### Design
    -   #### Colour Scheme
        -   The main colours in the website theme for header, background, footer and text labels are Black, Blue, and White.
    -   #### Typography
        -   I used a standard Bootstrap theme with all the components and styling. Montserrat  and Segoe UI are the main fonts used.
    -   #### Imagery
        -   Imagery was chosen to go with the website's colour and content theme. I'm using Events and Booking  images, soothing colours and attractive graphics. 

*   ### Wireframes
    -   #### Discrepancy with original ideas
        -   I originally intended to create my own HTML pages and CSS styling, however, I decided to use a standard Bootstrap theme instead, which saved me a huge amount of time. I simply followed the theme layout, customized text labels for various forms, so the original wireframes were not used at all. As the theme is fully responsive, I didn't create mobile device wireframes after deciding to use Bootstrap. By using a Boostrap theme, my theme is more unified, too.
    -   #### Links to Wireframes

        -   Frontend Wireframe - [View](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/wireframes/frontend_wireframe.pdf)

        -   User Dashboard Wireframe - [View](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/wireframes/User_dashboard.pdf)

        -   User Dashboard Login Wireframe - [View](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/wireframes/User_Dashboard_Login.pdf)

        -   Login Page Wireframe - [View](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/wireframes/Login%20Page%20Wireframe.pdf)

        -   User Dashboard Register Wireframe -[View](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/wireframes/User_Dashboard_Register.pdf)
          
        -   User Dashboard Bookings Wireframe -[View](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/wireframes/User_dashboard_Bookings.pdf)
          
        -   User Dashboard Events Wireframe -[View](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/wireframes/User_dashboard_events.pdf)
          
        -   User Dashboard Create Events Wireframe -[View](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/wireframes/User_dashboard_Create_events.pdf)
          
        -   User Dashboard Manage Events Wireframe -[View](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/wireframes/User_dashboard_Manage_Events.pdf)



# Features

-   ### Responsivity

The application is responsive on all device sizes, thanks to the Boostrap theme. In mobile view there is a collapsible menu icon. All images, text labels, forms get appropriately resized. However there are small exceptions.

-   ### Features to add in future   
    -   #### I would like to add A Notification System, where users get latest Events notification after subscription.

## Technologies Used
# Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used
1. [Django:](https://www.djangoproject.com/)
    - The Python-based Django framework was used to set up the structure, functionalities,  data model and database of the website.
1. [Bootstrap:](https://startbootstrap.com/theme/freelancer)
    - Freelancer Bootstrap theme was used to assist with the responsiveness and styling of the Front-End website.
1. [Bootstrap:](https://startbootstrap.com/template/sb-admin)
    - SB-Admin Bootstrap theme was used to assist with the responsiveness and styling of the User-Panel Dasboard.  
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript. It is also used for the Bootstrap Tempus Dominus datetime picker.
1. [Javascript:](https://en.wikipedia.org/wiki/JavaScript)  
    - Javascript was used to define visibility duration for popup messages that signal successful completion of different form related activities.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [PostgreSQL database:](https://en.wikipedia.org/wiki/PostgreSQL)

1. [Heroku:](https://www.heroku.com/)
    -  Heroku is used for the deployment and ultimate cloud-based storage of my application.
    -  Also Heroku CLI

# Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every pagefor HTML and CSS of the project to ensure there were no syntax errors in the project. I used the inbuilt pylint compiler to validate the Python files.

-   [W3C URI Validator](https://validator.w3.org/#validate_by_uri)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [Gitpod Pylint](https://pylint.org/)

-



# Deployment

### Heroku

The project was created in Github and pushed to Heroku using Git

## Initial Deployment  

1. **Create a Heroku App**:
   - Log in to Heroku and create a new app.

2. **Add Postgres to the Heroku App**:
   - In the Heroku dashboard, navigate to the Resources tab.
   - Under Add-ons, search for "Heroku Postgres" and add it to your project.

3. **Get the DATABASE_URL from Heroku**:
   - In the Heroku Settings tab, click on "Reveal Config Vars".
   - Copy the DATABASE_URL value for later use.

4. **Configure the Database in Django**:
   - In your `settings.py` file, update the database configuration:
     ```python
     import dj_database_url

     DATABASES = {
         'default': dj_database_url.config(default='your_default_database_url')
     }
     ```

5. **Generate a Django Secret Key**:
   - You can generate a secret key using Python:
     ```python
     import random
     import string

     secret_key = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=50))
     print(secret_key)
     ```
   - Copy the generated secret key and add it to your Heroku config vars and `settings.py`.

6. **Update Allowed Hosts**:
   - In your `settings.py`, set the allowed hosts:
     ```python
     ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com', 'localhost']
     ```

7. **Configure Static and Media Files**:
   - Set up Cloudinary or any other service you prefer. For Cloudinary:
     - Sign up and get your Cloudinary API details.
     - Add Cloudinary to your `requirements.txt`:
       ```
       django-cloudinary-storage
       cloudinary
       ```
     - Update your `settings.py`:
       ```python
       INSTALLED_APPS += [
           'cloudinary',
           'cloudinary_storage',
       ]

       CLOUDINARY_STORAGE = {
           'CLOUD_NAME': 'your_cloud_name',
           'API_KEY': 'your_api_key',
           'API_SECRET': 'your_api_secret'
       }

       STATIC_URL = '/static/'
       STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
       STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

       MEDIA_URL = '/media/'
       DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
       ```

8. **Create Required Files**:
   - **runtime.txt**:
     ```
     python-3.9.2
     ```
   - **Procfile**:
     ```
     web: gunicorn your_project_name.wsgi
     ```

9. **Prepare and Push Code to GitHub**:
   - Ensure you have a `requirements.txt`:
     ```bash
     pip freeze > requirements.txt
     ```
   - Commit and push your changes:
     ```bash
     git add .
     git commit -m "Prepare for Heroku deployment"
     git push origin main
     ```

10. **Deploy to Heroku**:
    - In Heroku, under the Deploy tab, connect your app to GitHub.
    - Enable Automatic Deployments and deploy the branch.
    - Once deployed, open the app to check if everything is working.

11. **Turn Off Debug Mode**:
    - Set `DEBUG = False` in `settings.py`.
    - Remove `DISABLE_COLLECTSTATIC` from Heroku config vars.
    - Commit and push the changes:
      ```bash
      git add .
      git commit -m "Disable debug mode and enable collectstatic"
      git push origin main
      ```

12. **Run Migrations and Collect Static Files**:
    - In the Heroku CLI, run:
      ```bash
      heroku run python manage.py migrate
      heroku run python manage.py collectstatic
      ```

## Running the App Locally

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/1link-event-management-system.git
    cd 1link-event-management-system
    ```

2. **Create a Virtual Environment and Install Dependencies**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Set Up Local Environment Variables**:
    - Create a `.env` file in your project root and add:
      ```
      SECRET_KEY=your_secret_key
      DATABASE_URL=your_database_url
      CLOUDINARY_URL=your_cloudinary_url
      ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Register or Log In**:
   - Use the registration or login page to create an account or log in.

2. **Create and Manage Events**:
   - Use the user dashboard to create and manage events.

3. **Profile Management**:
   - Update your profile and manage your bookings.

## Contributing

1. **Fork the Repository**.
2. **Create Your Feature Branch** (`git checkout -b feature/your-feature`).
3. **Commit Your Changes** (`git commit -am 'Add some feature'`).
4. **Push to the Branch** (`git push origin feature/your-feature`).
5. **Create a New Pull Request**.

# Screenshots:
Some Snipped of my project
Front End:
![All devices](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/screenshots/Laptop.png)
![All devices](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/screenshots/Modal_front_end.png)
![All devices](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/screenshots/tab2.png)
User Panel:
![All devices](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/screenshots/user_panel.png)
![All devices](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/screenshots/mobile_userpanel.png)
![All devices](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/screenshots/Manage.png)
Admin Panel:
![All devices](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/screenshots/django.png)
![All devices](https://github.com/ihr2295/1link-event-management-system/blob/main/static/docs/screenshots/django2.png)

# Credits

### Code
-   [Bootstrap Template](https://startbootstrap.com/): Start Bootstrap Theme used throughout the project  to style pages and make site responsive.
-   [Bootstra5 Template](https://startbootstrap.com/template/sb-admin): SB-Admin Bootstrap Theme used throughout the project  to style pages and make User Dashboard responsive.

-   [Official Django Documentation](https://docs.djangoproject.com/en/3.2/) was researched for syntax, code expressions, code functionalities.

-   Stack Overflow was was researched for syntax, code expressions, code functionalities, problem solving. Validation function for reservation date and time is from there.

-   ChatGPT


### Media

-   Images are from freepik.com and from the Bootstrap template.
### Acknowledgements
-   My family for their patience. Thanks for putting up with me in these intense times.
-   StackOverflow
-   ChatGPT
