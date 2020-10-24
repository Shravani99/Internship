# Shravani N. Poman
# **Problem 4**
# Example:
# Input:Enter String: hello world
# Output: HelloWorld
# Contact: shravanipoman1999@gmail.com

def CamelCase(string):
    #splits the string in an array
    b=string.split()
    camel=[]
    c=''
    #Assigns the first letter of string as uppercase always and rest lower
    for i in b:
        c=i[0].upper()
        c+=i[1:].lower()
        camel.append(c)

    camel=''.join(camel) 
    return(camel)

if __name__ == "__main__":
    testcase=input("Enter Number of testcases:")
    for i in range(int(testcase)):
        string=input("Enter String:")
        ans=CamelCase(string)
        print(ans)