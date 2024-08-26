import requests


url = 'http://127.0.0.1:5000'
response = requests.get(url + "/words")
words = response.json()

def play():
    # while words.length() > 0:
    #     continue
    print_table(words[2])


def print_table(word):
    colums = len(word)

    print('+---' * colums + '+')
    print(end='|')
    for colum in range(colums):
        print(end=' ' + word[colum] + ' |')
    print()
    print('+---' * colums + '+')


if __name__ == '__main__':
    play()