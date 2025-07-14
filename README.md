
# 🖥️ Stationery Desk Object Detector (Using Azure Computer Vision)

## 📖 Project Meaning / Objective

This project uses **Artificial Intelligence (AI)** to check if a student's desk is set up and ready for studying by analyzing objects on the desk.

It uses **Azure Computer Vision API** to automatically detect items like:
- 🖊️ Pen
- 📘 Book or Notebook
- 📱 Mobile phone
- 🍼 Water bottle
- 💻 Laptop

Based on what items are present, the app decides whether the student is ready to study or not.

### 🧪 Example:
- If the image has **pen + book** → ✅ "You're ready to study!"
- If the image has **mobile + chips** → ⚠️ "Distraction detected!"

---

## 🎯 Purpose of the Project

- Promote focus and discipline in students.
- Use AI for study habit monitoring.
- Introduce students to real-world applications of AI and computer vision.
- Show how images can be understood by machines using Microsoft Azure.

---

## 💡 Real-Life Use Cases

- 📚 Study environment check before online classes.
- 📸 Classroom desk scanning for automated readiness.
- 👨‍🏫 Teachers can monitor if students are prepared.
- 🧘 For mental wellness apps like **MindEase**, this can be part of a “Focus Mode” detector.

---

## 🧰 Tech Stack

- **Azure Computer Vision API**
- **Python**
- **Streamlit** for UI
- **Pillow (PIL)** for image editing
- **REST API** requests using `requests`

---

## 📁 Folder Structure

```
stationery_detector_cvapi/
├── images/                # Contains sample desk image
├── outputs/               # (optional) save processed images
├── vision_config.py       # Azure API key and endpoint
├── detect_with_azure.py   # Image analysis + drawing boxes
├── ui_streamlit.py        # Main Streamlit UI
├── requirements.txt       # Python dependencies
├── README.md              # Project description
```

---

## 🚀 How to Run

1. Replace Azure credentials in `vision_config.py`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run ui_streamlit.py
   ```

---

## 👤 Author
Made with ❤️ by Katta Vivek (Final Year Student, JITS)
