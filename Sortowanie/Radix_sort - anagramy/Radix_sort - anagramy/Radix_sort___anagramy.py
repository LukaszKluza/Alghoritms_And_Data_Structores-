def counting_sort_radix(T,col):
    nT = len(T)
    Count = [0]*27
    Out = [0]*nT 
    base = ord('a')-1
    for word in T:
        idx = ord(word[col])-base if len(word) > col else 0
        Count[idx] += 1
    for i in range(1,27):
        Count[i]+=Count[i-1]

    for word in reversed(T):
        idx = ord(word[col])-base if len(word) > col else 0
        Out[(Count[idx]-1)] = word 
        Count[idx] -= 1
    return Out


def Radix_sort(T):
     n = len(max(T, key = len))
     for i in range(n-1,-1,-1):
        T = counting_sort_radix(T,i)
     return T

def counting_sort(word):
    A = [0]*26
    res = ''
    base = ord('a')
    for c in word:
        A[ord(c)-base]+=1
    for i in range(26):
        while A[i] > 0:
            res+=chr(i+base)
            A[i] -= 1
    return res

def anagram(T):
    n = len(T)
    for i in range(n):
        T[i] = counting_sort(T[i]) 
    T = Radix_sort(T)
    print(T)
    res = temp = 1
    for i in range(1,n):
        if T[i] == T[i-1]:
           temp+=1
        else:
            res = max(res,temp)
            temp = 1
    return max(res,temp)


def partition(T,p,k):
    print(p,k)
    q = (p+k)//2
    T[q],T[k] = T[k],T[q] 
    x = T[k]
    i = p-1
    for j in range(p,k):
        if T[j] < x:
            i += 1
            T[i],T[j] = T[j],T[i]
    T[i+1],T[k] = T[k], T[i+1]
    print(T,i+1)
    return i+1

def Quick_sort(T,p,k):
    while p<k:
        q = partition(T,p,k)
        Quick_sort(T,p,q-1)
        p = q+1


def anagram1(T):
    n = len(T)
    for i in range(n):
         T[i] = counting_sort(T[i])
    Quick_sort(T,0,len(T)-1)
    print(T)
    res = temp = 1
    for i in range(1,n):
        if T[i] == T[i-1]:
           temp+=1
        else:
            res = max(res,temp)
            temp = 1
    return max(res,temp)




T = ["ok","ko","kk"]
K = [4,22,5,1,4,12,41,523]
lst = ['aa', 'a', 'ab', 'abs', 'asd', 'avc', 'axy', 'abid']
A = ['tygrys','kot','wilk','trysyg','wlik','sygryt','likw','tygrys']
#print(T)
#print(Radix_sort(T),sorted(T))

#print(anagram1(T))
Quick_sort(K,0,len(K)-1)
print(K)