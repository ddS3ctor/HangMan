import random
import requests

url = 'http://127.0.0.1:5000'
response = requests.get(url + "/words")
words = response.json()

def play():
    # while words.length() > 0:
    #     continue
    word_length = len(words[2])
    hiddenIndeces = word_length // 2
    print_table(words[2], hide_indeces(words[2]))

def solve(word):
    fill_chars = []

    print_table(word)


def hide_indeces(word):
    word_length = len(word)
    hidden_indeces = word_length // 2
    hidden = []
    
    for i in range(0, hidden_indeces):
        hide = random.randint(i, word_length - 1)
        while hide in hidden:
            hide = random.randint(i, word_length - 1)
        hidden.append(hide)

    return hidden


def print_table(word, hiddenIndeces):
    print(hiddenIndeces)
    colums = len(word)
    score = 0

    print('+---' * colums + '+')
    print(end='|')

    for column in range(colums): print(end=' ' + str(column+1) + ' |')
    print()

    print('+---' * colums + '+')
    print(end='|')
    for column in range(colums):
        if column in hiddenIndeces: print(end=' _ |')
        else: print(end=' ' + word[column] + ' |')
    print()
    print('+---' * colums + '+')

    if len(str(score)) == 1: print(end='| score:  ' + str(score) + ' |')
    elif len(str(score)) == 2: print(end='| score: ' + str(score) + ' |')
    elif len(str(score)) == 3: print(end='| score: ' + str(score) + '|')
    print()
    print('+' + '---' * 3 + '--+')


if __name__ == '__main__':
    play()