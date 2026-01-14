employees = input().split()
happiness_factor = int(input())

happiness_of_employees = [int(employee) * happiness_factor for employee in employees]

average_happiness = sum(happiness_of_employees) /len(happiness_of_employees)

happy_count = len([employee for employee in happiness_of_employees if employee >= average_happiness])

total_count = len(happiness_of_employees)

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
