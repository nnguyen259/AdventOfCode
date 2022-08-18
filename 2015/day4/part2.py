import hashlib

data = "bgvyzdsv"

i = 1
while True:
    key = f"{data}{i}"
    result = hashlib.md5(key.encode()).hexdigest()
    if result.startswith("000000"):
        print(i, result)
        break
    i += 1
