# Wasteless Table: Ingredient Search & Recipe Reviews

Wasteless Table is an online tool and blog that encourages users to avoid discarding food by utilizing what ingredients they already have in the kitchen. A search function provides recipes tailored to what ingredients the user has at hand. Users are invited to join and contribute to a community of people reviewing, sharing and updating recipes. 

Ireland is estimated to generate 1.1 million tonnes of food waste per year, according to the [Environmental Protection Agency](https://www.epa.ie/publications/circular-economy/resources/nature-and-extent-update-15th-June.pdf)


Live Website here: [Wasteless Table](https://portfolio-project-four-1f2f0bc1d6a0.herokuapp.com/)

![alt text]()

## Table of Contents
- Project Overview
- Process
    - Problem Statement
    - Research
    - Design
    - Development
        - Link to GitHub project board
        - User Stories
- Database
    - Reviews
    - Comments
    - Ingredients
    - Utensils
    - Cuisine Types
- Features
    - Crud Functionality
        - Add Review
        - Update Review
        - Delete Review
        - Add Comment
        - Edit Comment
        - Delete Comment
    - Authentication & Authorisation
    - Navigation
    - Recipe Search
    - Recipe Blog
    - About
    - Defensive Design
- Roadmap
- Bugs
- Technologies Used
    - Core Development Technologies
    - Libraries, Frameworks and Packages
    - Python & Django Packages
    - Infrastructural Technologies
- Testing
- Deployment
    - Local Deployment
    - Heroku Deployment
    - Environment Variables
- Credits

## Overview

## Process

### Research

### Design

### Development

### User Stories

- As a site user, I can search for so that I can find a recipe to eat.
- As a site user, I can search with ingredients, tag names or cuisine types so that I can find a list of recipes.

I implemented a search functionality on my website that allows users to search for recipes using a list of ingredients. The search also returns recipes based on cuisine type or dish name. A used who has reviewed the ingredients they have in their kitchen would want to input them one by one so the search functionality allows the inputs of tag names.

<details>
<summary>User Story 1 & 2</summary>
<br>

![User Story 1 & 2]()

</details>

- As a site user I can see my user profile so that I can see my details.

I have not yet achieved this capability on the website. Users can sign-in, login and if authenticated, leave reviews and comments. CRUD functionality is implemented with a link to Update Review if the user is the author of the review. I considered a dashboard for the user of some kind to not be a minimal viable product so it was not my focus.

<details>
<summary>User Story 3</summary>
<br>

![User Story 3]()

</details>

- As a site user I can view a list of paginated recipes so that select the recipe details.

I implemented pagination for the list of recipes to enhance user experience and page loading speed. Django's built-in pagination features to split the recipe list into manageable pages was used to do this.

<details>
<summary>User Story 4</summary>
<br>

![User Story 4]()

</details>

- As a user I can submit recipe reviews so that the admin can add a recipe review to the blog.

I created a database model for storing recipe reviews, associating them with specific recipes and users. I used a form for users to submit reviews for recipes. This is initially not published. It is the admins task to review the entry before publishing.

<details>
<summary>User Story 4</summary>
<br>

![User Story 4]()

</details>

- As a site user I can register an account so that I can leave a comment, rating and like.

I integrated Django's built-in authentication views and forms for user registration. Users can register with an account name and password. I have not yet given the user the ability to set up an account with an email. Users can be managed from the admin panel.

<details>
<summary>User Story 5</summary>
<br>

![User Story 5]()

</details>

- As a Site User I can click on a recipe so that I can see the details.

I developed a detailed view for each recipe, allowing users to click and view comprehensive details. A URL routing mechanism was used to handle recipe-specific views. By clicking a recipe, the user is taken to the entire blog post containing the review and comment features.

<details>
<summary>User Story 6</summary>
<br>

![User Story 6]()

</details>

- As a site administrator I can approve posts so that the blog is populated.

I used Django's admin interface to manage and approve recipe posts. I had to create custom admin views to maintain the posts. The admin has the ability to review the recipe, ingredients, utensils and images of the post before publishing.

<details>
<summary>User Story 7</summary>
<br>

![User Story 7]()

</details>

- As a site administrator I can create, read, update and delete so that the blog's content can be managed.

I developed views and forms for creating, reading, updating, and deleting recipes. Appropriate access controls were used to ensure only authorized users can perform these actions.

<details>
<summary>User Story 8</summary>
<br>

![User Story 8]()

</details>

- As a site administrator I can approve or disapprove comments and recipes so that I can filter content.

The approval system was extended to handle both comments and recipes. Similarly providing admin tools the functionality to easily approve or disapprove content.

<details>
<summary>User Story 9</summary>
<br>

![User Story 9]()

</details>

- As a site user and administrator I can view the comments on a recipe so that see what is being talked about.
- As a site user and administrator I can view the rating and number of likes/upvotes on each recipe so that I can determine the best and popular ones.

Views were used to display comments associated with each recipe. The comments and user who wrote it is rendered in the template. Similarly the overall rating and number of likes/upvotes for each recipe was displayed for anybody to see..

<details>
<summary>User Story 10 & 11</summary>
<br>

![User Story 10 & 11]()

</details>

The three screenshots below were taken at the start of development, the midway point and at the final stage. They show three columns - to do, in progress and completed. Only over the course of the few weeks developing the project did the lessons on Agile development begin to really make sense. In completing my own project, I recognised mistakes I had made in the planning process and how my development process had to completely change given the timeframe that the project needed to be completed in. The lessons on Agile development - and the entire point of the Agile manifesto - began to really make sense. 

Similarly, at the start of development, I never realised how useful of a tool GitHub projects/views could be.

<details>
<summary>Initial Agile Screenshot</summary>
<br>

![Initial Agile Screenshot](static/readme_images/agile/project_agile_initial_screenshot.png)

</details>

<details>
<summary>Midway Agile Screenshot</summary>
<br>

![Midway Agile Screenshot](static/readme_images/agile/project_agile_initial_screenshot.png)

</details>

<details>
<summary>Final Agile Screenshot</summary>
<br>

![Final Agile Screenshot](static/readme_images/agile/ZenTableAgileView.png)


I initially had the prioritisation of what features I needed to implement written down. I was recommended to use GitHub projects for this too so using the User Stories I created a new board to help visualise what did and what did not need to be prioritised. 

<details>
<summary>MoSCoW Prioritisation Screenshot</summary>
<br>

![MoSCoW Prioritisation Screenshot](static/readme_images/agile/ZenTableMoSCoW.png)

</details>

Again, using GitHub projects to help maintain the direction of my project, I created another board with Tasks to help visualise what I needed to do to complete my user stories.

<details>
<summary>Users & Tasks Screenshots 1</summary>
<br>

![Users & Tasks Screenshots 1](static/readme_images/agile/zentablestasks1.png)

</details>

<details>
<summary>Users & Tasks Screenshots 2</summary>
<br>

![Users & Tasks Screenshots 2](static/readme_images/agile/zentabletasks2.png)

</details>

<details>
<summary>Users & Tasks Screenshots 3</summary>
<br>

![Users & Tasks Screenshots 3](static/readme_images/agile/zentabletasks3.png)
</details>

</details>

### Data Models

#### PP4APP

**Review** represents a single recipe review. It's contains all the information for a specific review review on the review blog. It includes information such as:

- id
- title
- url
- slug
- author
- ingredients
- utensils
- updated_on
- content
- featured_image_a
- featured_image_b
- excerpt
- created_on
- cuisine_type
- status
- prep_time
- up_vote
- down_vote

**Ingredient** is a table containing a list of ingredients. It is in a many to many relationship with the review table. It contains a list of ingredients for each of our recipes:

- id
- name

**Utensil** is a table containing a list of utensils. It is in a many to many relationship with with our review table. It contains a list of utensils that can be associated with each review:

- id
- name

**CuisineType** is a table containing different cuisine types. It is in a many to one relationship with out review table. It contains the cuisine type to be associated with each review: 

- id
- name
- slug
  
**Comment** is a table to hold our comments. Each comment is in a one to one relationship with our review table as each comment is associated with one recipe:

- id
- review
- name
- email
- body
- created_on
- approved


<details>
<summary>Data Model Diagram</summary>
<br>

![Data Model Diagram](static/readme_images/datamodel.png)
</details>


## Features

### CRUD Functionality

**Create:** Any registered user can leave a review on a recipe provided by the API. A form is rendered on the submit review page to create a recipe review. The form is submitted and before it appears as published, it must be reviewed by the admin to monitor content.

**Read:** Any user of the website irrespective of registration status can read the reviews or comments posted once they have been published by the admin.

**Update:** If the user who wrote a specific post has logged in and is viewing a post they wrote, a button appears with the option to update the form. The clickable link will take them to an update review page with a form rendered allowing them to update their review. Update functionality is not yet available for comments. 

**Delete:** Similarly, if a user who wrote a specific post has logged in and is viewing a post they wrote, a button appears with the option to update the form. The clickable link will take them to an update review page. Alongside a button to update review, there is also a button to delete the post entirely. Delete functionality is extended to comment posts as if a logged in user has written a comment, a button appears to delete the comment.

### Authentication and Authorisation

**Django All Auth** is used for backend authentication

- Users can create an account in the sign-up page.
- Users can sign-in to their account to leave comments, posts and likes using the sign-in page.
- Users can login back into their account using the login page.
- Only authorised users can visit the submit review page and update review page.

### Navigation

<details>
<summary>Navbar</summary>
<br>

![Navbar](static/readme_images/screenshots/navbar_lg.png)
</details>

<details>
<summary>Navbar</summary>
<br>

![Navbar](static/readme_images/screenshots/navbar_sm.png)
</details>

<details>
<summary>Footer</summary>
<br>

![Footer](static/readme_images/screenshots/search_img.png)
</details>

### Recipe Search

<details>
<summary>Recipe Search</summary>
<br>

![Search Page](static/readme_images/screenshots/search_img.png)
</details>

<details>
<summary>Search Results</summary>
<br>

![Search Results](static/readme_images/screenshots/searchresults_img.png)
</details>

### Sign up

<details>
<summary>Sign-Up Page</summary>
<br>

![Sign-Up Page](static/readme_images/screenshots/signup_lg.png)
</details>

### Login & Logout

<details>
<summary>Login Page</summary>
<br>

![Login Page](static/readme_images/screenshots/login-img.png)
</details>

<details>
<summary>Logout Page</summary>
<br>

![Login Page](static/readme_images/screenshots/logout_sm.png)
</details>

### Recipe Blog

<details>
<summary>Recipe Blog A</summary>
<br>

![Recipe Blog A](static/readme_images/screenshots/review_img_a.png)
</details>

<details>
<summary>Recipe Blog B</summary>
<br>

![Recipe Blog B](static/readme_images/screenshots/review_img_b.png)
</details>

<details>
<summary>Recipe Blog C</summary>
<br>

![Recipe Blog C](static/readme_images/screenshots/review_img_c.png)
</details>

### Submit & Update review

<details>
<summary>Submit Review</summary>
<br>

![Submit Review](static/readme_images/screenshots/submitreview_img.png)
</details>

<details>
<summary>Update Review 1</summary>
<br>

![Update Review 1](static/readme_images/screenshots/updatereview_img.png)
</details>

<details>
<summary>Update Review 2</summary>
<br>

![Update Review 2](static/readme_images/screenshots/updatereview_img.png)
</details>

### Add comments

<details>
<summary>Added Comment</summary>
<br>

![Added Comment](static/readme_images/screenshots/reviewcomment_img.png)
</details>

<details>
<summary>Comments</summary>
<br>

![Comments](static/readme_images/screenshots/reviewcomments_img.png)
</details>

### About

<details>
<summary>About</summary>
<br>

![About](static/readme_images/screenshots/about_img.png)
</details>

### Features Left to Implement

## Bugs

### Fixed bugs and how I fixed them

### Known bugs unfixed

## Technologies Used

### Core Development Technologies

- [Django](https://www.djangoproject.com/) was used a full-stack framework.
- [JavaScript](https://ecma-international.org/publications-and-standards/standards/ecma-262/)
- [jQuery](https://jquery.com/)
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
- [HTML](https://html.spec.whatwg.org/multipage/)
- [Django Templating Language](https://docs.djangoproject.com/en/4.2/ref/templates/language/) for building pages

### Libraries, Frameworks and Packages

- [Edamam](https://www.edamam.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Select2](https://select2.org/)


### Python/Django packages

- [Gunicorn](https://pypi.org/project/gunicorn/)

- [psycopg2](https://pypi.org/project/psycopg2/)

- [Coverage](https://pypi.org/project/coverage/)

- [crispy_forms](https://django-crispy-forms.readthedocs.io/en/latest/)

- [django_summernote](https://pypi.org/project/django-summernote/)

  
### Infrastructural Technologies

- [PostgreSQL](https://www.postgresql.org/)
- [Heroku](https://www.heroku.com/home)
- [Cloudinary](https://cloudinary.com/)

## Testing

Full testing: [Testing.md](Testing.md)

## Deployment 

### Local Deployment

1. Find the repository on Github.
2. Click the "Codd" button and copy the URL.
3. Open the terminal in your IDE and open a session in the directory you want to use.
4. Type "git clone" followed by the URL into the terminal.
5. Type "pip install -r requirements.txt" in the terminal.
6. Set the the correct environment variables in an env.py file.
7. Once connected to your database, run migrations by typing "python manage.py migrate" into the terminal
8. Type "python manage.py createsuperuser" in the terminal and follow the prompts
9. Three .txt files are included to populate the database: ingredients.txt, utensils.txt, cuisine-types.txt.
10. Type "python manage.py runserver" in the terminal and open in browser.

### Heroku 

1. Login to Heroku.
2. Create a new app.
3. Connect to your GitHub repository.
4. In Heroku settings, set up environment variables in the Config Vars section in the settings tab.
5. Click on the deploy tab, and enable automatic deploys from your GitHub repository.
6. Click the "Deploy Branch" button the deploy the app.
7. Once fully deployed, click "Open App".

### Environment Variables

- Create an env.py file for local deployment in the root of the directory of the project.
- Set the environment variables in this file.

In env.py file:
- DATABASE_URL
- CLOUDINARY_URL
- EDA_APP_ID
- EDA_APP_KEY
- SECRET_KEY

In Django settings:
- SECRET_KEY
- DEBUG

- For Heroku deployment, set the environment variables in the Heroku dashboard or the Heroku CLI

## Credits
