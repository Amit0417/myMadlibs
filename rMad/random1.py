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

    madlibs = f'Today I went to my favorite Taco Stand called the {adj} {animal}.  \nUnlike most food stands, they cook and prepare the food in a {vehicle} while you {verb}. \nThe best thing on the menu is the {color} {noun}. \nInstead of ground beef they fill the taco with {food}, cheese, and top it off with a salsa made from {food2}. \nIf that does not make your mouth water, then it just like {person} always says: {saying}!'

    print(madlib)
