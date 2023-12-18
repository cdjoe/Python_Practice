def solution(inputString):
    if len(inputString) <= 50 and len(inputString) >= 3:
        s = ord('a')
        e = ord('z')
        for i in range(s,e):
            balance = 0
            for x in inputString:
                if i == ord(x):
                    balance += 1
                if i+1 == ord(x):
                    balance -= 1
            if balance < 0:
                return False
        return True

# test
print(solution('zyy'))