#!/usr/bin/python
	
emplyeeList = [ {'id': "001", 'name':"Mary", 'payRate':15, 'workHour': 40},
{'id': "002", 'name':"John", 'payRate':22, 'workHour': 25},
{'id': "003", 'name':"Bob", 'payRate':35, 'workHour': 4},
{'id': "004", 'name':"Mel", 'payRate':43, 'workHour': 62},
{'id': "005", 'name':"Jen", 'payRate':17, 'workHour': 33},
{'id': "006", 'name':"Sue", 'payRate':29, 'workHour': 45},
{'id': "007", 'name':"Ken", 'payRate':40, 'workHour': 36},
{'id': "008", 'name':"Dave", 'payRate':20, 'workHour': 17},
{'id': "009", 'name':"Beth", 'payRate':37, 'workHour': 37},
{'id': "010", 'name':"Ray", 'payRate':16.5, 'workHour': 80}
]

for employee in emplyeeList:
	if employee['workHour'] <= 40:
		salary = employee['payRate'] * employee['workHour']
	else:
		salary = employee['payRate'] * 40 + (1.5*employee['payRate'])*(employee['workHour'] - 40)
	
	print ("Name: ", employee['name'], " salary: ", salary)
		

	
	
	

