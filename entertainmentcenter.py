import media
import fresh_tomatoes

# This program creates a local website / html file
# for my favorite movies
# New Movies can be simply added by appending four items
#    title.append("Movie Title")
#    description.append(" write the storyline in 1-2 lines")
#    poster.append(" Wikipedia poster link")
#    trailer.append(" You tube trailer link")
#  All dependent files media.py and fresh_tomotoes to be located
# in the same folder as this
# the HTML produced will be create in the same location


title = []
description = []
poster = []
trailer = []

# Movie Toy story
title.append("Toy Story")
description.append("The story of boy and his toys who come to life")
poster.append("https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg")
trailer.append("https://www.youtube.com/watch?v=ZZv1vki4ou4")

# Movie Avatar
title.append("Avatar")
description.append("The story about Humans on a new moon in Avi Galaxy")
poster.append("https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg")
trailer.append("https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Movie men in black
title.append("Men In Black")
poster.append("https://upload.wikimedia.org/wikipedia/en/f/fb/Men_in_Black_Poster.jpg")
description.append("A sci-fi adventure comedy about two top secret agents policing alien activity")
trailer.append("https://www.youtube.com/watch?v=jM2tgZBZtQw")

# new movie  the Foreigner
title.append("The Foreigner")
poster.append("https://upload.wikimedia.org/wikipedia/en/0/05/The_Foreigner_%282017_film%29.jpg")
description.append("The story of Foreign angent trying to solve murder case on his own")
trailer.append("https://www.youtube.com/watch?v=om9YCk7ufHs")

# Movie Moana
title.append("Moana")
description.append("The small town girl breaks the curse")
poster.append("https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg")
trailer.append("https://www.youtube.com/watch?v=LKFuXETZUsI")

#MOvie Harry POtter sorcers stone
title.append("Harry Potter and Sorcerers Stone")
description.append("The story of a young wizard")
poster.append("https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG")
trailer.append("https://www.youtube.com/watch?v=PbdM1db3JbY")

# Add New Movies just as previous ones


# Create a list of Movie classes to be passed
# on to fresh_tomotoes

my_movies = []
i = 0
for ititle in title:
    imovie = media.Movie(title[i], description[i], poster[i], trailer[i])
    my_movies.append(imovie)
    i = i+1

#print media.Movie.__dict__

fresh_tomatoes.open_movies_page(my_movies)




