import requests

def make_request(param1, param2):
    url = f'http://127.0.0.1:5000/average_salary?job_title={param1}&location={param2}'
    response = requests.get(url)
    data = response.json()

    print (data['average_salary'])
    return data['average_salary']


job='software developer'
location = 'san diego'

make_request(job, location)