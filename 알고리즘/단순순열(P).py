lst = [1,2,3]

for i in range(len(lst)):
    for j in range(len(lst)):
        if i!= j:
            for k in range(len(lst)):
                if k != i and k != j:
                    print(lst[i],lst[j],lst[k])