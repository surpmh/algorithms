# 분해합
def constructor(n):
    sum = n
    n = str(n)
    
    for i in range(len(n)):
        sum += int(n[i])
    if sum == num:
        return True

def main():
    global num 
    num = int(input())
    for i in range(num+1):
        if constructor(i) == True:
            print(i)
            break
        if i == num:
            print(0)

if __name__ == "__main__":
    main()