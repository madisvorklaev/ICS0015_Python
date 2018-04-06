import sys
plaintext = 'None!'
shift = 'None!'
option = 'None!'
ord_buffer = []
chr_buffer = []

def ask_plaintext():
    global plaintext
    global shift
    global option
    option = input("Would you like to encrypt (1) or decrypt (2) a message? ")
    if option == 1:
        plaintext = raw_input("Enter text to be encrypted: ").lower()  #get user input and convert to lowercase
    elif option == 2:
        plaintext = raw_input("Enter text to be decrypted: ").lower()  #get user input and convert to lowercase
    else:
        print("Please choose 1 or 2")
        sys.exit()    
    for character in plaintext:
        if ord(character)!= 32: #if not SPACE
            if ord(character) < 97 or ord(character) > 122: #check if input is a-z
                print("Please enter only basic Latin alphabet characters")
                sys.exit()
    shift = input("Enter shift value: ") 
    while shift > 25:   #26 characters from a to z, a+25=z
        shift = shift - 25
    while shift < -25:
        shift = shift + 25
        
def ask_file():
    global plaintext
    global shift
    global option
    option = input("Would you like to encrypt (1) or decrypt (2) a message? ")
    if option == 1:
        input_file = open(raw_input("Enter the name of the file "))
        plaintext = input_file.read()
        plaintext = plaintext.lower()  #get user input and convert to lowercase
        input_file.close()
    elif option == 2:
        input_file = open(raw_input("Enter the name of the file "))
        plaintext = input_file.read()
        plaintext = plaintext.lower()  #get user input and convert to lowercase
        input_file.close()
    else:
        print("Please choose 1 or 2")
        sys.exit()    
    for character in plaintext:
        if ord(character)!= 32: #if not SPACE
            if ord(character) < 97 or ord(character) > 122: #check if input is a-z
                print("Please enter only basic Latin alphabet characters")
                sys.exit()
    shift = input("Enter shift value: ") 
    while shift > 25:   #26 characters from a to z, a+25=z
        shift = shift - 25
    while shift < -25:
        shift = shift + 25


def encrypt(plaintext, shift):
    del ord_buffer[:]   #clear buffer list, necessary when checking the result
    del chr_buffer[:]   #clear buffer list, necessary when checking the result
    for character in plaintext:
        number = ord(character) + shift #convert characters to ASCII dec and add the shift value
        if number - shift != 32: #if not SPACE
            if number < 97:     #a-1=z
                number = number + 26
            if number > 122:    #z+1=a
                number = number - 26
        ord_buffer.append(number)
    for number in ord_buffer:
        character = chr(number)   #convert ASCII dec to characters
        chr_buffer.append(character)
    return ''.join(chr_buffer)  #join list elements to a string

def decrypt(plaintext, shift):
    del ord_buffer[:]   #clear buffer list, necessary when checking the result
    del chr_buffer[:]   #clear buffer list, necessary when checking the result
    for character in plaintext:
        number = ord(character) - shift #convert characters to ASCII dec and substract the shift value
        if number != 32: #if not SPACE
            if number < 97:
                number = number + 26
            if number > 122:
                number = number - 26
        ord_buffer.append(number)
    for number in ord_buffer:
        character = chr(number)
        chr_buffer.append(character)
    return ''.join(chr_buffer)

#ask_plaintext()
ask_file()
if option == 1:
    encrypted_text = encrypt(plaintext, shift)
    print ("The encrypted message is: ") + encrypted_text
    decrypted_text = decrypt(encrypted_text, shift) #check if program works correctly
    print ("The decrypted message was: ") + decrypted_text
else:
    decrypted_text = decrypt(plaintext, shift)
    print ("The decrypted message is: ") + decrypted_text
    encrypted_text = encrypt(decrypted_text, shift) #check if program works correctly
    print ("The encrypted message was: ") + encrypted_text
