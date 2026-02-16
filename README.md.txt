# 🍷 Advanced 3D Wine Analytics Dashboard

An end-to-end data analytics pipeline that automates dataset ingestion using the Kaggle API, performs data cleaning and anomaly detection, and delivers interactive 3D visual insights through a modern Streamlit dashboard powered by Plotly.

---

## 🚀 Project Overview

This project simulates a real-world data engineering and analytics workflow, starting from automated data acquisition to delivering decision-ready insights via an interactive web dashboard.

It demonstrates industry practices such as automated pipelines, data preprocessing, analytics modeling, and modern visualization techniques.

---

## 🎯 Problem Statement

Organizations often face challenges including:

* Manual data collection processes
* Lack of real-time insights
* Static reporting systems
* Difficulty analyzing large datasets visually

This project solves these challenges by creating a fully automated data analytics pipeline with interactive visualization capabilities.

---

## ⭐ Key Features

### 🔹 Automated Data Ingestion

* Uses Kaggle API to download datasets automatically
* Eliminates manual dataset handling
* Supports reproducible data workflows

---

### 🔹 Data Cleaning Pipeline

* Handles missing values
* Removes redundant features
* Performs data validation
* Produces clean, analysis-ready datasets

---

### 🔹 Analytics & Insight Engine

* Extracts business insights
* Identifies trends and correlations
* Performs anomaly detection
* Generates statistical summaries

---

### 🔹 Interactive 3D Dashboard

* Built using Streamlit + Plotly
* Features include:

  * 3D visual analytics
  * Heatmaps & distribution charts
  * Dynamic filters
  * Modern dark-theme UI

---

### 🔹 Scalable Architecture

Designed using modular pipeline components for easy extension and deployment.

---

## 🏗️ System Architecture

```
Kaggle Dataset
      ↓
Automated API Download
      ↓
Data Cleaning Pipeline
      ↓
Analytics & Insight Engine
      ↓
Interactive Visualization Dashboard
```

---

## 🧰 Tech Stack

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly (3D interactive charts)
* Streamlit (dashboard framework)

### Data Source

* Kaggle API

---

## 📂 Project Structure

```
wine-analytics-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── pipeline/
│   ├── download_data.py
│   ├── clean_data.py
│   ├── analyze_data.py
│   ├── analyze_insights.py
│   └── visualize_data.py
│
└── assets/
    └── screenshots/
```

---

## 📥 Dataset Information

The dataset is **not stored in the repository** due to GitHub size limits.

It is automatically downloaded using the Kaggle API.

---

## ⚙️ Installation & Setup

### Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/wine-analytics-dashboard.git
cd wine-analytics-dashboard
```

---

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3 — Configure Kaggle API

1. Generate Kaggle API token from:
   [https://www.kaggle.com/settings](https://www.kaggle.com/settings)

2. Set environment variables:

```bash
setx KAGGLE_USERNAME "your_username"
setx KAGGLE_KEY "your_api_key"
```

Restart terminal after setting.

---

## ▶️ Running the Project

### Step 1 — Download Dataset

```bash
python pipeline/download_data.py
```

---

### Step 2 — Clean Data

```bash
python pipeline/clean_data.py
```

---

### Step 3 — Launch Dashboard

```bash
streamlit run app.py
```

---

## 📊 Dashboard Features

The dashboard provides:

* Wine production insights by country
* Price distribution analytics
* Price vs rating relationship visualization
* 3D market landscape analysis
* Interactive filtering capabilities

---

## 📈 Business Insights Generated

The system automatically identifies:

* Dominant wine-producing regions
* Relationship between price and quality
* Premium wine clusters
* Market price trends
* High-value anomaly products

---

## 🌍 Real-World Applications

This project simulates real enterprise use cases such as:

* Business intelligence dashboards
* Market analytics systems
* Sales performance monitoring
* Data-driven decision platforms

---

## 🚀 Future Enhancements

Potential improvements include:

* Real-time data streaming
* Cloud deployment automation
* Machine learning price prediction
* Alert notification system
* Database integration

---

## 💼 Resume Highlights

This project demonstrates:

* API-based data ingestion
* Data engineering workflow design
* Interactive analytics system development
* Full pipeline automation
* Dashboard deployment readiness

---

## 📜 License

This project is for educational and demonstration purposes.

---

# ⭐ OPTIONAL (Highly Recommended)

Add this at the very top of README after deployment:

```
🔗 Live Demo: https://wine-analytics-dashboard-rrvxs6glzuhzoeefhdx4qt.streamlit.app



