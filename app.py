import streamlit as st
import random

# App Title
st.title("AuraSync ⚡")
st.subheader("The Persona & Style Manifestation Studio")

# Database
AESTHETIC_DATABASE = {
    "Heisei Japanese Streetwear": {
        "description": "Nostalgic, heavily accessorized, chaotic Harajuku/Y2K energy.",
        "quest": "Raid storage boxes for vintage keychains or charms to build an Ita-bag base."
    },
    "Dark Alt & Goth": {
        "description": "Moody, industrial hardware, velvet/mesh textures, and deep tones.",
        "quest": "Repurpose household items into moody, asymmetric lighting setups ($0 budget)."
    },
    "Modern Baddie": {
        "description": "High-confidence, sculpted silhouettes, and luxury street-edge.",
        "quest": "Run a 15-minute high-energy alignment and posture check in front of the mirror."
    },
    "Clean Girl / Minimalist": {
        "description": "Effortless skin-forward wellness, neutral tones, and frictionless organization.",
        "quest": "Strip your workspace completely bare and remove all aesthetic friction."
    }
}

# Session State to track user progress
if "stage" not in st.session_state:
    st.session_state.stage = "test"
    st.session_state.style = None
    st.session_state.streak = 0

# Stage 1: Diagnostic Test
if st.session_state.stage == "test":
    st.write("Tap below to run your rapid Vibe Frequency Diagnostic:")
    if st.button("Run Diagnostic Swipe Test"):
        st.session_state.style = random.choice(list(AESTHETIC_DATABASE.keys()))
        st.session_state.stage = "gate"
        st.rerun()

# Stage 2: The Confirmation Gate
elif st.session_state.stage == "gate":
    style = st.session_state.style
    st.success(f"Detected Match: **{style}**")
    st.write(AESTHETIC_DATABASE[style]["description"])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, lock it in!"):
            st.session_state.stage = "journey"
            st.rerun()
    with col2:
        if st.button("Retake Test"):
            st.session_state.stage = "test"
            st.rerun()

# Stage 3: The Journey & Quests
elif st.session_state.stage == "journey":
    style = st.session_state.style
    st.header(f"Your Custom Journey: {style}")
    st.metric(label="Aura Streak", value=f"🔥 {st.session_state.streak} Days")
    
    st.info(f"**Level 1 Quest:** {AESTHETIC_DATABASE[style]['quest']}")
    
    if st.button("Complete Today's Quest"):
        st.session_state.streak += 1
        st.success("Quest completed! Streak updated.")
        st.rerun()
        
    if st.button("Reset App"):
        st.session_state.stage = "test"
        st.session_state.streak = 0
        st.rerun()

