# Milestone Project Three – Data Centric Development.

I have created a fully functional online community cookbook under the fictional company name ‘Gutsy’. The goal? To create an online cookbook which allows any user to receive, edit, delete and create their own recipes and cuisines for the community to take advantage of.

Effective navigation, simple user interface, nice bright colour scheme and simple instructions on how to make the most of relevant pages means the whole experience a user will undertake is a simple and effortless one. A user does not need to use much cognitive power while working on the site to make the most of all of the available benefits; creating a positive user experience.

The project was made possible written with the python micro web framework; flask. The project constantly uses a back-end system to push and pull content from the database (MongoDB), which is accessible and editable when required. Creating a completely personal experience to the community of users and making it satisfying to see their creations displayed in a simple, yet beautiful layout for all to see on a range of different device sizes.

## UX

To give the project its best chance to be a success, it was vital for me to understand who exactly the target audience were, and how to meet their specific needs. The following groups are what I consider to be the 2 main groups, along with an explanation as to why.

##### 1. Adventurous family members / chefs wanting to discover new recipes.

* The cookbook displays recipes in a well organised, easy on the eye manner. The users are forced make full advantage of this organisation by using the ‘cuisine section’ on the homepage; using the section to filter the recipe selection. This makes the browsing process for recipes on the site much quicker as it filters results down after just one click based on the recipes cuisine. 

* Once a cuisine is selected, the user will be taken to a page where all the recipes which fall into the cuisine group are presented in a series of collapsible pop out boxes (implemented using CSS framework; Materialize). The initial presentation of the recipes will display the recipe name, dish difficulty and how many people the dish serve. All the user will have to do is simply press on the specific recipe and the full catalogue of information such as the ingredients and steps are all shown as the box ‘pops out’ in an organised display.

##### 2. Chefs / food enthusiasts wanting to share their ideas with a community.

* This target group requires the ability to document their own recipes, and to share them to the community. This is achievable with the use of the ‘create recipes’ and ‘create cuisine’ sections of the site (accessible via the main navigation at the top of the screen). The user is then presented with a short form which includes all the elements required to create either a new recipe or cuisine.

* Once a form is complete, the user will find a clear submit button at the bottom of the page which when clicked; will push the content to the database and will be presented in the cookbook immediately along with the rest of the existing recipes and cuisines.

* This process is very simple, and a user can create their own recipes and cuisines to share in no more than 4 mouse clicks; requiring little brain power and making the user experience positive. 

## User Stories

##### 1. As a casual user, I want to be able to locate desired recipes quick and easy, so I don’t have to spend time browsing books or other websites instead.

* The ease of use factor throughout the cookbook was vital, as I understood that if a user must think, for even 5 seconds; you are vulnerable for loosing that user forever. In consideration for this, I made the browsing functionality throughout the site achievable in very low amount of click, and low brain power from the user.

* In this situation and to achieve this user story I developed the following. When the site initially loads; the user is presented with a welcome message and a blue pulsing button (with a downwards arrow inside) indicating the user should either press it or simply scroll down to view content. The user then arrives at the ‘cuisine section’, where they see a range of different cuisines to choose from in a clean, easy to read manner. when their desired cuisine is selected; they are directed to a page displaying all relevant recipes and making it quick and easy to find the recipe they want.

* A user can realistically get from the homepage, to their recipe in full description in no more than 3 clicks.

##### 2. As a food enthusiast who wishes to share my own ideas, I want to be able to document and enter my own cuisines and recipes into the cookbook, but it needs to be quick and easy for me.

* The process of creating both recipes and cuisines are very similar. The user is presented with a main navigation bar (or clickable burger button on smaller devices), where they are given two main sections; recipes and cuisines. Once the relevant section is selected the user is then given two further subsections; edit and create.

* For the sake of this scenario; after the create subsection is chosen, a user is then directly taken to a relevant short form. Once this form is completed; the recipe or cuisine is instantly pushed to the database. The new content is then instantly accessible throughout the cookbook for the community of users.

* Each form input field have relevant placeholders; meaning the exact use of each field is immediately understandable for the user, which eradicates a large portion of natural human error and makes for a much cleaner cookbook.

