
class isPangram:
    def func(self, word):
        if (type(word) != str):
            return False
        else:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            for letter in alphabet:
                if letter not in word and letter.upper() not in word:
                    return False
            return True