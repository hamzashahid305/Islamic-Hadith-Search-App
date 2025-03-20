import streamlit as st
import requests

# App ka Title
st.title("📖 Islamic Hadith Search App")

# User Input: Hadith Book & Hadith Number
book_name = st.selectbox("Hadith Book Select Karein:", ["Bukhari", "Muslim", "Tirmidhi", "Abu Dawood"])
hadith_number = st.text_input("Hadith Number Likhein (Jaise: 12):")

if st.button("🔍 Search Hadith"):
    if hadith_number:
        # API Request URL
        api_url = f"https://hadithapi.com/api/hadiths?book={book_name}&hadith_number={hadith_number}"
        
        # API key (Ye tumhe Streamlit secrets me store karni hogi)
        headers = {"Authorization": f"Bearer {st.secrets['HADITH_API_KEY']}"}
        
        # API Request bhejna
        response = requests.get(api_url, headers=headers)
        data = response.json()

        # Agar hadees mili to show karo
        if "data" in data and len(data["data"]) > 0:
            hadith = data["data"][0]["hadith"]
            st.success(f"📜 **{book_name} Hadith #{hadith_number}:**")
            st.write(hadith)
        else:
            st.error("⚠️ Hadith nahi mili, sahi number ya kitaab check karein.")
    else:
        st.warning("⚠️ Pehle Hadith Number likhein!")
