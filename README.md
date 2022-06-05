## Author 
 - linetlucy Genchabe 

 ## Description 

 This is a clone of Instagram. You can post, comment and view pictures posted on this App just like on Instagram.

 ## User Stories
- Users need to Sign in to the application to start using.

- Users can view different photos.

- Users can click on a single photo to view it and also view details of the photo.

- Users can search for different photos.

- Users can Upload their pictures to the application.

- Users can see their profile with all their picture.

- Users can view  a picture and leave a comment on it.




### Installion and Setup instructions


1. Clone this repo: git clone https://github.com/linetlucy-genchabe/Instagram-Clone

2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to instaclone then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
    
    
       pip install -r requirements.txt
4. On your terminal,Create database instaclonedb using the command below.


       CREATE DATABASE instaclonedb; 
       **if you opt to use your own database name, replace instaclone your preferred name, then also update settings.py variable DATABASES > NAME

5. Migrate the database using the command below


       python3.9 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


## Running the tests

python manage.py test lynneinsta

## Technologies Used
* python
* html5
* Django
* Postgres

## License

MIT LICENSE

## Live Site

#### https://lynnegram.herokuapp.com/
 

<p align = "center">
    &copy; 2022 @linetlucy genchabe.
</p>