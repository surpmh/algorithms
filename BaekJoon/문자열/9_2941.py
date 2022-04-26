croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
num = 0

for i in range(len(croatia)):
    count = word.count(croatia[i])
    print(count)
    num += count 

print(len(word) - num)