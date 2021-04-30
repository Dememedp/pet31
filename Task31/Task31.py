import string
alphabet = string.ascii_lowercase
length = len(alphabet)

def in_all(array):
    count = 0
    i = 0
    arrayofchar = list()
    lenlen = len(array)
    for letter in alphabet:
        while i < lenlen:
            for let in array[i]:
                if let == letter:
                    count +=1
            i +=1
        if count >= lenlen:
            arrayofchar.append(letter)
        count = 0
        i = 0
    return arrayofchar

def in_one(array):
    count = 0
    i = 0
    arrayofchar = list()
    lenlen = len(array)
    for letter in alphabet:
        while i < lenlen:
            for let in array[i]:
                if let == letter:
                    count +=1
            i +=1
        if count >= 1:
            arrayofchar.append(letter)
        count = 0
        i = 0
    return arrayofchar

def in_two(array):
    count = 0
    i = 0
    arrayofchar = list()
    lenlen = len(array)
    for letter in alphabet:
        while i < lenlen:
            for let in array[i]:
                if let == letter:
                    count +=1
                    break
            i +=1
        if count >= 2:
            arrayofchar.append(letter)
        count = 0
        i = 0
    return arrayofchar

def not_used(array):
    count = 0
    i = 0
    arrayofchar = list()
    lenlen = len(array)
    for letter in alphabet:
        while i < lenlen:
            for let in array[i]:
                if let == letter:
                    count +=1
            i +=1
        if count == 0:
            arrayofchar.append(letter)
        count = 0
        i = 0
    return arrayofchar


array = ["apple", "adickk", "a4lenk"]
while True:
    print("in all - 1\nin one - 2\nin two - 3\nnot used - 4\nexit - 0")
    a = int(input())
    if a == 1:
        print(in_all(array))
    elif a == 2:
        print(in_one(array))
    elif a == 3:
        print(in_two(array))
    elif a == 4:
        print(not_used(array))
    else:
        print("ok")
        break

