#Caesar Cipher implemented by Shees Ikram
#This is a simple implementation of the Caesar Cipher in Python
#The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet
#For example, with a shift of 1, A would be replaced by B, B would become C, and so on
#The method is named after Julius Caesar, who apparently used it to communicate with his officials
#The encryption can also be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A -> 0, B -> 1,..., Z -> 25
#Encryption of a letter x by a shift n can be described mathematically as E_n(x) = (x + n) mod 26
#Decryption is a similar process that can be mathematically described as D_n(x) = (x - n) mod 26
#Here is a simple implementation of the Caesar Cipher in Python



class CaesarCipher:
    def __init__(self):
        self.alphabet_lower:list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
        self.alphabet_upper:list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def encrypt(self,text:str,shift:int)->None:
        new_letters:list = []
        for char in text:
            if char in self.alphabet_lower:
                position = (self.alphabet_lower.index(char) +shift) % 26
                new_letters.append(self.alphabet_lower[position])
            elif char in self.alphabet_upper:
                position = (self.alphabet_upper.index(char) +shift) % 26
                new_letters.append(self.alphabet_upper[position])
            else:
                new_letters.append(char)
        print("".join(new_letters))

    def decrypt(self,text:str,shift:int)->None:
        new_letters:list = []
        for char in text:
            if char in self.alphabet_lower:
                position = (self.alphabet_lower.index(char) -shift) % 26
                new_letters.append(self.alphabet_lower[position])
            elif char in self.alphabet_upper:
                position = (self.alphabet_upper.index(char) -shift) % 26
                new_letters.append(self.alphabet_upper[position])
            else:
                new_letters.append(char)
        print("".join(new_letters))

    """
    the decrypt method is the same thing as self.encrypt(text,-shift)
    """

def main():
    caesar = CaesarCipher()
    user_text:str = input('What text would you like to encrypt or decrypt with the caesar cipher?\n')
    user_shift:int = int(input("What is the shift amount?\n"))
    type:str = input("Do you want to encrypt or decrypt\n")
    if type.lower() == "decrypt":
        caesar.decrypt(user_text,user_shift)
    else:
        caesar.encrypt(user_text, user_shift)



if __name__ == "__main__":
    main()
    