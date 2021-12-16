## Challenge 1
def sum_to(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum




## Challenge 2
def largest(list):
    holder = list[0]
    for n in list:
        if n > holder:
            holder = n
    
    return holder




## Challenge 3
def occurances(str1,str2):
    arr = str1.split(str2)
    return (len(arr)-1)


## Challenge 4
def product(*args):
    prod = 1
    for arg in args:
        prod *= arg

    return prod

print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop','ee'))


