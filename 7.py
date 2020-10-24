# Shravani N. Poman
# **Problem 7**
# Example:
# Input:enter fraction:10/7
# Output: 1 3/7
# Contact: shravanipoman1999@gmail.com
def getFraction(no):
    li=[]
    newli=[]
    numer=''
    denom=''
    # gets numerator and denominator
    for i in no:
        li.append(i)   
    newli=li    

    for i in range(len(li)):
        if li[0]=="-":
            li=li[1:]
            
        if li[i]!='/':
            numer+=li[i]
        else:
            divi=i
            break
    m=li[divi+1:]
    for i in  m:
        denom+=i
    n1=int(numer)    
    d1=int(denom)


    # gcd of numer denom
    small = min(n1,d1)
    if n1%small ==0 and d1%small==0:
        Num=n1//( small)
        Den=d1//( small)
            
    else:
        start = 1
        hcf =1
        while start<=small:
            if n1%start==0 and d1%start==0:
                hcf= max(hcf,start)
            start = start +1  
        gcd=hcf    
        Num=n1//(gcd )
        Den=d1//(gcd )
    

    #***solve**
    f1=Num//Den
    f2=Num-(Den*f1)
    # if the fraction is negative 
    if newli[0]=="-":
        if f2==0:
            return(f1)
        else:
            if f1==0:
                a=f'- {f2}/{Den}'
                return(a)
            else:
                a=f'-{f1} {f2}/{Den}'
                return(a) 
    #if fraction is positive            
    else:      
        if f2==0:
            return(f1)
        else:
            if f1==0:
                a=f'{f2}/{Den}'
                return(a)
            else:
                a=f'{f1} {f2}/{Den}'
                return(a) 


if __name__ == "__main__":
    testcase=input("ENter number of testcase:")
    for i in range(int(testcase)):
        string=input("enter fraction:")
        answer=getFraction(string)
        print(answer)
        
