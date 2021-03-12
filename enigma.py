# Importing all libraries
# We need ascii_lowercase from string to get the english alphabet
from string import ascii_lowercase
# We need json library to add the possibility for enigma to import settings from a json format
import json

def __init__(self, steckerbrett = {" ":" "}, settings_file=None, alpha=None, beta=None, gama=None):
    ''' The initial setting of enigma before the encryption '''
    # Creating a list of all alphabet letters
    self.alphabet = list(ascii_lowercase)

    '''
        Steckerbrett is a system of sockets that connects pairs of letters that are interchanged between them,
        without going through all the rotors of enigma
    '''
    self.steckerbrett = steckerbrett
    if settings_file != None:
        ''' If the setting sites is got then we load the setting from it as a json format '''
        try:
            # I verify if there is a such file with setting that we got
            self.settings = json.load(open(settings_file, 'r'))[0]
        except IOError as e:
            # The first enigma error - There is no such a settings file
            print("Enigma Error 1: There is no such setting file")
        finally:
            # steckerbratt -> a dictionary with pairs of interchangeable pairs of letters
            self.steckerbrett = self.settings['steckerbrett']
            # Setting the states of rotors
            self.alpha = self.settings['alpha']
            self.beta = self.settings['beta']
            self.gama = self.settings['gama']
    elif alpha != None and beta != None and gama != None and steckerbrett != None:
    
    ''' Setting the rotors and the steckerbrett manually '''
    if type(steckerbrett) is not dict:
        self.steckerbrett = {" " : " "}
    self.alpha = alpha
    self.beta = beta
    self.gama = gama
    else:
    # Setting all rotors to base states and steckerbrett to have only space case
    if type(steckerbrett) is not dict:
        self.steckerbrett = {" " : " "}
    rotors = [self.alpha, self.beta, self.gama]
    for rotor in rotors:
        if rotor == None or type(rotor) is not int or type(rotor) is not float:
            rotor = 0
        else:
            rotor = rotor % 26
    self.alpha = rotors[0]
    self.beta = rotors[1]
    self.gama = rotors[2]
    
    # Making the steckerbrett interchangeable and removing these pairs from the alphabet
    for letter in list(self.steckerbrett.keys()):
        if letter in self.alphabet:
            self.alphabet.remove(letter)
            self.alphabet.remove(self.steckerbrett[letter])
            self.steckerbrett.update({self.steckerbrett[letter]:letter})
    # Setting the reflector
    self.reflector = [leter for leter in reversed(self.alphabet)]

    def permutate(self, rotor):
        ''' This function is permutatting the alphabet depending on the rotors settings '''
        new_alphabet = ''.join(self.alphabet)
        new_alphabet = list(new_alphabet)
        for iter in range(rotor):
            new_alphabet.insert(0, new_alphabet[-1])
            new_alphabet.pop(-1)
        return new_alphabet
    
    def inverse_permutation(self, rotor):
        ''' This function is permutatting the alphabet depending on the rotors settings on the back way '''
        new_alphabet = ''.join(self.alphabet)
        new_alphabet = list(new_alphabet)
        for iter in range(rotor):
            new_alphabet.append(new_alphabet[0])
            new_alphabet.pop(0)
        print(self.alphabet)
        print(new_alphabet)
        return new_alphabet

    def encrypt_text(self, text):
        ''' This function encrypts a string '''
        encrypted_text = []
        # Text preprocessing
        text = text.lower()
        text.split()
        for letter in text:
        # Checking if the letter is in steckerbrett
        if letter in self.steckerbrett:
            # If it is, the we encrypt it as it's pair
            encrypted_text.append(self.steckerbrett[letter])
            # Turning the rotors
            self.alpha += 1
            if self.alpha % 26 == 0:
                self.beta += 1
                self.alpha = 0
            if self.beta % 26 == 0 and self.alpha % 26 != 0 and self.beta >= 25:
                self.gama += 1
                self.beta = 1
                else:
            # Encrypting throw rotors
            # Letter is encrypted by first rotor
            temp_letter = self.permutate(self.alpha)[self.alphabet.index(letter)]
            # Letter is encrypted by second rotor
            temp_letter = self.permutate(self.beta)[self.alphabet.index(temp_letter)]
            # Letter is encrypted by third rotor
            temp_letter = self.permutate(self.gama)[self.alphabet.index(temp_letter)]

        # Reflector is returning the inverse of that letter
temp_letter = self.reflector[self.alphabet.index(temp_letter)]
# Back way
# Letter is encrypted by third rotor
temp_letter = self.inverse_permutation(self.gama)[self.alphabet.index(temp_letter)]
print("gama - {}".format(temp_letter))
# Letter is encrypted by second rotor
temp_letter = self.inverse_permutation(self.beta)[self.alphabet.index(temp_letter)]
print("beta - {}".format(temp_letter))
# Letter is encrypted by first rotor
temp_letter = self.inverse_permutation(self.alpha)[self.alphabet.index(temp_letter)]
print("alpha - {}".format(temp_letter))
encrypted_text.append(temp_letter)
print(temp_letter)

Enigma = enigma({"b":'a', ' ':' ', 'e':'z'}, alpha=5, beta=17, gama=24)

print(Enigma.encrypt_text('there is no time'))
#iuzkz tj on itpz

print(Enigma.encrypt_text('iuzkz tj on itpz'))
#there is no time