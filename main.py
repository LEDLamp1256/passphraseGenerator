import secrets

#common password requirements:
#-12 characters + (do length check)
#-Uppercase/lowercase (
#-numbers
#-symbols if letters in word not in symbolSubstitutes, then add random punctuation
#get around random

# test = "yacht yearn yeast yield young youth"
# splitTest = test.split(" ")
# for text in splitTest:
#     print(text)

numberSubstitutes = {"i" : "1", "e" : "3", "s" : "5", "b" : "8", "o" : "0"}
symbolSubstitutes = {"i" : "!", "a" : "@", "t" : "+"}

characterLengthReq = int(input("How long should the password be?"))
uppercaseReq = eval(input("Does the password need to contain uppercase characters? (T/F)").capitalize())
numbersReq = eval(input("Does the password require numbers? (T/F)").capitalize())
symbolsReq = eval(input("Does the password require symbols? (T/F)").capitalize())

if characterLengthReq % 5 == 0:
    numWords = (characterLengthReq//5) + secrets.choice([0, 1])
else:
    numWords = (characterLengthReq//5) + secrets.choice([1, 2])



print(numWords)
print(characterLengthReq)
print(uppercaseReq)
print(numbersReq)
print(symbolsReq)
#number of words
#number and symbol location

with open("words.txt") as f:
    #all words that can be used split into a list
    splitWords = f.read().split()

password = []
if uppercaseReq:
    for i in range(numWords):
        password.append(secrets.choice(splitWords).capitalize())
else:
    for i in range(numWords):
        password.append(secrets.choice(splitWords))

passwordJoin = "".join(password)


def substitution(passwordSub, substituteDict):
    for letter in passwordSub:
        if letter in substituteDict:
            passwordSub = passwordSub.replace(letter, substituteDict[letter])
    return passwordSub


if secrets.choice([1, 2]) == 1:
    passwordJoin = substitution(passwordJoin, numberSubstitutes)
    passwordJoin = substitution(passwordJoin, symbolSubstitutes)
else:
    passwordJoin = substitution(passwordJoin, symbolSubstitutes)
    passwordJoin = substitution(passwordJoin, numberSubstitutes)


print(passwordJoin)
