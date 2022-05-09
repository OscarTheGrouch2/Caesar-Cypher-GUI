#2022 Fall
#CS-212
#Practical Python
#Version 2
#Sunday, 17 April 2022
#Oscar Michua-Zarate
from EncrClass import *
# Description: This class contains the bruteforce algorithm which
#             passes values and strings to other classes that will also use this output

class BruteForce:
    """
        Purpose: To give all possiblities of a string to be able to see a decrypted messsage
        Responsibilities: Will be responsible for shifting the string from its
                          current string to many encrypted string until one of them
                          is readable to the user
    """
    def BruteForceFunc (key,text):
        """
            Description: Will print all possible strings with all possible shifts
            Inputs: string, self
                    self: instance of self
                    String: A string to hold the string input from the user to later shift
            Outputs: None
        """
        for key in range(26):
            key = key + 1
            print(key)
            print(EncryptClass.EncryptFunc(key,text))

 