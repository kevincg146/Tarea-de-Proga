
def cd_util(n,b):
    if n<10:
        if n<b:
            return 1
        else:
            return 0
    else:
        if(n%10)**cd(n)-1<b:
            return 1+cd_util(n//10, b)
        else:
            return 0

def cd(n):
    if n<10:
        return 1
    else:
        return 1+cd(n//10)

def camb_base(n,b,A):
    if(cd(n)==cd_util(n,b)):
        if n<b:
            A.append(n)
            return A
    else:
        if len(A)==0:
            A.append(n%b)
            return camb_base(n//10,b,A)
        else:
            A.append(n%b)
            return camb_base(n//10,b,A)
print(camb_base(24436,6,[]))


    