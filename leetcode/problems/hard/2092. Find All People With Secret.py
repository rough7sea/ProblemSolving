from typing import List, Any


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> set[int | Any]:
        secret_keepers = {0, firstPerson}

        if len(secret_keepers) == n:
            return secret_keepers

        sorted_meetings = sorted(meetings, key=lambda meeting: meeting[2])
        print(sorted_meetings)

        graph = Graph()
        to_flash = False
        prev_time = sorted_meetings[0][2]

        for meeting in sorted_meetings:
            x = meeting[0]
            y = meeting[1]
            time = meeting[2]

            # if x == 4608 or y == 4608:
            #     print("here")

            if prev_time < time:
                if to_flash:
                    # parse and save calculate result
                    calculate = graph.calculate(secret_keepers)
                    secret_keepers.update(calculate)
                    # print(f"Time = {prev_time}. Calculation = {calculate}")

                # clear graph
                graph.clear()
                to_flash = False

            if to_flash or y in secret_keepers or x in secret_keepers:
                to_flash = True

            # add node
            graph.add_node(x, y)
            graph.add_node(y, x)
            prev_time = time

        if to_flash:
            # parse and save calculate result
            secret_keepers.update(graph.calculate(secret_keepers))

        return secret_keepers


class Graph:
    def __init__(self):
        self.graph = dict()

    def clear(self):
        self.graph = dict()

    def add_node(self, left, right):
        if left not in self.graph:
            self.graph[left] = set()
        nodes = self.graph[left]
        nodes.add(right)

    def calculate(self, keepers: set):
        result = set()
        keys = list(self.graph.keys())

        while len(keys) > 0:
            flash = False
            queue = {keys[0]}
            match_buffer = set()

            while len(queue) > 0:
                key = queue.pop()
                nodes = self.graph[key]
                if nodes is None:
                    # already been here
                    continue

                # remove for duplication
                keys.remove(key)
                self.graph[key] = None

                queue.update(nodes)
                match_buffer.add(key)

                if flash is False:
                    if key in keepers:
                        flash = True

            if flash:
                result.update(match_buffer)

        return result


sol = Solution()

with open('../test/2092.find_all_people-with-secret_test_data') as f:
    lines = f.readlines()
    line: str = lines[0][2:-2]
    split_list = line.split(sep='],[')
    meetings = []
    for row in split_list:
        m_str = row.split(',')
        meeting_int = [int(m_str[0]), int(m_str[1]), int(m_str[2])]
        meetings.append(meeting_int)

# print('\n\n')
print(sol.findAllPeople(n=7336, meetings=meetings, firstPerson=6384))
# print(sol.findAllPeople(n=6, meetings=[[1, 2, 5], [0, 3, 5], [2, 3, 8], [0, 4, 8], [1, 5, 10]], firstPerson=1))
# print(sol.findAllPeople(n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3))
# print(sol.findAllPeople(n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1))
# print(sol.findAllPeople(n=6, meetings=[[0, 2, 1], [1, 3, 1], [4, 5, 1]], firstPerson=1))

