from typing import List


def update_state_map(line, left_j, right_j, states_map):
    if line not in states_map:
        states_map[line] = []
    states_map[line].append([left_j, right_j])
    print(f"New state i={line} {[left_j, right_j]}")


def process_line(land, i, j, states_map, result) -> int:
    if land[i][j] == 0:
        # continue iteration with state
        return j + 1

    left_i = i
    left_j = j

    right_i = i
    right_j = j

    while right_j < len(land[0]) - 1 and land[left_i][right_j + 1] != 0:
        right_j += 1

    while right_i < len(land):
        if land[right_i][right_j] == 0:
            break

        if right_i != i:
            update_state_map(right_i, left_j, right_j, states_map)
        right_i += 1

    # fix new area
    result.append([left_i, left_j, right_i - 1, right_j])
    print(f"New result {[left_i, left_j, right_i - 1, right_j]}")
    return right_j + 2


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        states_map = {}
        i = 0
        while i < len(land):
            j = 0

            if i not in states_map:
                states_map[i] = [[-1, 0]]
            else:
                states_map[i].sort(key=lambda x: x[0])

            cur_line_states = states_map[i]
            cur_line_state = cur_line_states.pop(0)

            while j < len(land[0]):
                if cur_line_state[0] == -1:
                    j = process_line(land, i, j, states_map, result)
                    continue

                if cur_line_state[0] - 1 > j:
                    j = process_line(land, i, j, states_map, result)
                    continue

                if cur_line_state[0] - 1 <= j:
                    j = cur_line_state[1] + 1

                if cur_line_state[1] <= j:
                    while len(cur_line_states) > 0:
                        cur_line_state = cur_line_states.pop(0)
                        if cur_line_state[1] > j:
                            break

            # remove current state
            del states_map[i]
            update_state_map(i + 1, 310, 310, states_map)
            i += 1
        return result


sol = Solution()
# land = [
#     [0, 0, 0, 1],
#     [0, 1, 0, 0],
#     [0, 0, 1, 1],
#     [1, 0, 1, 1],
# ]

# [[0, 3, 1, 6], [1, 0, 3, 1], [3, 4, 5, 6], [5, 0, 5, 1]]
# land = [
#     [0, 0, 0, 1, 1, 1, 1],
#     [1, 1, 0, 1, 1, 1, 1],
#     [1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 1, 1, 1],
#     [0, 0, 0, 0, 1, 1, 1],
#     [1, 1, 0, 0, 1, 1, 1],
# ]

# [[0, 4, 1, 4], [1, 0, 2, 0], [1, 2, 2, 2], [1, 6, 2, 6], [2, 2, 2, 2]]
land = [
    [0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1]
]

print(sol.findFarmland(land))
