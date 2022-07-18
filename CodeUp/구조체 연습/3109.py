# 정올 참여 학생 리스트 만들기 2
import sys
input = sys.stdin.readline

class Student:
    def __init__(self, num, name):
        self.num = num
        self.name = name
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num):
        self.__num = num
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

n=int(input())
arr=[]
nums=[]
for i in range(n):
    code, num, name = input().strip().split()
    if code == "I":
        if int(num) not in nums:
            nums.append(int(num))
            arr.append(Student(int(num),name))
        else:
            nums.append(int(num))
            arr.insert(0,Student(int(num),name))
    elif code == "D":
        if int(num) in nums:
            nums.remove(int(num))
            for j in range(len(arr)):
                if arr[j].num == int(num):
                    del arr[j]
                    break
        
value = input().strip().split()
arr.sort(key=lambda x:x.num)

for v in value:
    print(arr[int(v)-1].num, arr[int(v)-1].name)