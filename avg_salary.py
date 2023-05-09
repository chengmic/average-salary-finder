from flask import Flask, request, render_template
import requests

APP_ID = "07482c23"
APP_KEY = "c25c7a82ad25690db4364fc6146e474a"

app = Flask(__name__)

def get_average_salary(job_title, location):
    url = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={APP_ID}&app_key={APP_KEY}&results_per_page=0&what={job_title}&where={location}"
    
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        return result['mean']
    else:
        return None


@app.route('/average_salary', methods=['GET'])
def result():
    job_title = request.args.get('job_title')
    location = request.args.get('location')
    
    average_salary = get_average_salary(job_title, location)

    return {"average_salary": average_salary}

if __name__ == '__main__':
    app.run(debug=True)
