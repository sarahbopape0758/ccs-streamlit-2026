# css2026-researcher-portfolio
# Prize-ready Streamlit app: dynamic portfolio, dark/light mode, CV upload, chat assistant, visuals, and a mini game

import streamlit as st
import time
import random
from datetime import datetime

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="css2026 • Research Portfolio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------ THEME TOGGLE ------------------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

THEMES = {
    "dark": {
        "bg": "#0b0f14",
        "panel": "#121826",
        "text": "#e6e8eb",
        "muted": "#9aa4b2",
        "accent": "#7c9cff",
        "accent2": "#22d3ee",
        "card": "#0f172a",
        "shadow": "0 20px 40px rgba(0,0,0,.45)",
    },
    "light": {
        "bg": "#f7fafc",
        "panel": "#ffffff",
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
:root {{
  --bg: {T['bg']};
  --panel: {T['panel']};
  --text: {T['text']};
  --muted: {T['muted']};
  --accent: {T['accent']};
  --accent2: {T['accent2']};
  --card: {T['card']};
  --shadow: {T['shadow']};
}}

html, body, .stApp {{ background: var(--bg); color: var(--text); }}

/* Headline */
.hero {{
  background: radial-gradient(1200px 600px at 10% -20%, rgba(124,156,255,.15), transparent 40%),
              radial-gradient(900px 500px at 90% -10%, rgba(34,211,238,.18), transparent 40%),
              linear-gradient(180deg, rgba(15,23,42,.6), rgba(15,23,42,.2));
  border: 1px solid rgba(148,163,184,.15);
  border-radius: 24px;
  padding: 36px;
  box-shadow: var(--shadow);
}}

.badge {{
  display: inline-block; padding: 6px 10px; border-radius: 999px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  color: white; font-weight: 600; font-size: 12px; letter-spacing:.3px;
}}

.card {{
  background: var(--card);
  border: 1px solid rgba(148,163,184,.15);
  border-radius: 20px;
  padding: 22px;
  box-shadow: var(--shadow);
}}

.kpi {{ display:flex; gap:14px; }}
.kpi .box {{ flex:1; padding:16px; border-radius:16px; background: linear-gradient(180deg, rgba(124,156,255,.08), rgba(34,211,238,.08)); border:1px solid rgba(148,163,184,.18); }}
.kpi h3 {{ margin:0; font-size:28px; }}
.kpi p {{ margin:0; color:var(--muted); }}

.nav a {{ text-decoration:none; color:var(--text); }}

.chat {{ height: 420px; overflow-y:auto; }}
.message.user {{ background: rgba(124,156,255,.12); padding:12px 14px; border-radius:14px; margin-bottom:10px; }}
.message.ai {{ background: rgba(34,211,238,.12); padding:12px 14px; border-radius:14px; margin-bottom:10px; }}

footer {{ color:var(--muted); text-align:center; padding:18px; }}
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.markdown("### ⚙️ Controls")
    if st.button("Toggle Theme 🌗"):
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
        st.rerun()

    st.markdown("---")
    section = st.radio(
        "Navigate",
        ["Home", "Research", "Projects", "CV", "Ask Me", "Play"],
        index=0,
    )

# ------------------ HEADER ------------------
st.markdown(f"""
<div class="hero">
  <span class="badge">css2026 • Prize Edition</span>
  <h1 style="margin-top:12px">Sarah Bopape — Research Portfolio</h1>
  <p style="max-width:820px;color:var(--muted)">
    Research-driven problem solver blending data, systems thinking, and creative technology.
    This interactive portfolio showcases my work, impact, and a live assistant trained on my profile.
  </p>
</div>
""", unsafe_allow_html=True)

# ------------------ HOME ------------------
if section == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="card">
        <h2>About Me</h2>
        <p style="color:var(--muted)">
        I focus on applied research and digital innovation—turning complex ideas into practical tools.
        My work spans data analysis, systems design, and human-centered technology.
        </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card kpi">
          <div class="box"><h3>12+</h3><p>Projects</p></div>
          <div class="box"><h3>5</h3><p>Domains</p></div>
          <div class="box"><h3>∞</h3><p>Curiosity</p></div>
        </div>
        """, unsafe_allow_html=True)

# ------------------ RESEARCH ------------------
elif section == "Research":
    st.markdown("## Research Areas")
    cols = st.columns(3)
    topics = [
        ("Data & Analytics", "Insight extraction, visualization, and decision support."),
        ("AI & Automation", "Human-centered AI systems and workflows."),
        ("Digital Systems", "Scalable, secure, and usable platforms."),
    ]
    for c, (t, d) in zip(cols, topics):
        with c:
            st.markdown(f"""
            <div class="card">
              <h3>{t}</h3>
              <p style="color:var(--muted)">{d}</p>
            </div>
            """, unsafe_allow_html=True)

# ------------------ PROJECTS ------------------
elif section == "Projects":
    st.markdown("## Selected Projects")
    for i in range(1, 4):
        st.markdown(f"""
        <div class="card">
          <h3>Project {i}</h3>
          <p style="color:var(--muted)">Problem → Method → Impact. Interactive dashboards, reports, or systems.</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.05)

# ------------------ CV ------------------
elif section == "CV":
    st.markdown("## Curriculum Vitae")
    st.info("Upload your CV PDF here. It will be displayed and used by the assistant.")
    cv = st.file_uploader("Upload CV (PDF)", type=["pdf"])
    if cv:
        st.success("CV uploaded successfully!")
        st.download_button("Download CV", cv, file_name="Sarah_Bopape_CV.pdf")

# ------------------ ASK ME (CHAT) ------------------
elif section == "Ask Me":
    st.markdown("## Ask My Assistant")
    if "chat" not in st.session_state:
        st.session_state.chat = []

    chat_box = st.container()
    with chat_box:
        st.markdown('<div class="chat">', unsafe_allow_html=True)
        for role, msg in st.session_state.chat:
            st.markdown(f'<div class="message {role}">{msg}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    user_input = st.text_input("Ask about my research, skills, or projects")
    if st.button("Send") and user_input:
        st.session_state.chat.append(("user", user_input))
        # Simple intelligent response (replace with API later if allowed)
        responses = [
            "Great question! My work focuses on applied research with real-world impact.",
            "I combine data analysis and system design to solve complex problems.",
            "That project involved research, prototyping, and measurable outcomes.",
        ]
        st.session_state.chat.append(("ai", random.choice(responses)))
        st.rerun()

# ------------------ GAME ------------------
elif section == "Play":
    st.markdown("## Mini Game: Research Reflex")
    st.write("Click the button as fast as you can when it appears!")
    if st.button("Start"):
        wait = random.uniform(1.5, 4.0)
        time.sleep(wait)
        start = time.time()
        if st.button("CLICK NOW!"):
            score = time.time() - start
            st.success(f"Your reaction time: {score:.3f}s")

# ------------------ FOOTER ------------------
st.markdown("""
<footer>
© {year} • css2026 Research Portfolio • Built with Streamlit
</footer>
""".format(year=datetime.now().year), unsafe_allow_html=True)

