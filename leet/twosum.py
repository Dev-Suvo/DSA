def twoSum(n):
        lst = []
        while(n>0):
            num = int(input("Enter the numbers:"))
            lst.append(num)
            n-=1
        
        target=int(input("Enter target value:"))
        print(lst, type(lst))

            

n = int(input("Enter the count of the list:"))
twoSum(n+2)