import yaml
data = {
    "word": ['a', 'b', 'c', 'd'],
    "int": 2,
    "dict":{136: '€',181:'µ'}
}

with open('file.yaml', 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=True, allow_unicode = True)

with open('file.yaml') as f_n:

    if f_n.read()== data:
        print('Cовпадают данные')
    else:print('Отличаются данные')


