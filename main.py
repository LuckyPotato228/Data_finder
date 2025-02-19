import re
file = open("data.txt", "r", encoding="utf-8").read()
pattern = '.+@.+\..+'
file = re.findall(pattern,file)
print(file)