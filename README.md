<h1  align="center">
<a  href=""  target="_blank"><img  src="/static/img/Landingpage.png"  alt="Book Nook Screen"/></a>

</h1>

BOOK NOOK

  

This Project is for milestone 3 python and data centric design

<br>
</div>

  

## Table of Contents

1.  [**UX**](#ux)
-  [**Project Goals**](#project-goals)
-  [**User goals**](#user-goals)
-  [**User Stories**](#user-stories)
-  [**Design**](#design)
-  [**Wireframes**](#wireframes)

  
2.  [**Features**](#features)
-  [**Existing Features**](#existing-features)
-  [**Features Left to Implement**](#features-left-to-implement)
3.  [**Database**](#database)
4.  [**Technologies used**](#technologies-used)
5.  [**Testing**](#testing)
6.  [**Deployment**](#deployment)
7.  [**Acknowledgements**](#acknowledgements)
8.  [**Disclaimer**](#disclaimer)

  
## UX

  

### Project Goals

  
The main goal of this project was to utilize my knowledge of Python and Databases in order to make A book review website where users can
submit reviews and give them recomendations , while also being able to search for other reviews 
  

#### User goals
User goals in brief are as follows:

 1. To view other users book reviews and give a like to reviews
  2. To create an account on the site
   3. To add a review of their own and edit any existing ones they have
   4. To remove their reviews and account if they wish
   5. To have an amazon link that leads to the book

  

#### User Stories

1. I want to see book review summarys when i go to the landing page of the site.
2. I want reviews to be limited to a certain number so my screen is not cluttered.
3. The reviews on the landing page should have the option to view them.
4. The book reviews should show who wrote them.
5. The book review should show what category the book falls under.
6. The book review should show the full review, summary, author and book name.
7. The full book review should allow me to give the review a like and to link to the book in the amazon site.
8. I would like to be able to create an account to leave my own reviews.
9. I would like to be able to log in easily when details are correct.
10. On the book review page, I want to be able to delete or edit my reviews.
11. I want the abilty to view my profile and i should be able to view any reviews associated to my account.
13. I would like to be able to remove my account should i choose.
14. There should be options to register and login on the site navigation,
15. If im logged in i should see navigation options to log out, view all my reviews and to view my profile.

  

### Design

  
**Fonts**

I decided to use the 'Ubuntu' font from google("https://fonts.googleapis.com/css?family=Ubuntu") It has a nice and easy look that makes it stand out and is not sharp and jarring


**Colours**

I am very fond of contrasting colors so i went with white and black with a background of bookshelves it gives it a nice warm feeling.

**Topography**

The site uses bootstrap 4 be responsive across devices, also media queries were used to change how the intro text appears across different devices to provide a smooth user experience.

### Wireframes

WireFrames were created using Figma at recomendation of my tutor. https://www.figma.com/  
they can be found here [desktop](documentation/WireFrames) 
The original design that was chosen was too complicated and whould have taken time away from Python and more difficult tasks the website was simplified multiple times insired by old blogs and review sites i made it much simpler. it shares simalr designs as forums.

  

## Features

### Existing Features

1. Users can view all reviews.
2. Users can create unique usernames to login and add, edit and delete a review.
3. Users can remove their own profiles.
4. Users can click on an amazon search link to find the relevant book.

### Future Features to Implement

Future versions of the project may have the following:

1. Ability to reset an account password.
2. Prevent the user adding multiple likes to the a review.
3. Ability for user to view in their profile all likes they have added to other reviews.
4. Searching the database for books via keywords



 

## Database

MongoDB Atlas is the database that i used it has two collections "reviews " and "users".

### Database collections 

**users collection:**

```
{
"_id":"",
"username":"",
"password":""
}
```
**reviews collection:**
```

{
"_id":"",
"author":"",
"book_title":" ",
"summary":".",
"review":"",
"category":"",
"amazon":"",
"icon":"",
"upvote":{"$numberInt":""},
"username":""
}

```

  

## Technologies Used

  

This project uses Python, Flask, MongoDB, HTML, CSS and JavaScript technologies.

  

-  [Python](https://www.python.org/)
The project uses **Python 3** to create the app, create the routes, create the functions within those routes and handles all back end interactions.

-  [Flask](https://flask.palletsprojects.com/en/1.1.x/)
The project uses **Flask 1.1** framework to create and populate the templates.

-  [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
The project uses **MongoDB Atlas** as a backend database.

- [JQuery](https://jquery.com)
 The project uses **JQuery** as part of bootstrap 4 and to create a character counter on the text area fields.

-  [Bootstrap 4](https://getbootstrap.com/)
The project uses **Bootstrap** to simplify the structure of the website and make the website responsive easily.

-  **HTML 5 and CSS3**
The project uses **HTML5 and CSS3** for website structure and design.

-  [Google Fonts](https://fonts.google.com/)
The project used the **Google 'Ubuntu' font** across the site

-  [GitHub](https://github.com/)
This project uses **GitHub** to remotely store the source code in a repository. The project can be cloned or downloaded from here. See [Deployment](#deployment) section

-  [StackEdit](https://stackedit.io)
This project uses **StackEdit** to build the markdown for this readme file

 
  
  

## Testing

  

Testing was done incrementaly and influnced the end result of the project.

  

As this was my first major project in Python testing was slow and a lot of time was speant pouring over errors and hours pouring over youtube videos and tutorials
i tested the python code with https://extendsclass.com/python-tester.html and came back with no syntax errors 
CCS was tested with https://jigsaw.w3.org/css-validator/ there where 2 warnings but i have chosen to ignore these as they cause no problems
the html validator https://validator.w3.org/ showed up multiple errors as the techincque to create templates was casuing flags these where ignored.

  

When the project was fully completed i went through the below testing scenarios to further test the project to make sure that it reached my goal.


  

| Test | Expected |Passed |
| :------------- |:-------------| :-----:|
| User loads the landing page of site | Page displays without error and reviews can be viewed | &#9745; |
| User loads the homepage of the site | Reviews are displayed | &#9745; |
| User selects the 'review' button of a particular review on homepage | Review page displays without error and the correct review can be viewed | &#9745; |
| User selects the 'review' button of a particular review on homepage whilst not logged in | Review page displays without error and the correct review can be viewed and the 'edit and 'delete' buttons are not visible | &#9745; |
| User clicks on the recommend button on a review page | recommend like should increase by 1 | &#9745; |
| User clicks on amazon link on a review page | amazon site should load and show a link to the book if it exists in amazon | &#9745; |
| User clicks on delete button on review page when logged in | delete notice should pop up with warning and confirm / cancel buttons | &#9745; |
| User clicks on confirm delete button on review page delete notice when logged in | review is removed from the db and confirmation message displayed | &#9745; |
| User clicks on any nav link | All nav links should be fully functional both logged in and logged out and go to the correct destination | &#9745; |
| User clicks on any nav link | All nav links should be fully functional both logged in and logged out and go to the correct destination | &#9745; |
| User logs in | Nav items change from ***login***, ***register*** and ***about*** to ***my profile***, ***my reviews***, ***about*** and ***log out*** | &#9745; |
| User selects ***Register*** from top nav | Register form page loads | &#9745; |
| User enters username smaller than 3 characters and larger than 20 characters and clicks ***Register Now***| Form does not submit and shows error message to user that username must be between 3 and 20 characters long | &#9745; |
| User enters correct **username** but enters different values in ***password*** and ***confirm password*** fields| Form does not submit and shows error message to user that passwords must match | &#9745; |
| User enters correct ***username*** and ***password*** and ***confirm password*** fields match| Forms submits, landing page is loaded with message confirming successful registration | &#9745; |
| User selects ***log In*** from top nav | ***log in*** form page loads | &#9745; |
| User enters username smaller than 3 characters and larger than 20 characters and clicks ***Log in Now***| Form does not submit and shows error message to user that username must be between 3 and 20 characters long | &#9745; |
| User enters correct **username** and enters correct values in ***password*** field of log in form| form submits and logs customer in and message is displayed to show successful log in | &#9745; |
| User enters correct **username** but enters the wrong values in ***password*** field of log in form| Form does not submit and shows error message to user that password is incorrect | &#9745; |
| User enters incorrect **username** | Form does not submit and shows error message to user that the user does not exist and shows a link to register | &#9745; |
| User tries to **edit** / **delete** a review that they havent created under their username | User is messaged that they can't delete / edit reviews they do not own | &#9745; |
| User **edits** a **review** they own| All edits are submitted successfully once they pass form validation and can be seen when review loads | &#9745; |
| User selects to **delete** a **review** they do not own| user gets warning message informing that they cant delete someone else review | &#9745; |
| User selects to **confirm delete** on delete modal| review is removed from list of reviews and user message| &#9745; |
| User selects to **cancel delete** on delete modal| review is not removed from list of reviews and user return to review page| &#9745; |
| User selects to **delete profile**| delete profile modal pops up with warning| &#9745; |
| User selects to **cancel delete profile** on modal| user is returned to profile without any removals| &#9745; |
| User selects **confirms to delete profile**| profile and all associated reviews are removed, user seesion is removed and user is sent back to index| &#9745; |





## Deployment

I personally used vscode on my local machine to develop the site using Python 3.7.3  and deployed to Heroku via Github.

1. To download or clone the site to your local machine you will need to go to (https://github.com/OriHillairetdev/Milestone-project-3) see steps in https://help.github.com/en/articles/cloning-a-repository .
2. Before you download or clone the site you will need to ensure you have [Python 3.7](https://www.python.org/downloads/) installed. 
3. Once you have Python installed, created a virtual environment as appropriate to you chosen IDE and os.
4. Run the requirements.txt file as appropriate to your IDE to install the relevant required packages dependencies for the project into your virtual environment.
5. Run the app.py file as appropriate to your chosen environment and os.
6. You should now be able to view the site on your localhost on port 5000.

### Acknowledgements

Thanks to the people on slack for always posting usefull information
thanks to the Codeinstitute templates
and Thanks to my Mentor Precious Ljege for teaching me some tricks of the trade
  

#### Disclaimer

The content of this website is educational purposes only  