import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
  "A story of a boy and his toys that come to life",
  "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
  "https://www.youtube.com/watch?v=vwyZH85NQC4")

school_of_rock = media.Movie("School of Rock",
  "Storyline",
  "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
  "https://www.youtube.com/watch?v=3PsUJFEBC74")


matrix = media.Movie("Matrix",
  "A story of Neo",
  "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
  "https://www.youtube.com/watch?v=7GSgWzmR_-c")

love_exposure = media.Movie("Love Exposure",
  "A Japanese film about love, family, religion and the art of upskirt photography",
  "https://upload.wikimedia.org/wikipedia/en/e/ef/Love_exposure_poster.jpg",
  "https://www.youtube.com/watch?v=sG13M1YwoVg")

the_lives_of_others = media.Movie("The Lives of Others",
  "A German film about the monitering of East Berlin residents by Stagi, the secret police",
  "https://upload.wikimedia.org/wikipedia/en/9/9f/Leben_der_anderen.jpg",
  "https://www.youtube.com/watch?v=n3_iLOp6IhM")


the_intouchables = media.Movie("The Intouchables",
  "A story of an aristocrat and an ex-con",
  "https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
  "https://www.youtube.com/watch?v=34WIbmXkewU")

movies = [toy_story, school_of_rock, matrix, love_exposure, \
the_lives_of_others, the_intouchables]


fresh_tomatoes.open_movies_page(movies)

