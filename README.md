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

* The deployment process for this process takes advantage of two different services (both explained above in the ‘technologies used’ section), Github and Heroku. 

* The first task was to generate a git repository; using the ‘git init’ command from the terminal. This allows me to have a safe place to store all my work so I could retrieve it from anywhere. (shown below)

* Next the job was to install Heroku, by using the command ‘sudo snap install heroku’. Due to Heroku’s specification; I needed to create a requirements.txt and Procfile. From this point I can then push to both Github and Heroku combined; keeping my work safe and able to push to a live app.

* Once this initial stage is complete, as the project gradually grows with new content and features; I continuously commit all the changes to my git repository. The changes are then pushed to my remote repository with a comment to explain what progress has been made at each point. This will also aid external developers who may look at the code in future, creating well-structured code and committing with relevant comments will help them understand what is happening from commit to commit.

* I can still edit my code while a live version is active. The live app version can be defined as the deployed version, while the code I can still edit and add upon is considered the development version and is still saved to my own private workspace. I use this to edit, upgrade, and test all areas of the project safely while the deployed version stays the same. Once I am happy with an upgrade and I want to apply these to the deployed version, all I need to do is follow the same process as before. Once the new code was pushed on to the remote repository the deployed version is then upgraded for the public to use.


## Testing

Testing is a vital aspect of any project, with ‘Gutsy’ being no different. Without thorough testing, you leave yourself and your project wide open for mistakes, user complaints and a negative experience for users; resulting in them leaving and not coming back.

Naturally during the testing processes of my project, I met several little bugs along the way which needed to be resolved before carrying on. I believe a developer can never be too careful when testing for errors as a deployed website full of errors can be disastrous.

I needed to make sure the goals stated by my written user stories were easily achievable for any user (regardless of IT knowledge or experience).  

I have listed the user stories below and will explain how each is easily achievable for the user with very low cognitive power needed.

##### 1. As a casual user, I want to be able to locate desired recipes quick and easy, so I don’t have to spend time browsing books or other websites instead.

* This user story was a priority of mine, if the user came across difficulty searching and finding recipes; they would simply leave the site and look somewhere else, without any doubt. 

* Baring this in mind, on the homepage of the website (above-the-fold on all device), the users are shown a pulsing blue button aiming downwards. The reason being is this indicates to the user that they must either scroll down or press the button to uncover the benefits of the cookbook, without even thinking about it.

* From here they are presented with a range of different cuisines with a welcome message and very short instruction, educating to the user that they can go ahead and select a cuisine which their desired recipe will fall into the same category. The process is extremely quick, and it also filters recipes before they are even displayed, making for more consistent and clean recipe display pages.

* I tested several different ways to display the cuisine selection cards, however taking advantage of “Materialize” simple cards gave me a range of advantages. The main advantages being that I could display a high number of options/cuisines in a clean and organised manner, it gave me ample room to display a header and relevant buttons while dynamically pulling in content from the database and it allowed me to create a well organised responsive design which does not affect the quality of styling on a smaller device.

* A user can go from the homepage to opening their recipes full description within 3 click maximum, saving a great deal of time and effort from the user.

##### 2. As a food enthusiast who wishes to share my own ideas, I want to be able to document and enter my own cuisines and recipes into the cookbook, but it needs to be quick and easy for me.

* A successful project which relies on a community input must make the process very simple. People are busy and do not have/want the time to spend it struggle trying to share their own ideas on a cookbook, if the process is difficult; they will not do it and this leads to an empty community cookbook which is no good to anyone.

* This user story caters the chefs/ food enthusiasts wanting to share their own ideas, without this target group; the cookbook would not be a success. People need to be willing to share their own ideas first before anyone could possibly visit the site and read them. For this reason, developing a solid method to creating recipes and cuisines was a must, as the project can be considered a failure without it.

* The route to the create pages is a simple one, the main navigation bar (positioned at the top of the page) is initially split into two section; recipes and cuisines. This immediately can guide the user into the right path, clicking the section in relation to what they want to create. Following this step, they are then presented to a further two subsections; edit and create. In this scenario, the user will select create.

* They will immediately be directed at the relevant create form, which has numerous input field headings, placeholders and selection inputs where possible (especially on the create recipe form) to minimize human error and confusion. The results of this? A quick and easy way to document your ideas to a community of people will very little effort.

* It was due to testing that resulted the addition of several placeholders and headings. Although the process is understandable for people who share a passion for food and recipe creating; the goal was to ensure the everyday person, even little no technology experience can arrive at the page and create a recipe or cuisine without very few minutes. The easy the process for the user; the better. 

##### 3. As a user, if I see an error in a recipe or cuisine, or simply want to update my own contributions. I want to be able to modify these quickly and easily so the cookbook can remain up to date and fresh.

