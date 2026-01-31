# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from PIL import Image

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

# ---------------- GLOBAL CSS ----------------
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
}}
</style>
""", unsafe_allow_html=True)

# ---------------- PORTFOLIO DATA ----------------
profile_info = {
    "name": "MMATSIE SARA BOPAPE",
    "title": "Computer Science Researcher | Cybersecurity & Data Science",
    "university": "Walter Sisulu University",
    "bio": (
        "Final-year Computer Science student with strong interests in "
        "cybersecurity, data science, and building secure, data-driven systems "
        "that solve real-world problems."
    ),
    "skills": {
        "Python": 85,
        "Data Science": 80,
        "Cybersecurity": 75,
        "Research": 70,
        "Problem Solving": 90
    },
    "projects": [
        {
            "title": "Career Guidance Decision Support System",
            "desc": "Uses learner marks and career interests to provide recommendations. Built using Python & Streamlit."
        },
        {
            "title": "Cybersecurity Case Study Analysis",
            "desc": "Analysed real-world cyber attacks, identified threats and vulnerabilities, and proposed mitigation strategies."
        }
    ],
    "research_journey": [
        "2023 – Started BSc in Computer Science",
        "2024 – Developed interest in cybersecurity & data analysis",
        "2025 – Built data-driven and Streamlit applications",
        "2026 – Aspiring cybersecurity & data science researcher"
    ],
    "future_questions": [
        "How can data science improve career guidance accuracy?",
        "How can secure systems protect learner data?",
        "How can AI support education equity?"
    ]
}

# ---------------- SIDEBAR NAV ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Explore",
    [
        "Home",
        "Research Journey",
        "Purpose & Philosophy",
        "Projects",
        "Data Science Insights",
        "Skills",
        "AI: Ask About Me",
        "Future Research",
        "Contact"
    ]
)

# ---------------- FUNCTION TO LOAD IMAGE ----------------
def load_image(path):
    try:
        img = Image.open(path)
        return img
    except Exception:
        st.error(f"Profile image not found at {path}")
        return None

# ---------------- FUNCTION TO PLOT SKILLS ----------------
def plot_skills(skills_dict):
    skills = list(skills_dict.keys())
    values = list(skills_dict.values())
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    ax.bar(skills, values, color=accent)
    ax.set_ylim(0, 100)
    ax.tick_params(colors=text_color, labelcolor=text_color)
    for spine in ax.spines.values():
        spine.set_edgecolor(text_color)
    return fig

# ---------------- PAGES ----------------
if page == "Home":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    profile_img = load_image("profile.jpg")
    if profile_img:
        st.image(profile_img, width=200)
    st.title(profile_info["name"])
    st.subheader(profile_info["title"])
    st.write(profile_info["bio"])
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Research Journey":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Research Journey")
    for item in profile_info["research_journey"]:
        st.write(item)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Purpose & Philosophy":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Problem I Want to Solve")
    st.write(
        "Many students and communities lack access to reliable career guidance "
        "and secure digital platforms. I aim to build secure, intelligent, "
        "and data-driven systems that support informed decision-making."
    )
    st.header("Research Philosophy")
    st.write(
        "I believe technology should be ethical, secure, and data-informed. "
        "Combining cybersecurity and data science allows systems to be both "
        "intelligent and trustworthy."
    )
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Projects":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Projects")
    for p in profile_info["projects"]:
        st.subheader(p["title"])
        st.write(p["desc"])
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Data Science Insights":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Data Science Example")
    data = {"Field": ["IT", "Engineering", "Health", "Education", "Business"],
            "Interest (%)": [30, 25, 20, 15, 10]}
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Field"), use_container_width=True)
    st.caption("Example of how data informs career guidance decisions.")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Skills":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Skills")
    fig = plot_skills(profile_info["skills"])
    st.pyplot(fig)
    for s in profile_info["skills"]:
        st.markdown(f"<span class='badge'>{s}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "AI: Ask About Me":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Ask Me Anything")
    q = st.text_input("Ask a question about my work")
    if q:
        q = q.lower()
        if "data" in q:
            st.success("I use data science to analyse patterns and support evidence-based decisions.")
        elif "cyber" in q:
            st.success("Cybersecurity ensures the systems I build are secure and trustworthy.")
        else:
            st.info("Hmm… this is a question outside my current answers. Sarah will personally reply to this question soon! ✨")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Future Research":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Future Research Questions")
    for q in profile_info["future_questions"]:
        st.write(f"- {q}")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Contact":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("📫 Contact")
    st.write("Walter Sisulu University")
    st.write("Computer Science Department")
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("© 2026 | MMATSIE SARA BOPAPE | Interactive Researcher Portfolio")

