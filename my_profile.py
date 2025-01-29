import streamlit as st
import pandas as pd
from PIL import Image
import time



# --- Page Config ---
st.set_page_config(
    page_title="🚀 Researcher Profile - Mickalan Joshua Subramoney",
    page_icon="🌌",
    layout="wide",
st.markdown(
    """
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <div id="particles-js"></div>
    <style>
        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            z-index: -1;
            top: 0;
            left: 0;
            background: black;
        }
    </style>
    <script>
        particlesJS.load('particles-js', 'particles.json', function() {
            console.log('particles.js loaded - cosmic effect');
        });
    </script>
    """,
    unsafe_allow_html=True
)
# --- Cool Animated Header ---
st.markdown(
    "<h1 style='text-align: center; color: #FFD700;'>🚀 Researcher Profile Page 🌌</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: #ADD8E6;'>Exploring the Universe, One Dataset at a Time</h3>",
    unsafe_allow_html=True,
)

# --- Load & Display Profile Image ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    image = Image.open("my_pic.jpg").rotate(270)
    st.image(image, width=500, caption="🔭 Astrophysicist | Researcher | Cosmic Explorer")

# --- Research & Publications Section ---
st.subheader("📚 Research & Publications")

with st.expander("🔬 **My Qualifications** (Click to Expand)"):
    st.markdown("""
    -  **Matric** : completed 2019
    -  **BSc undergrad (Astronomy & Applied Mathematics)**: 2020-2022 (Summa Cum Laude)
    -  **BSc Hon Physics (NASSP)**: completed 2023
    -  **MSc Applied Mathematics (Astronomy)**: 2024-present
    """)    


with st.expander("🔬 **My Research Areas** (Click to Expand)"):
    st.markdown("""
    - 🌌 **Cross-Correlation Cosmology**: Exploring the relationship between cosmic shear and HI redshifts.
    - 🔭 **Large-Scale Structure Analysis**: Investigating galaxy distributions and dark matter effects.
    - 🤖 **Machine Learning in Cosmology**: Applying AI to analyze cosmic datasets.
    - 🛰 **Radio Astronomy & HI Surveys**: Studying neutral hydrogen at cosmic scales.
    - 📡 **Next-Gen Telescopes**: Working with HIRAX & LSST to probe the early universe.
    """)
    

# --- Upload Publications CSV ---
uploaded_file = st.file_uploader("📂 Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.success("✅ File Uploaded Successfully!")
    
    # Display Publications
    with st.expander("📄 **View Full Publication List**"):
        st.dataframe(publications)

    # Keyword Search for Publications
    keyword = st.text_input("🔍 Search Publications by Keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"🎯 Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.info("Showing all publications")

# --- Research Project Trends ---
st.subheader("📊 Research Trends")
if uploaded_file and "Year" in publications.columns:
    year_counts = publications["Year"].value_counts().sort_index()
    st.bar_chart(year_counts)
else:
    st.warning("No 'Year' column found in the uploaded CSV.")

# --- Interactive Fun Facts Section ---
st.subheader("✨ Fun Space Fact Generator")
if st.button("Click for a Random Space Fact 🚀"):
    space_facts = [
        "The universe is approximately 13.8 billion years old.",
        "There are more stars in the universe than grains of sand on Earth.",
        "A neutron star is so dense that a sugar-cube-sized amount of its material weighs about a billion tons.",
        "The Andromeda Galaxy and the Milky Way will collide in about 4.5 billion years.",
        "Black holes are so powerful that not even light can escape their gravity."
    ]
    st.success(f"💡 {space_facts[int(time.time()) % len(space_facts)]}")

# --- Contact Section ---
st.subheader("📧 Get in Touch")
st.markdown(f"""
💌 **Email:** [Mickalansubramoney@gmail.com](mailto:Mickalansubramoney@gmail.com)  
📍 **Institution:** University of Kwa-Zulu Natal  
🔗 **GitHub:** [https://github.com/Mickalan](#)  
📄 **LinkedIn:** [linkedin.com/in/Mickalan](#)
""")

# --- Closing Remarks ---
st.markdown("---")
st.markdown(
    "<h4 style='text-align: center; color: #FFD700;'>“Whether or not you can never become great at something, you can always become better at it.” – Niel Degrasse Tyson</h4>",
    unsafe_allow_html=True,
)

