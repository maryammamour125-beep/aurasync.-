import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="The Method | Style Academy",
    page_icon="✨",
    layout="centered"
)

# Custom Styling for "Duolingo-style" Aesthetic, Fabulous Colors & Dark Mode
st.markdown("""
    <style>
    .stApp {
        background-color: #0f1016;
        color: #ffffff;
    }
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(45deg, #ff758c, #ff7eb3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-header {
        text-align: center;
        color: #a0aec0;
        font-size: 1rem;
        margin-bottom: 25px;
    }
    .unit-card {
        background: linear-gradient(135deg, #1e1b4b, #311042);
        border: 2px solid #7c3aed;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
    }
    .lesson-box {
        background-color: #181824;
        border: 1px solid #3f3f46;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #ec4899, #8b5cf6);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        padding: 12px;
        box-shadow: 0 4px 12px rgba(236, 72, 153, 0.4);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #db2777, #7c3aed);
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Define Styles & Their 4 Manifestation Units
STYLES_DATA = {
    "Heisei Japanese Retro": {
        "tagline": "Pearly skin, loose uniform styling, nostalgia, and pager aesthetics.",
        "units": {
            "Unit 1: Environment & Space": [
                "De-clutter desk and add 90s/00s Japanese magazine cutouts to the wall.",
                "Set up a warm, nostalgic desk lamp with soft orange ambient glow.",
                "Clear phone home screen, replacing icons with Heisei retro aesthetic themes.",
                "Incorporate small nostalgic knick-knacks (e.g., vintage keychains or charms).",
                "Create a dedicated vanity or corner mirror space for styling checks."
            ],
            "Unit 2: Accessories": [
                "Incorporate chunky statement rings and layered beaded bracelets.",
                "Source retro rimless or tinted gradient sunglasses.",
                "Add scrunchies, pearl hair clips, or butterfly clips to daily hair routines.",
                "Attach nostalgic strap accessories, straps, or plush charms to your phone or bag.",
                "Wear layered necklaces featuring crosses, hearts, or retro pendants."
            ],
            "Unit 3: Clothes & Makeup": [
                "Layer oversized blazers, cardigans, or loose knitwear over fitted tops.",
                "Experiment with slouchy socks, platform loafers, or chunky sneakers.",
                "Apply soft, dewy glow base with minimal natural eyeliner and glossy lips.",
                "Incorporate plaid skirts, pleated skirts, or relaxed wide-leg denim.",
                "Play with muted, earthy or vintage pastel color palettes."
            ],
            "Unit 4: Mindset & Vibe": [
                "Adopt a calm, daydreamy, and effortlessly detached public demeanor.",
                "Curate a daily playlist of 90s/00s City Pop or Japanese indie rock.",
                "Practice taking candid, polaroid-style or grainy flash photos of your day.",
                "Cultivate appreciation for retro media, vintage magazines, and analog feelings.",
                "Walk through your city with quiet, artistic confidence like you're in a film scene."
            ]
        }
    },
    "Clean Old Money": {
        "tagline": "Timeless elegance, cashmere, neutral tones, and effortless luxury.",
        "units": {
            "Unit 1: Environment & Space": [
                "Declutter all surfaces to maintain absolute minimalist luxury order.",
                "Add fresh white flowers (like lilies or roses) to your living room space.",
                "Incorporate subtle gold-accented decor, classic books, and scented candles.",
                "Keep your workspace completely tidy with sleek leather organizers.",
                "Organize your wardrobe by color spectrum to mimic a high-end boutique."
            ],
            "Unit 2: Accessories": [
                "Wear a classic minimalist analog watch with a leather or gold mesh strap.",
                "Incorporate simple pearl studs or small gold hoop earrings.",
                "Carry a structured, brand-free leather handbag with clean architecture.",
                "Use a silk scarf tied neatly around your neck or bag handle.",
                "Wear sleek tortoiseshell sunglasses."
            ],
            "Unit 3: Clothes & Makeup": [
                "Build outfits using neutral palettes: cream, beige, navy, black, and white.",
                "Wear crisp linen button-downs, tailored trousers, and fine-knit sweaters.",
                "Opt for a clean, 'no-makeup' makeup look with filled brows and tinted lip balm.",
                "Keep nails meticulously manicured in clean sheer pinks or milky white.",
                "Choose classic footwear like loafers, ballet flats, or clean white leather sneakers."
            ],
            "Unit 4: Mindset & Vibe": [
                "Speak clearly, deliberately, and with low vocal volume (graceful composure).",
                "Prioritize peace of mind, healthy boundaries, and private self-care routines.",
                "Read classic literature, financial texts, or culture columns during commutes.",
                "Maintain posture that commands quiet respect without arrogance.",
                "Treat every daily errand as a calm, graceful outing."
            ]
        }
    },
    "Y2K Cyber Baddie": {
        "tagline": "Glossy lips, metallic sheen, low-rise attitude, and futuristic edge.",
        "units": {
            "Unit 1: Environment & Space": [
                "Set up vibrant LED strip lighting in purple, pink, or neon blue hues.",
                "Display vintage tech items, flip phones, or retro gaming gear as props.",
                "Decorate room walls with glossy Y2K era magazine spreads and posters.",
                "Organize your digital files with bright, futuristic desktop aesthetic folders.",
                "Add metallic or holographic decorative pillows to your bed or couch."
            ],
            "Unit 2: Accessories": [
                "Rock futuristic wrap-around sunglasses or tinted frameless shades.",
                "Use butterfly clips, claw clips, or chunky headband statements.",
                "Wear heavy chain necklaces, body chains, or nameplate necklaces.",
                "Carry a metallic shoulder bag, baguette bag, or rhinestone-studded clutch.",
                "Stack heavy chunky rings and ear cuffs."
            ],
            "Unit 3: Clothes & Makeup": [
                "Wear low-rise cargo pants, parachute pants, or baby tees with bold prints.",
                "Incorporate velour tracksuits, metallic puffer jackets, and mesh tops.",
                "Apply icy blue or frosty pink eyeshadow with heavy lip gloss.",
                "Use face gems or graphic glitter liner for special outings.",
                "Step out in platform boots, chunky mules, or futuristic sneakers."
            ],
            "Unit 4: Mindset & Vibe": [
                "Radiate absolute high-energy confidence and unstoppable main-character aura.",
                "Curate an upbeat, high-tempo playlist featuring early 2000s pop, techno, and hip-hop.",
                "Post unapologetically confident, stylized mirror selfies with flash.",
                "Walk with sharp rhythm and fierce intentionality.",
                "Embrace a bold, playful, and completely fearless attitude towards style risks."
            ]
        }
    }
}

# Initialize Session States
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "style" not in st.session_state:
    st.session_state.style = None
if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = []

# ==========================================
# FLOW 1: LOGIN / SIGN UP PROFILE CREATION
# ==========================================
if not st.session_state.logged_in:
    st.markdown('<p class="main-header">✨ THE METHOD ✨</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Manifest your dream style step-by-step, Duolingo-style.</p>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown("### 👤 Create Your Profile")
        username_input = st.text_input("Choose your handle / username", placeholder="e.g. styleicon99")
        bio_input = st.text_input("Your style goal / bio mantra", placeholder="e.g. Transforming into my ultimate aesthetic")
        
        if st.button("Start Your Style Journey 🚀"):
            if username_input.strip():
                st.session_state.username = username_input
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.warning("Please enter a username to continue!")

# ==========================================
# FLOW 2: STYLE QUIZ (IF NO STYLE CHOSEN YET)
# ==========================================
elif st.session_state.style is None:
    st.markdown(f'<p class="main-header">Welcome, @{st.session_state.username}! 💖</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Take the style diagnostic test to unlock your true aesthetic persona.</p>', unsafe_allow_html=True)

    # Simplified interactive quiz mapping to our styles
    st.markdown("### 🔮 Style Diagnostic Test")
    
    q1 = st.radio(
        "1. What is your ideal vibe when walking down the street?",
        ("Nostalgic, effortless, indie film atmosphere (Heisei)",
         "Timeless, polished, wealthy and graceful elegance (Clean Old Money)",
         "Fierce, glossy, futuristic, and attention-grabbing (Y2K Cyber Baddie)")
    )
    
    q2 = st.radio(
        "2. Choose your dream everyday color palette:",
        ("Muted vintage tones, earth shades, soft pastels",
         "Neutrals like cream, beige, black, and navy",
         "Metallics, bright pinks, purples, and high-contrast gloss")
    )

    if st.button("Reveal My True Style 🌟"):
        # Map choice to our catalog
        if "Heisei" in q1 or "pastels" in q2:
            st.session_state.style = "Heisei Japanese Retro"
        elif "Old Money" in q1 or "Neutrals" in q2:
            st.session_state.style = "Clean Old Money"
        else:
            st.session_state.style = "Y2K Cyber Baddie"
        st.rerun()

# ==========================================
# FLOW 3: MAIN APP DASHBOARD (DUOLINGO-STYLE UNITS)
# ==========================================
else:
    active_style_name = st.session_state.style
    style_info = STYLES_DATA.get(active_style_name, STYLES_DATA["Heisei Japanese Retro"])

    st.markdown(f'<p class="main-header">⚡ @{st.session_state.username} | {active_style_name} ⚡</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header">"{style_info["tagline"]}"</p>', unsafe_allow_html=True)

    # Sidebar / Profile manager
    with st.sidebar:
        st.markdown(f"### Profile: @{st.session_state.username}")
        st.markdown(f"**Target Style:** {active_style_name}")
        if st.button("🔄 Retake Style Quiz"):
            st.session_state.style = None
            st.rerun()
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.style = None
            st.rerun()

    st.markdown("---")
    st.markdown("### 🗺️ Your Real-Life Manifestation Path")
    st.write("Complete the 4 core units step-by-step to fully bring this style to life in your physical world.")

    # Render the 4 Units like Duolingo Skill Tree
    for unit_title, lessons in style_info["units"].items():
        with st.container():
            st.markdown(f'<div class="unit-card">', unsafe_allow_html=True)
            st.markdown(f"### 🏆 {unit_title}")
            st.write(f"*Progress: 0 / {len(lessons)} Lessons Completed*")
            
            # Expandable lessons list
            with st.expander("Open Unit Lessons 📚"):
                for idx, lesson in enumerate(lessons, 1):
                    st.markdown(f'<div class="lesson-box">', unsafe_allow_html=True)
                    st.markdown(f"**Lesson {idx}:** {lesson}")
                    # Interactive checkbox for real-life completion
                    done = st.checkbox(f"Mark Completed in Real Life", key=f"{unit_title}_{idx}")
                    if done:
                        st.balloons()
                        st.success("Lesson mastered! Real-world manifestation updated ✨")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
            st.markdown('</div>', unsafe_allow_html=True)
