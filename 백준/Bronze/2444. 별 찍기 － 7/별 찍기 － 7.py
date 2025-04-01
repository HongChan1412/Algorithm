N = int(input())
for i in range(N-1):
    print(" "*(N-1-i)+"*"*(2*i+1))
print("*"*(2*N-1))
for i in reversed(range(N-1)):
    print(" "*(N-1-i)+"*"*(2*i+1))