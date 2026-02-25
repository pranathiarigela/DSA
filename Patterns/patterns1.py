def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()
pattern1(4)

def pattern2(n):
    for i in range(n):
        for j in range(0,i+1):
            print("*",end="")    
        print()
pattern2(5)

def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
pattern3(5)

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end="")
        print()
pattern4(5)

def pattern5(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print("*",end="")
        print()
pattern5(5)

def pattern6(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(j,end="")
        print()
pattern6(5)

def pattern7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end="")
        print()
pattern7(5)
print("\n")
def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range((2*n)-(2*i)-1):
            print("*",end="")
        for j in range(i):
            print(" ",end="")
        print()
pattern8(5)

print("\n")

def pattern9(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end="")
        print()
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range((2*n)-(2*i)-1):
            print("*",end="")
        for j in range(i):
            print(" ",end="")
        print()
pattern9(5)

def pattern10(n):
    for i in range(2*n-1):
        stars=i
        if i>n:
            stars=2*n-i
        for j in range(1,stars):
            print("*",end="")
        print()
pattern10(5)

def pattern11(n):
    for i in range(n):
        start=1
        if i%2==0:
            start=1
        else:
            start=0
        for j in range(i):
            print(start,end="")
            start=1-start
        print()
pattern11(5)

def pattern12(n):
    space=2*(n-1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        for j in range(space):
            print(" ",end="")
        for j in range(i,0,-1):
            print(j,end="")
        print()
        space-=2
pattern12(5)

def pattern13(n):
    num=1
    for i in range(1,n+1):
        for j in range(i):
            print(num,end=" ")
            num=num+1
        print()
pattern13(4)

def pattern14(n):
    for i in range(1, n + 1):
        ch = ord('A')
        for j in range(i):
            print(chr(ch), end="")
            ch += 1
        print()
pattern14(5)

def pattern15(n):
    for i in range(n, 0, -1):
        ch = ord('A')
        for j in range(i):
            print(chr(ch), end="")
            ch += 1
        print()
pattern15(5)

def pattern16(n):
    for i in range(n):
        ch=chr(ord('A')+i)
        for j in range(i+1):
            print(ch,end=" ")
        print()
pattern16(5)

def pattern17(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        ch = "A"
        breakpoint = (2 * i + 1) // 2
        for j in range(2 * i + 1):
            print(ch, end="")
            if j < breakpoint:
                ch = chr(ord(ch) + 1)
            else:
                ch = chr(ord(ch) - 1)
        print()
pattern17(5)

def pattern18(n):
    for i in range(n):
        ch = ord('A') + (n - i - 1)
        while ch <= ord('A') + n - 1:
            print(chr(ch), end=" ")
            ch += 1
        print()
pattern18(5)

def pattern19(n):
    iniS = 0
    for i in range(n):
        for j in range(n - i):
            print("*", end="")
        for j in range(iniS):
            print(" ", end="")
        for j in range(n - i):
            print("*", end="")
        iniS += 2
        print()
    iniS = 2 * (n - 1)
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        for j in range(iniS):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        iniS -= 2
        print()
pattern19(5)

def pattern20(n):
    spaces = 2 * n - 2
    for i in range(1, 2 * n):
        stars = i
        if i > n:
            stars = 2 * n - i
        for j in range(stars):
            print("*", end="")
        for j in range(spaces):
            print(" ", end="")
        for j in range(stars):
            print("*", end="")
        print()
        if i < n:
            spaces -= 2
        else:
            spaces += 2
pattern20(5)

def pattern21(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
pattern21(4)

def pattern22(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            top = i
            left = j
            right = (2 * n - 2) - j
            down = (2 * n - 2) - i
            value = n - min(top, left, right, down)
            print(value, end=" ")
        print()
pattern22(4)