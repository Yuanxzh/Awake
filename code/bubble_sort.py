def bubble_sort(numbers):
    result = list(numbers)

    for i in range(len(result) - 1):
        swapped = False

        for j in range(len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # 本轮没有交换，说明已经有序
        if not swapped:
            break

    return result


numbers = [5, 3, 8, 4, 2]
print("排序前：", numbers)
print("排序后：", bubble_sort(numbers))
