def madlib():
    Animals = input("Animals :")
    Feeling = input("Feeling :")
    Things = input("Things(Plural) :")
    Professional = input("A Professional (like “Baker”) :")
    Clothing = input("A Piece of Clothing :")
    Things2 = input("Things(Plural) :")
    Person = input("A Person :")
    Place = input("Place :")
    Verb = input("Verb (ending in 'ing') :")
    Food = input("Food : ")

    madlib = f'Say {Food}, the photographer said as the camera flashed! {Person} and I had gone to {Place} to get our photos taken today.' \
             f'\nThe first photo we really wanted was a picture of us dressed as {Animals} pretending to be a {Professional}.' \
             f'\nWhen we saw the proofs of it, I was a bit {Feeling} because it looked different than in my head.' \
             f'\n(I had not imagined so many {Things} behind us.)\nHowever, the second photo was exactly what I wanted.' \
             f'\nWe both looked like {Things2} wearing {Clothing} and {Verb}--exactly what I had in mind!'
    print(madlib)