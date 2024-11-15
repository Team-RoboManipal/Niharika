#1
n=int(input("Enter the number:"))
if(n%2==0):
    print("Even")
else:
    print("Odd")

#2
n=int(input("Enter the number:"))
sum=0
x=n
while(x!=0):
    rd=x%10
    sum+=rd
    x=x//10

print(sum)


#3
lst=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    e=int(input("Enter the element:"))
    lst.append(e)
print(lst)

lst.sort()
print(lst[-1])


#4
lst=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    ch=input("Enter the character:")
    lst.append(ch)
print(lst)
s='"'
for el in lst:
    s=s+el
s+='"'
print(s)

#5
n=int(input("Enter the number:"))
p=0
for i in range(2,n):
    if n%i==0:
        p+=1
        break
if p==0:
    print("Prime")
else:
    print("Not Prime")

#6
nlst=eval(input("Enter the list:"))
def flatten(nlst):
    fl = []  
    for i in nlst: 
        if isinstance(i, list):  
            fl += flatten(i)  
        else:
            fl.append(i)  
    return fl
res = flatten(nlst)
print(res)


#7
s1=set({})
s2=set({})
s=set({})

n1=int(input("Enter the number of elements for first list:"))
for i in range(n1):
    e1=int(input("Enter the element:"))
    s1.add(e1)

n2=int(input("Enter the number of elements for second list:"))
for i in range(n2):
    e2=int(input("Enter the element:"))
    s2.add(e2)

print("Set1:",s1)
print("Set2:",s2)

for i in s1:
    for j in s2:
        if i==j:
            s.add(i)
print(s)

#8
x1=input("Enter the first string:")
x2=input("Enter the second string:")
s1=x1.lower()
s2=x2.lower()

l=len(s1)
t=0
if len(s1)==len(s2):
    for i in s1:
        for j in s2:
            if i==j:
                t+=1
    if t==l:
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")



#9
lst1=[]
lst2=[]

n1=int(input("Enter the number of elements for first list:"))
for i in range(n1):
    e1=int(input("Enter the element:"))
    lst1.append(e1)

n2=int(input("Enter the number of elements for first list:"))
for i in range(n2):
    e2=int(input("Enter the element:"))
    lst2.append(e2)

print(lst1)
print(lst2)

lst3=[]

for el1 in lst1:
    for el2 in lst2:
        if el1==el2:
            lst3.append(el1)

print(lst3)


#10
lst1=[]
lst2=[]
lst=[]
n1=int(input("Enter the number of dictionaries:"))
n2=int(input("Enter the number of elements for dictionary:"))
for i in range(n1):
    dict = {}
    for j in range(n2):
        key = input("Enter the element for key: ")
        value = input("Enter the element for value: ")
        dict[key] = value  

    lst.append(dict) 
print(lst)

k=input("Key:")
sorted_data = sorted(lst, key=lambda x: x[k])
print(sorted_data)



#11
lst1=[]
lst2=[]
n1=int(input("Enter the number of elements for first list:"))
for i in range(n1):
    e1=input("Enter the element for key:")
    lst1.append(e1)
    e2=input("Enter the element for value:")
    lst2.append(e2)

print("Keys:",lst1)
print("Values:",lst2)

dict={}

for i in lst1:
    for j in lst2:
        dict[i]=j
print(dict)


#12
s=input("Enter the sentence:")
lst=[]
lst1=s.split()

for i in lst1:
    x=len(i)
    lst.append(x)
        
print(lst)

#13
def longest_increasing_subsequence(lst):

    n = len(lst)
    lis = [1] * n  
    
    for i in range(1, n):
        for j in range(i):
            if lst[i] > lst[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    return max(lis)


lst = eval(input("Enter the list:"))
result = longest_increasing_subsequence(lst)
print("Length of the longest increasing subsequence:", result)


#14
def create_node(data):
    return {'data': data, 'next': None}

def insert(node, data):
    new_node = create_node(data)
    new_node['next'] = node
    return new_node

def delete(node, value):
    if node is None:
        return None
    if node['data'] == value:
        return node['next']
    node['next'] = delete(node['next'], value)
    return node

def traverse(node):
    current = node
    while current:
        print(current['data'], end=' -> ')
        current = current['next']
    print("None")


head = None
head = insert(head, 30)
head = insert(head, 20)
head = insert(head, 10)

print("Linked List:")
traverse(head)


head = delete(head, 20)

print("\nAfter deleting 20:")
traverse(head)


#15
def create_stack():
    return []

def push(stack, item):
    stack.append(item)
    return stack

def pop(stack):
    if len(stack) < 1:
        return None
    return stack.pop()

def is_empty(stack):
    return len(stack) == 0

my_stack = create_stack()

my_stack = push(my_stack, 5)
my_stack = push(my_stack, 10)

popped_item = pop(my_stack)
print("Stack after operations:", my_stack)

print("Is stack empty?", is_empty(my_stack))


