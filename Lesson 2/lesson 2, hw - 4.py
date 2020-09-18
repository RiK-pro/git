string = input("введите строку ")
word = string.split()
for ind, el in enumerate(word, 1):
    print(ind, el[0:10])