* Where possible, the user is presented with a selection dropdown menu for input values (prominent on the recipe creation form). The examples include dish difficulty, recipe cuisine type and how many people each dish serves. The reason for this is so the input throughout the cookbook is consistent and it means it is impossible for the user to input invalid data.

* All these features make the process of creating recipes and cuisines a quick one, and as always; does not require a lot of cognitive power from the user and is immediately understandable. Creating a positive user experience and makes for a cleaner cookbook for the community to take advantage of.

##### 3. As a user, if I see an error in a recipe or cuisine, or simply want to update my own contributions. I want to be able to modify these quickly and easily so the cookbook can remain up to date and fresh.

* This process is can be considered very similar for the user when comparing to the method for creating a recipe or cuisine. When the user is presented with the subsections ‘create’ and ‘edit’ within the main navigation; they shall proceed by pressing edit to be directed to the relevant page (differing for recipe and cuisine).

* If a user decides to edit a cuisine, they will be directed to the edit cuisine homepage and will be presented with all cuisines within the cookbook, taking advantage of simple card design, creating minimal and clean aesthetics so the user has a clear view of the options in front of them; without straining the eyes. They are also offered extra buttons; edit and delete.

* The delete button will immediately remove the cuisine from the cookbook and will completely delete the cuisine from the database.

* If a user selects the cuisine edit button however; the page they are directed to will be a clone of the create cuisine form. The only difference; the form will be pre-loaded with the selected cuisine ready to be edited within the input field. Once the desired modification is made within the form, the submit button will push the data to the database and will be presented correctly to the cookbook for the community to see.

* The process for editing a recipe is very similar. If the user selects the ‘edit recipe’ subsection on the main navigation; they will be taken to the edit recipe homepage where once again all cuisines are displayed for the user to choose from. The reason they are presented with the cuisines first is so the user can access specific filtered recipes quicker and make the whole experience easier and quicker for the user.

* Once the user has selected the cuisine in which the recipe they want to edit will be within; they will be shown all relevant recipes with two buttons once again, edit and delete. The delete button will immediately remove the recipe from the cookbook and the edit button will direct the user to a clone of the create recipe form with the same difference as explained before; the form will be pre-loaded with the chosen recipe’s content already inserted into the forms input fields. Once all modifications have been made, the submit button will push the new content to the database and the cookbook will then be up to date straight away.

##### 4. As a user, I want to be able to navigate across all pages of the cookbook quick and easy so I can spend time on more important things.

* I kept in consideration that given the nature of the project, users will not want to spend countless hours searching through the site getting from once place to another. The process of getting from A to B had to be as simple as possible; this was a must! 

* I took advantage of the CSS framework ‘Materialize’ and used their responsive dropdown navigation bar. The advantages of this was a very simple installation for a very robust feature on my part, but for the user it provides an amazing central hub for navigation. Users naturally understand to use nav bars to get around modern websites, so the user does not have to think at all when it comes to where to look and how to get around the site.

* The navigation bar offers (as explained previously) two main sections; recipe and cuisines, along with two subsections for each; edit and create. The navigation bar will also transform into a clickable burger button on smaller devices to aid the visualisation and keep the design minimal and clean. The user can get to wherever they want to be in a maximum of 5 clicks (from the home page to on a fully loaded edit recipe/cuisines form on mobile), making the site easy to use and satisfying for the user.

## Features

##### 1. Main navigation bar

* Naturally positioned at the very top of the site following a modern website’s logical order. The navigation bar (and burger button clickable button on mobile) offers a user a perfect hub to get from A to B within very few clicks and cognitive effort. Two main sections followed by two subsections means the users can get to anywhere they want to go through the navigation bar. Responsive elements mean no matter what device is used; anyone can take full advantage of the main navigation features.

##### 2. Collapsible pop-out bars for recipe display

* Collapsible pop-out bars are used to displays recipes to the user. The reasons being while a user is actively searching for a desired recipe within a relevant cuisine type, the recipes will be placed one by one in a neat order and only displaying vital first glance information (dish name, dish difficulty and how many people the dish will serve) and a relevant food icon. This current state aids the design and compliments the minimalistic aesthetics of the website, keeping it clean and easily scannable for people browsing recipes on the cookbook.

