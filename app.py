from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from college_data import chatbot_logic
import datetime
import os

app = Flask(__name__)
app.secret_key = "campus_guide_secure_key" 

# --- SETTINGS ---
ADMIN_PASSWORD = "admin123"
LOG_FILE = "unanswered_questions.txt"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

# Updated Support Route
@app.route('/unanswered')
def unanswered():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in reversed(lines):
                if "|" in line:
                    parts = line.split("|", 1)
                    logs.append({"time": parts[0].strip(), "question": parts[1].strip()})
    return render_template('support.html', logs=logs)

# Secure Clear Route
@app.route('/clear_logs', methods=['POST'])
def clear_logs():
    input_password = request.form.get('password')
    if input_password == ADMIN_PASSWORD:
        if os.path.exists(LOG_FILE):
            open(LOG_FILE, 'w').close()
        flash("History cleared successfully! ✅", "success")
    else:
        flash("Incorrect password! Access denied. ❌", "danger")
    return redirect(url_for('unanswered'))

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message', '')
    reply = chatbot_logic(user_message)

    if reply == "UNANSWERED_QUERY":
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} | {user_message}\n")
        reply = "I've noted your question for my developer! Please try asking about Amity, ITS, or BITS."

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)