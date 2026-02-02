"""
Pulse: A Semantic News Analysis Tool
Author: [Vignesh Cheni]
Description: This application fetches real-time technology news using NewsAPI 
and performs semantic similarity scoring using TF-IDF and Cosine Similarity 
to rank results based on user relevance.
"""

import streamlit as st, requests
import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- 1. APP CONFIGURATION & STYLING ---
st.set_page_config(page_title="Pulse", page_icon="📡", layout="centered")

# Security: Fetching key from Streamlit Secrets
MY_API_KEY = st.secrets["NEWS_API_KEY"]

# Custom CSS for Glassmorphism UI components
st.markdown("""<style>
    /* Dark theme background with gradient */
    .stApp { background: linear-gradient(135deg, #0f172a, #1e293b); color: #f8fafc; }
    .main-header { text-align: center; padding: 40px 0; }
    
    /* Uniform styling for trending topic buttons */
    .stButton>button { 
        background: rgba(56, 189, 248, 0.1); color: #38bdf8; border: 1px solid #38bdf8; border-radius: 10px;
        height: 3.5em !important; min-height: 3.5em !important; display: flex !important; align-items: center !important;
        justify-content: center !important; text-align: center !important;
    }
    .stButton>button:hover { background: #38bdf8; color: #0f172a; }
    
    /* News result cards with backdrop blur */
    .news-card { 
        background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px); 
        padding: 25px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); 
        margin-bottom: 25px; 
    }
    .score-badge { 
        background: #38bdf8; color: #0f172a; padding: 4px 12px; 
        border-radius: 50px; font-weight: 800; font-size: 10px; 
    }
</style>""", unsafe_allow_html=True)

st.markdown("<div class='main-header'><h1>📡 Pulse</h1><p>The Semantic Future of Technology Analysis</p></div>", unsafe_allow_html=True)

# --- 2. INTERACTIVE TRENDING GRID ---
st.write("### 🔥 Trending 2026 Tech")
trends = ["Agentic AI", "Quantum Computing", "Confidential Computing", "SpaceX Starship", "AI Supercomputing", "EV Battery Tech", "Cyber Defense", "Cloud 3.0"]

# Initialize Session State to track selected topic across app reruns
if 'topic' not in st.session_state: 
    st.session_state.topic = ""
    
# Create a 4-column grid for the trending buttons
cols = st.columns(4)
for i, topic in enumerate(trends):
    if cols[i % 4].button(topic, use_container_width=True, key=f"t_{i}"):
        st.session_state.topic = topic

# Search bar linked to session state
user_input = st.text_input("", value=st.session_state.topic, placeholder="Search specific 2026 trends...")

# --- 3. DATA FETCHING & SEMANTIC ANALYSIS ENGINE ---

# GLOBAL SCOPE DATE LOGIC: Define these here so the Sidebar (Section 4) can always access them
today = datetime.date.today()
start_date = today - datetime.timedelta(days=30)

# Ensure our search window stays within the year 2026
if start_date.year < 2026:
    start_date = today.replace(month=1, day=1)

if user_input:
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": user_input,
        "from": start_date.isoformat(),
        "sortBy": "relevancy",
        "language": "en",
        "apiKey": MY_API_KEY
    }
    
    with st.spinner("AI Analysis in progress..."):
        try:
            response = requests.get(url, params=params)
            data = response.json()

            if data.get("status") == "ok" and data.get("articles"):
                articles = data['articles']
                titles = [a['title'] for a in articles]
                
                # TF-IDF & Cosine Similarity Pipeline
                vec = TfidfVectorizer(stop_words='english')
                mtx = vec.fit_transform([user_input] + titles)
                scores = cosine_similarity(mtx[0:1], mtx[1:]).flatten()
                
                st.markdown(f"### Results for: **{user_input}**")
                
                # Display Top 5 matches based on highest similarity score
                top_indices = scores.argsort()[-5:][::-1]
                
                for i in top_indices:
                    art = articles[i]
                    st.markdown(f"""<div class="news-card">
                        <span class="score-badge">MATCH: {scores[i]*100:.1f}%</span>
                        <h3 style="margin-top:10px;">{art['title']}</h3>
                        <p style="color: #cbd5e1;">{(art['description'] or 'No summary available')[:200]}...</p>
                        <a href="{art['url']}" target="_blank" style="color: #38bdf8; font-weight: bold; text-decoration: none;">Read More →</a>
                    </div>""", unsafe_allow_html=True)
            
            elif data.get("status") == "error":
                st.error(f"API Error: {data.get('message')}")
            else: 
                st.warning(f"No news found for '{user_input}' in the last 30 days.")

        except Exception as e: 
            st.error(f"Connection error: {e}")
else:
    st.markdown("<br><p style='text-align:center; color:#94a3b8;'>Select a trending topic above or type a keyword to begin.</p>", unsafe_allow_html=True)

# --- 4. OPTIONAL FOOTER ---
with st.sidebar:
    st.title("About Pulse")
    st.info("Pulse uses Scikit-Learn to perform real-time semantic analysis.")
    # start_date and today are now guaranteed to be defined above
    st.caption(f"Data Window: {start_date.strftime('%b %d')} - {today.strftime('%b %d, %Y')}")
