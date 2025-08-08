def calculate_sum(a, b):
    return a + b

def calculate_product(a, b):
    return a * b

def validate_input(value):
    return isinstance(value, (int, float))

# Additional functions added to further simulate outdated state
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def sort_numbers(numbers, reverse=False):
    return sorted(numbers, reverse=reverse)

def remove_duplicates(items):
    return list(set(items))

def count_occurrences(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts
