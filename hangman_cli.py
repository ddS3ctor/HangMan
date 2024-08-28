import random
import requests

url = 'http://127.0.0.1:5000'
response = requests.get(url + "/words")
words = response.json()

def play():
    # while words.length() > 0:
    #     continue
    print_table(words[2])

def solve(word):
    fill_chars = []

    print_table(word)


def print_table(word):
    colums = len(word)
    score = 0

    print('+---' * colums + '+')
    print(end='|')

    for column in range(colums): print(end=' ' + str(column+1) + ' |')
    print()

    print('+---' * colums + '+')
    print(end='|')
    for column in range(colums): print(end=' ' + word[column] + ' |')
    print()
    print('+---' * colums + '+')

    if len(str(score)) == 1: print(end='| score:  ' + str(score) + ' |')
    elif len(str(score)) == 2: print(end='| score: ' + str(score) + ' |')
    elif len(str(score)) == 3: print(end='| score: ' + str(score) + '|')
    print()
    print('+' + '---' * 3 + '--+')


if __name__ == '__main__':
    play()