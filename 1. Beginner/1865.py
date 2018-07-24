# -*- coding: utf-8 -*-


def main():
    C = int(input())
    heroes = []

    for i in range(C):
        heroes.append(input())

    for hero in heroes:
        if 'Thor' in hero:
            print('Y')
        else:
            print('N')


if __name__ == "__main__":
    main()
