

def pickingNumbers_continuous(arr):
    res = 1
    max_res = 0

    min_index = 0
    max_index = 0

    for i in range(len(arr) - 1):
        n = i + 1
        cur = arr[n]
        prev = arr[n - 1]

        min_val = min(arr[min_index], prev)
        if prev == min_val:
            min_index = n - 1

        max_val = max(arr[max_index], prev)
        if prev == max_val:
            max_index = n - 1

        if abs(cur - min_val) <= 1 and abs(cur - max_val) <= 1:
            res += 1
            continue
        elif abs(cur - min_val) > 1:
            max_res = max(max_res, res)
            res = n - min_index
        elif abs(cur - max_val) > 1:
            max_res = max(max_res, res)
            res = n - max_index

    return max(max_res, res)


# a = [1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 1, 2]
a = [1, 2, 2, 3, 1, 2, 1, 1, 3, 3, 3, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9]

# print(pickingNumbers_continuous(a))


def pickingNumbers(arr):
    dict = {}
    max_res = 0
    for cur in arr:
        cur_count = dict.get(cur)

        if cur_count:
            cur_count += 1
        else:
            cur_count = 1

        dict[cur] = cur_count

        prev_count = dict.get(cur - 1)
        next_count = dict.get(cur + 1)

        if prev_count:
            max_res = max(max_res, prev_count + cur_count)

        if next_count:
            max_res = max(max_res, next_count + cur_count)

        max_res = max(max_res, cur_count)

    return max_res


print(pickingNumbers(a))