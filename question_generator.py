



import random
import spacy
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration

# Load Spacy for sentence segmentation
nlp = spacy.load("en_core_web_sm")

# Load the T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("valhalla/t5-small-qg-prepend")
model = T5ForConditionalGeneration.from_pretrained("valhalla/t5-small-qg-prepend")

# Initialize the question generation pipeline
question_generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def split_text(text):
    """
    Split text into sentences or manageable segments.
    """
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

def generate_questions(text):
    """
    Generate questions from text using the question-generation model.
    """
    questions = question_generator(f"generate question: {text}")
    return [q['generated_text'] for q in questions]

def generate_test(text):
    """
    Generate multiple questions based on segmented text.
    """
    segments = split_text(text)
    all_questions = []
    
    for segment in segments:
        questions = generate_questions(segment)
        for q in questions:
            all_questions.append({"question": q, "context": segment})

    return all_questions
