# This file contains the business logic to separate logic from routes. Used here to define a callable function

def analyze_text(text: str):
    return {"length":len(text), "uppercase":text.upper(), "word_count":len(text.split())}