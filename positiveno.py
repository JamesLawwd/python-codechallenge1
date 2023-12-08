# program to check for two of three positive numbners
def positive_numbers(a,b,c):
    # positive number count
    positive = 0
    if a > 0:
        positive += 1
    if b > 0:
         positive += 1
    if c > 0:
         positive += 1

# conditon to check for two positive integers
    if positive == 2:
         return True
    else:
         return False
    
# prompt user for an input
option1 = int(input("Enter a:"))
option2 = int(input("Enter b:"))
option3 = int(input("Enter c:"))

result = positive_numbers(option1,option2,option3)

# print result
print(result)