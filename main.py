alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
def caesar(start_text, cipher_shift, cipher_direction):
       end_text = ""
       for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + cipher_shift
        else:
            new_position = position - cipher_shift
        end_text += alphabet[new_position]
       print(f" the {cipher_direction} text is {end_text}")
caesar(start_text = text, cipher_shift = shift, cipher_direction = direction)