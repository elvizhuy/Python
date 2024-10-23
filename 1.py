import json

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

test_cases = int(input())

for _ in range(test_cases):
    year, month = input().split()
    found = False
    for flight in data['flights']:
        if flight['year'] == year and flight['month'].lower() == month.lower():
            print(flight['passengers'])
            found = True
            break
    if not found:
        print("Invalid")
