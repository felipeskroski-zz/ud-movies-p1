Documentation
-------------
This is a simple python app that generates a website out of a python list.
This is the first project of the Udacity Full Stack Web Developer Nanodegree


# structure of movie class
``` python
Movie(title, storyline, poster_image, youtube_trailer)
```
title -> the movie title
storyline -> a short plot of the movie
poster_image -> the poster image url
youtube_trailer -> the long youtube URL *attention the short URL wont work*
# example of movie class

``` python
matrix = media.Movie("Matrix",
    "The Matrix is a shared simulation of the world as it was in 1999 in "
    "which the minds of the harvested humans are trapped and pacified; "
    "Neo has lived in it since birth. Morpheus and his crew belong to a "
    "group of rebels who hack into the Matrix and \"unplug\" enslaved humans, "
    "recruiting them as rebels.",
    "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # URL
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")
```

# methods
``` python
yourmovie.show_trailer()
```
Opens trailer on youtube


# usage
on your working directory do:
```
python entertainment_center.py

```

# dependencies

``` python
import webbrowser
import os
import re
```

# license

MIT
