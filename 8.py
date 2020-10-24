# Shravani N. Poman
# **Problem 8**
# Example:
# Input:Enter String:Success
# Output:(())())
# Contact: shravanipoman1999@gmail.com
def NewString(string):
    from collections import Counter
    string.lower()
    #Counts number of particular alphabet/letter/symbol in string
    dicti= dict(Counter(string))
    c=''
    #Comparisons
    for i in string:
        if i in dicti:
                if dicti[i]>1:
                    c+=")"
                else:
                    c+="("    

    return(c)        

if __name__ == "__main__":
    testcase=input("enter no.of testcases:")
    string=input("Enter String:")
    answer=NewString(string)
    print(answer)