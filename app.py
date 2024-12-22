import streamlit as st
import requests

# API Hugging Face
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {st.secrets['HUGGINGFACE_API_TOKEN']}"}

# Fungsi untuk memanggil API
def query(image):
    response = requests.post(API_URL, headers=headers, data=image)
    return response.json()

# Streamlit UI
st.title("Image Captioning with BLIP")
st.write("Unggah gambar untuk mendapatkan deskripsi otomatis.")

uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)
    st.write("Menganalisis...")

    # Membaca file gambar
    image_data = uploaded_file.read()

    # Memanggil API
    with st.spinner("Memproses..."):
        result = query(image_data)

    # Menampilkan hasil
    if "error" in result:
        st.error(f"Terjadi kesalahan: {result['error']}")
    else:
        st.success("Caption berhasil dibuat!")
        st.write(f"Deskripsi Gambar: {result[0]['generated_text']}")
