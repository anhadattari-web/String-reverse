class reverse:
    def __init__(self, s=" "):
        self.__s = s
    def reverse_string(self):
        return self.__s[::-1]
word = input("Enter a word: ")
obj = reverse(word)
print("Reversed string is going to be:", obj.reverse_string())