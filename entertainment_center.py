import fresh_tomatoes
import media

#created 1st movie
Top_Gun_2 = media.Movie("Top Gun 2",
                        "After more than thirty years of service as one of the Navy's top aviators, Pete Mitchell is where he belongs, pushing the envelope as a courageous test pilot and dodging the advancement in rank that would ground him.",
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQV4uINuubqA5G4b6fHWfy8wI465HQp9Tey8VykfBGOxPKCSgfj&usqp=CAU",
                        "https://www.youtube.com/watch?v=qSqVVswa420")


#created 2nd movie
high_school_musical = media.Movie("High School Musical",
                                  "Love stroy of a school boy and girl",
                                  "https://upload.wikimedia.org/wikipedia/en/a/a5/HSMposter.jpg",
                                  "https://www.youtube.com/watch?v=ukDLkkvZYFk")


#created 3rd movie
Joker = media.Movie("Joker" ,
                    "Forever alone in a crowd, failed comedian Arthur Fleck seeks connection as he walks the streets of Gotham City. Arthur wears two masks -- the one he paints for his day job as a clown, and the guise he projects in a futile attempt to feel like he's part of the world around him. Isolated, bullied and disregarded by society, Fleck begins a slow descent into madness as he transforms into the criminal mastermind known as the Joker." ,
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJKLiEyyz1Q9RC8EBYl3ijr3nuGeyO2ETmwy6Kdq0AQtD0elWD" ,
                    "https://www.youtube.com/watch?v=t433PEQGErc")


#created 4th movie
Toy_Story_4 = media.Movie("Toy Story 4" ,
                          "On the road of life there are old friends, new friends, and stories that change you." ,
                          "https://lumiere-a.akamaihd.net/v1/images/p_toystory4_inhome_ddt-18133_f7a24937.jpeg" ,
                          "https://www.youtube.com/watch?v=a_S8kAFNydg")


#created 5th movie
URI = media.Movie("URI",
                  "The film is based on the surgical strikes conducted in 2016 by the Indian Army, against militant launch pads in Pakistan occupied Kashmir",
                  "https://i.pinimg.com/474x/1a/3b/9b/1a3b9b7eabc7844050cd37d975583bdd.jpg",
                  "https://www.youtube.com/watch?v=VVY3do673Zc")

#created 6th movie
queen = media.Movie("Queen",
                    "A homely girl who decides to go on her honeymoon alone when her fiance call off the wedding",
                    "https://upload.wikimedia.org/wikipedia/en/4/45/QueenMoviePoster7thMarch.jpg",
                    "https://www.youtube.com/watch?v=RxxUGWC3GiY")

#created 7th movie
sairat = media.Movie("Sairat",
                     "Story of College friends Archi and Parshya, who have contrasting personalities and belong to different castes, fall in love. However, their relationship falls prey to the stringent practice of casteism." ,
                     "https://upload.wikimedia.org/wikipedia/en/a/a1/Sairat_Marathi_Film_Poster.jpg",
                     "https://www.youtube.com/watch?v=wMrMKnoYWwA")

#created 8th movie
Marriage_Story = media.Movie("Marriage Story" ,
                             "A stage director and his actor wife struggle through a gruelling, coast-to-coast divorce that pushes them to their personal and creative extremes." ,
                             "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQlBUUHL54OXdJZ2fHgN8OlktkZs8ePfuhN66fiUYa8HJm_3XXz" ,
                             "https://www.youtube.com/watch?v=5XTlfPKBIOM")

#created 9th movie
dangal = media.Movie("Dangal",
                     "Story of a father who trained his daughters for the Commonwealth Games despite societal pressures.",
                     "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

#array of movies
movies = [Top_Gun_2, high_school_musical, Joker, Toy_Story_4, URI, queen, sairat, Marriage_Story, dangal]

#opening movie page for movies using fresh.tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
