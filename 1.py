import json

# Load JSON data
flights_data = '''
{
    "flights": [
        {"year": "1949", "month": "January", "passengers": "112"},
        {"year": "1949", "month": "February", "passengers": "118"},
        {"year": "1949", "month": "March", "passengers": "132"}
    ]
}
'''
data = json.loads(flights_data)

# Input reading and processing
test_cases = int(input())  # Number of test cases

for _ in range(test_cases):
    year, month = input().split()
    found = False
    for flight in data['flights']:
        if flight['year'] == year and flight['month'] == month:
            print(flight['passengers'])
            found = True
            break
    if not found:
        print("Invalid")
