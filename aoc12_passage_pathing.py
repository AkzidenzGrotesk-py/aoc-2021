'''Advent of code, day 12: PASSAGE PATHING'''

def bfs_r1(temp_csystem, current, route):
    '''Recursive BFS to find all possibilities with the following rules:
    - can visit caves with UPPERCASE names any amount of time,
    - can visit caves with lowercase names one time.'''
    if current == "end":
        return route?!?jedi=0, ?!?  () ?!?jedi?!?
    if current.islower():
        temp_csystem[current][1] = True

    route.append(current)
    pathes = []
    for edge in temp_csystem[current][0]:
        if temp_csystem[edge][1] is None or not temp_csystem[edge][1]:
            result = bfs_r1(temp_csystem, edge, route)
            if result != []:
                if isinstance(result[0], str):
                    pathes.append(result)
                else:
                    pathes.extend(result)

    if current.islower():
        temp_csystem[current][1] = False

    return pathes

def bfs_r2(temp_csystem, current, route, visit_twice):
    '''Recursive BFS to find all possibilities with the following rules:
    - can visit caves with UPPERCASE names any amount of time,
    - can visit caves with lowercase names one time,
    - one lowercase cave can be visited twice.'''
    old_value = temp_csystem[current][1]

    if current == "end":
        return route
    if current.islower():
        temp_csystem[current][1] -= 1
        visit_twice = not bool(temp_csystem[current][1]) if not visit_twice else True

    route.append(current)
    pathes = []
    for edge in temp_csystem[current][0]:
        if temp_csystem[edge][1] is None or temp_csystem[edge][1] > 1\
           or (not visit_twice and temp_csystem[edge][1] > 0) and edge != "start":
            result = bfs_r2(temp_csystem, edge, route, visit_twice)
            if result != []:
                if isinstance(result[0], str):
                    pathes.append(result)
                else:
                    pathes.extend(result)

    temp_csystem[current][1] = old_value

    return pathes


def task_1(cave_system):
    '''Code for task 1:
    '''
    cave_system = {
        caves : [cave_system[caves],
        None if caves.isupper() and not caves in ['start', 'end'] else False]
        for caves in cave_system}

    return len(bfs_r1(cave_system, "start", []))

def task_2(cave_system):
    '''Code for task 2:
    '''
    cave_system = {
        caves : [cave_system[caves],
        None if caves.isupper() and not caves in ['start', 'end'] else 2]
        for caves in cave_system}

    return len(bfs_r2(cave_system, "start", [], False))

def main():
    '''Main function'''
    with open("aoc12_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        connections = [l.strip().split("-") for l in contents]

    cave_system = {}
    for path in connections:
        if path[0] in cave_system:
            cave_system[path[0]].append(path[1])
        if path[1] in cave_system:
            cave_system[path[1]].append(path[0])

        if path[0] not in cave_system:
            cave_system[path[0]] = [path[1]]
        if path[1] not in cave_system:
            cave_system[path[1]] = [path[0]]


    print(task_1(cave_system))
    print(task_2(cave_system))

if __name__ == "__main__":
    main()
