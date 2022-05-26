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

"""
Second code 
"""

# text = input().lower()
# h = text.find('h')
# res = False
# if h != -1:
#     e = text.find('e', h + 1)
#     if e != -1:
#         l1 = text.find('l', e + 1)
#         if l1 != -1:
#             l2 = text.find('l', l1 + 1)
#             if l2 != -1:
#                 o = text.find('o', l2 + 1)
#                 if o != -1:
#                     res = True
# print('YES' if res is True else 'NO')
