# New module added to simulate outdated state
def process_data(data):
    return [item * 2 for item in data]

def validate_input(value):
    return isinstance(value, (int, float))

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def format_output(data, format_type="json"):
    if format_type == "json":
        return str(data)
    elif format_type == "csv":
        return ",".join(str(item) for item in data)
    else:
        return str(data)
