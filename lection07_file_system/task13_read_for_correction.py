with open('text_test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))
        