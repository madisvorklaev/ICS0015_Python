import sys
plaintext = 'None!'
shift = 'None!'
ord_buffer = []
chr_buffer = []
FIRST_CH = 97
LAST_CH = 122
SPACE_CH = 32


def get_data():
    global plaintext
    global shift
    input_file = open(raw_input("Enter the name of the file "))
    plaintext = input_file.read().lower()
    input_file.close()
    for character in plaintext:
        if ord(character)!= SPACE_CH:
            #check if input is a-z
            if ord(character) < FIRST_CH or ord(character) > LAST_CH:
                print("Please enter only basic Latin alphabet characters")
                sys.exit()
    shift = input("Enter shift value: ") 
    #26 characters from a to z, a+25=z
    while shift > 25:
        shift = shift - 25
    while shift < -25:
        shift = shift + 25


def encrypt(plaintext, shift):
    #clear buffer lists, necessary when checking the result
    del ord_buffer[:]  
    del chr_buffer[:]
    for character in plaintext:
        #convert characters to ASCII dec and add the shift value
        number = ord(character) + shift
        if number - shift != SPACE_CH:
            #make the alphabet roll: a-1=z and z+1=a
            if number < FIRST_CH:
                number = number + 26
            if number > LAST_CH:
                number = number - 26
        ord_buffer.append(number)
    for number in ord_buffer:
        #if not a-z, then it must be space. necessary when checking the result
        if number < FIRST_CH or number > LAST_CH:
            number = SPACE_CH
        #convert ASCII dec to characters
        character = chr(number)
        chr_buffer.append(character)
    #join list elements to a string and return it
    return ''.join(chr_buffer)

def decrypt(plaintext, shift):
    del ord_buffer[:]
    del chr_buffer[:]
    for character in plaintext:
        number = ord(character) - shift
        if number != SPACE_CH:
            if number < FIRST_CH:
                number = number + 26
            if number > LAST_CH:
                number = number - 26
        ord_buffer.append(number)
    for number in ord_buffer:
        if number < FIRST_CH or number > LAST_CH:
            number = SPACE_CH
        character = chr(number)
        chr_buffer.append(character)
    return ''.join(chr_buffer)

option = input("Would you like to encrypt (1) or decrypt (2) a message? ")
if option > 2:
    print("Please choose 1 or 2")
    sys.exit()    
get_data()
if option == 1:
    encrypted_text = encrypt(plaintext, shift)
    print ("The encrypted message is: ") + encrypted_text
    #check if program works correctly, must return the input text
    decrypted_text = decrypt(encrypted_text, shift)
    print ("The decrypted message was: ") + decrypted_text
else:
    decrypted_text = decrypt(plaintext, shift)
    print ("The decrypted message is: ") + decrypted_text
    encrypted_text = encrypt(decrypted_text, shift)
    print ("The encrypted message was: ") + encrypted_text

##def ask_plaintext():
##    global plaintext
##    global shift
##    global option
##    option = input("Would you like to encrypt (1) or decrypt (2) a message? ")
##    if option == 1:
##        plaintext = raw_input("Enter text to be encrypted: ").lower()  #get user input and convert to lowercase
##    elif option == 2:
##        plaintext = raw_input("Enter text to be decrypted: ").lower()  #get user input and convert to lowercase
##    else:
##        print("Please choose 1 or 2")
##        sys.exit()    
##    for character in plaintext:
##        if ord(character)!= SPACE_CH: #if not SPACE
##            if ord(character) < FIRST_CH or ord(character) > LAST_CH: #check if input is a-z
##                print("Please enter only basic Latin alphabet characters")
##                sys.exit()
##    shift = input("Enter shift value: ") 
##    while shift > 25:   #26 characters from a to z, a+25=z
##        shift = shift - 25
##    while shift < -25:
##        shift = shift + 25
##        

