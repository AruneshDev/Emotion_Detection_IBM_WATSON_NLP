# Emotion Detection Web App using Watson NLP

## 📑 Project Overview
This project is an **AI-based web application** that detects human emotions from text input using **Watson NLP libraries**. Built as part of an e-commerce company's initiative, the application analyzes customer feedback to understand emotions such as **joy, sadness, anger, fear, and disgust**.

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
- **Python 3.13**
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
http://localhost:5000/
```

---

## 📝 Usage Instructions
1. Open the web app in your browser.
2. Enter a sentence or a phrase expressing emotion.
3. Click **"Analyze"**.
4. View the analyzed emotion and emotion scores displayed on the screen.

---

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
   ![App Screenshot](screenshots/app_running.png)

2. **PyLint Score:**
   ![PyLint Score](screenshots/pylint_10.png)

---

## 🌐 Deployment
The app can be deployed on any web server. Follow these steps for deployment on **Heroku**:

### Step 1: Install Heroku CLI
```bash
brew tap heroku/brew && brew install heroku
```

### Step 2: Create a Heroku App
```bash
heroku create emotion-detection-app
```

### Step 3: Deploy the App
```bash
git push heroku main
```

### Step 4: Open the App
```bash
heroku open
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
