# Twitch Stream Analysis

This project analyzes the **Top Twitch Channels (July 17 – Aug 16, 2025)** dataset to extract useful insights for streamers.  
It explores **efficiency, audience stability, and streaming strategies** using Python.

## 🔍 Features
- Exploratory Data Analysis (EDA) of Twitch channels
- Custom metrics like:
  - Viewers per Hour
  - Audience Stability
  - Engagement Efficiency
- Clustering streamers into categories
- Visualizations & leaderboards

## 📊 Example Insights
- Some channels stream only a few hours but dominate viewership (event-driven streamers).
- Others grind long hours but have relatively low engagement efficiency.
- Audience stability varies greatly between top creators.

## 🛠️ Tech Stack
- Python (pandas, matplotlib, seaborn, scikit-learn)
- Jupyter Notebooks
- Streamlit (for interactive dashboard)

## 🚀 How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/twitch-stream-analysis.git
   cd twitch-stream-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the analysis notebooks:
   ```bash
   jupyter notebook notebooks/01_exploration.ipynb
   ```

4. (Optional) Run the dashboard:
   ```bash
   streamlit run dashboard/app.py
   ```

## 📂 Project Structure
```
twitch-stream-analysis/
│
├── data/                       # dataset storage
├── notebooks/                  # Jupyter analysis notebooks
├── src/                        # reusable scripts (cleaning, analysis, viz)
├── dashboard/                  # optional Streamlit dashboard
├── README.md                   # project documentation
├── requirements.txt            # dependencies
└── LICENSE
```

---
✨ Inspired by data-driven content creation and Twitch analytics.
