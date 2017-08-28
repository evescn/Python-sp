lock = "lock.txt"
logfile = "login.txt"
lock_info = 0
i = 0

while i < 3 and lock_info== 0:
    name = input("Please input your name: ")
    password = input("Please input password: ")

    f = open(lock, "r")
    if name in f:
        lock_info = 1
        # print("This %s is locked" % username)
        f.close()
        break
    else:
        f = open(logfile, "r")
        for line in f.readlines():
            # print(line)
            user_file, pass_file = line.split()
            # print(user_file)
            # print(pass_file)
            if user_file == name and pass_file == password:
                print("Bingo!")
                break
        else:
            print("You name or password is errer!")
        f.close()
    i += 1
else:
    if i == 3 or lock_info == 1:
        f = open(lock, "a")
        f.write(name + "\n")
        f.close()
    print("This %s is locked" % name)
