# Filename: home.py
# Descrption: The main entry for the movie trailer application.
#
# import statements for dependencies.  All files must be located in the
# same directory
import fresh_tomatoes
import movie
import operator

# Initialize an empty list that will contain the instances of all the movies to be displayed
movies = []

# Each movie is appended to the array
url = "https://upload.wikimedia.org/wikipedia/en/f/fd/Templegrandin.jpg"
movies.append(
    movie.Movie(title="Temple Grandin",
                trailer_url="https://youtu.be/cpkN0JdXRpM",
                poster_image_url=url))

url = "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg"
movies.append(
    movie.Movie(title="Kung Fu Panda",
                trailer_url="https://www.youtube.com/watch?v=PXi3Mv6KMzY",
                poster_image_url=url))
url = "https://upload.wikimedia.org/wikipedia/commons/f/f4/\
Marx_Brothers_1931.jpg"
movies.append(
    movie.Movie(title="Room Service",
                trailer_url="https://youtu.be/iIXjftgRtHI",
                poster_image_url=url))

url = "https://upload.wikimedia.org/wikipedia/en/c/cc/\
Underworld_%282003_film%29_poster.jpg"
movies.append(
    movie.Movie(title="Underworld",
                trailer_url="https://youtu.be/MqT-e44kIM8",
                poster_image_url=url))

url = "https://upload.wikimedia.org/wikipedia/en/b/bd/\
Underworld_Rise_of_the_Lycans_poster.jpg"
movies.append(
    movie.Movie(title="Underworld: Rise of the Lycans",
                trailer_url="https://youtu.be/lyWzw5nmSEw",
                poster_image_url=url))

url = "https://upload.wikimedia.org/wikipedia/en/5/5a/\
Underworld2evolution.jpg"
movies.append(
    movie.Movie(title="Underworld: Evolution",
                trailer_url="https://youtu.be/fvXp_ZuM2FA",
                poster_image_url=url))
url = "https://upload.wikimedia.org/wikipedia/en/b/ba/\
Adventures_of_buckaroo_banzai.jpg"
movies.append(
    movie.Movie(title="Buckaroo Banzai",
                trailer_url="https://youtu.be/RdanCNK4ayo",
                poster_image_url=url))

# Sort the list of movies by title
movies.sort(key=lambda x: x.title)

# Invoke fresh tomatoes to create and open the web page in a browser
fresh_tomatoes.open_movies_page(movies)
