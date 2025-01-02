import streamlit as st
import pandas as pd
import requests

# Set page configuration
st.set_page_config(page_title="Job Dashboard", layout="wide")

# Title
st.title("Job Dashboard")
st.markdown("Search for jobs by keyword and location.")

# Sidebar for filters
st.sidebar.header("Filters")
keyword = st.sidebar.text_input("Keyword (e.g., 'Data Analyst')", value="Data Analyst")
location = st.sidebar.text_input("Location (e.g., 'New York')", value="New York")
min_salary = st.sidebar.slider("Minimum Salary", min_value=0, max_value=200000, value=50000)

# Fetch jobs (replace this with an API or local dataset)
@st.cache
def fetch_jobs(keyword, location):
    # Mock data for demonstration; replace with an API like LinkedIn or Indeed
    jobs = pd.DataFrame({
        "Title": ["Data Scientist", "Data Analyst", "Machine Learning Engineer"],
        "Company": ["Company A", "Company B", "Company C"],
        "Location": ["New York, NY", "Los Angeles, CA", "Chicago, IL"],
        "Salary": [120000, 95000, 110000],
        "Link": ["http://example.com/job1", "http://example.com/job2", "http://example.com/job3"]
    })
    filtered_jobs = jobs[
        (jobs["Title"].str.contains(keyword, case=False)) &
        (jobs["Location"].str.contains(location, case=False)) &
        (jobs["Salary"] >= min_salary)
    ]
    return filtered_jobs

# Fetch data and display results
jobs_df = fetch_jobs(keyword, location)
st.subheader(f"Jobs for '{keyword}' in '{location}'")
st.write(f"Found {len(jobs_df)} job(s).")

# Display table of jobs
for index, row in jobs_df.iterrows():
    st.markdown(f"""
    **{row['Title']}**  
    🏢 {row['Company']}  
    📍 {row['Location']}  
    💵 ${row['Salary']}  
    [Apply here]({row['Link']})  
    ---
    """)

# Add some style
st.markdown(
    """
    <style>
    .sidebar .sidebar-content { background-color: #f8f9fa; }
    </style>
    """, unsafe_allow_html=True
)