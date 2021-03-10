
def build_order1(project_list, dependency_tuples):
    adj_map = create_adj_map1(project_list, dependency_tuples)
    build_list = []
    while len(build_list) < len(project_list):
        found = False  # found project with no incoming edges
        new_build_projects = set()
        for k,v in adj_map.items():
            if len(v) == 0:
                found = True
                new_build_projects.add(k)
                build_list.append(k)

        if not found:
            return -1  # we have detected a cycle

        for project in new_build_projects:
            adj_map.pop(project, None)

        for k,v in adj_map.items():
            matched_projects = new_build_projects.intersection(v)
            if matched_projects:
                for item in matched_projects:
                    v.remove(item)

    return build_list


def create_adj_map1(project_list, dependencies):
    adj_map = {}
    for p in project_list:
        adj_map[p] = set()
    for d in dependencies:
            adj_map[d[0]].add(d[1])   # values are dependencies for the key
    return adj_map


def create_children_map(project_list, dependency_list):
    adj_map = {}
    for p in project_list:
        adj_map[p] = [set(), 0]  # set of children, number of dependencies

    for d in dependency_list:
        adj_map[d[1]][0].add(d[0])  # update children for a dependency
        adj_map[d[0]][1] += 1       # update consumer with number of its dependencies

    return adj_map


def find_buildable_projects(build_list, dep_map, offset,project_list=None):
    if project_list:
        for p in project_list:
            if dep_map[p][1] == 0:
                build_list[offset] = c
                offset += 1
        return offset
    else:
        pass
        # UNCOMMENT WHEN we don't consider current_children (@param: project_list)
        # for k, v in dep_map.items():
        #     if v[1] == 0:
        #         build_list[offset] = k
        #         offset += 1

                # v[1] = -1  # so that it doesn't come in the build_list again
    return offset


def build_project(project, dep_map):
    for child in dep_map[project][0]:
        dep_map[child][1] -= 1


def build_order2(project_list, dependency_list):
    dep_map = create_children_map(project_list,
                                  dependency_list)  # {project: [set(children/consumers), #num_dependencies]}

    build_list = [ -1 for _ in range(len(project_list))]

    end_of_list = find_buildable_projects(build_list, dep_map, 0, project_list)
    processed = 0
    while processed < len(project_list):

        if build_list[processed] == -1:
            return -1  # we have a cycle

        build_project(build_list[processed], dep_map)
        current_children = dep_map[build_list[processed]][0]
        print('current node: {}'.format(build_list[processed]))
        print('current children: {}'.format(current_children))
        processed += 1
        # Next Buildable projects can only be among current children as their dependencies got built
        end_of_list = find_buildable_projects(build_list, dep_map, end_of_list, current_children)

    return build_list


def run():
    p = [1,2,3,4,5]
    dep = [(5,1),(2,1),(3,2),(4,3)]  # 1 is dependency of 5
    print(build_order2(p, dep))


if __name__ == '__main__':
    run()
