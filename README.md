# Directors and Movies
## Usage

The different API's endpoints are:

- "/" - root:
Provide links to the directors/ and movies/ end points

- "api/token/" - get access and refresh token:
     - POST/: Response with an access and a refresh token

- "directors/" - Directors List:
     - GET/: A list of all directors
     - POST/: Creates a new user with the following fields:<br>
            {
                "username": "YOUR_USERNAME",
                "password": "YOUR_PASSWORD"
            }
- "directors/id/" - Specific director's details:
     - GET/: get the attributes of the specific director
     - PUT/: (Requires Token) update the user password
     - DELETE/: (Requires Token) delete the user
     
- "movies/" - Movie List:
     - GET/: list of all movies
     - POST/: (Requires Token) create a new movie with the following format:<br>
      {<br>
          "name": "MOVIE_NAME",<br>
          "duration": "HH:MM:SS",<br>
          "genre": "MOVIE_GENRE",<br>
          "description": "MOVIE_DESCRIPTION"<br>
      }<br>
  
 - "movies/id/" - Specific movie details:
     - GET/: Specific movie details
     - PUT/: (Requires Token and to be the owner) update the movie attributes
     - DELETE/: (Requires Token and to be the owner) delete the movie
