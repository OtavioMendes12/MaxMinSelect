def max_min_select(arr, left, right):

    if left == right:
        return arr[left], arr[left]


    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]


    mid = (left + right) // 2


    min1, max1 = max_min_select(arr, left, mid)
    min2, max2 = max_min_select(arr, mid + 1, right)

    # Combina os resultados
    return min(min1, min2), max(max1, max2)


if __name__ == "__main__":
    arr = [3, 5, 1, 8, 2, 9, 4, 7, 6]
    min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
    print(f"Menor elemento: {min_val}, Maior elemento: {max_val}")