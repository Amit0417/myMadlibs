def madlib():
    adj = input("Adjective : ")
    food = input("Food(plural) :")
    verb = input("Verb: ")
    saying = input("Saying :")
    noun = input("Noun : ")
    food2 = input("Food(plural) :")
    color = input("Color : ")
    vehicle = input("Something you would ride in : ")
    animal = input("Animal :")
    person = input("Person :")

    madlib1 = f'Today I went to my favorite Taco Stand called the {adj} {animal}.  ' \
              f'\nUnlike most food stands, they cook and prepare the food in a {vehicle} while you {verb}. ' \
              f'\nThe best thing on the menu is the {color} {noun}. ' \
              f'\nInstead of ground beef they fill the taco with {food}, cheese, and top it off with a salsa made from {food2}. ' \
              f'\nIf that does not make your mouth water, then it just like {person} always says: {saying}!'

    print(madlib1)
