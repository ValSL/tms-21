'''Даны три слова.
Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
т. е. таким, которое читается одинаково слева направо и справа налево.
(Определить функцию, позволяющую распознавать слова палиндромы.)'''


def is_palindrom(word: str) -> str:
    if word == word[::-1]:
        return 'palindrome'
    else:
        return 'not palindrome'


def main():
    words = ['aga', 'net', 'omlet']
    for word in words:
        print(f'word {word} is {is_palindrom(word)}')


if __name__ == '__main__':
    main()
