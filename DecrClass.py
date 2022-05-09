#2022 Fall
#CS-212
#Practical Python
#Version 2
#Sunday, 17 April 2022
#Oscar Michua-Zarate

# Description: This class contains the decrypt algorithm which 
#             passes values and strings to other classes that will also use this output

class DecryptClass:
    """
        Purpose: To change the string to be back to its origional form
        Responsibilities: Will be responsible for shifting the string from its
                          current string to hopefully the origional.
    """
    def DecryptFunc (key, text):
        """
            Description: Will shift input string back
            Inputs: key, string
                    key: a value for class decrypt to know how many alphabetical
                         shifts it requires
                    text: A string to hold the string input from the user to later shift
            Outputs: decrypted
                     decrypted: Returns the modified string back to the canvas to show
        """
        decrypted = ""
        for text in text:
            if text.isupper(): 
                keyShifts = ord(text) - ord('A')
                # shift the current character to left by key positions to get its original position
                origionalPosition = (keyShifts - key) % 26 + ord('A')
                origionalText = chr(origionalPosition)
                decrypted += origionalText
            elif text.islower(): 
                keyShifts = ord(text) - ord('a') 
                origionalPosition = (keyShifts - key) % 26 + ord('a')
                origionalText = chr(origionalPosition)
                decrypted += origionalText
            #checks if it's a number to shift its real value   
            elif text.isdigit():
                origionalText = (int(text) - key) % 10
                decrypted += str(origionalText)
            else:
                #if its none of above, just leave it as is
                decrypted += text
        return decrypted

