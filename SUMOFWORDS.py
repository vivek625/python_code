# nuclear software coding question
'''
A = 0
B = 1
C = A+B
D = C+B
----------------------------
INPUT1 = str 
OUTPUT = int
-----------------------------
EX = 'MAN'
OUT = 377
----------------------------
EXPLANTION = M = 144 , A = 0 , N = 233 last add(MAN) = 144+0+233 == 377
'''


s = "MAN"
ss = { 'A': 0,
    'B': 1,
    'C': A+B,
    'D': C+B,
    'E': D + C,
    'F': E+D,
    'G':F+E,
    'H': G+F,
    'I': H+G,
    'J':I+G,
    'K': J+I,
    'L': K+J,
    'M': L+K,
    'N': M+L,
    'O': N+M,
    'P': O+N,
    'Q': P+O,
    'R': Q+P,
    'S': R+Q,
    'T': S+R,
    'U': T+S,
    'V': U+T,
    'W': V+U,
    'X': W+V,
    'Y': X+W,
    'Z': Y+X
    }
k = []
for i in ss:
    for j in s:
        if j == i:
            k.append(ss[i])
print(sum(k))
