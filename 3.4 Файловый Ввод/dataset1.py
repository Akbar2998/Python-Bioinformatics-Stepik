with open('dxc.txt',"r") as inf:
    result = ""
    count = 0
    s = inf.readline()
    harflar = []
    sonlar = []
    xc = ""
    son = ""
    for x in s:
        if x.isalpha():
            count += 1
            harflar.append(x)
            xc += x
            if count > 1:
                sonlar.append(int(son))
                xc += son
            son = ""
        
        else:
            son += x
    sonlar.append(int(s[len(xc)::]))
    for i in range(len(sonlar)):
        print(harflar[i]*sonlar[i],end="")
