analyst = 'Anatoly'

years = 2

has_job = False



analyst_2 = 'Olga'

years_2 = 3

has_job_2 = True



analysts = ['Anatoly', 'Olga', 'Beslan']

years = [2, 3, 4]

analysts.append('Michael')

analysts.pop(3)

analysts





has_job = False

if has_job:
    happy_message = 'Anatoly is happy!'
    print(happy_message)
else:
    sad_message = 'Anatoly is sad!'
    print(sad_message)

if has_job:
    message = 'Anatoly is happy!'
    print(message)





job_years = 0.5

salary = 200000

message = 'Addition is equal {coef}. New salary is {new_salary}!'

if job_years < 1:
    coefficient = 0
elif job_years >= 1 and job_years <=2:
    coefficient = 0.2
else:
    coefficient = 0.4

new_salary = salary + salary * coefficient

print(message.format(coef=coefficient, new_salary=new_salary))





analysts = ['Anatoly', 'Olga', 'Beslan']

for i in analysts:
    if i == 'Anatoly':
        print('Analyst name is {}!'.format(i))





analysts_data = {'Anatoly': [2, 100000], 'Olga': [3, 200000], 'Beslan': [4, 300000]}



analysts_data['Michael'] = 10

analysts_data['Michael']

for i in analysts_data:
    if analysts_data[i][0] > 3:
        print(i)

