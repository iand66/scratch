l1 = [1,2,3,1,2,3]
l2 = list(set(l1))
print(l2)

employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Corey']
developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']
result = set(employees).difference(gym_members, developers)
print(result)