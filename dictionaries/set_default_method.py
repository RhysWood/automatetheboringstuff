cats = {
    'name': 'Winston',
    'species': 'cat',
    'age': 12
}

if 'color' not in cats:
    cats['color'] = 'black'
#{'name': 'Winston', 'species': 'cat', 'age': 12, 'color': 'black'}

#but you can do this with the setDefault method in one line
cats.setdefault('size', 'small')
print(cats)

#{'name': 'Winston', 'species': 'cat', 'age': 12, 'color': 'black', 'size': 'small'} 

#If it doesn't exist, it adds it - if it does, it leaves it - below would do nothing
cats.setdefault('size', 'medium')
print(cats)
#{'name': 'Winston', 'species': 'cat', 'age': 12, 'color': 'black', 'size': 'small'}