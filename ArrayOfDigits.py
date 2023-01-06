
def ArrayOfDigits(num):
    array = [int(digit) for digit in str(num)]

    # array = []                            #this is another possible solution that takes retrieves the last number and then adds it the array
    # while(num>0):                         #if you want to run this solution, please comment the above solution and uncomment the already commented solutions
    #     d = num%10                            
    #     array.insert(0,d)
    #     num //= 10
    return array

num = int(input("Enter the number: ").strip())
print(ArrayOfDigits(num))