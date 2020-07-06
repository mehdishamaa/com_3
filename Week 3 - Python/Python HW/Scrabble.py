# Base Scrabble word calculator instructions
# Given the below scoring create a Scrabble word calculator that will provide the correct scores dependent on the string provided.
#
# Letter                             Value
# A, E, I, O, U, L, N, R, S, T       1
# D, G                               2
# B, C, M, P                         3
# F, H, V, W, Y                      4
# K                                  5
# J, X                               8
# Q, Z                               10

scrabble_dictionary = {tuple(["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]): 1, tuple(["D", "G"]): 2,
                       tuple(["B", "C", "M", "P"]): 3,
                       tuple(["F", "H", "V", "W", "Y"]): 4, tuple(["J", "X"]): 8, tuple(["Q", "Z"]): 10
                       }




def scrabble_calc():
    scrabble_points = 0
    word = input("Please type in your Scrabble word:")
    for i in word:
        scrabble_points = scrabble_points + scrabble_dictionary[i]
        return scrabble_points


print(scrabble_calc(word))

