# Milestone Project Three – Data Centric Development.

I have created a fully functional online cookbook under the fictional company name ‘Gutsy’. The goal? To create an online cookbook which allows any user to receive, edit, delete and create their own recipes and cuisines for the community to take advantage of.

An extremely simple user interface, a nice bright colour scheme and instructions on how to make the most of relevant pages means the whole experience a user will undertake is a simple and pleasing one. A user does not need to use much user brain power while working on the site; making a positive overall experience.

The project was made possible written with the python micro web framework; flask. The project constantly uses a back-end system to push and pull content from a database which is accessible and editable when required. Making the experience completely personal to the user and satisfying to see their creations displayed in a simple, yet beautiful layout for all to see on a range of different device sizes.

## UX

To give the project its best chance to be a success, it was vital for me to understand who exactly the target audience were, and how to meet their specific needs. The following groups are what I consider to be the 2 main groups, along with an explanation as to why.

**Adventurous family members / chefs wanting to discover new recipes to attempt.**

* The site displays all recipes entered to the cookbook in a well organised, easy on the eye manner. The target group is forced make full advantage of this organisation by using the ‘cuisine section’ on the homepage; using it to filter the recipe selection down. This makes the browsing process for recipes on the site much quicker as it filters results down after just one click based on the recipes cuisine.
 
* Once a cuisine is chosen, the user will be taken to a page in which all the recipes what fall into the cuisine group are presented in a series of ‘collapsible pop out boxes (implemented using CSS framework; Materialize). The initial presentation of recipes will display the recipe name, dish difficulty and a confirmation of dish cuisine. All this user will have to do is simply press on the specific recipe and information such as the ingredients and steps are all shown as the box ‘pops out’ in a clean manner.

**Chefs / food enthusiasts wanting to share their ideas with a community**

* This target group has the ability to document their own recipes to share to the community by taking advantage of the ‘create recipes’ and ‘create cuisine’ sections of the site (accessible via the main navigation at the top of the screen). The user is then presented with a short form which includes all the elements required to create either a new recipe or cuisine. 

* Once the form is complete the user will find a clear submit button at the bottom of the page which when clicked; will push the content to the database and will be presented in the cookbook along with the rest of the existing recipes within the same cuisine. 

* This process is very simple and a user can create their own recipes and cuisines in no more than 4 mouse clicks; requiring little brain power from the user and making the user experience a pleasant one.

### User Stories

##### As a casual user, I want to be able to locate desired recipes quick and easy, so I don’t have to spend time searching books or the internet instead.**

* The ease of use throughout the website was vital, as I understand that if a user must think (for even 5 seconds); you are vulnerable for loosing that user forever. In consideration for this, I made the functionality throughout the site achievable in very low amount of click, and low brain power from the user.

* In this situation and to achieve this user story I developed the following. When the site initially loads; the user is presented with a welcome message and a blue pulsing button (with a downwards arrow inside) indicating the user should either press it or simply scroll down to view content. The user then arrives at the ‘cuisine section’, where they see a range of different cuisines to choose from and when their desired cuisine is pressed; took to a page presenting all relevant recipes and making it very quick and easy to find exactly what they want. 

* A user can realistically get from the homepage, to their recipe in full description in no more than 3 clicks, every single time. 

##### As a person who wishes to share their own ideas, I want to be able to document and enter my own cuisines and recipes to the cookbook, so I only need to share the ideas once for everyone.

* The process of creating both recipes and cuisines are very similar. The user is presented with a main navigation bar (or clickable burger button on smaller devices), where they are given two main sections; recipes and cuisines. Once selected the relevant section they are then given two further subsections; edit and create.

* Once create is selected a user is then directly taken to a short form where once completed; the recipe or cuisine is instantly pushed to the database and the user is then redirected to the homepage, allowing access to the new recipe or cuisine straight away in the same method as explained above in the first user story.

* Each form field has a relevant placeholder; meaning the exact use of each field is immediately understandable for the user, which eradicates a large portion of natural human error and makes for a much cleaner cookbook.

* Where possible the user is presented with dropdown boxes for input values, examples include dish difficulty and how many people each dish serves. The reason for this is so the input throughout the cookbook is consistent and it means it is impossible for the user to input an incorrect value.

* All these features make the process of creating recipes and cuisines a quick one, and as always; does not require a lot of brain power from the user and is immediately understandable. Creating a positive user experience and a much cleaner cookbook for the community to take advantage of.

##### As a user, if I see an error in a recipe or cuisine or simply want to update my own contributions, I want to be able to edit these quickly and easily so the cookbook can remain up to date and fresh.