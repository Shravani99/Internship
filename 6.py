# Shravani N. Poman
# **Problem 6**
# Example:
# Input:
# Enter String: ababdefgh
# Longest substring is: abdefgh
# Contact: shravanipoman1999@gmail.com

def longestAlpha(string):
    answer = "" 
    maxi = ""
    
    for i in range(len(string) -1):
        # checks consecutive element if they are in order
        if(string[i] <= string[i+1] ):
            # if in order appends them in variable answer
            answer = answer + string[i] 
            # when it reachs to the end it appends the last element
            if(i==len(string) -2):
                answer = answer + string[i+1]
        # if consecutive elements are not in order
        else:
            answer  = answer + string[i]       
            #if length of the answr is greater then the maxi then the current answer becomes maxi 
            if(len(answer) > len(maxi)):
                maxi = answer
            answer = ""        

    if(len(string) == 1):
        answer = string
    return answer

if __name__ == '__main__':
    testcase = input("Enter number of testcases: ")
    for i in range(int(testcase)):
        string = input("Enter String: ")
        answer = longestAlpha(string)
        print('Longest substring is: '+answer)
    
