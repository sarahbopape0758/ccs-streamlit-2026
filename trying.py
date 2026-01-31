# app_streamlit_native.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# ---------------- THEME SWITCH ----------------
theme = st.sidebar.selectbox("Choose Theme", ["Dark", "Light"])

if theme == "Dark":
    bg_color = "#0f172a"
    text_color = "#e5e7eb"
    accent = "#38bdf8"
    chart_bg = "#0f172a"
else:
    bg_color = "#f8fafc"
    text_color = "#020617"
    accent = "#2563eb"
    chart_bg = "#ffffff"

st.markdown(f"""
<style>
body {{background-color: {bg_color}; color: {text_color};}}
</style>
""", unsafe_allow_html=True)

# ---------------- PROFILE ----------------
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
    "projects_folder": "projects",
    "future_research": [
        "Improve accuracy of career guidance using AI",
        "Protect learner data with secure systems",
        "Use AI to support education equity"
    ]
}

# ---------------- LOAD IMAGE ----------------
def load_image(path):
    if os.path.exists(path):
        return Image.open(path)
    else:
        st.warning(f"Image not found: {path}")
        return None

# ---------------- PLOT SKILLS ----------------
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

# ---------------- LOAD PROJECTS ----------------
def load_projects(folder):
    projects = []
    if os.path.exists(folder):
        for f in os.listdir(folder):
            if f.endswith(".txt"):
                title = f.replace(".txt","").replace("_"," ").title()
                desc = open(os.path.join(folder,f)).read()
                image_file = os.path.join(folder, f.replace(".txt",".jpg"))
                projects.append({"title":title,"desc":desc,"image":image_file})
    return projects

# ---------------- SIDEBAR NAV ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Explore", ["Home","Journey","Projects","Skills","AI Q&A","Future Research","Contact"])

# ---------------- PAGES ----------------
if page=="Home":
    img = load_image(profile["profile_image"])
    if img: st.image(img, width=200)
    st.title(profile["name"])
    st.subheader(profile["title"])
    st.write(profile["bio"])

elif page=="Journey":
    st.header("Research Journey")
    for item in profile["journey"]:
        with st.container():
            st.markdown(f"- {item}")

elif page=="Projects":
    st.header("Projects")
    projects = load_projects(profile["projects_folder"])
    for p in projects:
        with st.container():
            st.subheader(p["title"])
            if os.path.exists(p["image"]):
                st.image(load_image(p["image"]), width=300)
            st.write(p["desc"])
            st.divider()

elif page=="Skills":
    st.header("Skills")
    st.pyplot(plot_skills(profile["skills"]))
    for skill in profile["skills"]:
        st.markdown(f"`{skill}`", unsafe_allow_html=True)

elif page=="AI Q&A":
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

elif page=="Future Research":
    st.header("Future Research")
    for f in profile["future_research"]:
        st.markdown(f"- {f}")

elif page=="Contact":
    st.header("Contact")
    st.write("Walter Sisulu University")
    st.write("Computer Science Department")

st.caption("© 2026 | MMATSIE SARA BOPAPE | Interactive Portfolio")

