
# 🏥 Hospital Analytics Dashboard

## Overview

The **Hospital Analytics Dashboard** is an interactive web application built with **Python** and **Streamlit** to provide real-time insights into hospital operations. It analyzes patient demographics, medical conditions, financial performance, and hospital/doctor metrics, helping users make informed decisions based on hospital data.

---

## Features

* **Overview:** Total patients, revenue, average billing, average hospital stay.
* **Patient Demographics:** Age distribution, gender distribution, and medical condition breakdowns.
* **Medical Conditions:** Most common diseases, average bills per condition.
* **Financial & Insurance Insights:** Revenue by admission type, insurance coverage, and billing trends.
* **Doctor Performance:** Top doctors by revenue and number of patients treated.
* **Hospital Performance:** Hospitals with highest patient volume, shortest/longest average stay, and stay trends by admission type.
* **Interactive Charts:** Built with **Plotly** and **Altair** for dynamic, easy-to-read visualizations.

---

## Dataset

The dashboard works with hospital datasets containing:

* Patient information (age, gender)
* Hospital and doctor data
* Admission and discharge details
* Length of stay
* Medical conditions
* Billing and insurance details
* Treatment information

Each record represents a **hospital visit** by a patient.

---

## Technologies Used

* **Python** → Data processing and scripting
* **Pandas** → Data manipulation and aggregation
* **Plotly / Altair** → Interactive visualizations
* **Streamlit** → Web dashboard interface
* **PostgreSQL** → Database backend for storing hospital data

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/hospital-analytics-dashboard.git
   cd hospital-analytics-dashboard
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Update database connection in `main.py`:

   ```python
   conn=psycopg2.connect(
       host="localhost",
       database="hospitaldb",
       user="postgres",
       password="YOUR_PASSWORD",
       port=5432
   )
   ```
4. Place the path of the sql code file you dounloded in the space pointed by a comment


---

## Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

* Navigate using the **sidebar menu**.
* Explore metrics, charts, and dashboards for **patients, doctors, hospitals, and financial data**.
* Use the **Upload Data** page to update datasets.

---

## Project Structure

```
hospital-analytics-dashboard/
│
├─ main.py                # Main Streamlit app
├─ queries/               # SQL query files
├─ data/                  # Sample datasets
├─ requirements.txt       # Python dependencies
└─ README.md              # Project documentation
```

---

## Why This Matters

Healthcare data is complex. This dashboard turns raw hospital data into:

* **Actionable insights**
* **Clear visualizations**
* **Performance monitoring** for hospitals and doctors
  It demonstrates how **data science and visualization improve healthcare decision-making**.

---

## License

MIT License. Free to use, modify, and distribute.

---

If you want, I can also make a **short, GitHub-friendly version** with emojis and badges that’s ready to paste directly into your repo—it’ll look professional and modern. Do you want me to do that?

