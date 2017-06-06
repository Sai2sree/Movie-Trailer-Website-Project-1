import media
import fresh_tomatoes

# Create multiple instances of the Python Class to represent the movies

The_Godfather = media.Movie("The Godfather",
                            "https://s-media-cache-ak0.pinimg.com/736x/a1/"
                            "04/d7/a104d7bf99fe08a48520566f1d81509d.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")
Titanic = media.Movie("Titanic",
                      "http://www.freemovieposters.net/posters/"
                      "titanic_1997_6121_poster.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")
The_Dark_Knight = media.Movie("The Dark Knight",
                              "https://paulmmartinblog.files.wordpress.com/"
                              "2011/07/the_dark_knight_poster.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")
Beauty_and_the_Beast = media.Movie("Beauty and the Beast",
                                   "https://cdn.traileraddict.com/content/"
                                   "walt-disney-pictures/beauty-"
                                   "and-beast-2017-5.jpg",
                                   "https://www.youtube.com/"
                                   "watch?v=e3Nl_TCQXuw")
Bahubali_2 = media.Movie("Bahubali 2",
                         "https://www.desiretrees.in/wp-content/uploads"
                         "/2017/01/Bahubali-2-Posters.jpg",
                         "https://www.youtube.com/watch?v=G62HrubdD6o&t=15s")
The_Shawshank_Redemption = media.Movie("The Shawshank Redemption",
                                       "http://thegalileo.co.za/wp-content/"
                                       "uploads/2015/09/"
                                       "9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",
                                       "https://www.youtube.com/"
                                       "watch?v=NmzuHjWmXOc")

# Group all the instances together in a list

movies = [The_Godfather,
          Titanic,
          The_Dark_Knight,
          Beauty_and_the_Beast,
          Bahubali_2,
          The_Shawshank_Redemption]

fresh_tomatoes.open_movies_page(movies)
