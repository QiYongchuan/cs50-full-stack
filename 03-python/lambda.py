people = [
  {"name":"harry","house":"Gry"},
  {"name":"cho","house":"Rav"},
  {"name":"Dro","house":"Sly"}
]


# def f(person):
#   return person['house']

# people.sort(key=f)


# 或者用lambda表达式

people.sort(key=lambda person:person['name'])

print(people)