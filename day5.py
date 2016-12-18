import hashlib

#hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()

INPUT = "ojvtpuvg"

index = 0
password = {}

for _ in range(8):
    while len(password) < 8:
        if index % 100000 == 0:
            print password, index

        s = INPUT + str(index)
        h = hashlib.md5(s).hexdigest()
        index += 1
        if h[:5] == "00000":
            print h
            try:
                pwd_index = int(h[5], 0)
            except:
                continue
            ch = h[6]
            print pwd_index, ch

            if pwd_index > 7:
                continue
            if pwd_index not in password:
                password[pwd_index] = ch


print [password[index] for index in range(8)]
