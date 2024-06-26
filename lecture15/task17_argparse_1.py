import argparse
parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')


'''
python .\lecture15\task17_argparse_1.py 42 3.14 73
python .\lecture15\task17_argparse_1.py --help
python .\lecture15\task17_argparse_1.py "Hello world!"

'''