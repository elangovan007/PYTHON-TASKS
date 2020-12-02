#create a list and do folowing operation
lst=[25,63,95,36,49]
print("Original list:")
print(lst)
n=int(input("Enter the number to add in the list:"))
lst.append(n)
print("After add a new element",lst)
lst.pop()
print("After delete a element",lst)
print("Largest Element in the list is",max(lst))
print("Smallest element in the list is",min(lst))
print('\n')

#reverse the tuple
tpl=('abc',234,12.34,'python')
tpl1=()
print("Original tuples:")
print(tpl)
for i in reversed(tpl):
    tpl1= tpl1 +(i,)
    print("Reversed tuple:")
print(tpl1)
print('\n')


#convert the tuple to list
print("Tuple:",tpl)
l=list(tpl)
print("list\n",l)
