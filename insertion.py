import array as arr
my_array = arr.array('i', [1,2,4,5,6,567,9])
my_array.insert(0,50)
my_array.insert(4,50)
my_array.insert(2,50)

print(my_array)
 

def trav(my_array):
    for i in my_array:
        print(i)

out = trav(my_array)


def access(my_array, index):
    if index> len(my_array):
        print('out of index')
    else :
        print(my_array[index])

out2=access(my_array,3)
