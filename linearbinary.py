def linear_search(account_ids, target):
    for account_id in account_ids:
        if account_id == target:
            return True
    return False

def binary_search(account_ids, target):
    low, high = 0, len(account_ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if account_ids[mid] == target:
            return True
        elif account_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

customer_ids = [105, 23, 890, 400, 56, 77, 12]
search_id = 56

# Linear search (works on unsorted list)
found_linear = linear_search(customer_ids, search_id)
print(f"Linear Search: Is account ID {search_id} present? {found_linear}")

# Binary search requires sorted list
sorted_customer_ids = sorted(customer_ids)
found_binary = binary_search(sorted_customer_ids, search_id)
print(f"Binary Search: Is account ID {search_id} present? {found_binary}")

