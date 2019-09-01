from numpy import *
from struct import unpack
A = mat([[1,1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,-1,1,1,-1,-1,1,-1,1,1],
[1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,1],
[1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,1,-1,-1,1,1,1,-1,1,-1],
[1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1],
[1,-1,-1,1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1],
[1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1],
[1,-1,1,1,1,-1,1,1,1,1,-1,1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1],
[1,1,-1,-1,-1,1,1,-1,1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,1,1,1,1,1,-1,1,-1,1,1,1,1,-1,-1],
[1,-1,-1,1,1,-1,1,1,1,1,1,-1,-1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1],
[1,1,1,-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,1],
[1,-1,1,1,-1,-1,1,1,-1,-1,-1,-1,1,1,1,-1,1,-1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,-1,1,1],
[1,-1,1,1,1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,1,1,-1,1,-1,1,1,1,1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1],
[1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1],
[1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1],
[1,1,1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1],
[1,-1,1,1,1,1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,1,-1,1,1,1,1,-1,1,1,-1],
[1,-1,1,1,-1,-1,1,1,1,1,1,-1,1,-1,1,1,1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,1],
[1,1,1,1,1,-1,1,1,1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,1,1,-1],
[1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1],
[1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1,1,-1,1,-1,-1,-1,1,1,-1],
[1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,1,-1,1,-1],
[1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1],
[1,1,1,1,1,1,1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,-1,1,1],
[1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1],
[1,1,-1,1,1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,1,1,-1],
[1,-1,1,1,-1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,1,1],
[1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,1,1],
[1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1],
[1,-1,1,1,1,-1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,-1,1,1,1],
[1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,1,1,1,1,1,-1,-1,1,1,-1,1,1,-1,1],
[1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1],
[1,1,-1,1,1,-1,-1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,-1],
[1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,1,1,-1,1,-1,1,1,1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,1,-1,1],
[1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1],
[1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1],
[1,-1,1,1,1,-1,-1,1,1,-1,-1,1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,-1],
[1,1,1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,-1,1,1,-1],
[1,-1,-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,-1,1,-1,-1,1,-1,-1,-1],
[1,1,1,1,-1,1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1],
[1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,1],
[1,-1,-1,-1,1,1,1,-1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,-1,-1,1,1,-1,1,1,1,1],
[1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1]])
res = "FFFFFF94FFFFFF3800000126FFFFFF28FFFFFC1000000294FFFFFC9E000006EA000000DC00000006FFFFFF0CFFFFFDF6FFFFFA82FFFFFCD000000182000003DE0000014E000002B2FFFFF8D800000174FFFFFAA6FFFFF9D4000001C2FFFFF97C0000035A00000146FFFFFF3CFFFFFA14000001CE000007DCFFFFFD48000000980000085EFFFFFDB0FFFFFFBC0000036EFFFFFF4EFFFFF836000005C0000006AE0000069400000022".decode("hex")
y = []
for i in range(42):
    tmp = res[i*4:i*4+4]
    tmp = unpack(">i",tmp)[0]
    y.append(tmp)
B = mat(y)
B = B.reshape(42,1)
B = A.I*B
B = B.reshape(1,42)
B = B.tolist()[0]
for i in range(42):
    B[i] = int(round(B[i]))
    B[i]^=i
    B[i] = (B[i]>>3)|(B[i]<<5)
    B[i]&=0xff
print("".join(map(chr,B)))