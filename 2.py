# Shravani N. Poman
# **Problem 2**
# Example:
# Enter number of Testcases:1
# Enter String: coDe
# Output:       code
# Contact: shravanipoman1999@gmail.com

def ConvertString(string):
    ans=''
    countLower=0
    countUpper=0
    # Checks whether input is in lowercase or uppercase
    for i in string:
        if i.islower():
            countLower+=1
            
        else:
            countUpper+=1
    # converts string to respective case    
    if countLower>countUpper or countLower==countUpper:
        ans=string.lower()
    else:
        ans=string.upper()
    return(ans)   

if __name__ == "__main__":
    testcase=input("Enter number of Testcases:")
    for i in range(int(testcase)):
        string=input("Enter String:")
        answer=ConvertString(string)
        print(answer)