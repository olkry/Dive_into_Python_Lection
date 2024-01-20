SIZE = 20
with open('text_test.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)
