# API Snowflake Pipeline Project

## Overview

This project is an end-to-end data engineering pipeline that integrates:

- Data extraction from public APIs
- Data loading into Snowflake data warehouse
- Data transformation using dbt (data build tool)
- Pipeline orchestration and scheduling with Apache Airflow

All components are configured both through code and via their respective user interfaces for flexibility and ease of management.

---

## Features

- **API Data Extraction:** Pull data from external sources programmatically.
- **Snowflake Integration:** Load and store data efficiently in Snowflake.
- **dbt Transformations:** Define and run modular SQL transformations and tests.
- **Airflow Orchestration:** Schedule, monitor, and manage pipeline workflows.
- **UI Connectivity:** Manage Snowflake, dbt, and Airflow configurations and monitoring through their respective user interfaces.

---

## Getting Started

### Prerequisites

- Python 3.7+
- Apache Airflow 3.x
- Snowflake account and Python connector
- dbt installed with Snowflake adapter
- Git (for version control)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shreyas-gk/api_snowflake_pipeline.git
   cd api_snowflake_pipeline

2. Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate

3. Install required packages:

bash
Copy
Edit
pip install -r requirements.txt

4. Configure connections and credentials for Snowflake, Airflow, and dbt as per your environment.

Usage
Airflow: Use the Airflow UI to trigger and monitor DAGs. DAGs are stored in the dags/ folder.

dbt: Run dbt commands such as dbt run, dbt test, and dbt docs generate from the command line.

Snowflake: Use Snowflake UI or SnowSQL CLI to interact with the loaded data.

Project Structure
bash
Copy
Edit
api_snowflake_pipeline/
│
├── dags/                     # Airflow DAGs
├── dbt_project/              # dbt models, tests, and configs
├── scripts/                  # Python scripts for API extraction or utilities
├── requirements.txt          # Python dependencies
├── README.md                 # This documentation file
└── airflow_home/             # Airflow configs, logs, and DB

Additional Notes
All pipeline components are designed to work seamlessly together, offering the option to manage configurations and monitor via both code and UIs.

Customize your Airflow connections and dbt profiles to suit your cloud and Snowflake setup.

Use dbt docs serve to generate and view documentation for your dbt models.

Contact
For questions or support, please contact Shreyas at shreyasgk1234@gmail.com