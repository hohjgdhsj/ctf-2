secret=[0x49,0xE6,0x57,0xBD,0x3A,0x47,0x11,0x4C,0x95,0xBC,0xEE,0x32,0x72,0xA0,0xF0,0xDE,0xAC,0xF2,0x83,0x56,0x83,0x49,0x6E,0xA9,0xA6,0xC5,0x67,0x3C,0xCA,0xC8,0xCC,0x05]
xor=[0,0,8,0,128,0,0,1,0,48,8,1,128,0,12,1,64,0,0,0,0,0,8,1,64,0,0,2,0,16,4,0,192,16,0,0,192,48,0,2,128,16,8,0,64,32,4,2,0,48,0,3,192,16,4,2,192,0,8,1,128,48,0,2,192,0,0,1,128,16,4,1,128,48,4,2,0,16,12,2,192,0,4,3,0,32,12,1,0,16,12,0,192,32,12,3,192,16,0,2,128,48,0,2,64,16,12,3,64,32,4,2,128,0,12,0,128,48,8,1,192,48,0,1,0,48,8,0,0,16,4,0,0,0,8,0,128,0,12,3,192,0,12,2,192,32,8,1,64,48,12,3,0,0,12,1,0,0,4,1]
print(len(secret))
print(len(xor))
a=''

for i in range(len(secret)):
    a+=chr(secret[i]^xor[4*i]^xor[4*i+1]^xor[4*i+2]^xor[4*i+3])
print(a)