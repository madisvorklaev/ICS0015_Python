#Class Example v1.0:
#Uses class and method to create an object.
#However, it's allowed to create oen object only.
#Tested with Python 3.6

import time

class Fairytale:
        def __init__(self, character):
                self.character = character

        def printCharacter(self):
                check = 1/thumbelinas_left
                print("    O    ")
                time.sleep(0.3)
                print("  /. .\  ")
                time.sleep(0.3)
                print(" /.   .\ ")
                time.sleep(0.3)
                print(" .     . ")
                time.sleep(0.3)
                print("   I I   ")
                time.sleep(0.3)

        def __str__(self):
                return "%s is ready" %(self.character)

thumbelinas_left = 1
while True:
        try:
                p = input("Enter any character to make a fairytale character: ")
                t = Fairytale("Thumbelina")
                t.printCharacter()
                print(t) #calls the __str__ method
                thumbelinas_left -=1
        except ZeroDivisionError as error :
                print("I'm sorry, Thumbelina is one and only...")
                break
        finally:
                print("Thank you for the 10 points!")
