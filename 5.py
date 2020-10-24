# Shravani N. Poman
# **Problem 5**
# Example:
# Input:Enter Array: 1 3 6 10
# Output:[20, 19, 16, 10, 0]
# Contact: shravanipoman1999@gmail.com


def AddArray(arr):
    new=[]
    ans=[]
    #deducts one by one elements in array 
    for i in range(len(arr)):
        m=arr[i:]
        new.append(m)
    # Adds the elements 
    for i in new:
        summ=0
        for j in range(len(i)):
            summ+=i[j]
        ans.append(summ)
    ans.append(0)    
    return(ans)

if __name__ == "__main__":
    testcase = input("Enter number of testcases:")
    for i in range(int(testcase)):
        print("Enter Array:")
        arr = list(map(int, input().split()))
        answer = AddArray(arr)
        print(answer)

     