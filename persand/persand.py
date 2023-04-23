from time import sleep as sp; SPEED=1
def run(file):
    has_future = [[1]]
    with open(file, 'r+') as f:
        lines = f.readlines()
        lines = [i[:-1]+' '*(max([len(i) for i in lines])-len(i)) for i in lines]
        f.seek(0)
        f.write('\n'.join(lines))
    while sum([sum(i) for i in has_future])>0:
        with open(file, 'r+') as f:
            lines = [i[:-1] for i in f.readlines()]
            has_future = [[0 for i in range(len(lines[y]))] for y in range(len(lines))]
            for y in range(len(lines)):
                for x in range(len(lines[y])):
                    c = lines[y][x]
                    if y+1<len(lines) and x<len(lines[y+1]):
                        c_below = lines[y+1][x]
                    else:
                        c_below = ''
                    if x-1>=0 and y+1<len(lines):
                        c_below_left = lines[y+1][x-1]
                    else:
                        c_below_left = ''
                    if y+1<len(lines) and x+1<len(lines[y+1]):
                        c_below_right = lines[y+1][x+1]
                    else:
                        c_below_right = ''
                    has_future[y][x] = int((c_below.isspace() or c_below_left.isspace() or c_below_right.isspace()) and not c.isspace())
                    if not c.isspace() and has_future[y][x]:
                        if c_below.isspace() and not c_below=='':
                            lines[y+1] = lines[y+1][:x]+c+lines[y+1][x+1:]
                            lines[y] = lines[y][:x]+' '+lines[y][x+1:]
                        elif c_below_left.isspace() and not c_below_left=='':
                            lines[y+1] = lines[y+1][:x-1]+c+lines[y+1][x:]
                            lines[y] = lines[y][:x]+' '+lines[y][x+1:]
                        elif c_below_right.isspace() and not c_below_right=='':
                            lines[y+1] = lines[y+1][:x+1]+c+lines[y+1][x+2:]
                            lines[y] = lines[y][:x]+' '+lines[y][x+1:]   
                    f.seek(0)
                    f.write('\n'.join(lines))
        sp(0.1/SPEED)
