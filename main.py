from flask import Flask
import random
from datetime import datetime
from freezegun import freeze_time

movies = ["Lord of the Rings", "Star Wars", "Bruce Almighty", "Hateful Eight", "Princess Bride"]

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/")
def index():
    # choose a movie by invoking our new function
    #movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    #content += "<li>" + movie + "</li>"
    content += "<li>" + get_todays_movie() + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    #content += "<li>" + get_random_movie() + "</li>"
    content += "<li>" + get_tomorrows_movie() + "</li>"
    content += "</ul>"
   
    return content

#def get_random_movie():

    # TODO: make a list with at least 5 movie titles
#    movies = []
 #   movies = ["Lord of the Rings", "Star Wars", "Bruce Almighty", "Hateful Eight", "Princess Bride"]
    # TODO: randomly choose one of the movies, and return it
   
#   print('You are here!')
 #   return random.choice(movies)

def get_todays_movie():
    today = int(datetime.now().strftime('%d'))
    todays_index = today % 5
   
    return movies[todays_index]

def get_tomorrows_movie():
    today = int(datetime.now().strftime('%d'))
    tomorrows_index = (today + 1) % 5
     
    return movies[tomorrows_index]    


with freeze_time('2018-05-29'):
    app.run()
