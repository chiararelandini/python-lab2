"""
Given a “2D dictionary” of tasks, like this one (i.e., tasks):
task1 = {‘toodo’: ‘call John for AmI project organization’, ‘urgent’: True}
task2 = {‘toodo’: ‘buy a new mouse’, ‘urgent’: True}
task3 = {‘toodo’: ‘find a present for Angelina’s birthday’, ‘urgent’: False}
task4 = {‘toodo’: ‘organize mega party (last week of April)’, ‘urgent’: False}
task5 = {‘toodo’: ‘book summer holidays’, ‘urgent’: False}
task6 = {‘toodo’: ‘whatsapp Mary for a coffee’, ‘urgent’: False}
return a new dictionary, using the same “2D” format, that contains only the urgent tasks, i.e.,
take the dictionaries that have a True value in the urgent field and combine them in a single
new dictionary as shown in the example.
"""


tasks = {'task1': {'todo': 'call John for AmI project organization', 'urgent': True},
    'task2' : {'todo': 'buy a new mouse', 'urgent': True},
    'task3' : {'todo': 'find a present for Angelina’s birthday', 'urgent': False},
    'task4' : {'todo': 'organize mega party (last week of April)', 'urgent': False},
    'task5' : {'todo': 'book summer holidays', 'urgent': False},
    'task6' : {'todo': 'whatsapp Mary for a coffee', 'urgent': False}}

urgent_tasks = {}

for key in tasks.keys():
    if tasks[key]["urgent"] == True:
        urgent_tasks[key] = tasks[key]['todo']

print(urgent_tasks)