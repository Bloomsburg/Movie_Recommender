## Sean Bloomsburg
## sbloomsburg@gmail.com
##
## The function in this module uses the sample
## ratings and movie definition files to create
## a dictionary of movies with mean user ratings
## and a dictionary of movie id's with genre data.
##


import string
import re


def dbase_analysis():

    attribute_re = re.compile('\d+')
    genre_re = re.compile('[0-1]')
    delimeter_re = re.compile('\|+')
    title_re = re.compile('[^|]*')
    genre_head_re = re.compile('\|\d\|')

    ratings_data = open( "Ratings.txt", "r")
    movie_list = {}      ## Temporary dictionary used to collect all given ratings for each movie   
    movie_rating_dictionary = {}  ## Final dictionary of each movie with the mean user rating
    title_genre_dictionary = {}    ## Dictionary used to store the genre of each movie
    genre_list = []      ## Temporary list used to store a given movies genre data
  
    for line in ratings_data:
        item = line
        ## The first part of each item is a user
        user = attribute_re.search(item).group()
        length = attribute_re.search(item).span()
        item = item[length[1]:]

        ## The second part of the item is a movie
        movie = attribute_re.search(item).group()
        length = attribute_re.search(item).span()
        item = item[length[1]:]

        ## The last part of the item is how the user rated
        ## that particular movie.
        rating = attribute_re.search(item).group()
        length = attribute_re.search(item).span()
        item = item[length[1]:]

        if movie in movie_list:
            current_movie = movie_list[movie]
            rating = float(rating) + float(current_movie[0])
            tally = current_movie[1] + 1
            movie_list[movie] = (rating, tally)
        else:
            movie_list[movie] = (rating, 1)

    for i in range(len(movie_list)):
        pair = movie_list.popitem()
        key = pair[0]
        score = pair[1]
        final_score = float(score[0]) / float(score[1])
        movie_rating_dictionary[key] = int(round(final_score))

    movie_info = open( "Item.txt", "r")

    for line in movie_info:
        item = line
        movie_id = attribute_re.search(item).group()
        length = attribute_re.search(item).span()
        item = item[length[1]:]

        delimeteter = delimeter_re.search(item).group()
        length = delimeter_re.search(item).span()
        item = item[length[1]:]

        title = title_re.search(item).group()
        length = title_re.search(item).span()
        item = item[length[1]:]

        genre = genre_head_re.search(item).group()
        genre_list.append(genre[1])
        length = genre_head_re.search(item).span()
        item = item[length[1]:]

        while genre_re.search(item):
            genre = ""
            genre = genre_re.search(item).group()
            genre_list.append(genre)
            length = genre_re.search(item).span()
            item = item[length[1]:]    

        title_genre_dictionary[movie_id] = (title, genre_list)
        genre_list = []
    return movie_rating_dictionary, title_genre_dictionary
  
if __name__ == dbase_analysis:
    dbase_analysis
