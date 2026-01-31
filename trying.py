import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- THEME SWITCH ----------------
theme = st.sidebar.selectbox("Choose Theme", ["Dark", "Light"])

if theme == "Dark":
    bg_color = "#0f172a"
    card_color = "#020617"
    text_color = "#e5e7eb"
    accent = "#38bdf8"
else:
    bg_color = "#f8fafc"
    card_color = "#ffffff"
    text_color = "#020617"
    accent = "#2563eb"

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Interactive Researcher Portfolio",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(f"""
<style>
body {{
    background-color: {bg_color};
    color: {text_color};
}}
h1, h2, h3 {{
    color: {accent};
}}
.card {{
    background-color: {card_color};
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 0 20px rgba(0,0,0,0.15);
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
</style>
""", unsafe_allow_html=True)

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

# ---------------- HOME ----------------
if page == "Home":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.image("profile.jpg", width=200)
    st.title("MMATSIE SARA BOPAPE")
    st.subheader("Computer Science Researcher | Cybersecurity & Data Science")
    st.write("""
    I am a final-year Computer Science student at **Walter Sisulu University**
    with strong interests in **cybersecurity**, **data science**, and
    building secure, data-driven systems that solve real-world problems.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- JOURNEY ----------------
elif page == "Research Journey":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Research Journey")
    st.markdown("""
    **2023** – Started BSc in Computer Science  
    **2024** – Developed interest in cybersecurity & data analysis  
    **2025** – Built data-driven and Streamlit applications  
    **2026** – Aspiring cybersecurity & data science researcher
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PURPOSE ----------------
elif page == "Purpose & Philosophy":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Problem I Want to Solve")
    st.write("""
    Many students and communities lack access to reliable career guidance
    and secure digital platforms. I aim to build **secure, intelligent,
    and data-driven systems** that support informed decision-making.
    """)
    st.header("Research Philosophy")
    st.write("""
    I believe technology should be **ethical**, **secure**, and **data-informed**.
    Combining cybersecurity and data science allows systems to be both
    intelligent and trustworthy.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif page == "Projects":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Academic Projects")
    st.markdown("""
    **Career Guidance Decision Support System**  
    - Uses learner marks and career interests  
    - Applies data analysis for recommendations  
    - Built using Python & Streamlit  

    **Cybersecurity Case Study Analysis**  
    - Analysed real-world cyber attacks  
    - Identified threats and vulnerabilities  
    - Proposed mitigation strategies
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DATA SCIENCE ----------------
elif page == "Data Science Insights":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Data Science Example")
    data = {"Field": ["IT", "Engineering", "Health", "Education", "Business"],
            "Interest (%)": [30, 25, 20, 15, 10]}
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Field"))
    st.caption("Example of how data informs career guidance decisions.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SKILLS ----------------
elif page == "Skills":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Skills")
    skills = ["Python", "Data Science", "Cybersecurity", "Research", "Problem Solving"]
    values = [85, 80, 75, 70, 90]
    fig, ax = plt.subplots()
    ax.bar(skills, values)
    ax.set_ylim(0, 100)
    st.pyplot(fig)
    for s in skills:
        st.markdown(f"<span class='badge'>{s}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- AI ----------------
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
            st.success("I am a Computer Science student focused on secure, data-driven solutions.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FUTURE ----------------
elif page == "Future Research":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Future Research Questions")
    st.markdown("""
    - How can data science improve career guidance accuracy?
    - How can secure systems protect learner data?
    - How can AI support education equity?
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif page == "Contact":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("📫 Contact")
    st.write("Walter Sisulu University")
    st.write("Computer Science Department")
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("© 2026 | Interactive Researcher Portfolio")
