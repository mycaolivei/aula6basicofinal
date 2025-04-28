A=[0, 0, 0, 0, 0]
x=0
m=[0, 0, 0, 0, 0]
for i in range(len(A)):
    A[i]=int(input("Digite um número: "))
x=int(input("Digite um valor para multiplicar: "))
for i in range(len(m)):
    m[i]=x*A[i]
print(A)
print(x)
print(m)


