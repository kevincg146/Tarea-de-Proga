def cd_util(n, b):
    if(n<10):
        if(n<b):
            return 1
        else:
            return 0
    else:
        if n%10<b:
            return cd(n)
            return 1 + cd_util(n//10, b)
        else:
            return 0

def cd(n):
    if(n<10):
        return 1
    else:
        return 1+cd(n//10)


def camb_Base(n, b, A):
        if(n<b):
            A.append(n)
            A.reverse()
            return A
        else:
            if len(A)==0:
                A.append(n%b)
                return camb_Base(n//b, b, A)
            else:
                A.append(n%b)
                return camb_Base(n//b, b, A)


def camb_diez(n, b, c, B):
        if(cd(n)==cd_util(n,b)):
            if n<b:
                B = B + (n*b**c)
                return B
            else:
                if B==0:
                    B = B + ((n%10)*b**c)
                    return camb_diez(n//10, b, c+1, B)
                else:
                    B = B + ((n%10)*b**c)
                    return camb_diez(n//10, b, c+1, B)
        else:
            return "No se puede hacer"
            

print(camb_Base(245, 9, []))
print(camb_diez(302, 9, 0 ,B))