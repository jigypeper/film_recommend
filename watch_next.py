"""
This is a notebook with some observations on Semantic Similarity
Note: for this to run you will need to install spacy and download the language model
'pip install spacy'
'python3 -m spacy download en_core_web_md'
"""

import spacy

# load the language models
nlp = spacy.load("en_core_web_md")

# define empty dictionary for raw data
raw_data: dict = {}

# open the movie text file and read the data
with open(file="./movies.txt", mode="r") as movie_file:
    # dictionary comprehension to create a dictionary of keys (movie names) and values (synopsis)
    raw_data = {
        movie.split(" :")[0]: movie.strip("\n").split(" :")[1] for movie in movie_file.readlines()
    }

# comparison data
film, synopsis = "Planet Hulk", "Will he save their world or destroy it? When the Hulk becomes " \
                                "too dangerous for the Earth, the Illuminati trick Hulk into a shuttle " \
                                "and launch him into space to a planet where the Hulk can live in peace. " \
                                "Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery " \
                                "and trained as a gladiator"


# function that takes a synopsis and dictionary of film names with synopsis as values and returns the best
# match for a next watch as a tuple (movie name, similarity score)
def get_recommendation(desc: str, data: dict) -> tuple:
    # define variable to hold the similarity
    comparator: float = 0.0

    # define variable to hold movie title
    movie: str = ""

    # pass synopsis into model
    model_synopsis = nlp(desc)

    # loop through dictionary
    for item in data:
        # get the similarity by comparing synopsis with model synopsis
        similarity = nlp(data[item]).similarity(model_synopsis)

        # check if similarity is greater
        if similarity > comparator:
            # assign similarity to comparator and the movie name (item) to movie
            comparator = similarity
            movie = item

    # return the movie name and similarity score tuple
    return movie, comparator


# run the function and upack the results to variables
recommendation, similarity_score = get_recommendation(synopsis, raw_data)

# print the result with the synopsis
print(f"Based on your like of {film}, you should watch {recommendation}\n the similarity score "
      f"is {round(similarity_score, 2)}\n\n{recommendation} Synopsis\n=================\n{raw_data[recommendation]}")
