N = 50

    
hasil = []

def is_kelipatan3(a):
    for i in range(1, a):
        return a % 3 == 0
    
def is_prima(x):
    for i in range(2, x):
        
        return x % i != 0

# def list_kelipatan3(N):
#     kelipatan3 = []
    
#     for i in range(N + 1):
#         if is_kelipatan3(i):
#             kelipatan3.append(i)
#     return kelipatan3
for i in range(1, N):
    if i:
        hasil.append(i)
    if is_kelipatan3(i):
        hasil.append("Frontend")
        hasil.remove(i)
    if is_prima(i):
        hasil.append("Backend")
        

print(hasil)