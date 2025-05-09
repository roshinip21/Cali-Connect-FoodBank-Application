# app.py

import streamlit as st
import googlemaps
import streamlit.components.v1 as components
from models import load_centers, build_knn_model, find_nearest_center



st.set_page_config(page_title="Nearest Donation Center", layout="wide")
st.title("Cali Food Connect 🥑")

# 2) Inject external-URL background via CSS
BACKGROUND_URL = "https://github.com/roshinip21/Snowflake-Costing-Dashboards/blob/main/Dashboard%204.png"
st.markdown(
    f"""
    <style>
    /* full-screen background */
    .stApp {{
        background: url("{BACKGROUND_URL}") no-repeat center center fixed;
        background-size: cover;
    }}
    /* optional overlay for readability */
    .stApp::before {{
      content: "";
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: rgba(200, 400, 210, 0.3);
      z-index: -1;
    }}
    /* style your headings */
    h1, h2 {{
        color: #E63946;
        text-shadow: 1px 1px 2px #000;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# rest of the application code
st.subheader("Nearest Donation Center Locator 🍎")

st.write(
    """
    Type your address in California or choose one of the CA cities,
    to locate the food bank closest to you.
    """
)

# — expanded sample locations —
sample_locs = [
    "",
    "Los Angeles, CA",
    "San Diego, CA",
    "Irvine, CA",
    "Sacramento, CA",
    "Concord, CA",
    "Santa Barbara, CA",
    "Riverside, CA",
    "Santa Rosa, CA",
    "Oakland, CA",
]
choice = st.selectbox("Choose a sample city:", sample_locs)
address = choice or st.text_input("Or type your full street address here:")

if st.button("Find Nearest Center"):
    if not address:
        st.error("🚨 Please enter or select an address.")
        st.stop()

    # 1) Geocode via Google Maps
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    gmaps = googlemaps.Client(key=API_KEY)
    geo = gmaps.geocode(address)
    if not geo:
        st.error("❌ Could not geocode that address. Try again.")
        st.stop()
    loc = geo[0]["geometry"]["location"]
    user_lat, user_lon = loc["lat"], loc["lng"]

    # 2) Load centers & build KNN
    centers = load_centers()
    knn = build_knn_model(centers)

    # 3) Find nearest
    center, dist_km = find_nearest_center(knn, centers, user_lat, user_lon)
    st.success(f"✅ **{center.name}** is nearest — {dist_km:.1f} km away.")
    st.write(f"📍 **Address:** {center.address}")

    # 4) Embed Google Maps directions widget
    map_url = (
        "https://www.google.com/maps/embed/v1/directions"
        f"?key={API_KEY}"
        f"&origin={user_lat},{user_lon}"
        f"&destination={center.lat},{center.lon}"
        "&zoom=10"
    )
    components.iframe(map_url, width=700, height=500)
