#input={'ID':{1,2,3},'Name':{'XYZ','ABC','PQR'},'Address':{'Pune','Baner','Mumbai'}}
#output=[{'ID': 1, 'Name': 'XYZ', 'Address': 'Mumbai'}, {'ID': 2, 'Name': 'PQR', 'Address': 'Baner'}, {'ID': 3, 'Name': 'ABC', 'Address': 'Pune'}]


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
