alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(text_to_encrypt, shift, choice):
    position_list = []
    shifted_list=[]
    encrypted_text_list = []
    encrypted_text = ""

    #get index of the letter found in the text, assign to the new list
    for letter in text_to_encrypt:
        if letter in alphabet:
            position_list.append(alphabet.index(letter))

    if choice == "encode":
        #shift the letters
        for var in position_list:
            if var + shift < len(alphabet):
                shifted_list.append(var + shift)
            else:
                shifted_list.append(shift - (len(alphabet) - var))
    elif choice == "decode":
        # shift the letters
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
    print(f"Caesar text {encrypted_text}")

caesar(text_to_encrypt=text, shift=shift, choice = direction)



    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
