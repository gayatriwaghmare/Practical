input={'ID':{1,2,3},'Name':{'XYZ','ABC','PQR'},'Address':{'Pune','Baner','Mumbai'}}
l=[]
for i in input:
    d={}
    l.append(d)
for k,v in input.items():
    i=0
    for j in v:
        l[i][k]=j
        i+=1
print(l)