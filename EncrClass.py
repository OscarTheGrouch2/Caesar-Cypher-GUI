#2022 Fall
#CS-212
#Practical Python
#Version 2
#Sunday, 17 April 2022
#Oscar Michua-Zarate

# Description: This class contains the Encrypt algorithm which 
#             passes values and strings to other classes that will also use this output

class EncryptClass:
    """
        Purpose: To change the string to an encrypted form
        Responsibilities: Will be responsible for shifting the string from its
                          current string to an encrypted version.
    """

    def __init__(self,key,text):
        self.key = key
        self.text = text

    def EncryptFunc(key, text):
        """
            Description: Will shift input string forward so many alphabetical positions
            Inputs: Key, string 
                    Key: a value for class decrypt to know how many alphabetical
                         shifts it requires
                    text: A string to hold the string input from the user to later shift
            Outputs: encrypted
                     encrypted: Returns the modified string back to the canvas to show
        """
        encrypted = ""
        for text in text:
            #check if it's an uppercase character
            if text.isupper(): 
                textIndex = ord(text) - ord('A')
                # shift the current character by key positions
                keyShifts = (textIndex + key) % 26 + ord('A')
                result = chr(keyShifts)
                encrypted += result
            #check if its a lowecase character    
            elif text.islower(): 
                textIndex = ord(text) - ord('a') 
                keyShifts = (textIndex + key) % 26 + ord('a')
                result = chr(keyShifts)
                encrypted += result
            #checks if it's a number to shift its real value
            elif text.isdigit():
                result = (int(text) + key) % 10
                encrypted += str(result)
            else:
                #if its none of above, just leave it as is
                encrypted += text
        return encrypted

    