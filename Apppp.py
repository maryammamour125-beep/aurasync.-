import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="The Method",
    page_icon="🎭",
    layout="centered"
)

# Custom Styling for Dark Minimalist Theme
st.markdown("""
    <style>
    .main {
        background-color: #0a0a0a;
        color: #ffffff;
    }
    .stTextInput input {
        background-color: #1c1c1c;
        color: #ffffff;
        border: 1px solid #333333;
    }
    .card {
        background-color: #141414;
        border: 1px solid #262626;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Static Archetype Data
ARCHETYPES = {
    "The Noir Detective": {
        "tagline": "Deliberate, cynical, and observant.",
        "quest": "Order your coffee using concise, minimal phrasing. Observe three details about a stranger today.",
        "props": ['Tortoiseshell glasses', 'Leather folio or notebook', 'Neutral-toned trench or coat']
    },
    "The Minimalist Architect": {
        "tagline": "Clean lines, purposeful spaces, absolute clarity.",
        "quest": "Clear your physical workspace of all non-essential items before starting your work.",
        "props": ['Monochrome watch', 'Plain black or white notebook', 'Fountain pen']
    },
    "The 1970s Journalist": {
        "tagline": "Inquisitive, fast-paced, relentless truth-seeker.",
        "quest": "Ask three deep, open-ended questions in conversations today instead of small talk.",
        "props": ['Vintage messenger bag', 'Portable tape recorder or voice memo app ready', 'Corduroy or textured jacket']
    }
}

# Initialize Session State
if "selected_archetype" not in st.session_state:
    st.session_state.selected_archetype = None

# --- SCREEN 1: ARCHETYPE SELECTION ---
if st.session_state.selected_archetype is None:
    st.markdown("# THE METHOD")
    st.markdown("Select your persona to begin transmission.")
    st.write("")

    for name, data in ARCHETYPES.items():
        with st.container():
            st.markdown(f"### {name}")
            st.markdown(f"*{data['tagline']}*")
            if st.button(f"Initialize {name}", key=name):
                st.session_state.selected_archetype = name
                st.rerun()
            st.markdown("---")

# --- SCREEN 2: MAIN DASHBOARD & REFLECTION ---
else:
    active_name = st.session_state.selected_archetype
    active_data = ARCHETYPES[active_name]

    # Header Layout
    col1, col2 = st.columns([3, 1])
    with col1:
        st.caption("ACTIVE ARCHETYPE")
        st.markdown(f"## {active_name}")
    with col2:
        st.write("")
        if st.button("Switch"):
            st.session_state.selected_archetype = None
            st.rerun()

    st.markdown("---")

    # Daily Scene Quest
    with st.container():
        st.markdown("### 📌 TODAY'S SCENE QUEST")
        st.info(active_data["quest"])
        quest_done = st.checkbox("Mark Quest Complete")

    st.write("")

    # Capsule Checklist
    with st.container():
        st.markdown("### 🧳 PROP & WARDROBE CHECKLIST")
        for prop in active_data["props"]:
            st.markdown(f"- {prop}")

    st.write("")

    # End of Day Reflection
    with st.container():
        st.markdown("### 📝 END OF DAY REFLECTION")
        reflection = st.text_area(
            "How did you embody the character today? Where did you break?",
            placeholder="Log your thoughts here..."
        )
        
        if st.button("Log Daily Performance"):
            if reflection.strip():
                st.success("Transmission Logged Successfully ✓")
            else:
                st.warning("Please enter a brief reflection before logging.")
