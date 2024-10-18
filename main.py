import pandas
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [data_dic[c] for c in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()

#Data Frame way:
#TODO 1. Create a data frame in this format:
# data = pandas.read_csv("nato_phonetic_alphabet.csv") == data_frame = pandas.DataFrame(data)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# word = input("Enter a word: ").upper()
# word_c = [c for c in word]
# result = [row.code for c in word_c for (index,row) in data_frame.iterrows() if c == row.letter]
# print(result)
