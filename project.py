import pprint
import sys


def count_fixed_polyominoes(the_graph,untried,n, p, c=0):
    while not len(untried) == 0:
        u = untried.pop()
        p.append(u)
        if len(p) == n:
            c += 1
        else:
            neighboor = set()
            neig = the_graph.get(u)
            for the_u in neig:
                if the_u not in untried:
                    if the_u not in p:
                        p_without_u = p.copy()
                        p_without_u.remove(u)
                        the_u_values = the_graph.get(the_u)
                        a = list(set(the_u_values).intersection(p_without_u))
                        if len(a) == 0 :
                            neighboor.add(the_u)
            new_untried = untried.copy()
            if len(new_untried) == 0:
                new_untried = neighboor
            else:
                new_untried.update(neighboor)
            c = count_fixed_polyominoes(the_graph,new_untried, n , p, c)
        p.remove(u)
    return c


def main(my_input, out):
    my_graph = {
        (0, 0): [],
    }

    for j in  range(0,my_input-1):
        key_list = list(my_graph.keys())
        val_list = list(my_graph.values())
        for i in range(0, len(key_list)):
            x = key_list[i][0]
            y = key_list[i][1]
            if y>0 or (y == 0 and x>=0):
                if (x+1,y) not in my_graph:
                    my_graph.update({(x + 1, y): [(x, y)]})
                    my_graph[(x,y)].append((x+1 , y))
                elif (x,y) not in my_graph[(x+1,y)]:
                    my_graph[(x,y)].append((x+1 , y))
                    my_graph[(x + 1, y)].append((x, y))
                if (x, y + 1) not in my_graph:
                    my_graph.update({(x, y + 1): [(x, y)]})
                    my_graph[(x, y)].append((x, y+1))
                if y>=1:
                    if (x-1,y) not in my_graph:
                        my_graph.update({(x - 1, y): [(x, y)]})
                        my_graph[(x, y)].append((x - 1, y))
                        if ((x-1,y) in my_graph) and ((x-1,y-1) in my_graph):
                            my_graph[(x - 1,y)].append((x-1,y-1))
                            my_graph[(x - 1, y - 1)].append((x - 1,y))
    if out:
        pprint.pprint(my_graph)

    p = []
    a = count_fixed_polyominoes(my_graph, {(0,0)}, my_input, p)
    print(a)


if len(sys.argv) == 1 or len(sys.argv) > 3:
    print("The arguments are not correct")
else:
    if len(sys.argv) == 2:
        the_input = sys.argv[1]
        out_graph = False
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-p":
            the_input = sys.argv[2]
            out_graph = True
            print(the_input)
        else:
            print("error: something happened")
    main(int(the_input), out_graph)
