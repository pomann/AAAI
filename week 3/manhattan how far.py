def h(start, goal):
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    
    # 2x 2D lists
    start = [[i for i in start[0:3]],[i for i in start[3:6]],[i for i in start[6:9]]]
    goal = [[i for i in goal[0:3]],[i for i in goal[3:6]],[i for i in goal[6:9]]]
    
    # Work out the manhattah distance of each tile from its eventual goal

    def findNew(x,y,item):
        for i,v in enumerate(goal):
            for i2,v2 in enumerate(v):
                if v2 == item:
                    return abs(x - i) + abs(y - i2)


    dis = 0

    for i,v in enumerate(start):
        for i2,v2 in enumerate(v):
            if v2 != ' ':
                dis += findNew(i,i2,v2)
    
    return dis