* As the community essentially creates the cookbook itself, eventually you will come across simple errors which cannot be avoided, such as typo’s or an incorrect section input. This is only natural and is guaranteed to happen. 

* For this reason, it was very important for me to develop an area for users to go back into their contributions and edit where necessary. How was best way to do this? Create a clone of the exact method a user takes to create a recipe/cuisine but give the form a slightly altered use. Going back to the main navigation and two main sections of it (recipes and cuisines), for this scenario; we will say the user selects edit. 

* If a user spots a mistake within one of the cuisines within the cookbook and they select the edit cuisines tab within the main navigation; they will be directed to the edit cuisine homepage. This page displays the cuisine the same way as the homepage, the only difference this time is that the user is offered two different buttons to choose from, edit and delete.

* Like the homepage; testing was carried out to see which style was more efficient on displaying the cuisines for both aesthetics and quality of responsiveness, which resulted in the simple card design again. The same can be said about the colour scheme of the two buttons, they needed to stand out but also give meaning to the use of the button without the user having to offer any cognitive power to figure it out. In the end I believed green for edit and red for delete gave a clear indication for what each button may do and makes the page look very aesthetically pleasing and makes the user experience a better one. 

* If a user selects the delete button, the cuisine would disappear and would be removed from the database and cookbook. If a user selected edit, they would be directed to a page which is a clone of the create form, but this time the input fields will be pre-loaded with all the relevant content, so all a user would need to do is make the correct adjustments and submit them to push the new content to the cookbook. 

* Similarly, if the user selected edit recipe, they will again be directed to a page with the cuisines listed, but this time it will be for the sake of filtering recipe display (just like the homepage). Once a relevant cuisine is selected all the necessary recipes will be presented with the same two buttons as mentioned previous for the edit cuisines homepage; edit and delete. The process following is the same, with the delete button removing the recipe and the edit button generating a clone of the create form but with the input fields already pre-loaded with the correct information ready to be modified. 

* This whole process was developed and tested with the user in mind, the steps from the homepage to edit form or the delete button was very intentional. It would have been easy to gather all of the recipes in the cookbook and list them in one place and let the user find and edit it themselves, but this would not be practical or efficient for a user and would not end in a successful project. The process includes easy on the eye card design, filtering (cuisine selection for recipe edit), access from the main navigation and guidance on each page. All of this is to help the user as much as possible and make the process as simple as possible.

##### 4. As a user, I want to be able to navigate across all pages of the cookbook quick and easy so I can spend time on more important things.

* One of the most important aspects of the project during the planning stages was to ensure the user can get from the homepage, to anywhere they want to be in a minimal number of steps/clicks. I believe this fact is apparent when viewing the final product.

* Through the successful use of the responsive main navigation, users can get to anywhere at all in the site with very little effort, no what device, or no matter where they want to get to.

Another prominent goal of the project was to successfully develop a fully responsive website, making sure the cookbook works and looks brilliant no matter what device size. This process proved successful but naturally took a lot of trial and error in terms of features such as font sizing, positioning and hiding certain descriptions on smaller devices. It was made possible using media queries and styling based within specific breakpoint parameters. This styling was written in SASS and then compiled into CSS.

I did naturally come across some bugs while within the testing process of the project. An example of this is the fact I felt the need to re-structure the database to aid the create/edit process for recipes. I was having a lot of trouble pulling content such as dish difficulties to display to the user, it was either pulling every option submitted to the site, or none. The solution I found was to create separate collections within my MongoDB Atlas database and pull the content from them separately and combine once submitted to form the recipe. This applied for the ‘serves’, ‘dish difficulty’ and ‘cuisine’ sections. This made for a more structured database and an effective working cookbook, allowing users to edit and create recipes successfully.

Another problem I came across during development was that my stylesheet was getting very cluttered and disorganised. To battle this and create some order within the styling, I converted all the CSS to SASS. Separating styling into separate partials, I made use of mixins and media queries and then compiled the SASS to CSS successfully. This aids the styling organisation a huge amount, speeds up development and makes it much easier later to make any necessary modifications. 

Another minor error I came across during the testing process was a fade in function on the cookbook. When the site loaded up, the content faded in smoothly, this was a great idea on paper. During my own manual testing on the site I found this feature irritating and repetitive, if I found this during production, chances are users will feel the same. Due to this reason, I then decided to remove it for the sake of user experience.

## Credits 
##### Content 

* No external source of content was used for this project.

##### Media

* The hero image and license can be seen here - https://pixabay.com/illustrations/chef-character-cook-gourmet-1417239/

* The background image can be found here- http://www.heropatterns.com/
* With License here - https://creativecommons.org/licenses/by/4.0/

##### Acknowledgements





















































































































