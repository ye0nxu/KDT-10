# 확장자 : Better Comments
## //  
## todo
## ?
## !
## *
## =======================================
def solution(n):
    i = 2
    ret=[]
    while i <= n :
        if (n/i) == (n//i) : ## 나눠지면
            n = n/i
            ret.append(i)
        else:
            i += 1
        
    ret = list(set(ret))
    return ret

print(solution(420))   # 4

for i in range(-3,2,1):
    print(i)

