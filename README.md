# twitch-streamer-analytics
Data is from :
# https://streamhatchet.com/rankings/twitch/?period=last-30-days

This project analyzes the **Top Twitch Channels (July 17 – Aug 16, 2025)** dataset to extract useful insights for streamers.  
It explores **efficiency, audience stability, and streaming strategies** using Python.

## How to Run
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

## Project Structure
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
