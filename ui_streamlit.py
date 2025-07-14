import streamlit as st
from detect_with_azure import analyze_image, draw_boxes
import tempfile

st.set_page_config(page_title="📚 Stationery Desk Detector", page_icon="📷")
st.title("📚 Stationery Desk Object Detector")
st.caption("Uses Azure Computer Vision to detect objects on your desk.")

uploaded_file = st.file_uploader("Upload a desk photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    with st.spinner("Analyzing image..."):
        analysis = analyze_image(temp_path)
        detected_image = draw_boxes(temp_path, analysis)

    st.image(detected_image, caption="Detected Objects", use_container_width=True)

    detected_items = [obj["object"] for obj in analysis.get("objects", [])]
    st.markdown("### 🧠 Detected Items:")
    
    if detected_items:
        st.write(", ".join(detected_items))
    else:
        st.warning("⚠️ No objects detected using Azure Object Detection.")

    # Fallback using tags
    if not detected_items and analysis.get("tags"):
        tags = [tag["name"] for tag in analysis["tags"]]
        st.markdown("### 🏷️ Tags from Image (Backup):")
        st.write(", ".join(tags))
        if "pen" in tags or "book" in tags or "notebook" in tags or "stationery" in tags:
            st.info("📌 Tags suggest you're ready to study.")
        else:
            st.warning("⚠️ Couldn’t detect useful tags like pen or book.")

    # Main condition using detected items
    if "pen" in detected_items and "book" in detected_items:
        st.success("📘 You're ready to study!")
    elif "cell phone" in detected_items:
        st.warning("📱 Distraction detected!")
