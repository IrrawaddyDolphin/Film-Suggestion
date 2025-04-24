from app.database import add_rating, your_rating
from app.recommender import suggested_movie

def run_cli():
    print("Hello, this is your private movie recommendation app")
    falsz=False
    while not falsz:
        wybor=input("What would you like to do?\n1.Show recommendation\n2.Rate a movie\n3.Show my ratings\nType number: ")

        if wybor=="1":
            name=input("Name of the movie: ")
            number=int(input("How many recommendation would you like to see? "))
            suggestion=suggested_movie(name,number)
            print(suggestion)
            falsz=True
        if wybor=="2":
            userId="Dawid"
            movieId=input("Which movie would you like to rate? ")
            rating=int(input("What's your rating? "))
            add_rating(userId, movieId, rating)
            falsz=True
        if wybor=="3":
            userId="Dawid"
            oceny=your_rating(userId)
            for ocena in oceny:
                print(ocena)
            falsz=True
        else:
            print("Bye bye")
            falsz=True
