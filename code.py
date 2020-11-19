txt = input()

txt=txt.split(" ")
n=0
lenlist=[]
while n<len(txt):
 lenword=len(txt[n])
 lenlist.append(lenword)
 n+=1
maxlen=max(lenlist)
index_max=lenlist.index(maxlen)
print(txt[index_max])
 
