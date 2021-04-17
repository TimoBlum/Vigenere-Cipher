import pygame

pygame.init()

print("### Vignere Cipher ###")
text = input("Your Text here (to encode): ")
key = input("What key to use for encoding?: ")
encoded = ""

abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,!? "

abcs = []


def findPlace(s, lst):
    counter = 0
    for i in lst:
        if i == s:
            return counter
        else:
            counter += 1


def makeKeyStream(key, text):
    keystream = ""
    c = 0
    if len(key) > len(text):
        for l in range(0, len(text)):
            keystream += key[l]

    elif len(key) < len(text):
        while len(keystream) != len(text):
            if c == len(key):
                c = 0
            else:
                keystream += key[c]
                c += 1
    else:
        keystream = key
    return keystream


keystream = makeKeyStream(key, text)


def shiftText(txt, shift):
    global abc
    newWord = ""
    for i in txt:
        if shift + findPlace(str(i), abc) > len(abc) - 1:
            newWord += abc[(shift + findPlace(str(i), abc) - len(abc))]
        else:
            newWord += abc[shift + findPlace(str(i), abc)]
    return newWord


def makeABC():
    global abcs
    for l in range(0, len(abc)):
        abcs.append(shiftText(abc, l))


makeABC()

for l in range(0, len(text)-1):
    encoded += abcs[findPlace(text[l], abc)][findPlace(keystream[l], abc)]

print("The Keystream is: ", keystream)
print("Encoded: ", encoded)
