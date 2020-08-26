# Directors and Movies

## Requirements
- Python 3.7.2
- Django (3.1)
- Django REST Framework
- Simple JWT

## Installation
```
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
```

## Usage

The different API's endpoints are:

- "/" - root:
Provide links to the directors/ and movies/ end points

- "api/token/" - get access and refresh token:
     - POST/: Response with an access and a refresh token. Once the user has a token. It's must be used to authorize certain request. In order to authorize a request, the header must be contain the following:
     
     ```
     "Authorization: Bearer yJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
     ```

- "directors/" - Directors List:
     - GET/: A list of all directors
     - POST/: Creates a new user with the following fields:

          ```json
            {
                "username": "YOUR_USERNAME",
                "password": "YOUR_PASSWORD"
            }
          ```

- "directors/id/" - Specific director's details:
     - GET/: get the attributes of the specific director
     - PUT/: (Requires Token) update the user password
     - DELETE/: (Requires Token) delete the user
     
- "movies/" - Movie List:
     - GET/: list of all movies
     - POST/: (Requires Token) create a new movie with the following format:
          ```json
          {
               "name": "MOVIE_NAME",
               "duration": "HH:MM:SS",
               "genre": "MOVIE_GENRE",
               "description": "MOVIE_DESCRIPTION"
          }
          ```
  
 - "movies/id/" - Specific movie details:
     - GET/: Specific movie details
     - PUT/: update the movie attributes. Requires authorization header: 
     - DELETE/: (Requires Token and to be the owner) delete the movie
