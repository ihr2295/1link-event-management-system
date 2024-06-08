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

### Unresolved Bugs

-   #### In general
    1. In the Gitpod Development Environment the site works with full CSS styling by now when Debug is off in the settings.py file. However, the admin page (/admin) comes up without CSS styling.



# Deployment

### Heroku

The project was created in Github first and then transferred to the Gitpod development environment by the use of the green Gitpod button.

## Initial Deployment  

1. In the Gitpod environment a skeleton django project was created (project, app and relating files).
2. A Heroku app was created in Heroku.
3. In Heroku, under the Resources tab, in Add-ons, I searched for Postgres. When found I submitted a request to use it. 
This attached Heroku Postgres to my project in Heroku.
4. In the Heroku Settings tab I clicked on "Reveal Config Vars" and copied the automatically added postgres link from beside the DATABASE_URL variable. 
5. In Gitpod dev environment, I looked for the env.py file that was automatially generated from the CI template at the beginning. This file stores environment variables.
6. After importing the os into the env.py file, I added the database URL from Heroku into env.py.
7. I added a secret key in the env.py file after having it generated on the [Django Secret Key Generator - MiniWebtool](https://miniwebtool.com/django-secret-key-generator/) website.
8. I added the secret key into the Heroku Settings > config vars as well.
9. In the settings.py file in Gitpod I imported os and added an if statement saying that outside the development environment the environment variables must be used from env.py, including the secret key.
10. Still in the settings.py file, I commented out the present code for databases and added code to use the currently set up django database URL as set in the env.py file and also in the Heroku config vars.
11. I migrated these changes in Gitpod using python3 manage.py migrate
12. To get static and media sites stored on Cloudinary, I went to the dashboard of my previously created Cloudinary account and copied the API Environment Variable.
13. I added this to the Gitpod env.py file and into the Heroku Settings > config vars. 
14. I also added DISABLE_COLLECTATIC = 1 to the Heroku config vars. 
15. I added cloudinary and cloudinary_storage to the installed apps in settings.py. 
16. I set up the static file storage, static file directory, the static root, the media url, the default file storage and the templates directory in settings.py.
17. I added the Heroku name followed by herokuapp.com to the ALLOWED_HOSTS variable name in settings.py, followed by a comma and 'localhost' (to allow running in the development environment).
18. I created 3 directories at the top level: media, static, templates.
19. I created a Procfile at the top level directory. 
20. I did a git add, git commit and git push.
21. In the Deployment tab in Heroku, in Deployment method, I added Github, set up Enable Automated Deployment, looked for my Github repository, connected my Heroku app to it and clicked on Deploy Branch at the bottom of the page.
22. When I opened the app after the app was built and deployed, I saw the success message page with a rocket.
23. After  my application was built, as the first step of the final deployment I turned Debug to False in the settings.py file in Gitpod.
24. In Heroku I removed the DISABLE_COLLECTSTATIC variable.
25. I saved my changes on all my files and performed a git add, git commit and git push.
26. As automatic depoyment had been enabled in Heroku, I waited until my app was built, then I opened it and made sure that all functionalities work.

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