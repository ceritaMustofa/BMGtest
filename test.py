N = 50

hasil = []


def is_kelipatan3(a):
    for i in range(1, a):
        return a % 3 == 0
    
def is_kelipatan5(a):
    for i in range(1, a):
        return a % 5 == 0
    
def is_kelipatan15(a):
    for i in range(1, a):
        return a % 15 == 0

for i in range(1, N + 1):
    
    
    if is_kelipatan15(i):
        hasil.append("Frontend Backend")
    elif is_kelipatan3(i):
        hasil.append("Frontend")
    elif is_kelipatan5(i):
        hasil.append("Backend")
    else:
        hasil.append(i)
    

print(hasil)