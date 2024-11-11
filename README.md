
# SmartQraft - AI-Powered Question Generator

SmartQraft is an AI-driven question generation tool that helps educators, students, and self-learners to create quizzes and assessments from any text-based content. Built with Flask and powered by the T5 transformer model, SmartQraft generates relevant questions from input text, making it a versatile tool for reinforcing learning and enhancing study materials.



---

## Features

- **AI-Generated Questions**: Generate insightful and contextually relevant questions from any input text.
- **Regenerate Capability**: Refine your questions by regenerating from the same text for variety.
- **Data Collection for Improvement**: Stores user-generated questions and input text for potential fine-tuning and improvement of the model.
- **User-Friendly Interface**: Simple, clean, and intuitive UI built with HTML and Bootstrap for easy navigation.

---

## How It Works

SmartQraft leverages the T5 (Text-To-Text Transfer Transformer) model to convert educational or informative content into a question-answer format. By parsing the input text, SmartQraft identifies key concepts and generates questions that encourage deeper understanding and retention.

1. **Input Text**: Users provide a passage or paragraph of text.
2. **Question Generation**: The T5 model generates questions related to the key points in the text.
3. **Data Storage**: Each session's data (input text and generated questions) is saved in a CSV file for potential future fine-tuning.
4. **Regeneration Option**: Users can regenerate questions to receive different phrasing or new questions based on the same input.

---

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/SmartQraft.git
   cd SmartQraft
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download spaCy Model** (for text segmentation):
   ```bash
   python -m spacy download en_core_web_sm
   ```

### Running the Application

To start the Flask app, run:

```bash
python app.py
```



---

## Usage

1. **Navigate to the Home Page**: Enter the text you wish to generate questions from.
2. **Generate Questions**: Click the "Generate Questions" button to see AI-generated questions based on the input text.
3. **Regenerate Questions**: Use the "Regenerate" option to create a new set of questions from the same text.
4. **View and Download**: Generated questions are displayed on the results page, allowing for easy review and saving.

---

## Project Structure

```plaintext
SmartQraft/
├── app.py                  # Main Flask application with routes and data handling
├── question_generator.py    # Question generation logic using T5 model
├── requirements.txt         # Project dependencies
├── static/                  # Static files (CSS, images, etc.)
├── templates/               # HTML templates for the front end
└── user_data.csv            # CSV file for storing user input and generated questions (ignored in .gitignore)
```

---

## Technologies Used

- **Flask**: Backend framework to handle routing and server operations.
- **Hugging Face Transformers**: T5 model for question generation.
- **spaCy**: For text segmentation and pre-processing.
- **Bootstrap**: Front-end styling for a clean and responsive interface.
- **Pandas**: For efficient CSV handling and data storage.

---

## Future Enhancements

- **Fine-Tuning**: Use stored user data for fine-tuning the T5 model to improve question quality.
- **Custom NER Integration**: Integrate custom Named Entity Recognition (NER) for enhanced entity-based question generation.
- **Export Options**: Allow users to export questions in PDF or DOCX formats for easy sharing and printing.
- **User Authentication**: Add login functionality to let users save and track generated questions.

---


---

## Contact

For any questions or feedback, please contact us at:
- **Email**: support@smartqraft.com
- **GitHub Issues**: [Report an Issue](https://github.com/yourusername/SmartQraft/issues)
