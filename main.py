import pandas

is_continue = "yes"
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}
while is_continue == 'yes':
    user_input = (input("Enter a word: ")).upper()
    try:
        result = [nato_alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry! Only letters in the alphabet please")
    else:
        print(result)
        is_continue = input("Continue? (Type 'yes' or 'no') ")

