import os
import re


#cubes either red green blue
# which games would be possible if the bag only had 12r, 13g, 14b

def findSum():

    max_red = 12
    max_green = 13
    max_blue = 14

    f = open("input.txt", 'r')
    results = f.read()
    # results = results.replace("\n", "")

    split_results = results.split("\n")
    # print(split_results)

    for result in split_results:
        result = result[result.find(":") + 1:]
        game = result.split(";")
        game2 = [item.replace(" ", "") for item in game]
        game3 = [item.replace(",", " ") for item in game2]
        print(game3)
        # print(re(r"^red")
        # r_index = result.find('red')
        # result.split()


findSum()
