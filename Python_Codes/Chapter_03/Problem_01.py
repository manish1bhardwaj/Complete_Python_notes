# =========================================================String Methods=================================================


Name = "I Am Manish Bhardwaj from Btech Cs"
word = Name.split() # to reverse words of string.
Reversed_word = ''.join(reversed(Name))   #syntax to reverse string
print(Reversed_word)                      
# Output : sC hcetB morf jawdrahB hsinaM mA I

#====================================================Split=======================================================

text = "hello, world!"
print(text.split(", "))  # Output: ["hello", "world!"]

# =========================================================join=====================================================

words = ["hello", "world"]
print(", ".join(words))  # Output: "hello, world"
