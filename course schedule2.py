from collections import defaultdict, deque
def generateSchedule(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for prerequisite in prerequisites:
        course, prereq = prerequisite
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque()
    schedule = []

    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)

    while queue:
        course = queue.popleft()
        schedule.append(course)

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(schedule) == numCourses:
        return schedule     
    else:
        None

numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]

schedule = generateSchedule(numCourses, prerequisites)

if schedule:
    print("Valid course schedule:", schedule)
else:
    print("No valid course schedule possible.")
