# Shravani N. Poman
# **Problem 3**
# Example:
# Input:Enter number > 1:12
# Output:[2, 3, 4, 6]
# Contact: shravanipoman1999@gmail.com

def Divisor(number):
    li=[]
    #checks if the number is divisible
    for i in range(2,(number//2)+1):
        if number%i==0:
            li.append(i)
    #if list is empty then declares number as prime        
    if len(li)==0:
        return(f"{number} is a prime number")
    else:
        return(li)            
          




if __name__ == "__main__":
    testcase=input("enter no. of testcases:")
    for i in range(int(testcase)):
        number=input("Enter number > 1:")
        answer=Divisor(int(number))
        print(answer)