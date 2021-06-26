school_class = "9 Иванов\n\
10 Петров\n\
11 Сидоров\n\
9 Григорьев\n\
9 Сергеев\n\
10 Яковлев".split("\n")

for line in school_class:
    school_class[school_class.index(line)]= line.split()

school_class = sorted(school_class, key=lambda x: int(x[0]))

for elem in school_class:
    print(elem[0], elem[1])