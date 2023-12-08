# time converting program from 12 hour to 24 hour
# input 09:04:45 pm | output 21:04:30

def convert24(t):

    if t[-2] == "AM" and t[:2] == "12":
        return "00" + t[2:-2]
    # exclude the AM
    elif t[-2] == "AM":
        return t[:-2]
    
    # if the last two elements is PM and first two elements is 12
    elif t[-2] == "PM" and t[:2] == "12":
        #remove PM

        return t[:-2] 
    
    # adding 12 to pm

    else: 
        return str(int(t[:2]) +12) + t[2:8]
    
prompt = input('Enter time in 12 hour:')
result = convert24(prompt)
# print result
print(result)
