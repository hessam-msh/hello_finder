def check_string(text, to_find):
    c = 0
    for i in text:
        if i == to_find[c]:
            c += 1
        if c == len(to_find):
            return "YES"
    return "NO"


text = input()
to_find = "hello"

print(check_string(text, to_find))
