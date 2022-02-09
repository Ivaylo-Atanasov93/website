This is a website developed for a friend.

He has the  following requirements for the website:

  - To display some quotes that he like on the home page
  - To display pictures
  - To display his videos from YouTube
  - To display his resume
  - To has contact form
  - To display list with his concert dates and locations
  
  And not required by him but added from me was the Booking form
  as its his main source of income.
  
  
 Description of the solutuons:
 
 1. Home page - I have used a Bootstrap carousel for the quotes that he wants to display. He can change the output of the index page by editing the content from the Admin panel.
 2. Biography - There is displayed his resume that is also stored in the database and is changable via the Admin panel so every time when he has to update anything in his resume he can do it easily.
 3. Concerts - This page displays list of his upcoming concerts. Displays Title, Description, Date and Time and Location. For the Location I have used the google maps EmbedMap, which is currently hard to use because everytime he has to edit the link before put it in the form, but it will be fixed.
 4. Photos - For this page I have a Liss CBV and the pictures have to be uploaded somewhere before that since the model is working with photo_url variable that stores only the url, but not the picture itself. This is because the website is deployed on Heroku, and they are deleting all the media that is not used for styling.
 5. Videos - This page contains Embed YouTube videos straight from his channel and it could be watched on full screen.
 6. Contact me - For this form I have used Bootstrap, row and col layout.
 7. Book a lesson - Like the Contact form, this one uses Bootstrap as well, and the layout is the same. The time section uses Options declared in the forms.py in order to fill the time in the correct format everytime.


Link to the deployed website:

https://dimitarkanchev.herokuapp.com/
