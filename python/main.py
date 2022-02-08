import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('No integer is given as the execution parameter.')

    for i in range(len(args)):
        if i == 0:
            continue

        print(args[i])
