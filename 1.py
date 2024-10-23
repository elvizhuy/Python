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

flight_dict = {}
for flight in data['flights']:
    flight_dict[(flight['year'], flight['month'].lower())] = flight['passengers']

test_cases = int(input())

for _ in range(test_cases):
    year, month = input().split()
    key = (year, month.lower())
    if key in flight_dict:
        print(flight_dict[key])
    else:
        print("Invalid")
