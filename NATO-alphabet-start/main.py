# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_dict)

is_crap = True

while is_crap:
    word = input("Type a word to NATO-ise: ").upper()
    try:
        output = [new_dict[letter] for letter in word]
        is_crap = False
    except KeyError:
        print("Loser!  Only letters, please!")

print(output)
