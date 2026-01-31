# dynamic_portfolio.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# ---------------- THEME SWITCH ----------------
theme = st.sidebar.selectbox("Choose Theme", ["Dark", "Light"])

if theme == "Dark":
    bg_color = "#0f172a"
    card_color = "#020617"
    text_color = "#e5e7eb"
    accent = "#38bdf8"
    chart_bg = "#0f172a"
else:
    bg_color = "#f8fafc"
    card_color = "#ffffff"
    text_color = "#020617"
    accent = "#2563eb"
    chart_bg = "#ffffff"

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MMATSIE SARA BOPAPE Portfolio",
    page_icon="💻",
    layout="wide",
)

# ---------------- CSS ----------------
st.markdown(f"""
<style>
body {{
    background-color: {bg_color};
    color: {text_color};
    font-family: 'Segoe UI', sans-serif;
}}
h1, h2, h3 {{
    color: {accent};
}}
.card {{
    background-color: {card_color};
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(0,0,0,0.2);
    margin-bottom: 25px;
    transition: all 0.3s ease;
}}
.card:hover {{
    box-shadow: 0 0 40px {accent};
}}
.badge {{
    display: inline-block;
    background-color: {bg_color};
    padding: 8px 14px;
    border-radius: 25px;
    margin: 6px;
    color: {accent};
    font-size: 14px;
}}
.stButton>button {{
    background-color: {accent};
    color: {text_color};
    border-radius: 10px;
    padding: 8px 20px;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------
profile = {
    "name": "MMATSIE SARA BOPAPE",
    "title": "Computer Science Researcher | Cybersecurity & Data Science",
    "bio": "Final-year CS student passionate about cybersecurity and data science. Building intelligent, secure, data-driven systems.",
    "profile_image": "profile.jpg",
    "skills": {"Python":85,"Data Science":80,"Cybersecurity":75,"Research":70,"Problem Solving":90},
    "journey": [
        "2023 – Started BSc in Computer Science",
        "2024 – Developed interest in cybersecurity & data analysis",
        "2025 – Built data-driven and Streamlit applications",
        "2026 – Aspiring cybersecurity & data science researcher"
    ],
    "projects_folder": "projects",  # folder with project images + .txt descriptions
    "future_research": [
        "Improve accuracy of career guidance using AI",
        "Protect learner data with secure systems",
        "Use AI to support education equity"
    ]
}

# ---------------- FUNCTIONS ----------------
def load_image(path, width=None):
    if os.path.exists(path):
        return Image.open(path)
    else:
        st.error(f"Image not found: {path}")
        return None

def plot_skills(skills):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    names = list(skills.keys())
    vals = list(skills.values())
    ax.bar(names, vals, color=accent)
    ax.set_ylim(0,100)
    ax.tick_params(colors=text_color, labelcolor=text_color)
    for spine in ax.spines.values():
        spine.set_edgecolor(text_color)
    return fig

def load_projects(folder):
    projects = []
    if os.path.exists(folder):
        for f in os.listdir(folder):
            if f.endswith(".txt"):
                title = f.replace(".txt","").replace("_"," ").title()
                desc = open(os.path.join(folder,f), "r").read()
                image_file = os.path.join(folder, f.replace(".txt",".jpg"))
                projects.append({"title":title,"desc":desc,"image":image_file})
    return projects

# ---------------- SIDEBAR NAV ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Explore", ["Home","Journey","Projects","Skills","AI Q&A","Future Research","Contact"])

# ---------------- PAGES ----------------
if page=="Home":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    img = load_image(profile["profile_image"],200)
    if img: st.image(img, width=200)
    st.title(profile["name"])
    st.subheader(profile["title"])
    st.write(profile["bio"])
    st.markdown("</div>", unsafe_allow_html=True)

elif page=="Journey":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Research Journey")
    for item in profile["journey"]:
        st.write(f"- {item}")
    st.markdown("</div>", unsafe_allow_html=True)

elif page=="Projects":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Projects")
    projects = load_projects(profile["projects_folder"])
    for p in projects:
        st.subheader(p["title"])
        if os.path.exists(p["image"]):
            st.image(load_image(p["image"]), width=300)
        st.write(p["desc"])
    st.markdown("</div>", unsafe_allow_html=True)

elif page=="Skills":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Skills")
    st.pyplot(plot_skills(profile["skills"]))
    for s in profile["skills"]:
        st.markdown(f"<span class='badge'>{s}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page=="AI Q&A":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Ask Me Anything")
    q = st.text_input("Ask a question about my work")
    if q:
        ql = q.lower()
        if "data" in ql:
            st.success("I use data science to analyse patterns and support evidence-based decisions.")
        elif "cyber" in ql:
            st.success("Cybersecurity ensures the systems I build are secure and trustworthy.")
        else:
            st.info("Hmm… this is a question outside my current answers. Sarah will personally reply to this question soon! ✨")
    st.markdown("</div>", unsafe_allow_html=True)

elif page=="Future Research":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Future Research")
    for f in profile["future_research"]:
        st.write(f"- {f}")
    st.markdown("</div>", unsafe_allow_html=True)

elif page=="Contact":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Contact")
    st.write("Walter Sisulu University")
    st.write("Computer Science Department")
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("© 2026 | MMATSIE SARA BOPAPE | Interactive Portfolio")
