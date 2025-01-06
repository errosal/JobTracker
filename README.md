Job Tracker Dashboard

Overview

The Job Tracker Dashboard is a Streamlit-based application designed to help users log, track, and manage job applications. It allows you to store job details such as the company name, job title, tools required, salary range, and the platform where you applied (e.g., LinkedIn, Glassdoor). It also provides options for viewing, filtering, and managing job logs, including the ability to delete logs.

Features
	•	Log New Jobs: Add job details, including company name, job title, tools required, job type, salary range, perks, and the platform where you applied.
	•	Manage Jobs: Filter and manage job applications by company. You can also delete specific job logs.
	•	View Logs: View all logged jobs in a tabular format.
	•	Job Statistics: Track job types and other statistics with interactive charts.

Requirements

To run this project, make sure you have Python 3.x installed and the following packages:
	•	Streamlit: For the web interface
	•	Pandas: For managing the data

You can install the required packages by running:

pip install streamlit pandas

Setup & Usage
	1.	Clone the repository:

git clone https://github.com/errosal/JobTracker.git


	2.	Run the Streamlit app:

streamlit run app.py

	3.	Log a Job:
	•	In the “Log Job” section, fill out the details for a new job application, including:
	•	Company Name
	•	Job Title
	•	Tools Required
	•	Job Type (Hybrid, Remote, On-site, or NA)
	•	Salary Range
	•	Perks
	•	Applied On (Date picker)
	•	Where Applied (e.g., LinkedIn, Glassdoor)
	•	Click Save Job to log the details.
	4.	View Job Logs:
	•	In the “View Logs” section, you can see all the job logs you’ve entered, displayed in a table format.
	5.	Manage Logs:
	•	In the “Manage Logs” section, you can filter jobs by company name and delete specific job entries.

CSV File

All job logs are stored in a CSV file named job_logs.csv in the project directory. This file is automatically created the first time the app is run. Each job entry contains the following columns:
	•	company_name: Name of the company
	•	job_title: Job title for the position
	•	tools_required: Tools or technologies required for the job
	•	job_type: Type of employment (Hybrid, Remote, On-site)
	•	location: Job location
	•	salary_range: Salary range for the position
	•	perks: Perks offered with the job
	•	applied_on: Date when you applied for the job
	•	where_applied: Platform where the job was found (e.g., LinkedIn, Glassdoor)

Contributing

Feel free to fork the repository, make changes, and create a pull request. Contributions are welcome!

License

This project is licensed under the MIT License - see the LICENSE file for details.
