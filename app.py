
# from flask import Flask, render_template, request, redirect, url_for, session
# from question_generator import generate_test

# app = Flask(__name__)
# app.secret_key = "your_secret_key"  # Needed for session handling

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/generate', methods=['POST'])
# def generate():
#     text = request.form.get('text')
#     session['text'] = text  # Store the input text in the session for regeneration
#     questions = generate_test(text)
#     return render_template('result.html', questions=questions)

# @app.route('/generate')
# def regenerate():
#     # Retrieve text from session and regenerate questions
#     text = session.get('text')
#     if not text:
#         return redirect(url_for('home'))  # Redirect to home if text is not in session
#     questions = generate_test(text)
#     return render_template('result.html', questions=questions)



# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, session
from question_generator import generate_test
import pandas as pd
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session handling

# CSV file to store user data
DATA_FILE = "user_data.csv"

# Function to save data to CSV
def save_user_data(input_text, questions):
    timestamp = datetime.now().isoformat()  # Current timestamp
    data = {
        "timestamp": timestamp,
        "input_text": input_text,
        "questions": [q["question"] for q in questions],
        "contexts": [q["context"] for q in questions]
    }
    # Convert the data to a DataFrame and append to the CSV
    df = pd.DataFrame([data])
    df.to_csv(DATA_FILE, mode='a', index=False, header=not pd.io.common.file_exists(DATA_FILE))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get('text')
    session['text'] = text  # Store the input text in the session for regeneration
    questions = generate_test(text)
    
    # Save data to CSV file after generating questions
    save_user_data(text, questions)

    return render_template('result.html', questions=questions)

@app.route('/generate')
def regenerate():
    # Retrieve text from session and regenerate questions
    text = session.get('text')
    if not text:
        return redirect(url_for('home'))  # Redirect to home if text is not in session
    questions = generate_test(text)
    
    # Save regenerated data to CSV file
    save_user_data(text, questions)
    
    return render_template('result.html', questions=questions)

if __name__ == "__main__":
    app.run(debug=True)

