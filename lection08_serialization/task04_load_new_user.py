import json

with open('new_user.json', 'r', encoding='utf-8') as f:
    file_rid = json.load(f)

print(f'{file_rid = }')
print(f'{file_rid['children'][1]['age'] = }')