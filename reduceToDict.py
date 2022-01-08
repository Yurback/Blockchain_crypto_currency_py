from functools import reduce

arr = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y , arr, 0)

print(sum)

words = ['orange', 'grapefruit', 'banana', 'grapefruit', 'banana', 'banana', 'banana']

# должны получить [banana, grapefruit, orange];

def nO(x,y):
    x['sum'] = x['sum'] + y if 'sum' in x else y
    return x


newObj = reduce(nO, arr, {})

print(newObj)


