def check_path(path):
    if len(path) == 1:
        return True
    else:
        for i in range(len(path) - 1, -1, -1):
            if i == 0:
                break
            parent = path[i].get_parent()
            if parent != path[i - 1]:
                return False
            
        return True
    
    # return true/false depending on whether the path is valid or not.