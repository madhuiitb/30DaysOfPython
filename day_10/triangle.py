print("--------------------------------------------------")

for i in range(1,8):
    temp = ""
    for j in range(i):
        temp = str(temp + '#')
    print(temp)
print("--------------------------------------------------")

for i in range(1,8):
    temp = ""
    for j in range(8):
        temp = str(temp + '#')
    print(temp)
print("--------------------------------------------------")

for i in range(11):
    print('{}x{}={}'.format(i,i,i*i))
print("--------------------------------------------------")

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in range(len(lst)):
    print(lst[i])

print("--------------------------------------------------")
for i in range(1,101):
    if i%2==0:
        print(i)

print("--------------------------------------------------")

for i in range(1,100):
    if i%2==1:
        print(i)

print("--------------------------------------------------")
sum = 0
for i in range(101):
    sum = sum + i
print(sum)

print("--------------------------------------------------")
even_sum = 0
odd_sum = 0
for i in range(101):
    if i%2==0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print(even_sum, odd_sum)