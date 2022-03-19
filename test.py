N = 50

hasil = []
kelipatan3 = []

def is_kelipatan3(a):
    for i in range(1, a):
        return a % 3 == 0
    
def is_kelipatan5(a):
    for i in range(1, a):
        return a % 5 == 0
    
def is_prima(x):
    for i in range(5, x):
        
        return x % i != 0

    
for i in range(1, N + 1):
    if is_kelipatan3(i):
        kelipatan3.append(i)

for i in range(1, N + 1):
    list_kelipatan3 = kelipatan3
    if i:
        hasil.append(i)
    if is_kelipatan3(i):
        hasil.append("Frontend")
    if is_kelipatan5(i):
        hasil.append("Backend")
        hasil.remove(i)
    if i == list_kelipatan3:
        hasil.remove(i)
    

print(hasil)