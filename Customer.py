## Sean Bloomsburg
## sbloomsburg@gmail.com
##
## The function in this module creates and returns
## a dictionary of users with a vector that represents 
## a mean of the movies they like.
##


from math import *
import re


def build_user_vector(movie_rating_dictionary, title_genre_dictionary):
    attribute_re = re.compile('\d+')

    customer_data = open( "learn.txt", "r")
    user_item_vector = {}
    user_movie_count = {}
    vector = []

    for i in range(20):
        vector.append(0)

    for line in customer_data:
        item = line
        user = attribute_re.search(item).group()
        length = attribute_re.search(item).span()
        item = item[length[1]:]
        
        current_movie = attribute_re.search(item).group()
        length = attribute_re.search(item).span()
        item = item[length[1]:]

        user_rating = attribute_re.search(item).group()
        length = attribute_re.search(item).span()
        item = item[length[1]:]

        if user in user_item_vector:
            vector = []
            vector.extend(user_item_vector[user])

            if float(user_rating) > 2:
                movie_rating = float(movie_rating_dictionary[current_movie])
                movie_data = title_genre_dictionary[current_movie]
                movie_genre = []
                movie_genre.extend(movie_data[1])

                for i in range(19):
                    vector[i] = float(vector[i]) + float(movie_genre[i])

                vector[19] = float(vector[19]) + float(movie_rating)
                user_item_vector[user] = vector
                user_movie_count[user] = user_movie_count[user] + 1

        if user not in user_item_vector:
           if float(user_rating) > 2:
                movie_rating = float(movie_rating_dictionary[current_movie])
                movie_data = title_genre_dictionary[current_movie]
                movie_genre = []
                movie_genre.extend(movie_data[1])
                vector = []

                for i in range(20):
                    vector.append(0)

                for i in range(19):
                    vector[i] = float(vector[i]) + float(movie_genre[i])

                vector[19] = float(vector[19]) + float(movie_rating)
                user_item_vector[user] = vector
                user_movie_count[user] = 1


    ## The user vector has genre totals and a rating total and 
    ## must now be replaced with a mean of those totals.
    users = user_item_vector.keys()
    for user in users:
        user_vector = []
        user_vector.extend(user_item_vector[user])
        movie_count = 0
        movie_count = user_movie_count[user]
        vector = []
        for element in user_vector:
            value = (float(element) / float(movie_count))
            vector.append(value)

        user_item_vector[user] = vector

    return user_item_vector

if __name__ == build_user_vector:
    build_user_vector
