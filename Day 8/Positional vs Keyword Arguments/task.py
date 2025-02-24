# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


# greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# greet_with(name="henk", location="amsterdam")

def calculate_love_score(name1, name2):
    true_amount = 0
    love_amount = 0

    name = name1+name2
    for char in "true":
        if name.count(char) > 0:
            true_amount += name.count(char)

    for char in "love":
        if name.count(char) > 0:
            love_amount += name.count(char)
    print(f" {true_amount}{love_amount}")
calculate_love_score("Angela Yu", "Jack Bauer")

calculate_love_score("Kanye West", "Kim Kardashian")