# css2026-sarah-bopape-portfolio
# Premium Streamlit portfolio for Mmatsie Sara Bopape - Upgraded

import streamlit as st
import random
import hashlib
from PIL import Image, ImageDraw, ImageFont
import io

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Mmatsie Sara Bopape | Cybersecurity Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------ THEME ------------------
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

.skill-card {{
  display:inline-block; background:{T['accent']}; color:#fff;
  padding:12px 18px; border-radius:12px; margin:5px;
  cursor:default;
}}

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
    st.markdown(f"""
    <div class="hero">
      <h1>Mmatsie Sara Bopape</h1>
      <h3>Cybersecurity Enthusiast & Final-Year Computer Science Student</h3>
      <p style="max-width:850px">
      Final year BSc Computer Science student at Walter Sisulu University, passionate about cybersecurity,
      networking, and building innovative solutions to complex security challenges.
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
      <h2>Welcome</h2>
      <p>This interactive portfolio showcases my academic journey, technical skills, certifications,
      and projects in cybersecurity, networking, and software development.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
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
      • Exam preparation and student support<br><br>
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
      Cryptography tool using a Caesar Cipher (shift letters by a fixed key).
    </div>
    """, unsafe_allow_html=True)

    # Encryption / Decryption Demo
    st.markdown("<h4>Try a quick encryption & decryption demo:</h4>", unsafe_allow_html=True)
    msg = st.text_input("Message")
    key = st.number_input("Shift key (1-25)", 1, 3)
    col1, col2 = st.columns(2)
    if col1.button("Encrypt"):
        encrypted = ''.join([chr(((ord(c)-65+key)%26)+65) if c.isupper() else
                             chr(((ord(c)-97+key)%26)+97) if c.islower() else c for c in msg])
        st.success(f"Encrypted message: {encrypted}")
        st.info("This demonstrates a Caesar cipher shift. Letters are shifted by the key.")
    if col2.button("Decrypt"):
        decrypted = ''.join([chr(((ord(c)-65-key)%26)+65) if c.isupper() else
                             chr(((ord(c)-97-key)%26)+97) if c.islower() else c for c in msg])
        st.success(f"Decrypted message: {decrypted}")
        st.info("Decryption reverses the shift to reveal the original message.")

# ------------------ SKILLS ------------------
elif section == "Skills":
    st.markdown("<h2>My Skills</h2>", unsafe_allow_html=True)
    skills = {
        "Python": "Used for automation, scripts, and cybersecurity tools.",
        "Java": "Experience in OOP and building desktop/web apps.",
        "C++": "Strong understanding of algorithms and system programming.",
        "Networking": "Knowledge of TCP/IP, routing, switching, Packet Tracer.",
        "Linux": "Proficient in CLI, Bash scripting, and server management.",
        "Cybersecurity": "Skills in cryptography, hashes, vulnerability testing."
    }
    for skill, desc in skills.items():
        st.markdown(f'<div class="skill-card" title="{desc}">{skill}</div>', unsafe_allow_html=True)

# ------------------ CV ------------------
elif section == "CV":
    st.markdown("## Download My CV")
    st.markdown("<div class='card'>Click below to download my CV.</div>", unsafe_allow_html=True)
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
        st.error("CV file not found. Include it in the project folder.")

# ------------------ CHAT ------------------
elif section == "Ask Me":
    st.markdown("## Ask Me Anything")
    knowledge = {
        "who is sarah": "Mmatsie Sara Bopape is a final-year BSc Computer Science student.",
        "who is mmatsie": "Cybersecurity enthusiast and final-year Computer Science student.",
        "when did she matriculate": "Matriculated in 2022 at Eqinisweni Secondary School.",
        "what does she study": "BSc Computer Science at Walter Sisulu University.",
        "what are her skills": "Cybersecurity, networking, C++, Java, Python, JavaScript, Linux.",
    }
    if "chat" not in st.session_state: st.session_state.chat=[]
    for role, msg in st.session_state.chat:
        st.markdown(f'<div class="message {role}">{msg}</div>', unsafe_allow_html=True)
    q = st.text_input("Ask a question about me or cybersecurity")
    if st.button("Send") and q:
        st.session_state.chat.append(("user", q))
        answer = next((knowledge[k] for k in knowledge if k in q.lower()), 
                      "Please contact Sara: bopapesarah2324@gmail.com")
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
            for _ in range(3): st.balloons()
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
    st.markdown("### SHA256 Hash Generator\nSHA256 creates a secure hash, used for password protection, digital signatures, and data integrity.")
    msg = st.text_input("Enter text to hash (SHA256)")
    if st.button("Hash Text") and msg:
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
        if st.button(f"Celebrate {year} milestone"):
            st.balloons()
            st.success(f"🎉 Milestone {year} celebrated!")

# ------------------ BADGES / CERTIFICATES ------------------
elif section=="Badges":
    st.markdown("## 🏆 Certificates & Badges")
    st.markdown("Click Next / Previous to view your achievements.")

    if "badge_index" not in st.session_state:
        st.session_state.badge_index = 0

    # Example list of badge images + info
    badges = [
        {"img":"cert1.png","name":"Cisco Networking","provider":"Cisco"},
        {"img":"cert2.png","name":"Python for Cybersecurity","provider":"Udemy"},
        {"img":"cert3.png","name":"Linux Fundamentals","provider":"Coursera"}
    ]

    # Load current badge
    badge = badges[st.session_state.badge_index]
    try:
        image = Image.open(badge["img"])
        st.image(image, caption=f'{badge["name"]} — {badge["provider"]}', use_column_width=True)
    except FileNotFoundError:
        st.warning(f"Image {badge['img']} not found. Add it to your project folder.")

    col1, col2 = st.columns(2)
    if col1.button("Previous"):
        st.session_state.badge_index = max(0, st.session_state.badge_index-1)
    if col2.button("Next"):
        st.session_state.badge_index = min(len(badges)-1, st.session_state.badge_index+1)

# ------------------ FOOTER ------------------
st.markdown(f"""
<footer>
© 2026 Mmatsie Sara Bopape • Cybersecurity Portfolio
</footer>
""", unsafe_allow_html=True)
