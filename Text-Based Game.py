# Final Project
# Well Moua
# April Browne
# Date Created: 5/20/2019
# Description: A text-based adventure game.

# Begin Coding:
import sys

def Game(): #Game Functions
    userChoice = input("Would you like to play? Enter yes or no: ")
    
    if userChoice.lower().strip() == "yes": #Answering Yes, will start the game.
        print ("\nYou woke up in a dark room."
               "\nYou noticed a light in the darkness in the distance."
               "\nIt seems to be block by a door."
               "\nDo you open this door or go back to sleep.")
        userChoice = input("Enter 1 to open the door or 2 to go back to sleep: ")

        if userChoice == "1": #Path decisions from the User's input. 
            print ("\nYou open the door to another world."
                   "\nIt seems to be different than your world back home."
                   "\nYou walk to the other side of the door."
                   "\nYou felt a slight breeze and noticed two weapon on a table."
                   "\nThere lies a sword and a spear."
                   "\nYou can only pick one!!!")
            userChoice = input("Enter 1 for the sword or 2 for the spear: ")

            if userChoice == "1": #First Path of Story and Additional story.
                print ("\nYou decided to pick the sword instead of the spear."
                       "\nOut of nowhere a monster came and attack you."
                       "\nSomehow the monster missed you by a few inch."
                       "\nThe monster was grotesque looking and seems to resemble a bird-like human."
                       "\nDo you fight it or run?")
                userChoice = input("Enter 1 to fight it or 2 to run away: ")

                if userChoice == "1": #Decisions of this path or the other one.
                    print ("\nYou decided to fight grotesque monster."
                           "\nWith your skills of not knowing how to use a sword."
                           "\nThe monster peck you with its large beak and feast on you."
                           "\nYou unlocked the achievement, ''Bird Meat''."
                           "\nGame over", "\n")
                    return Game()

                elif userChoice == "2":
                    print ("\nYou decided to run."
                           "\nAfter hours of walking, you reach a city, called, ''Phoenix City''."
                           "\nYou bumped into a figure."
                           "\nYou apologize to the figure."
                           "\nThe figure seems to be a man."
                           "\nHe noticed that you were strange."
                           "\nHe introduced himself and his name was Lok."
                           "\nHe told you that your sword was a legendary sword that was forged to fight evil."
                           "\nHe told you that you should head to Croust City for the calling.")
                    userChoice = input ("Enter 1 to go to Croust City or 2 not go to to Croust City: ")

                    if userChoice == "1":
                        print ("\nYou decided to go to Croust City for the calling."
                               "\nLok decided to join you as well. To help you fight off evil."
                               "\nThe two of you heads for Croust City."
                               "\nYou unlocked the achievement, ''The New Journey Ahead''."
                               "\nNew path will be add later on. \nThis is just the first part of the story.", "\n")
                        return Game()

                    elif userChoice == "2":
                        print ("\nYou told him that you didn't want to go to Croust City."
                               "\nHe keeps on telling you to go there and somehow convinced you to go."
                               "\nIn which Lok, also decided to go with you."
                               "\nWho knows what lies in Croust City, but there for your calling."
                               "\nYou unlocked the acheivement, ''The New Journey Ahead''."
                               "\nNew Path will be add later on. \nThis is just the first part of the story.", "\n")
                        return Game()

                    else:
                        print ("\nInvalid answer. \nGame Over", "\n")
                        return Game()
                    
                else:
                    print ("\nInvalid answer. \nGame Over", "\n")
                    return Game()

            elif userChoice == "2":
                print ("\nYou decided to pick the spear instead of the sword."
                       "\nOut of nowhere a monster attack you."
                       "\nLuckily you managed to not get hurt by it."
                       "\nThe monster was horrid and somewhat unsettingly to the eyes."
                       "\nThe monster seems to resemble a scaly reptile-human like.")
                userChoice = input("Enter 1 to fight this monster or 2 to run away: ")

                if userChoice == "1":
                    print ("\nYou decided to fight the horrid monster."
                           "\nWith your skills of watching action movies of people using spears."
                           "\nYou manage to graze it and wound it."
                           "\nFor some time, the horrid monster starts to run away.")
                    userChoice = input("Enter 1 to chase it or 2 to let it go: ")

                    if userChoice == "1":
                        print ("\nYou chased the monster inside to it's cave."
                               "\nSince you don't know the cave that great."
                               "\nYou were attacked by a horde of monsters."
                               "\nEnding your journey."
                               "\nYou unlocked the acheivement, ''No Mercy''." ,
                               "\nGame Over", "\n")
                        return Game()

                    elif userChoice == "2":
                        print ("\nYou let the monster escape and seek for a nearby city."
                               "\nAfter hours of walking, you see a city in the distance."
                               "\nYou made it to the city."
                               "\nIt was called, ''Phoenix City''."
                               "\nYou walked around until you bumped into a girl."
                               "\n''Hey watch where you're going."
                               "\nYou apologize."
                               "\nShe noticed that you look different than the person in the city."
                               "\n''You're not from around here are you''."
                               "\nYou nod."
                               "\nI can help you, if you want.")
                        userChoice = input("Enter 1 for her to help you or 2 to not let her help you: ")

                        if userChoice == "1":
                            print ("\nYou let her help you. She told you her name, and it was Kalsine."
                                   "\nShe told you that the spear you're carrying was a spear from the legends to fight evil."
                                   "\nShe insisted that you should head to Croust City to seek answers there."
                                   "\n''But before you go to Croust City, I'll come along and help you."
                                   "\nWithout no doubt, the two of you head to Croust City and beginning your new journey with a new friend."
                                   "\nYou unlocked the acheivement, ''The New Journey Ahead''."
                                   "\nNew Path will be added to the game soon, \nThis is just the first part.", "\n")
                            return Game()

                        elif userChoice == "2":
                            print ("\nYou didn't let her help you, but she helped you anyway,"
                                   "\nShe told you that the spear you're carrying was a spear from the legends to fight evil."
                                   "\nShe insisted that you should head to Croust City to seek answers there."
                                   "\n''But before you go to Croust City, I'll come along and help you."
                                   "\nWithout no doubt, the two of you head to Croust City and beginning your new journey with a new friend."
                                   "\nYou unlocked the acheivement, ''The New Journey Ahead''."
                                   "\nNew Path will be added to the game soon, \nThis is just the first part.", "\n")
                            return Game()
                        
                        else:
                            print ("\nInvalid answer. \nGame Over", "\n")
                            return Game()
                    
                    else:
                        print ("\nInvalid answer. \nGame Over", "\n")
                        return Game()

                elif userChoice == "2":
                    print("\nYou decided to run from this horrid monster.\nYou started to run until you stumbled from a log on the ground."
                          "\nYou trip and fell onto the tip of the spear. \nEnding your adventures in this world."
                          "\nYou unlocked the achievement, ''Just The Tip''. \nGame Over", "\n")
                    return Game()

                else:
                    print("\nInvalid Answer. \nGame Over", "\n")
                    return Game()

            else:
                print ("\nInvalid Answer. \nGame Over", "\n")
                return Game()

        elif userChoice == "2": #Alternative paths of the first path of the game.
             print ("\nYou went back to sleep."
                           "\nGoing back to your world never knowing what was behind that lit door."
                           "\nYou unlocked the acheivement, ''Easy Way Out''."
                           "\nGame Over", "\n")
             return Game()

        else: #If User's Inputted wrong, Game will tell of invalid answers.
            print ("\nInvalid answers. \nGame Over" "\n")
            return Game()

    elif userChoice.lower().strip() == "no":
        print ("That's too bad!!!")
        sys.exit()

    else:
        print ("\n")
        return Game()

Game()
