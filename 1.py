# Shravani N. Poman
# **Problem 1**
# Example:
# Input:
# Enter row and col(row*3): 5 15
# Output:
# ------.|.------
# ---.|..|..|.---
# ----WELCOME----
# ---.|..|..|.---
# ------.|.------
# Contact: shravanipoman1999@gmail.com

def make(row,col,dot,count):
    side = (col-dot*3)//2
    if count == row//2:
        #Base Case
        print('-'*((col-7)//2),end='')
        print('WELCOME',end='')
        print('-'*((col-7)//2),end='')
        dot = dot - 2
        print()
        return
    else:
        print('-'*side,end='')
        print('.|.'*dot,end='')
        print('-'*side,end='')
        print()
        #Recursion
        make(row,col,dot+2,count + 1)
    print('-'*side,end='')
    print('.|.'*dot,end='')
    print('-'*side,end='')
    dot = dot-2
    print()

if __name__ == "__main__":
    testcase=input("enter no. of testcases:")
    for i in range(int(testcase)):
        inp = list(map(int, input('Enter row and col(row*3): ').split()))
        row = inp[0]
        col = inp[1]
        make(row,col,1,0)
         