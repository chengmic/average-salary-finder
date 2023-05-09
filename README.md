# About
This microservice is a simple REST API built with Flask that retrieves information about the average salary of a job title using AdzunaAPI.

# How to Request Data:
Make a GET request to '/average_salary'.

</br>
Use the following parameters: </br>
<b>job_title:</b> The title of the job you want to search.  </br>
<b>location:</b> Where the job is located. For best results, use ZIP code. (NOTE: not all citites are present in Adzuna database but it should work with most major cities.)</br>


# How to Receive Data:
The data received is a JSON:</br>
{"average_salary": average_salary} </br>

# UML Sequence Diagram
<img width="968" alt="UML" src="https://user-images.githubusercontent.com/97090779/237007066-c34638e7-b77b-47fc-ba5d-cf1e2f341097.png">
