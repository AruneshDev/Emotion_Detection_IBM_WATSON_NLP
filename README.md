# Emotion Detection Web App using Watson NLP

## 📑 Project Overview
This project is an **AI-based web application** that detects human emotions from text input using **Watson NLP libraries**. Built as part of an e-commerce company's initiative, the application analyzes customer feedback to understand emotions such as **joy, sadness, anger, fear, and disgust**.

![Project Cover](Screenshots/Cover.png)

The application is built with **Flask** for web deployment and follows **PEP8 standards** with a perfect **10/10 score** in static code analysis using **PyLint**.

---

## 🚀 Features
1. **Emotion Detection:**
   - Uses IBM Watson NLP's BERT-based model to detect emotions from text input.
   - Provides scores for emotions like **anger, disgust, fear, joy, and sadness**.

2. **Web Interface:**
   - Built using Flask for simple and intuitive web interaction.
   - Accepts user input via a web form.

3. **Error Handling:**
   - Handles invalid input gracefully and provides feedback.

4. **Static Code Analysis:**
   - Code is thoroughly analyzed using **PyLint** with a **10/10 score**.
   - Follows PEP8 standards including the use of docstrings.

---

## 🛠️ Technologies Used
- **Python 3.11.11**
- **Flask:** Web framework for building the web application.
- **Watson NLP:** Used for emotion detection.
- **Requests:** For making API calls.
- **PyLint:** To ensure code quality and PEP8 compliance.

---


## 📂 Project Structure
```
final_project/
├── emotion_detection.py          # Main emotion detection logic
├── server.py                     # Flask web server and API
├── templates/
│   └── index.html                # Frontend web page
├── venv/                         # Virtual environment
├── __pycache__/                  # Compiled Python files
└── README.md                     # Project documentation
```

---

## 💻 Installation Instructions

### 1. Clone the Repository:
```bash
git clone https://github.com/username/emotion-detection-webapp.git
cd emotion-detection-webapp
```

### 2. Set Up the Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the Dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application:
```bash
python server.py
```
Access the application at:
```
http://localhost:8080/
```

---

## 📝 Usage Instructions
1. Open the web app in your browser.
2. Enter a sentence or a phrase expressing emotion.
3. Click **"Analyze"**.
4. View the analyzed emotion and emotion scores displayed on the screen.

---
## 🎯 Example Phrases for IBM Watson NLP

Here are some example phrases that you can use to test the emotion detection capabilities of IBM Watson:

    Joy:

        "I am feeling so happy today!"

        "This is the best day of my life!"

        "I love this! I feel amazing!"

    Sadness:

        "I feel really down today."

        "I'm so upset and tired."

        "Everything feels so empty right now."
        
        "I can't stand this mess anymore."

    Anger:

        "I am furious about this situation."

        "This is completely unacceptable!"

        "I can't believe this is happening, I am so angry!"

    Fear:

        "I'm so scared about what's going to happen next."

        "I am terrified of the consequences."

        "What if I fail? I am really nervous."

    Disgust:

        "This is disgusting, I can't even look at it."

        "I feel repulsed by how things are going."

## 🧪 Testing

### Unit Testing:
The application uses **unittest** for automated testing:
```bash
python -m unittest test_emotion_detection.py
```

### Static Code Analysis:
To maintain PEP8 compliance:
```bash
pylint server.py
```
Expected output:
```
Your code has been rated at 10.00/10
```

---

## 📸 Screenshots
1. **App Running:**
   ![App Screenshot](Screenshots/6b_deployment_test.png)

2. **PyLint Score:**
   ![PyLint Score](Screenshots/8b_static_code_analysis.png)
3. **Deployed UI**
    ![Deployed](Screenshots/Updated_UI.png)

---
## 🌐 Deployment

The app can be deployed on any web server. Follow these steps for deployment on Railway:
Step 1: Sign up for Railway

Visit Railway and sign up for an account.
Step 2: Link the project to Railway

    Create a new project on Railway.

    Connect your GitHub repository to Railway.

    Follow the setup steps on Railway's platform to deploy the project.

Step 3: Open the App

After deployment, you can access your app at:


### Step 4: Open the App
```bash
https://emotiondetector-productionupdated.up.railway.app/

```

---

## 🌟 Future Enhancements
- Integrate more nuanced emotion detection models.
- Add sentiment analysis for better customer feedback insights.
- Provide data visualization for emotion trends.

---

## 🤝 Contributing
Feel free to submit issues or pull requests on GitHub. Contributions are welcome!

---

## 📜 License
IBM AI Developer Final Project
