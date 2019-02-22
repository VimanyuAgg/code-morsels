def pond_sizes(earth):
    if earth is None or len(earth) == 0:
        return 0

    rows = len(earth)
    cols = len(earth[0])
    visited = [[False for _ in range(cols)] for __ in range(rows)]
    res = []
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                if earth[r][c] == 0:
                    size = pond_helper(earth, visited, r,c,rows,cols, 0)
                    res.append(size)

                else:
                    visited[r][c] = True

    return res


def pond_helper(earth, visited,r,c,rows,cols,size):
    visited[r][c] = True
    size += 1
    print(f"***pond_helper called for r:{r}, c:{c}, current_size:{size}***")
    print(f"visited_map:{visited}")
    r_vector = [-1,-1,-1,0,0,1,1,1]
    c_vector = [-1,0,1,-1,1,-1,0,1]

    for i in range(len(r_vector)):
        print(f"checking for r_vector[i]:{r_vector[i]}, c_vector[i]:{c_vector[i]}, overall_r:{r+ r_vector[i]}, overall_c:{c+c_vector[i]}")
        if is_valid(r+r_vector[i],c+c_vector[i],rows,cols):
            print(f"visited[r+r_vector[i]][c+c_vector[i]]:{visited[r+r_vector[i]][c+c_vector[i]]}")
            print(f"earth[r+r_vector[i]][c+c_vector[i]]:{earth[r+r_vector[i]][c+c_vector[i]]}")
            if earth[r+r_vector[i]][c+c_vector[i]] == 0 and (not visited[r+r_vector[i]][c+c_vector[i]]):
                print("calling new pond_helper")
                size = pond_helper(earth,visited,r+r_vector[i],c+c_vector[i],rows, cols, size)
                print(f"size found after recursive call: {size} - overall_r:{r+ r_vector[i]}, overall_c:{c+c_vector[i]}")
                print("visited_map")
                print(visited)

            visited[r+r_vector[i]][c+c_vector[i]] = True


    return size

def is_valid(i,j,rows,cols):
    res = (0<=i<rows) and (0<=j<cols)
    print(f"is_valid for r:{i},c:{j} - res:{res}")
    return res



