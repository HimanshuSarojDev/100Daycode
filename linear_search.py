def linear_search(my_list, tar):
        for i,value in enumerate(my_list):
            if value == tar:
                return i 
        return -1


my_list = [5,8,9,50,6]
tar = int(input(""))
print(linear_search(my_list,tar))