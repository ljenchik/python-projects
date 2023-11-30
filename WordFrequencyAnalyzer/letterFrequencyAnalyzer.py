import pandas as pd
from matplotlib import pyplot as plt

letters = list(map(chr, range(97, 123)))

def letterFrequencyAnalyzer(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            frequency_dictionary = dict()
            for char in content:
                char = char.lower()
                if char in letters:
                    if char not in frequency_dictionary.keys():
                        frequency_dictionary[char] = 1
                    else:
                        frequency_dictionary[char] += 1
            frequency_dictionary = {k: v for k, v in
                                    sorted(frequency_dictionary.items(), key=lambda item: item[1], reverse=True)}
            first = list(frequency_dictionary.keys())[0]
            most_frequent_letters = {}
            for item in frequency_dictionary:
                if frequency_dictionary[item] == frequency_dictionary[first]:
                    most_frequent_letters[item] = frequency_dictionary[item]
            if len(most_frequent_letters.keys()) == 1:
                print("The most frequent letters in the text is: ", ','.join(most_frequent_letters.keys()))
            else: print("The most frequent letters in the text are: ", ','.join(most_frequent_letters.keys()))

            print("The number of all different letters in the text is: ", len(frequency_dictionary.keys()))
            for key, value in frequency_dictionary.items():
                print(f'{key} : {value}')
            plt.bar(frequency_dictionary.keys(), frequency_dictionary.values())
            plt.show()
            return ','.join(most_frequent_letters.keys())
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied. Unable to access '{file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


#letterFrequencyAnalyzer('text.txt')
letterFrequencyAnalyzer('text1.txt')
