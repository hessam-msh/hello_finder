# This function find to_find in a arbitrary string(text)
def check_string(text, to_find):
    c = 0
    for i in text:
        if i == to_find[c]:
            c += 1
        if c == len(to_find):
            return "YES"
    return "NO"


text = input().lower()  # to become case-insensitive
to_find = "hello"  # u can change this word to whatever u want!

print(check_string(text, to_find))
