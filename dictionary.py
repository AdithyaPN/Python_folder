# student = ['Anu', 24, 'Vadakara', 4321567432, 'python', 3, 200]
student = {
    'name': 'Adithya',
    'age': '24',
    'address': 'Vadakara',
    'phone': 4356763221,
    'course': 'python',
    'duration': 3,
    'total mark': 200,
    # 'total mark': 300 # in case of 2 keys, it takes last key
}
print(student['name'])
print(student['age'])
print(student['total mark'])

students = [
    {
    'name': 'Adithya',
    'age': '24',
    'address': 'Vadakara',
    'phone': 4356763221,
    'course': 'python',
    'duration': 3,
    'total mark': 200
    },
    {
    'name': 'Anu',
    'age': '24',
    'address': 'Perambra',
    'phone': 9876543221,
    'course': 'java',
    'duration': 3,
    'total mark': 200
    }
]
print(students[1])
print(students[1]['phone'])
students[1]['duration'] = 6 #changing the duration of Anu
print(students[1]['duration'])