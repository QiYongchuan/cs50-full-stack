#create an empty set

s = set()


# add elements

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(4)


s.remove(1)
print(s)

length = len(s)

print(f"s的长度是{length},也就是{len(s)}")