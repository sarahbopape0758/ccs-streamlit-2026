# css2026-sarah-bopape-portfolio
# Ultimate Streamlit Portfolio for Mmatsie Sara Bopape

import streamlit as st
import random
from datetime import datetime
import plotly.graph_objects as go
import base64

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
    section = st.radio("Navigate", ["Home", "About", "Projects", "Skills", "CV", "Ask Me", "Game", "Tools", "Timeline", "Badges"])

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
    
    # Interactive Hill Cipher demo
    st.markdown("<h4>Try a quick encryption demo:</h4>", unsafe_allow_html=True)
    msg = st.text_input("Message to encrypt")
    key = st.number_input("Shift key (1-25)", 1, 25, 3)
    if st.button("Encrypt") and msg:
        encrypted = ''.join([chr(((ord(c)-65+key)%26)+65) if c.isupper() else
                             chr(((ord(c)-97+key)%26)+97) if c.islower() else c for c in msg])
        st.success(f"Encrypted message: {encrypted}")

# ------------------ SKILLS ------------------
elif section == "Skills":
    st.markdown("<h2>My Skills</h2>", unsafe_allow_html=True)

    categories = ['Python', 'Java', 'C++', 'Networking', 'Linux', 'Cybersecurity']
    values = [90, 70, 80, 85, 75, 95]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=values, theta=categories, fill='toself', name='Skill Level'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,100])))
    st.plotly_chart(fig, use_container_width=True)

# ------------------ CV ------------------
elif section == "CV":
    st.markdown("## Download My CV")
    st.markdown(
        "<div class='card'>My CV is available below. Click the button to download it.</div>",
        unsafe_allow_html=True,
    )
    try:
        with open("Mmatsie_Sara_Bopape_CV.pdf", "rb") as f:
            cv_bytes = f.read()
        st.download_button(
            label="📄 Download CV (PDF)",
            data=cv_bytes,
            file_name="Mmatsie_Sara_Bopape_CV.pdf",
            mime="application/pdf",
        )
    except FileNotFoundError:
        st.error("CV file not found. Please include it in the project folder.")

# ------------------ CHAT ------------------
elif section == "Ask Me":
    st.markdown("## Ask Me Anything")
    knowledge = {
        "who is sarah": "Mmatsie Sara Bopape is a final-year BSc Computer Science student at Walter Sisulu University with a strong interest in cybersecurity and networking.",
        "who is mmatsie": "Mmatsie Sara Bopape is a cybersecurity enthusiast and final-year Computer Science student at Walter Sisulu University.",
        "when did she matriculate": "She matriculated in 2022 at Eqinisweni Secondary School.",
        "what does she study": "She studies BSc Computer Science at Walter Sisulu University.",
        "what are her skills": "Her skills include cybersecurity fundamentals, networking, programming (C++, Java, Python, JavaScript), and Linux.",
        "what is cybersecurity": "Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks."
    }
    if "chat" not in st.session_state: st.session_state.chat=[]
    for role, msg in st.session_state.chat:
        st.markdown(f'<div class="message {role}">{msg}</div>', unsafe_allow_html=True)
    q = st.text_input("Ask a cybersecurity question or about me")
    if st.button("Send") and q:
        st.session_state.chat.append(("user", q))
        answer = next((knowledge[k] for k in knowledge if k in q.lower()), 
                      "This question is best directed to Sarah. Contact: 📧 bopapesarah2324@gmail.com")
        st.session_state.chat.append(("ai", answer))
        st.rerun()

# ------------------ GAME ------------------
elif section == "Game":
    st.markdown("## 🎉 Cyber Card Match / Mini CTF 🎉")
    if "secret_card" not in st.session_state:
        st.session_state.secret_card=random.randint(1,13)
        st.session_state.played=False
        st.session_state.win=False
        st.session_state.reveal_clicked=False
    guess = st.number_input("Pick your card number (1–13)", 1, 13)
    if st.button("Reveal Card"):
        st.session_state.reveal_clicked=True
        if random.random()<0.5: st.session_state.secret_card=guess
        st.session_state.played=True
    if st.session_state.reveal_clicked and st.session_state.played:
        st.write(f"The AI card number is **{st.session_state.secret_card}**")
        if guess==st.session_state.secret_card:
            st.session_state.win=True
            st.balloons()
            st.success("🎊 You won! Your cyber instincts are strong 🛡️✨")
        else:
            st.info("So close! Try again 💪")
    if st.button("Play Again"):
        st.session_state.secret_card=random.randint(1,13)
        st.session_state.played=False
        st.session_state.win=False
        st.session_state.reveal_clicked=False
        st.rerun()

# ------------------ TOOLS ------------------
elif section=="Tools":
    st.markdown("## 🔧 Cybersecurity Tools & Demos")
    # Hashing demo
    msg = st.text_input("Enter text to hash (SHA256)")
    if st.button("Hash Text") and msg:
        import hashlib
        h = hashlib.sha256(msg.encode()).hexdigest()
        st.success(f"SHA256 Hash: {h}")

# ------------------ TIMELINE ------------------
elif section=="Timeline":
    st.markdown("## 📅 My Journey")
    timeline_events = [
        ("2022", "Matriculated at Eqinisweni Secondary School"),
        ("2023", "Started BSc Computer Science"),
        ("2024", "First Internship / Project"),
        ("2025", "Tutor & IEC Assistant"),
        ("2026", "Final Year & Portfolio Showcase")
    ]
    for year, event in timeline_events:
        st.markdown(f"**{year}** — {event}")

# ------------------ BADGES ------------------
elif section=="Badges":
    st.markdown("## 🏆 Earn Your Badge")
    badge_text = "Visited Sara's Cybersecurity Portfolio"
    if st.button("Download Badge"):
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGB', (400,200), color=(44,62,80))
        d = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        d.text((20,80), badge_text, fill=(255,255,255), font=font)
        import io
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        st.download_button("Download PNG", buf.getvalue(), file_name="badge.png", mime="image/png")

# ------------------ FOOTER ------------------
st.markdown(f"""
<footer>
© 2026 Mmatsie Sara Bopape • Cybersecurity Portfolio
</footer>
""", unsafe_allow_html=True)
