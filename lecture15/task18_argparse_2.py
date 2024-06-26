import argparse

parser = argparse.ArgumentParser(prog='average',
                                 description='My first argument parser',
                                 epilog='Returns the arithmetic mean')

parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')


'''
python .\lecture15\task18_argparse_2.py 42 3.14 73
python .\lecture15\task18_argparse_2.py --help
python .\lecture15\task18_argparse_2.py "Hello world!"

'''
