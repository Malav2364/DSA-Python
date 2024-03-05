# for i in range(5, 0, -1):
#     print("* " * i)

#diamond pattern
# space = 4
# for i in range(1, 10, 2):
#     print(" "*space+"*"*i)
#     space-=1

#prime number 
# for num in range(20, 41):
#     count = 0
#     for factor in range(1, num+1):
#         if num%factor == 0:
#             count +=1
#     if count == 2:
#         print(num)

def hello(*keys):
    print("Values: ", keys)

hello(10, 20, 30, 23 ,23, 2,3 ,23 ,23,)

