#Two merge two dictionary
d={'prgm':'python','coding':'java'}
d1={'fruit':'apple','vegetable':'carrot'}
d2=d.copy()
d2.update(d1)
print(d2)
print('\n')

#remove a specify key
d={'Chennai':'Csk','Mumbai':'MI','Dehli':'DC','Punjab':'KXIP'}
print(d)
del(d['Mumbai'])
print(d)
print('\n')

#to map two list into dictionary
lst=["Kerala","Karnataka","Bihar","Tamil Nadu"]
lst1=["Kochi","Bangalore","Patna","Chennai"]
print("original key list:",lst)
print("Original Value list:",lst1)
d={}
for key in lst:
    for v in lst1:
        d[key]=v
print(d)
print('\n')

#find the length of a set
st=set()
st.add(54)
st.add(87)
st.add(65)
st.add(98)
st.add(90)
st.add(3)
print("length of the set is",len(st))
print('\n')

#intersection of two set
set1={12,23,63,25,15}
set2={14,25,35,23,15}
print("Original set")
print(set1)
print(set2)
print("After the intersection")
print(set1-set2)

