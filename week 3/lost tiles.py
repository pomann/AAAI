def h(start, goal):
    # ensure that start and goal are valid positions
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    start = [start[0:3],start[3:6],start[6:]]
    goal = [goal[0:3],goal[3:6],goal[6:]]
    out = 0
    for v,i in enumerate(start):
        for g,l in enumerate(i):
            if l != goal[v][g] and l != ' ':
                out += 1
    return out
    # Work out how many tiles are out of place
    
    