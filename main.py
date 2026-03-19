import psycopg2
import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
conn=psycopg2.connect(
      host="localhost",
      database="hospitaldb",
      user="postgres",
      password="YOUR_PASSWORD_HERE",  # <-- replaced private password
      port=5432
)
cursor = conn.cursor()
def run_query(file_path):
    with open(file_path, 'r') as f:
        sql = f.read()
    cursor.execute(sql)
    colnames = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=colnames)
    return df
def total_patients():
    data = run_query(r"the path to the file that have query named total_number_of_patients")
    total = data["total_number_of_patients"].iloc[0]
    st.metric("TOTAL NUMBER OF PATIENTS ", total)
def total_revenue():
     data = run_query(r"the path to the file that have query named total_revenue.sql")
     total = data["total_revenue"].iloc[0]
     st.metric("TOTAL REVENUE ", total)
def average_billper_patient():
    data=run_query(r"the path to the file that have query named average_bill_per_patient.sql")
    bill=data["average_bill_per_patient"].iloc[0]
    st.metric("AVERAGE BILL PER PATIENT",bill)
def average_days_stay():
    data=run_query(r"the path to the file that have query named averagedays_stay.sql")
    days=data["average_stay"].iloc[0]
    st.metric("AVERAGE DAYS OF STAY",days)
def Average_minimum_and_maximum_age():
    data=run_query(r"the path to the file that have query named Average_minimum_and _maximum_age.sql")
    age=data["average_age"].iloc[0]
    st.metric("AVERAGE AGE OF PATINTS",age)
    st.metric("THE LOWEST AGE RECORDED ",data["minimum_age"].iloc[0])
    st.metric("THE HIGHST AGE RECORDED",data["maximum_age"].iloc[0])
def Gender_count():
    data=run_query(r"the path to the file that have query named gender_count.sql")
    chart=px.bar(
        data,
        x="gender",
       y="count",
       color="gender"
    ) 
    chart.update_layout(
    bargap=0.5,       # space between all bars
    bargroupgap=0.2   # space between bars in the same group
)
    st.plotly_chart(chart)
def Age_Group_Distribution_by_Condition():
    data = run_query(r"the path to the file that have query named Age_Group_Distribution_by_Condition.sql")
    chart_data = data.melt(
    id_vars="medical_condition",
    var_name="Age_Group",
    value_name="Count"
)
    chart=px.bar(
        chart_data,
        x="medical_condition",
        y="Count",
        color="Age_Group",
        barmode="group"
        
    )
    st.plotly_chart(chart)
def Age_distribution_by_age_groups():
    data = run_query(r"the path to the file that have query named Age distribution by age groups.sql")
    chart_data = data.melt(var_name="Age_Group", value_name="Count")
    chart=px.bar(chart_data,
        x="Age_Group",
        y="Count",
        color="Age_Group",
        barmode="group"
        
    )
   
    st.plotly_chart(chart)
def top_5_common_medical_conditions():
    data = run_query(r"the path to the file that have query named top_5_most_common_cases.sql")
    
    fig = px.bar(
        data,
        x="medical_condition",
        y="number_of_patients",
        color="medical_condition",
        height=400,
    )
    fig.update_traces(width=0.5)  # make bars thinner
    st.plotly_chart(fig)
def average_bill_per_patient():
    data = run_query(r"the path to the file that have query named average_bill_per_patient.sql")
    st.metric("AVERAGE BILL PER PATIENT",data["average_bill_per_patient"].iloc[0])
def average_bill_per_condition():
    data = run_query(r"the path to the file that have query named average_bill_for_each_condition.sql")
    fig = px.bar(
        data,
        x="medical_condition",
        y="avg_billing",
        color="medical_condition",
        height=400
    )
    fig.update_traces(width=0.5)  # thinner bars
    st.plotly_chart(fig)

def revenues_from_each_admission_type():
    data = run_query(r"the path to the file that have query named revenues_from_each_admission_type.sql")
    
    fig = px.bar(
        data,
        x="admission_type",
        y="total_revenue",
        color="admission_type",
        height=400
    )
    fig.update_traces(width=0.5)  # thinner bars
    st.plotly_chart(fig)
def total_billing_by_insurance_companies():
    data = run_query(r"the path to the file that have query named total_billing_by_insurance_campanies.sql")
    chart = px.bar(
        data,
        x="insurance_provider",
        y="total_billing",
        color="insurance_provider",
        height=400
    )
    chart.update_traces(width=0.5)
    st.plotly_chart(chart)

