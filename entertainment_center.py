import media
import fresh_tomatoes

suicide_squad = media.Movie("Suicide Squad", "DC universe villans have to save the day", "https://upload.wikimedia.org/wikipedia/en/a/a7/Suicide_Squad_%28film%29_Logo.jpg", "https://www.youtube.com/watch?v=WI3hecGO_04")

alien = media.Movie("Alien", "Astronauts encounter an alien bieng", "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg", "https://www.youtube.com/watch?v=DGAHtWV7Ua8")

ghost_busters = media.Movie("Ghost Busters", "A group of fringe scientists open up a ghost control business.", "https://upload.wikimedia.org/wikipedia/en/c/c7/Ghostbusters_cover.png", "https://www.youtube.com/watch?v=vntAEVjPBzQ")

akira = media.Movie("Akira", "A member of a biker gang in the dystopian future develops psychic powers", "https://upload.wikimedia.org/wikipedia/en/5/5d/AKIRA_%281988_poster%29.jpg", "https://www.youtube.com/watch?v=FtPhrCTjMtQ")

full_metal_jacket = media.Movie("Full Metal Jacket", "A group of marines are trained and deployed in the Vietnam War", "https://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg", "https://www.youtube.com/watch?v=Ks_MbPPkhmA")

layer_cake = media.Movie("Layer Cake", "A man must go through the ups and downs of the crime world to fulfill his dream of leaving it", "https://upload.wikimedia.org/wikipedia/en/e/e8/Layer_Cake_Poster.JPG", "https://www.youtube.com/watch?v=e5R4iepdXqo")

the_dark_crystal = media.Movie("The Dark Crystal", "A young Gelfling must go on a magical adventure to restore his world", "https://upload.wikimedia.org/wikipedia/en/7/77/The_Dark_Crystal_Film_Poster.jpg", "https://www.youtube.com/watch?v=CF-53aIU5aY")

legend = media.Movie("Legend", "Young Jack must go on a magical adventure to save his world and the love of his life", "https://upload.wikimedia.org/wikipedia/en/9/98/Legendposter.jpg", "https://www.youtube.com/watch?v=als5pGB3Tfg")

#put all the movies into a list to be readable by the fresh tomatoes method open_movies_page
movies = [suicide_squad, alien, ghost_busters, akira, full_metal_jacket, layer_cake, the_dark_crystal, legend]

#
fresh_tomatoes.open_movies_page(movies)
