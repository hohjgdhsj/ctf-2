a=[0x3E,0x1A,0x56,0x0D,0x52,0x13,0x58,0x5A,0x6E,0x5C,0x0F,0x5A,0x46,0x07,0x09,0x52,0x25,0x5C,0x4C,0x0A,0x0A,0x56,0x33,0x40,0x15,0x07,0x58,0x0F]
a.reverse()
b=[]
for i in range(28):
    b.append(0)
    for j in range(0x7F):
        if ((j *0x3f)+0x7B)%0x80==a[i]:
            b[i]=j
s=''
for i in range(28):
    s+=chr(b[i])
print(s)