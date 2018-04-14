#Class Example v1.0:
#Uses class to create an object.
#However, it's allowed to create oen object only.

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
                print(self.character, "is ready")

thumbelinas_left = 1
while True:
        try:
                p = input("Enter any character to make a fairytale character: ")
                Thumbelina = Fairytale(character = "Thumbelina")
                Thumbelina.printCharacter()
                thumbelinas_left -=1
        except ZeroDivisionError as error :
                print("I'm sorry, Thumbelina is one and only")
                break