def number_of_patients_coverd_by_each_insurance():
    data = run_query(r"the path to the file that have query named number_of_patients_coverd_by_each_insurance.sql")
    chart = px.bar(
        data,
        x="insurance_provider",
        y="number_of_patients_coverd",
        color="insurance_provider",
        height=400
    )
    chart.update_traces(width=0.5)
    st.plotly_chart(chart)

def top_10_total_revenue_per_doctor():
    data = run_query(r"the path to the file that have query named top_10_total_revenue_per_doctor.sql")
    chart = px.bar(
        data,
        x="doctor",
        y="total_revenue_per_doctor",
        color="doctor",
        height=400
    )
    chart.update_traces(width=0.5)
    # st.plotly_chart(chart)
    return data, chart

def top_10_number_of_patients_doctors_treated():
    data = run_query(r"the path to the file that have query named top_10_number_of_patients_doctors_treated.sql")
    chart = px.bar(
        data,
        x="doctor",
        y="number_of_patients_doctor_treated",
        color="doctor",
        height=400
    )
    chart.update_traces(width=0.5)
    return data, chart

def top_10_patient_per_hospital():
    data = run_query(r"the path to the file that have query named top_10_patient_per_hospital.sql")
    chart = px.bar(
        data,
        x="hospital",
        y="patient_per_hospital",
        color="hospital",
        height=400
    )
    chart.update_traces(width=0.5)
    return data, chart
def top_10_lowest_stay_per_hospital():
    # Run your SQL query
    data = run_query(r"the path to the file that have query named top_10_lowest_stay_hospitals.sql")
    
    # Convert average_stay to numeric just in case
    data["average_stay"] = pd.to_numeric(data["average_stay"])
    
    # Create Plotly bar chart
    fig = px.bar(
        data,
        x="hospital",
        y="average_stay",
        color="hospital",
        text="average_stay",   # shows the value on top of each bar
        title="Top 10 Hospitals with Lowest Average Stay",
    )
    # Optional: show values on bars
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    
    # Return both data and chart figure
    return data, fig
def top_10_highst_stay_per_hospital():
    data = run_query(r"the path to the file that have query named top_10_hospitals_with_longest_stay.sql")
    data["average_stay"]=pd.to_numeric(data["average_stay"])
    chart=px.bar(
        data,
        x="hospital",
        y="average_stay",
        color="hospital",
        text="average_stay"
    )
    return data,chart
def avarage_stay_per_addmission_states():
    data = run_query(r"the path to the file that have query named avarage_stay_per_addmission_states.sql")
    data["average_stay"]=pd.to_numeric(data["average_stay"])
    chart=px.bar(
        data,
        x="admission_type",
        y="average_stay",
        color="admission_type"

    )
    chart.update_traces(width=0.5)
    return data,chart
