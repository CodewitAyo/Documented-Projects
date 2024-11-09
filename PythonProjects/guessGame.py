import random

cities = ["Saskatoon", "Lagos", "Berlin", "London", "Calgary", "Montreal", "New York",
          "Abidjan", "Helsinki", "Vancouver", "Paris", "Vienna"]
secret_city = random.choice(cities)
number_of_guesses = 0
print("Type a city from the given options. You have three guesses, good luck!")
print("Options:", cities)
while True:
    guess = input("Type your guess: ")
    number_of_guesses += 1
    if guess == secret_city:
        print("Congratulations! You guessed the secret city in ", number_of_guesses, " guesses!")
        break
    elif number_of_guesses == 3:
        print("You are out of guesses. The secret city was: ", secret_city, " .")
        break
    else:
        if 1 <= number_of_guesses < 2:
            print("Sorry that is incorrect city. Please try again, you have", 3 - number_of_guesses, "guesses left.")
        else:
            print("Sorry that is incorrect city. Please try again, you have", 3 - number_of_guesses, "guess left.")
