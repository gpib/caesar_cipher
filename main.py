alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text_to_encrypt, shift):
    position_list = []
    shifted_list=[]
    encrypted_text_list = []
    encrypted_text = ""

    #get index of the letter found in the text, assign to the new list
    for letter in text_to_encrypt:
        if letter in alphabet:
            position_list.append(alphabet.index(letter))

    #shift the letters
    for var in position_list:
        if var + shift < len(alphabet):
            shifted_list.append(var + shift)
        else:
            shifted_list.append(shift - (len(alphabet) - var))

    #create list with shifted letters
    for var in shifted_list:
        encrypted_text_list.append(alphabet[var])

    #merge letter into the string
    encrypted_text = ''.join(map(str, encrypted_text_list))
    print(f"Encrypted text {encrypted_text}")

def decrypt(text_to_encrypt, shift):
    position_list = []
    shifted_list=[]
    encrypted_text_list = []
    encrypted_text = ""

    #get index of the letter found in the text, assign to the new list
    for letter in text_to_encrypt:
        if letter in alphabet:
            position_list.append(alphabet.index(letter))

    #shift the letters
    for var in position_list:
        if var - shift >= 0:
            shifted_list.append(var - shift)
        else:
            shifted_list.append((len(alphabet) - abs(var - shift)))

    #create list with shifted letters
    for var in shifted_list:
        encrypted_text_list.append(alphabet[var])

    #merge letter into the string
    encrypted_text = ''.join(map(str, encrypted_text_list))
    print(f"Decrypted text {encrypted_text}")

encrypt(text_to_encrypt= text, shift = shift)
decrypt(text_to_encrypt= text, shift = shift)

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.