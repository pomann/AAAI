nodes = []

def minimax(tree):
    global nodes
    l = minimax_rec(tree.root)
    i = len(nodes)
    k = 1
    while i != 1:
        i = i / 3
        k += 1
        
    while k != 0:
        if k % 2 != 0:
            nodes = [max(x) for x in nodes]
        else:
            nodes = [min(x) for x in nodes]
        k -= 1
        if k != 0:
            nodes = [[x[1] for x in enumerate(nodes) if x[0] < i*3 and x[0] >= (3 * (i - 1))] for i in range(1,int(len(nodes)/3) + 1)]
    return nodes[0]
    
def minimax_rec(curr):
    global nodes
    if curr.mid.is_terminal():
        nodes.append([curr.left.val,curr.mid.val,curr.right.val])
        return
    else:
        if curr.val == -1:
            return minimax_rec(curr.left),minimax_rec(curr.mid),minimax_rec(curr.right)
        else:
            return curr.val, minimax_rec(curr.left),minimax_rec(curr.mid),minimax_rec(curr.right)
            
