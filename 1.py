import json

# Sample data (this should be read from a JSON file in a real scenario)
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

# Input handling
test_cases = int(input())  # Number of test cases

for _ in range(test_cases):
    year, month = input().split()  # Expecting year and month
    found = False
    for flight in data['flights']:
        if flight['year'] == year and flight['month'].lower() == month.lower():
            print(flight['passengers'])
            found = True
            break
    if not found:
        print("Invalid")
