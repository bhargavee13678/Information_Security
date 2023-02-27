#EXP1 
#IMPLEMENT CEASAR CIPHER
#each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet. 
#For example with a shift of 1, A would be replaced by B, B would become C, and so on.
# A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90

#converting plaintext into ciphertext
pt=input()
pt1= pt.upper()
shift=int(input())
mt=[]
pp=["4"]
for i in pt1:
  if i.isdigit():
    if ord(i)+shift>57:
      mt.append(ord(i)-57+shift-1)
    else:
      mt.append(0+shift)
  else:
    if ord(i)+shift>=90:
      mt.append(chr(ord(i)-26+shift))
    else:
      mt.append(chr(ord(i)+shift))

print(mt)

#BRUTE FORCE ATTACK
ct=input("Enter cipher text")
ct1=ct.upper()
mt=[]
for j in range(0,26):
  for i in ct1:
    if i.isdigit():
      if ord(i)-j>48:
        mt.append(chr(ord(i)-j))
      else:
        
        mt.append(chr((57-(j+48-ord(i)))))
    else:
      if ord(i)-j<65:
        mt.append(chr(90-(j-(ord(i)-65))))  
      else:
        mt.append(chr(ord(i)-j))
print(mt)
s=""
finlist=[]
for i in range(0,26*len(ct1),len(ct1)):
  for j in range(i,i+len(ct1)):
    
    s=s+mt[j]
  finlist.append(s)
  s=""
print(finlist)

