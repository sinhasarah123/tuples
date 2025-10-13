student_data=[
    {'id': 1, 'name': 'sarah', 'age': 11, 'subjects': ['math','science','english']},
    {'id': 2, 'name': 'john', 'age': 12, 'subjects': ['history','math','art']},
    {'id': 3, 'name': 'emily', 'age': 11, 'subjects': ['math','science','english']}
]
student_data.append({'id': 4, 'name': 'mike', 'age': 13, 'subjects': ['history','math','art']})
result={}
for key, value in student_data[0].items():
    result[key] = [student[key] for student in student_data]