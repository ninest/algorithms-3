def binary_search(sorted_list: 'list[int]', item: int) -> 'int | None':
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = left + (right - left) // 2
        current = sorted_list[mid]

        if current == item:
            return mid
        elif item < current:
            right = mid - 1
        else:
            left = mid + 1

    return None

if __name__ == '__main__':
    print(binary_search([0, 5, 7, 10, 15], 0))
    print(binary_search([0, 5, 7, 10, 15], 15))
    print(binary_search([0, 5, 7, 10, 15], 5))
    print(binary_search([0, 5, 7, 10, 15], 6))
