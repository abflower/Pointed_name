def point(x):
    if len(x) < 1:
        point = x
    if len(x) == 1:
        point = str(x)+'.'
    if len(x) > 1:
        if '.' in x:
            point = x
        if '-' in x:
            names = x.split('-')
            name1 = names[0]
            name1 = name1[:1]
            name2 = names[1]
            name2 = name2[:1]
            point = name1+'.-'+name2+'.'
        else:
            name = x[:1]
            point = name+'.'
    return point