def Doctor_Performance_page():
    table, chart = top_10_total_revenue_per_doctor()
    table2, chart2 = top_10_number_of_patients_doctors_treated()
    st.markdown(
        "<h2 style='text-align: center; color: #4B8BBE;'>🏥 Doctor Performance Dashboard</h2>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h4 style='text-align: center; color: #444;'>Key Highlights</h4>",
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    col1.metric(
        label=f"💰 {table.iloc[0,0]}",
        value=f"${table.iloc[0,1]:,}"
    )
    col1.markdown(
        "<p style='text-align:left; color:#1E90FF; font-weight:bold;'>Top revenue generated</p>",
        unsafe_allow_html=True
    )
    col2.metric(
        label=f"🏥 {table2.iloc[0,0]}",
        value=f"{table2.iloc[0,1]:,}"
    )
    col2.markdown(
        "<p style='text-align:left; color:#1E90FF; font-weight:bold;'>Most patients treated</p>",
        unsafe_allow_html=True
    )
    st.markdown("<hr style='border:1px solid #4B8BBE'>", unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: center; color: #FF5733;'>Top Revenue Doctors 💰</h4>"
             "<p style='text-align: center;'>Doctors generating the highest revenue across all departments.</p>",
            unsafe_allow_html=True
       )  
    st.plotly_chart(chart) 
    st.markdown(
            "<h4 style='text-align: center; color: #33C1FF;'>Most Active Doctors 🏥</h4>"
            "<p style='text-align: center;'>Doctors treating the most patients this period.</p>",
            unsafe_allow_html=True )
    st.plotly_chart(chart2) 
    st.info("💡 Tip: Hover over the chart bars to see exact numbers for revenue and patients treated. Use this dashboard to monitor doctor performance at a glance.")
def hospital_performace_page():
    table, chart = top_10_patient_per_hospital()
    table2, chart2 = top_10_lowest_stay_per_hospital()
    table3, chart3 = top_10_highst_stay_per_hospital()
    table4, chart4 = avarage_stay_per_addmission_states()
    st.markdown(
    "<h3 style='text-align: center; color: #4B8BBE;'>Top 10 Hospitals by Patient Count</h3>"
    "<p style='text-align: center;'>This chart displays the 10 hospitals with the highest number of patients.</p>",
    unsafe_allow_html=True
)   
    st.plotly_chart(chart)
    st.markdown(
    "<h3 style='text-align: center; color: #4B8BBE;'>Top 10 Hospitals With The Lowest Average Stay</h3>"
    "<p style='text-align: center;'>This chart displays 10 hospitals with the lowest average stay.</p>",
    unsafe_allow_html=True
)   
    st.plotly_chart(chart2, use_container_width=True)
    st.markdown(
    "<h3 style='text-align: center; color: #4B8BBE;'>Top 10 Hospitals With The Highst Average Stay</h3>"
    "<p style='text-align: center;'>This chart displays 10 hospitals with the highst average stay.</p>",
    unsafe_allow_html=True
)   
    st.plotly_chart(chart3,use_container_width=True)
    st.markdown(
    "<h3 style='text-align: center; color: #4B8BBE;'>Average Stay By Addmission States</h3>"
    "<p style='text-align: center;'>This graph showes the average stay by the 3 addmission states </p>",
    unsafe_allow_html=True
)   
    st.plotly_chart(chart4)

# PAGE CONFIG (place at the top of your file)
st.set_page_config(
    page_title="Hospital Analytics Dashboard",
    page_icon="🏥",
    layout="wide"
)
def main_dashboard():
    
    # ---------- DASHBOARD HEADER ----------
    st.markdown("""
    <h1 style='text-align:center; color:#4B8BBE;'>🏥 Hospital Analytics Dashboard</h1>
    <p style='text-align:center; font-size:18px; color:gray;'>
    Real-time insights into hospital operations, patient demographics,
    medical conditions, and financial performance.
    </p>
    <hr style='border:1px solid #4B8BBE'>
    """, unsafe_allow_html=True)


    # ---------- SIDEBAR ----------
    st.sidebar.markdown(
        """
        <h2 style='text-align:center; color:#4B8BBE;'>📊 Dashboard Menu</h2>
        <hr>
        """,
        unsafe_allow_html=True
    )

    choice = st.sidebar.selectbox(
        "📂 Select Dashboard Page",
        [
            "Dashboard",
            "Overview",
            "Patient Demographics",
            "Medical Conditions",
            "Financial & Insurance",
            "Doctor Performance",
            "Hospital Performance"
        ]
    )

    st.sidebar.markdown("---")

    if st.sidebar.button("🏠 Home"):
        st.session_state["page"] = "HOME"
        st.rerun()

    st.sidebar.markdown(
        """
        <hr>
        <p style='text-align:center; font-size:12px; color:gray;'>
        Hospital Data Analytics System<br>
        Built with Streamlit
        </p>
        """,
        unsafe_allow_html=True
    )


    # ---------- DASHBOARD HOME ----------
    if choice == "Dashboard":

        st.markdown("""
        <h2 style='text-align:center; color:#4B8BBE;'>📊 Dashboard Overview</h2>
        <p style='text-align:center; color:gray;'>
        Explore insights about hospital performance, patient demographics,
        financial statistics, and medical conditions.
        </p>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.info("👨‍⚕️ **Doctor Performance**\n\nAnalyze doctors generating the most revenue and treating the highest number of patients.")

        with col2:
            st.info("🏥 **Hospital Performance**\n\nCompare hospitals by patient count and patient stay duration.")

        with col3:
            st.info("💰 **Financial Insights**\n\nMonitor revenue streams, insurance coverage, and billing trends.")


    # ---------- OVERVIEW PAGE ----------
    elif choice == "Overview":

        st.markdown(
        "<h3 style='text-align:center; color:#4B8BBE;'>📈 Key Hospital Statistics</h3>",
        unsafe_allow_html=True
        )

        k1,k2,k3,k4 = st.columns(4)

        with k1:
            total_patients()

        with k2:
            total_revenue()

        with k3:
            average_billper_patient()

        with k4:
            average_days_stay()

        st.markdown("<hr>", unsafe_allow_html=True)

        colm1,colm2=st.columns(2)

        with colm1:
            Average_minimum_and_maximum_age()

        with colm2:
            average_days_stay()


    # ---------- PATIENT DEMOGRAPHICS ----------
    elif choice == "Patient Demographics":

        st.markdown(
        "<h3 style='text-align:center; color:#4B8BBE;'>👥 Patient Demographics</h3>",
        unsafe_allow_html=True
        )

        st.markdown(
        "<h4 style='color:#4B8BBE;'>Gender Distribution</h4>",
        unsafe_allow_html=True
        )
        Gender_count()

        st.markdown(
        "<h4 style='color:#4B8BBE;'>Age Distribution</h4>",
        unsafe_allow_html=True
        )
        Age_distribution_by_age_groups()

        st.markdown(
        "<h4 style='color:#4B8BBE;'>Age Distribution by Medical Condition</h4>",
        unsafe_allow_html=True
        )
        Age_Group_Distribution_by_Condition()


    # ---------- MEDICAL CONDITIONS ----------
    elif choice == "Medical Conditions":

        st.markdown(
        "<h3 style='text-align:center; color:#4B8BBE;'>🩺 Medical Conditions Analysis</h3>",
        unsafe_allow_html=True
        )

        top_5_common_medical_conditions()

        st.markdown(
        "<h4 style='color:#4B8BBE;'>Average Bill per Medical Condition</h4>",
        unsafe_allow_html=True
        )

        average_bill_per_condition()


    # ---------- FINANCIAL ----------
    elif choice=="Financial & Insurance":

        st.markdown(
        "<h3 style='text-align:center; color:#4B8BBE;'>💰 Financial & Insurance Insights</h3>",
        unsafe_allow_html=True
        )

        revenues_from_each_admission_type()

        total_billing_by_insurance_companies()

        number_of_patients_coverd_by_each_insurance()


    # ---------- DOCTOR PERFORMANCE ----------
    elif choice == "Doctor Performance":

        Doctor_Performance_page()


    # ---------- HOSPITAL PERFORMANCE ----------
    elif choice=="Hospital Performance":

        hospital_performace_page()

    


if "page" not in st.session_state:
    st.session_state["page"] = "HOME"


# ---------- HOME PAGE ----------

if st.session_state["page"] == "HOME":

    # Title
    st.markdown("""
    <h1 style='text-align:center; color:#4B8BBE;'>🏥 Hospital Analytics System</h1>
    <p style='text-align:center; font-size:18px; color:gray;'>
    Explore hospital insights including patient demographics, medical conditions,
    financial performance, and hospital operations.
    </p>
    <hr>
    """, unsafe_allow_html=True)

    st.write("")

    # Buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📊 Dashboard")
        st.write("View analytics and insights about hospital data.")
        if st.button("Open Dashboard"):
            st.session_state["page"] = "DASHBOARD"
            st.rerun()

    with col2:
        st.markdown("### ℹ️ About")
        st.write("Learn more about this project and how the dashboard works.")
        if st.button("About Project"):
            st.session_state["page"] = "ABOUT"
            st.rerun()

    with col3:
        st.markdown("### ⬆ Upload Data")
        st.write("Upload new hospital data to update the analytics.")
        if st.button("Upload Dataset"):
            st.session_state["page"] = "UPLOAD NEW DATA"
            st.rerun()

    st.write("")
    st.write("")

    st.markdown(
        "<p style='text-align:center; color:gray;'>Built with Streamlit • Hospital Data Analytics Dashboard</p>",
        unsafe_allow_html=True
    )


# ---------- DASHBOARD PAGE ----------

elif st.session_state["page"] == "DASHBOARD":

    main_dashboard()


# ---------- ABOUT PAGE ----------

elif st.session_state["page"] == "ABOUT":

    st.title("ℹ️ About This Project")

    st.markdown("""
    ## 🏥 Hospital Analytics Dashboard

    The **Hospital Analytics Dashboard** is an interactive data analysis application 
    designed to explore and visualize hospital data. It helps users understand 
    patient trends, hospital performance, medical conditions, and financial insights 
    through clear and interactive visualizations.

    This dashboard was built using **Python**, **Pandas**, **Matplotlib/Seaborn**, and **Streamlit** 
    to transform raw hospital datasets into meaningful insights.

    ---
    ## 🎯 Project Objectives

    The main goals of this project are to:

    - Analyze **hospital operational performance**
    - Understand **patient demographics**
    - Identify **common medical conditions**
    - Evaluate **doctor performance**
    - Explore **insurance and financial patterns**
    - Discover trends that may help improve healthcare decisions

    The dashboard allows users to quickly explore complex hospital datasets 
    without needing advanced technical knowledge.

    ---
    ## 📊 Dataset Information

    The dataset used in this project contains information such as:

    - Patient demographics (age, gender)
    - Hospital names
    - Doctors
    - Medical conditions
    - Admission and discharge details
    - Length of hospital stay
    - Insurance providers
    - Billing amounts
    - Treatment information

    Each record represents a **hospital visit by a patient**.

    This data helps analyze **how hospitals operate and treat patients**.

    ---
    ## 📈 Dashboard Features

    The dashboard contains several analysis sections:

    ### 1️⃣ Overview
    Provides general statistics about the dataset such as:

    - Total patients
    - Total hospitals
    - Total doctors
    - Average billing amount
    - Average hospital stay

    This section gives users a quick summary of the dataset.

    ---
    ### 2️⃣ Patient Demographics

    This section analyzes the **characteristics of patients**, including:

    - Age distribution
    - Gender distribution
    - Patient counts

    These insights help understand **who is receiving medical care**.

    ---
    ### 3️⃣ Medical Conditions

    This section focuses on **disease patterns** such as:

    - Most common medical conditions
    - Distribution of diagnoses
    - Frequency of treatments

    It helps identify **health trends among patients**.

    ---
    ### 4️⃣ Financial & Insurance Analysis

    This section explores the **financial side of healthcare**, including:

    - Billing amounts
    - Insurance providers
    - Payment distribution
    - Cost trends

    It helps understand **how healthcare costs vary**.

    ---
    ### 5️⃣ Doctor Performance

    This section analyzes **doctor-related metrics**, such as:

    - Number of patients treated
    - Average hospital stay per doctor
    - Treatment distribution

    These insights help evaluate **medical staff performance**.

    ---
    ### 6️⃣ Hospital Performance

    This section focuses on **hospital-level analysis**, including:

    - Hospitals with the shortest patient stays
    - Hospitals with high patient volumes
    - Performance comparisons

    It helps identify **efficient hospitals and operational trends**.

    ---
    ## 🖥️ How to Use the Dashboard

    Follow these steps to explore the dashboard:

    1️⃣ Start at the **Home Page**

    From the home page you can:
    - Open the Dashboard
    - Read about the project
    - Upload a new dataset

    2️⃣ Open the **Dashboard**

    Use the **sidebar menu** to navigate between sections:
    - Overview
    - Patient Demographics
    - Medical Conditions
    - Financial & Insurance
    - Doctor Performance
    - Hospital Performance

    3️⃣ Explore Visualizations

    Each page includes charts and statistics that allow you to 
    understand the data quickly.

    4️⃣ Upload New Data (Optional)

    The **Upload Data** section allows users to upload new datasets 
    to update the analysis.

    ---
    ## 🧠 Technologies Used

    This project was built using:

    - **Python** → Data processing
    - **Pandas** → Data analysis
    - **Matplotlib / Seaborn** → Data visualization
    - **Streamlit** → Interactive dashboard

    These tools allow fast data analysis and interactive web applications.

    ---
    ## 📌 Why This Dashboard Matters

    Healthcare data is complex and difficult to interpret in raw form.

    This dashboard helps transform large hospital datasets into:

    - Clear insights
    - Visual patterns
    - Actionable information

    It demonstrates how **data science and visualization can improve 
    healthcare decision-making**.

    ---
    """)

    st.success("🚀 Built with Streamlit for interactive hospital data analysis.")
    if st.button("BACK"):
        st.session_state["page"]="HOME"
        st.rerun()


# ---------- UPLOAD PAGE ----------

elif st.session_state["page"] == "UPLOAD NEW DATA":

    st.title("Upload New Data")
    st.write("This is where uploading new data will happen.")
