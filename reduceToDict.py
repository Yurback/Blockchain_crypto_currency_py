from functools import reduce

arr = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y , arr, 0)

print(sum)

# получаем {sum: 15}

def nO(x,y):
    x['sum'] = x['sum'] + y if 'sum' in x else y
    return x


newObj = reduce(nO, arr, {})

print(newObj)

# получаем {'0': 1, '1': 2, '2': 3, '3': 4, '4': 5}

ind=0

def nO(x,y):
    global ind
    x[str(ind)] = x['sum'] + y if 'sum' in x else y
    ind += 1
    return x


newObj = reduce(nO, arr, {})

print(newObj)
print(ind)

# получаем кумулятивный итог {'0': 1, '1': 3, '2': 6, '3': 10, '4': 15}

ind=0

def nO(x,y):
    global ind
    x[str(ind)] = x[str(ind-1)] + y if str(ind-1) in x else y
    ind += 1
    return x


newObj = reduce(nO, arr, {})

print(newObj)
print(ind)


