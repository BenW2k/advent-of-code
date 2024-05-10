import os

def decrypt_text():
    f = open("input.txt", "r")
    text = f.read()

    split_text = text.splitlines()
    code = 0
    count= 0

    for word in split_text:
        # k = 0
        # l = len(word)- 1
        num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        num_dict2 = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        number = ""
        startLoop = False
        stopLoop = False
        lowest_index = len(word)
        highest_index = -1
        word_found = False

        for key in num_dict:
            if key in word:
                if word.rfind(key) > highest_index:
                    highest_index = word.rfind(key)
                    highest_number = key
                if word.find(key) < lowest_index:
                    lowest_index = word.find(key)
                    lowest_number = key
                word_found = True

        if word_found == True:
            if lowest_index == highest_index:
                word = word[:highest_index] + str(num_dict[highest_number]) + word[highest_index +1:]
            else:
                lowest_letter = lowest_number[0]
                highest_letter = highest_number[0]
                word = word[:lowest_index] + str(num_dict[lowest_number]) + word[lowest_index + 1:]
                word = word[:highest_index] + str(num_dict[highest_number]) + word[highest_index + 1:]
                # word = word.replace(lowest_letter, str(num_dict[lowest_number]))
                # word = word.replace(highest_letter, str(num_dict[highest_number]))
        
        k = 0
        l = len(word) - 1

        while stopLoop == False:
            if word[k].isdigit():
                number = number + word[k]
                stopLoop = True
                startLoop = True
            else:
                k+=1
        
        while startLoop == True:
            if word[l].isdigit():
                number = number + word[l]
                code += int(number)
                count += 1
                print(f'word: {word} number: {number} and sum: {code} count: {count}')
                startLoop = False
            else:
                l-=1
    
    

decrypt_text()




