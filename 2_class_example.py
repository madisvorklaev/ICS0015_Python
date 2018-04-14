import time

class Thumbelina:
        def __init__(self):
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
                print("Thumbelina is ready")

thumbelinas_left = 1
while True:
        try:
                p = input("Enter any character to make a fairytale character: ")
                Thumbelina()
                thumbelinas_left -=1
        except ZeroDivisionError as error :
                print("I'm sorry, Thumbelina is one and only")
                break

# print(isinstance(blu, Parrot))
# print(issubclass(Parrot, Bird))
