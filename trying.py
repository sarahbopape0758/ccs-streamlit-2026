# css2026-sarah-bopape-portfolio
# Premium Streamlit portfolio for Mmatsie Sara Bopape

import streamlit as st
import time
import random
from datetime import datetime

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Mmatsie Sara Bopape | Cybersecurity Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------ THEME TOGGLE ------------------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

THEMES = {
    "dark": {
        "bg": "#0b0f14",
        "text": "#e6e8eb",
        "muted": "#9aa4b2",
        "accent": "#7c9cff",
        "accent2": "#22d3ee",
        "card": "#0f172a",
        "shadow": "0 20px 40px rgba(0,0,0,.45)",
    },
    "light": {
        "bg": "#f8fafc",
        "text": "#0f172a",
        "muted": "#475569",
        "accent": "#4f46e5",
        "accent2": "#06b6d4",
        "card": "#ffffff",
        "shadow": "0 20px 40px rgba(2,6,23,.15)",
    },
}

T = THEMES[st.session_state.theme]

# ------------------ GLOBAL CSS ------------------
st.markdown(f"""
<style>
html, body, .stApp {{ background:{T['bg']}; color:{T['text']}; }}

.hero {{
  border-radius:24px; padding:40px;
  background: radial-gradient(800px 400px at 10% -20%, rgba(124,156,255,.18), transparent 40%),
              radial-gradient(800px 400px at 90% -10%, rgba(34,211,238,.18), transparent 40%);
  box-shadow:{T['shadow']};
}}

.card {{
  background:{T['card']};
  border-radius:20px; padding:22px;
  box-shadow:{T['shadow']}; margin-bottom:20px;
}}

.kpi {{ display:flex; gap:14px; }}
.kpi div {{ flex:1; padding:16px; border-radius:16px; background:rgba(124,156,255,.12); }}

.chat {{ height:420px; overflow-y:auto; }}
.message.user {{ background:rgba(124,156,255,.15); padding:12px; border-radius:14px; margin-bottom:10px; }}
.message.ai {{ background:rgba(34,211,238,.15); padding:12px; border-radius:14px; margin-bottom:10px; }}

footer {{ text-align:center; color:{T['muted']}; padding:20px; }}
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    if st.button("Toggle Dark / Light 🌗"):
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
        st.rerun()

    st.markdown("---")
    section = st.radio("Navigate", ["Home", "About", "Projects", "Skills", "CV", "Ask Me", "Game"])

# ------------------ HERO ------------------
st.markdown("""
<div class="hero">
  <h1>Mmatsie Sara Bopape</h1>
  <h3>Cybersecurity Enthusiast & Final-Year Computer Science Student</h3>
  <p style="max-width:850px">
  Final year BSc Computer Science student at Walter Sisulu University, passionate about cybersecurity,
  networking, and building innovative solutions to complex security challenges.
  </p>
</div>
""", unsafe_allow_html=True)

# ------------------ HOME ------------------
if section == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="card">
        <h2>Welcome</h2>
        <p>
        This interactive portfolio showcases my academic journey, technical skills, certifications,
        and projects in cybersecurity, networking, and software development.
        </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card kpi">
          <div><h3>2026</h3><p>Final Year</p></div>
          <div><h3>10+</h3><p>Certifications</p></div>
          <div><h3>6+</h3><p>Languages</p></div>
        </div>
        """, unsafe_allow_html=True)

# ------------------ ABOUT ------------------
elif section == "About":
    st.markdown("""
    <div class="card">
    <h2>Education</h2>
    <b>BSc Computer Science</b> — Walter Sisulu University (2022–2026)<br>
    Modules: Data Structures, Computer Architecture, Operating Systems, Networking,
    Mathematics, Web Development, Software Engineering
    <hr>
    <b>Grade 12</b> — Eqinisweni Secondary School (2022)
    </div>

    <div class="card">
    <h2>Experience</h2>
    <b>Tutor</b> — Walter Sisulu University (Jan 2025 – Nov 2025)<br>
    • Teaching Linear Programming & Applied Computing<br>
    • Exam preparation and student support<br>
    <br>
    <b>IEC Digital Registration Assistant</b> (Aug 2025 – Sep 2025)<br>
    • Assisted community members with voter registration<br>
    • Improved digital literacy and ensured data accuracy
    </div>
    """, unsafe_allow_html=True)

# ------------------ PROJECTS ------------------
elif section == "Projects":
    st.markdown("""
    <div class="card">
    <h3>Smart Lecturer Scheduling & Navigation System</h3>
    React web app helping students check lecturer availability and campus directions.
    </div>
    <div class="card">
    <h3>Hill Cipher Encryption / Decryption Tool</h3>
    Cryptography tool using matrix mathematics and modular arithmetic.
    </div>
    """, unsafe_allow_html=True)

# ------------------ SKILLS ------------------
elif section == "Skills":
    st.markdown("""
    <div class="card">
    <h3>Programming</h3>
    C++, Java, JavaScript, Python, HTML, CSS
    </div>
    <div class="card">
    <h3>Tools & Technologies</h3>
    GitHub, Linux CLI, Cisco Packet Tracer, Wireshark
    </div>
    <div class="card">
    <h3>Languages</h3>
    Sepedi (Native), English, Zulu, Xhosa, Venda, Tsonga
    </div>
    """, unsafe_allow_html=True)

# ------------------ CV ------------------
elif section == "CV":
    st.markdown("## Download My CV")
    cv = st.file_uploader("Upload your CV PDF", type=["pdf"])
    if cv:
        st.download_button("Download CV", cv, file_name="Mmatsie_Sara_Bopape_CV.pdf")

# ------------------ CHAT ------------------
elif section == "Ask Me":
    st.markdown("## Ask Me Anything")
    if "chat" not in st.session_state:
        st.session_state.chat = []

    for role, msg in st.session_state.chat:
        st.markdown(f'<div class="message {role}">{msg}</div>', unsafe_allow_html=True)

    q = st.text_input("Ask about my skills, projects, or cybersecurity interests")
    if st.button("Send") and q:
        st.session_state.chat.append(("user", q))
        st.session_state.chat.append(("ai", "I am passionate about cybersecurity, networking, and secure systems design."))
        st.rerun()

# ------------------ GAME ------------------
elif section == "Game":
    st.markdown("## Cyber Cards vs AI")
    st.write("Draw a card. Highest number wins against the AI.")
    if st.button("Draw Card"):
        user = random.randint(1, 13)
        ai = random.randint(1, 13)
        st.write(f"You drew **{user}** | AI drew **{ai}**")
        if user > ai:
            st.success("You win! 🏆")
        elif user < ai:
            st.error("AI wins 🤖")
        else:
            st.info("Draw!")

# ------------------ FOOTER ------------------
st.markdown(f"""
<footer>
© {datetime.now().year} Mmatsie Sara Bopape • Cybersecurity Portfolio
</footer>
""", unsafe_allow_html=True)
