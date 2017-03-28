import media
import fresh_tomatoes

# Create all movie instances bellow

# Creates an instance of Avatar
avatar = media.Movie(
    "Avatar",
    "Because the planet's environment is poisonous, human/Na'vi hybrids, "
    "called Avatars, must link to human minds to allow for free movement on "
    "Pandora. Jake Sully, a paralyzed former Marine, becomes mobile again "
    "through one such Avatar and falls in love with a Na'vi woman.",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

# Creates an instance of The Matrix
matrix = media.Movie(
    "Matrix",
    "The Matrix is a shared simulation of the world as it was in 1999 in "
    "which the minds of the harvested humans are trapped and pacified; "
    "Neo has lived in it since birth. Morpheus and his crew belong to a "
    "group of rebels who hack into the Matrix and \"unplug\" enslaved humans, "
    "recruiting them as rebels.",
    "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Creates an instance of Point Break
point_break = media.Movie(
    "Point Break",
    "An FBI agent goes undercover to catch a gang of "
    "surfers who may be bank robbers.",
    "http://upload.wikimedia.org/wikipedia/en/7/7e/Pointbreaktheatrical.jpg",
    "https://www.youtube.com/watch?v=UuVDrpl1tIY")

# Creates an instance of City of God
city_of_god = media.Movie(
    "City of God",
    "Two boys growing up in a violent neighborhood of Rio de Janeiro take "
    "different paths: one becomes a photographer, the other a drug dealer.",
    "http://upload.wikimedia.org/wikipedia/en/1/10/CidadedeDeus.jpg",
    "https://www.youtube.com/watch?v=ioUE_5wpg_E")

# Creates an instance of Pulp Fiction
pulp_fiction = media.Movie(
    "Pulp Fiction",
    "The lives of two mob hit men, a boxer, a gangster's "
    "wife, and a pair of diner bandits intertwine in four "
    "tales of violence and redemption.",
    "http://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=R17lSf2nmLQ")

# Creates an instance of Wall E
wall_e = media.Movie(
    "Wall E",
    "In a distant, but not so unrealistic, future where "
    "mankind has abandoned earth because it has become "
    "covered with trash from products sold by the powerful "
    "multi-national Buy N Large corporation, WALL-E, a "
    "garbage collecting robot has been left to clean up "
    "the mess.",
    "http://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
    "https://www.youtube.com/watch?v=alIq_wG9FNk")

# Creates the movie list for the fresh_tomatoes class
movies = [avatar, matrix, point_break, city_of_god, pulp_fiction, wall_e]

# Sends the movie list to the fresh_tomatoes method to create the html page
fresh_tomatoes.open_movies_page(movies)
