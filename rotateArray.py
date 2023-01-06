def rotate(array,k):
    return (array[k:] + array[:k])  

array = list(map(int,input("Enter the array: \n").split(' '))) # Please enter the array of numbers in a single line with a space in between
k = int(input("Enter k: ").strip())                            # Enter k lower than or equal to the length of the array only
print(rotate(array,k))