# milestone3-tprice31

# How to Set-up and Deploy "tyroget's movie trends" app!
This file details the work behind the app displaying some of my favorite movies and how to set it up for deployment.


## Project Description

The movie discovery web app I have created and deployed shows information about my favorite movies and links to their Wikipedia 
page. Every time the app's page is refreshed, the film and its displayed data are updated, picked randomly. It is coded in **Python**, 
referencing the requests and python-dotenv libraries. The **requests library** allows you to send HTTP requests and reference the 
APIs. **Python-dotenv** passes our hidden keys as environment variables to get a response from the referenced APIs. The **Flask web 
framework** builds and displays the app on the endpoint "/" using templates for dynamic web page content and couples with **HTML** and **CSS** 
to style the page's features and structure. The displayed information -- the movie's name, tagline, genre, a corresponding image, and 
Wikipedia link -- generates dynamically from the **TheMovieDataBase (TMDB)** (a movie database for movies and TV shows) and **Wikipedia APIs**, 
respectively. **Git and Github** allowed for the incremental update of files. **Heroku** is the deployment system I use to deploy my app 
so it is viewable by others and not just locally. **HTML Forms** take in information from the user -- username and password on the registration/login
page and a comment and rating on the main movie web page. The data received is by **PostgreSQL**, a database management system used for saving the 
movie ratings, user usernames and passwords. The registration form saves the username and password to the database, and the login form checks to see 
if the information entered matches any previously saved user info. The movie review form tracks the movie on the screen's ID and the current user, 
sending that information to the database if a review is left. Reviews for the current movie populate the review section on the screen and are listed 
by user. **Flask-SQLAlchemy** is the flask extension providing an object-relational mapping between the database and Python logic. **Flask-Login** tracks 
if a user is logged in and if one is, what user that is. Code quality and formatting was done via **Pylint** and **Black**.

## Installation Requirements
Before getting started, run the following commands in your terminal:

### Python
    python3 -m ensurepip --upgrade  # install pip, which manages python packages
    pip3 install flask
    pip3 install requests
    pip3 install python-dotenv

### Heroku
    WSL users: sudo curl https://cli-assets.heroku.com/install.sh | sh 
   
    Mac users: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 
    
If you don't have Homebrew installed, then run: 
    
    brew tap heroku/brew && brew install heroku

### PostgreSQL setup
    brew install postgresql
    brew services start postgresql
    psql -h localhost  # this is just to test out that postgresql is installed okay - type "\q" to quit
    # if the above command gives you an error like "database <user> does not exist," try the workaround in this link: https://stackoverflow.com/questions/17633422/psql-fatal-database-user-does-not-exist
    pip3 install psycopg2-binary
    pip3 install Flask-SQLAlchemy==2.1


## TO SET UP THIS PROJECT:

### After copying this repository:
#### Create a TMDB
1. Start by creating a TMDB at https://www.themoviedb.org/.
2. Once you have an account, go to your account settings and fill out the form on the "API" link to 
   apply for an API key. Put a neutral response when asked for an app URL.


#### Set up
1. Create a .env file in your project directory
2. Add your TMDB API key with the line: export TMDB_KEY='YOUR_KEY'

#### Deploy to Heroku
1. Create a free account on Heroku https://signup.heroku.com/login
2. Log in to Heroku (run command in terminal): heroku login -i
3. Create a Heroku app: heroku create. This will create a new URL and associated host for you.
4. Create a new remote DB on your Heroku app: heroku addons:create heroku-postgresql:hobby-dev (If that 
   doesn't work, add a -a {your-app-name} to the end of the command, no braces)
5. See the config vars set by Heroku for you: heroku config. Copy paste the value for DATABASE_URL.
   Set the value of DATABASE_URL as an environment variable by entering this in the terminal: export DATABASE_URL='copy-paste-value-in-here'
6. Push your code to Heroku: git push heroku main. This pushes your code to Heroku's remote repository.
7. Go to https://dashboard.heroku.com/apps and click your App, then go to Settings, and click "Reveal Config Vars".
8. Add your API key from .env with the matching variable name (TMDB_KEY) and value (key).
9. Run heroku open. 

#### Heroku URL

http://tranquil-plains-75693.herokuapp.com


#### Question Response
**a. What are at least 3 technical issues you encountered with your project? How did you fix them?**
     
     1. An error I dealt with was tracking if the user was logged in. I overlooked this step in milestone 2, so missing this cause trouble down the line with only certain changes being able to be made when logged in.
     2. Another technical issue was getting the data out the console. I also struggle with this in HW7, and using the soluting and rewatching lectures on how to map the data correctly helped me to fix this issue.
     3. The third issue and an issue that is still currently an issue with my project is submitting the edited/deleted data. When pressing the delete button, it visibly deletes from the user edit page. However, upon 
        revisiting the page, the information is not removed from the database and is still listed in the user reviews.
     
**b. What was the hardest part of the project for you, across all milestones? What is the most useful thing you learned, across all milestones?**
     
     1. The hardest part was implementing react. From determining how to link a react page to the files I already had, to getting the JSON data from the console and actually onto the page, it was the most difficult part. 
        The most usefule thing I learned was how to make API calls and how to print the dictionary data in the console. I have struggled with determining the keys/parameters need for the calls, so being able to print in the 
        allows you to see the response and change your parameters accordingly.
