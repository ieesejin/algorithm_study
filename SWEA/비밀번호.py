# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8


for test_case in range(10):
    length, password = input().split()
    length = int(length)
    password = list(password)

    idx = 0
    while idx < length-1:
        if password[idx] == password[idx+1]:
            if idx == 0:
                password = password[idx+2:]
            else:
                password = password[:idx] + password[idx+2:]
                idx -= 1
        else:
            idx += 1

    print("#{} {}".format(test_case+1, int(''.join(password))))
