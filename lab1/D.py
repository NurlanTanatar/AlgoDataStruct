school_class = str(input()).split("\n")

for line in school_class:
    school_class[school_class.index(line)]= line.split()

school_class = sorted(school_class, key=lambda x: int(x[0]))

for elem in school_class:
    print(elem[0], elem[1])