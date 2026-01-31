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
.stFileUploader label, .stFileUploader span, .stFileUploader small {{ color: inherit !important; }}
.stFileUploader div {{ background-color: #0f172a !important; border-radius:12px; }}
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

# ------------------ HERO (HOME ONLY) ------------------

# ------------------ HOME ------------------
if section == "Home":
    st.markdown("""
    <div class=\"hero\">
      <h1>Mmatsie Sara Bopape</h1>
      <h3>Cybersecurity Enthusiast & Final-Year Computer Science Student</h3>
      <p style=\"max-width:850px\">
      Final year BSc Computer Science student at Walter Sisulu University, passionate about cybersecurity,
      networking, and building innovative solutions to complex security challenges.
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class=\"card\">
    <h2>Welcome</h2>
    <p>
    This interactive portfolio showcases my academic journey, technical skills, certifications,
    and projects in cybersecurity, networking, and software development.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class=\"card kpi\">
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

    # Predefined Q&A knowledge base
    knowledge = {
        "who is sarah": "Mmatsie Sara Bopape is a final-year BSc Computer Science student at Walter Sisulu University with a strong interest in cybersecurity and networking.",
        "who is mmatsie": "Mmatsie Sara Bopape is a cybersecurity enthusiast and final-year Computer Science student at Walter Sisulu University.",
        "when did she matriculate": "She matriculated in 2022 at Eqinisweni Secondary School.",
        "what does she study": "She studies BSc Computer Science at Walter Sisulu University.",
        "what are her skills": "Her skills include cybersecurity fundamentals, networking, programming (C++, Java, Python, JavaScript), and Linux.",
    }

    if "chat" not in st.session_state:
        st.session_state.chat = []

    for role, msg in st.session_state.chat:
        st.markdown(f'<div class="message {role}">{msg}</div>', unsafe_allow_html=True)

    q = st.text_input("Ask about my skills, education, or background")

    if st.button("Send") and q:
        st.session_state.chat.append(("user", q))
        key = q.lower().strip()

        answer = None
        for k in knowledge:
            if k in key:
                answer = knowledge[k]
                break

        if answer is None:
            answer = (
                "This question is best directed to Sarah herself. "
                "For more information, please contact her at "
                "📧 bopapesarah2324@gmail.com or connect via LinkedIn/GitHub listed in this portfolio."
            )

        st.session_state.chat.append(("ai", answer))
        st.rerun()

# ------------------ GAME ------------------

elif section == "Game":
    st.markdown("## 🎉 Cyber Card Match vs AI 🎉")
    st.write("A secret card is drawn. Choose a number (1–13). You **can win** — and when you do, enjoy the celebration! 🎈")

    # Initialize game state
    if "secret_card" not in st.session_state:
        st.session_state.secret_card = random.randint(1, 13)
        st.session_state.played = False
        st.session_state.win = False

    guess = st.number_input("Pick your card number", min_value=1, max_value=13, step=1)

    if st.button("Reveal Card") and not st.session_state.played:
        st.session_state.played = True

        # Friendly logic: slightly increases chance to win
        if random.random() < 0.5:
            st.session_state.secret_card = guess

        st.write(f"The AI card number is **{st.session_state.secret_card}**")

        if guess == st.session_state.secret_card:
            st.session_state.win = True
            st.balloons()
            st.success("🎊 Congratulations! You won! Your cyber instincts are strong 🛡️✨")
        else:
            st.info("So close! Try again — champions never quit 💪")

    if st.button("Play Again"):
        st.session_state.secret_card = random.randint(1, 13)
        st.session_state.played = False
        st.session_state.win = False
        st.rerun()

# ------------------ FOOTER ------------------


st.markdown(f"""
<footer>
© 2026 Mmatsie Sara Bopape • Cybersecurity Portfolio
</footer>
""", unsafe_allow_html=True)
