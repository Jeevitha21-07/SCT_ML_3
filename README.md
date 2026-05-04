# 🐶🐱 Cat vs Dog Classifier

## 📌 Project Overview

This project is an image classification web application that predicts whether an uploaded image is a **cat or a dog**.
It is built using **Machine Learning (SVM + HOG features)** and deployed using Streamlit for real-time predictions.

---
## 🚀 Live Demo

🔗 https://jeevitha21-07-sct-ml-3-app-zudpqn.streamlit.app/

---

## 🎯 Internship Details

* **Internship:** SkillCraft Technology
* **Task:** Task 3 – Image Classification
* **Objective:** Build and deploy a machine learning model to classify images into categories.

---


## 🧠 Technologies Used

* Python
* NumPy
* OpenCV
* Scikit-learn
* Scikit-image (HOG features)
* Streamlit

---

## ⚙️ How It Works

1. User uploads an image (cat or dog).
2. Image is preprocessed (resize, grayscale conversion).
3. HOG (Histogram of Oriented Gradients) features are extracted.
4. A trained **Linear SVM model** predicts the class.
5. The result is displayed instantly on the web interface.

---

## 📂 Project Structure

```
SCT_ML_3/
│
├── app.py              # Streamlit application  
├── model.pkl          # Trained ML model  
├── requirements.txt   # Dependencies  
├── backend/           # Training scripts  
└── dataset/           # Dataset (ignored in Git)  
```

---

## 🧪 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## ✨ Features

* Real-time image classification
* Simple and user-friendly UI
* Fast predictions using optimized model
* Deployed and accessible online

---

## 📈 Future Improvements

* Add confidence score for predictions
* Improve UI/UX design
* Support multiple image uploads
* Extend to more animal classes

---

## 🙌 Acknowledgement

This project was completed as part of the **SkillCraft Technology Internship (Task 3)**.

---

## 👩‍💻 Author

**Jeevitha S**

* AIML Engineering Student
* Passionate about AI, ML & App Development
