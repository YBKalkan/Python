adet = int(input("Kaç tane fibonacci elemanı gösterilsin: "))
a, b, i= 1, 1, 2

print(a,b, end=" ")
while i < adet: 
    a, b = b, a+b
    i += 1
    print(b, end=" " )
input()
    
