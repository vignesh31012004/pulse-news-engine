# 📡 Pulse: Semantic Data Discovery Engine

**Developed by:** `Vignesh Cheni`  
**Project Focus:** *Machine Learning & Real-Time Data Flow*

---

## 📖 Project Case Study: Engineering Pulse

The goal of **Pulse** was to move beyond static keyword searches. I built a system that combines **real-time data streams** with **content-based filtering** to provide high-precision news discovery for the 2026 tech landscape.

### ⚙️ The Engineering Workflow

* **Stream Integration:** Established a **RESTful connection** to fetch live technology metadata via **NewsAPI**.
* **Semantic Modeling:** Built a recommendation engine using **Machine Learning** to rank articles by contextual relevance rather than just word frequency.
* **Secure Deployment:** Configured a **"frictionless" cloud environment** using **Streamlit Secrets** to manage API credentials securely while providing a public-facing demo.
* **UI Injection:** Overrode standard framework constraints with **custom CSS** to create a high-contrast **Glassmorphism** interface.

---

## 🛠️ The Tech Stack

### 1. 🌐 Live Data Stream (NewsAPI)
Pulse acts as a consumer for the **NewsAPI data stream**, processing headlines from over **80,000 global sources** in real-time. This ensures that the platform always reflects the current state of the industry.

### 2. 🤖 Machine Learning Logic (Scikit-Learn)
The core of the discovery engine relies on two mathematical models:

* **TF-IDF Vectorization:** *(Term Frequency-Inverse Document Frequency)* This model calculates the statistical weight of every term in the data stream. It automatically suppresses "noise" words and amplifies **"signal"** terms (e.g., *Quantum Computing* or *Solid-state battery*).
* **Cosine Similarity:** The engine maps the user’s query into a **multi-dimensional vector space** and calculates the mathematical distance between that query and the news articles to find the closest contextual matches.



---

## 🧠 Under the Hood: The Data Flow

### **Phase 1: Data Retrieval** 📥
When a user interacts with the interface, the app triggers a data request. To ensure a **Zero-Friction experience**, I configured the app to pull my developer credentials from an **encrypted environment vault**. The user sees the results instantly without needing their own API key.

### **Phase 2: Text Processing & Scoring** 📊
The data is processed through our **ML logic**:

1.  **Tokenization:** The text is broken down into structured data points.
2.  **Vector Mapping:** Every headline is converted into a **numerical vector**.
3.  **Similarity Calculation:** The engine computes a **Relevance Score** based on the vector's angle. This allows Pulse to surface articles that are contextually related even if they don't share the exact keywords typed by the user.



### **Phase 3: High-Contrast Interface** 🎨
The visual layer uses **CSS Injection** to achieve a modern, futuristic look:

* **Backdrop Filter:** `blur(15px)` for a frosted-glass aesthetic.
* **Responsive Grid:** Custom **Flexbox CSS** to ensure trending buttons stay perfectly aligned across mobile and desktop.

---

## 🚀 Live Demo

**[Experience Pulse by Vignesh Cheni]**