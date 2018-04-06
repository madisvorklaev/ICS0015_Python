import sys
ord_buffer = []
chr_buffer = []

def encrypt(plaintext, shift):
    for character in plaintext:
        number = ord(character) + shift #convert characters to ASCII dec and add the shift value
        if number < 97:     #a-1=z
            number = number + 26
        if number > 122:    #z+1=a
            number = number - 26
        ord_buffer.append(number)
    for number in ord_buffer:
        character = chr(number)   #convert ASCII dec to characters
        chr_buffer.append(character)
    return ''.join(chr_buffer)  #join list elements to a string

def decrypt(encrypted_text, shift):
    del ord_buffer[:]   #clear buffer list
    del chr_buffer[:]   #clear buffer list
    for character in encrypted_text:
        number = ord(character) - shift #convert characters to ASCII dec and substract the shift value
        if number < 97:
            number = number + 26
        if number > 122:
            number = number - 26
        ord_buffer.append(number)
    for number in ord_buffer:
        character = chr(number)
        chr_buffer.append(character)
    return ''.join(chr_buffer)
    
plaintext = raw_input("Enter text to be crypted:").lower()  #get user input and convert to lowercase
for character in plaintext:
    if ord(character) < 97 or ord(character) > 122: #check if input is a-z
        print("Please enter only basic Latin alphabet characters")
        sys.exit()
shift = input("Enter shift value:") #26 characters from a to z
while shift > 25:
    shift = shift - 25
while shift < -25:
    shift = shift + 25

encrypted_text = encrypt(plaintext, shift)
print ("The encrypted message is: ") + encrypted_text
decrypted_text = decrypt(encrypted_text, shift)
print ("The decrypted message is: ") + decrypted_text