* Once a recipe is selected, the bar will collapse down and reveal the full description of the recipe. Which includes steps and ingredients along with confirmation of the dish name, dish difficulty and how many people the dish will serve. The steps and ingredients sections of the display are indented to aid readability and make the experience as smooth and positive as possible.

##### 3. Functioning create + edit forms

* Fully functioning forms are offered to the user, with relevant placeholders and headings to indicate the exact use of each form field. Selection drop down menus are also used to eliminate human error as much as possible and to also maintain consistent result display throughout the project. Once the short forms are submitted, the content will be pushed to the database and the dynamic content throughout the cookbook will be updated. 

* Both the create and edit forms are a clone of one another in the related subject (recipes and cuisines), however the edit form will generate pre-loaded content from the database related to the chosen recipe or cuisine. 

##### 4. Dynamic content from database (MongoDB)

* Throughout the site, dynamic content is pulled from the database and displayed to the user through making the most of jinja templating. This feature is what gives the cookbook its magic and allows the users to be able to create and document their ideas for all to see with very minimal code.

##### 5. Hidden content on smaller screens to aid UX and UI

* I have hidden certain content on small devices when compared to a full pc monitor screen. The reason for this; to maintain a nice, clear and minimalistic design. Attempting to cram all the same content from a large screen to a smaller device puts the site at risk of becoming cluttered and untidy on the eye. One example of hidden content we have on the site is under 375px device width, the cuisine section will hide the dynamic part of the selection button; the button will display ‘view recipes’ to ‘review *specific cuisine type* recipes’ once that breakpoint has been broken.
This method is used in many areas throughout the site with UI and UX in mind, keeping the aesthetics of the site a positive feature.

##### 6. Easy on the eye colour scheme

* The bright colour scheme used on the project was very intentional. The background is a bright white/grey with a light relevant outline of food. The main navigation bar is a light orange and a range of strong, colourful buttons means the website is extremely readable and is easy on the eye. 

* Due to the bright colours and a large black font, the user does not need to struggle at any point within the site to read any content or instructions; this makes the users life very easy and makes for an attractive website for all the use.

## Left to implement

##### 1. Further filter features on recipe display page

* Along with the current filter-by cuisine feature, I believe the project would benefit from further filter features on the actual recipe display pages. These could include filtering by difficulty, or number of people a dish serves. Features such as these will further aid the user to create a positive experience, which should always be considered.

## Technologies used

##### 1. HTML (https://www.w3.org/)

* HTML is used to create the foundations of the website. This includes the structure of the website, some site content, images and main navigation are all features made possible using Hypertext Markup Language.

##### 2. CSS (https://www.w3.org/Style/CSS/Overview.en.html)

* Although the CSS within this project was compiled and processed using Sass (described below), the CSS provides all styling throughout the project. Without this, the page will be very standard and not worthy of deployment. This styling was linked through an external style sheet and was linked through the head section of the base file.

##### 3. Syntactically Awesome StyleSheets / SASS (https://sass-lang.com/)

* Sass is used to create great styling and attributes for the page, which was then compiled into CSS. Many aspects of Sass make it a more effective and efficient way of styling when compared to standard CSS development. I used several partials to separate styling groups, along with variables, mixins and media queries to create rules to call at any time.

##### 4. Google Fonts (https://fonts.google.com/)

* Google fonts are used to receive professional style fonts for the page. They offer a huge catalogue of fonts suitable for any style and theme. The font I chosen to be used on the project would be 'Acme’, and this is present throughout.

##### 5. JavaScript (https://www.javascript.com/)

* The advantages gained using JavaScript can be seen throughout the project. The primary JavaScript libraries used throughout this project would be jQuery and Materialize. Features such as the collapsible pop out boxes, the main navigation bar responsiveness, several simple cards and initialization throughout the site were possible using JavaScript.

##### 6. Github (https://github.com/)

* GitHub is an essential technology to be used for developers across the world. Github is used to store and save the development of the project work and keeps it safe in a remote repository. I push my work regularly with comments to clarify what is new in contrast to my previous commits or saves.

##### 7. Heroku (https://www.heroku.com)

* Heroku is used to store and deploy the project to a live app. As the project is python based, Heroku is the best and most reliable solution for this task. 

## Deployment

















































































































