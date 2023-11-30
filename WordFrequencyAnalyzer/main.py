from spellchecker import SpellChecker

spell = SpellChecker()


def check(word):
    if word == spell.correction(word):
        return True
    else:
        return False


def frequencyAnalyzer(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            content_list = content.split()
            frequency_dictionary = dict()
            for word in content_list:
                if check(word):
                    if word not in frequency_dictionary.keys():
                        frequency_dictionary[word] = 1
                    else:
                        frequency_dictionary[word] += 1
            frequency_dictionary = {k: v for k, v in
                                    sorted(frequency_dictionary.items(), key=lambda item: item[1], reverse=True)}
            first = list(frequency_dictionary.keys())[0]
            most_frequent_words = {}
            for item in frequency_dictionary:
                if frequency_dictionary[item] == frequency_dictionary[first]:
                    most_frequent_words[item] = frequency_dictionary[item]
            print("The mos frequent words in the text are: ", ','.join(most_frequent_words.keys()))
            print("The number of all different words in the text is: ", len(frequency_dictionary.keys()))
            for key, value in frequency_dictionary.items():
                print(f'{key} : {value}')
            return ','.join(most_frequent_words.keys())
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied. Unable to access '{file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


frequencyAnalyzer('text.txt')
