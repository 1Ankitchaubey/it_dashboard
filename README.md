# 🖥️ IT Support Dashboard

Interactive dashboard for IT Support Daily Call Reports built with Python + Streamlit + Plotly.

---

## ⚡ Quick Setup (3 Steps)

### Step 1 — Install libraries
Open CMD / Terminal in this folder and run:
```
pip install -r requirements.txt
```

### Step 2 — Run the dashboard
```
streamlit run app.py
```
Browser automatically opens at: **http://localhost:8501**

### Step 3 — Upload your Excel file
- Sidebar mein "Upload Data" section mein apni Excel file drop karo
- Sab charts automatically update ho jayenge!

---

## 📊 Dashboard Features

| Feature | Details |
|---|---|
| 📈 Call Volume Trend | Daily / Weekly / Monthly toggle |
| 🔧 Call Type Split | Hardware vs Software vs Network |
| 👨‍💻 Engineer Performance | Total calls + Resolved comparison |
| 📍 Location Analysis | Stacked bar by location |
| 🏢 Dept × Engineer Heatmap | Cross analysis |
| ✅ Resolution Status | Pie chart |
| 💻 Device Type | Desktop vs Laptop |
| ⏱️ Avg Call Duration | Per engineer |
| 📋 Raw Data Table | With CSV download |
| 🔍 Smart Filters | Location, Engineer, Call Type, Date Range |

---

## 🌐 Deploy Online (Free) — Public URL banao

### Step 1 — GitHub pe daalo
1. GitHub.com pe free account banao
2. New repository banao: `it-dashboard`
3. Is folder ki files upload karo (app.py, requirements.txt)

### Step 2 — Streamlit Cloud connect karo
1. **share.streamlit.io** pe jao
2. GitHub se login karo
3. "New app" → apna repo select karo → `app.py` select karo
4. **Deploy!** — 2-3 minutes mein public URL mil jayega 🎉

### Example URL:
```
https://your-name-it-dashboard.streamlit.app
```

---

## 📁 File Structure
```
it_dashboard/
├── app.py              ← Main dashboard code
├── requirements.txt    ← Python libraries
└── README.md           ← Ye file
```

---

## 🔄 Data Update kaise karein
- Koi bhi nayi Excel file sidebar se upload karo
- Sab charts instantly refresh ho jayenge
- Filters bhi automatically update honge
