import streamlit as st
import pandas as pd

# Path to the CSV file where job details will be stored
CSV_FILE = "job_logs.csv"

# Load data from CSV or create a new DataFrame if not found
def load_data():
    try:
        return pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["company_name", "job_title", "tools_required", "job_type", "location", "salary_range", "perks", "applied_on", "where_applied"])

# Save data to CSV
def save_data(df):
    df.to_csv(CSV_FILE, index=False)

# Job logging form
def log_job():
    st.header("Log a New Job")
    df = load_data()

    # Predefined options
    job_type_options = ["Hybrid", "Remote", "On-site", "NA"]

    # Inputs
    company = st.text_input("Company Name")
    job_title = st.text_input("Job Title")
    tools_required = st.text_input("Tools Required (comma-separated)")
    job_type = st.selectbox("Job Type", job_type_options)
    location = st.text_input("Location")
    salary_range = st.text_input("Salary Range")
    perks = st.text_area("Perks")
    applied_on = st.date_input("Applied On")
    where_applied = st.text_input("Where Applied (e.g., LinkedIn, Glassdoor)")

    # Save job
    if st.button("Save Job"):
        if company and job_title and tools_required and salary_range and where_applied:
            new_job = pd.DataFrame([{
                "company_name": company,
                "job_title": job_title,
                "tools_required": tools_required,
                "job_type": job_type,
                "location": location,
                "salary_range": salary_range,
                "perks": perks,
                "applied_on": applied_on,
                "where_applied": where_applied
            }])
            df = pd.concat([df, new_job], ignore_index=True)
            save_data(df)
            st.success("Job logged successfully!")
        else:
            st.error("Please fill all required fields.")

# Manage logs
def manage_logs():
    st.header("Manage Job Logs")
    df = load_data()

    if df.empty:
        st.warning("No jobs logged yet.")
        return

    company_options = df["company_name"].unique().tolist()
    selected_company = st.selectbox("Select a Company", ["Select"] + company_options)

    if selected_company != "Select":
        filtered_jobs = df[df["company_name"] == selected_company]
        if filtered_jobs.empty:
            st.warning(f"No jobs logged for the company '{selected_company}'.")
        else:
            for i, row in filtered_jobs.iterrows():
                st.write(f"**Job Title**: {row['job_title']}")
                st.write(f"**Tools Required**: {row['tools_required']}")
                st.write(f"**Job Type**: {row['job_type']}")
                st.write(f"**Location**: {row['location']}")
                st.write(f"**Salary Range**: {row['salary_range']}")
                st.write(f"**Perks**: {row['perks']}")
                st.write(f"**Applied On**: {row['applied_on']}")
                st.write(f"**Where Applied**: {row['where_applied']}")
                if st.button(f"Delete Job: {row['job_title']}", key=f"delete_{row.name}"):
                    df = df.drop(index=row.name)
                    save_data(df)
                    st.success(f"Job '{row['job_title']}' deleted successfully!")
                    st.experimental_rerun()

# View logs
def display_logs():
    st.header("View Job Logs")
    df = load_data()

    if df.empty:
        st.warning("No jobs logged yet.")
    else:
        st.dataframe(df)

# Streamlit app layout
def main():
    st.title("Job Tracker Dashboard")
    option = st.sidebar.selectbox("Choose an option", ["Log Job", "View Logs", "Manage Logs"])
    if option == "Log Job":
        log_job()
    elif option == "View Logs":
        display_logs()
    elif option == "Manage Logs":
        manage_logs()

if __name__ == "__main__":
    main()