import spacy

# Initialize SpaCy NLP model
nlp = spacy.load("en_core_web_sm")


def extract_chemistry_terms(query_text: str):
    """
    Extract chemistry-related terms from the query using SpaCy.
    """
    doc = nlp(query_text)
    # Intial filter for nouns and proper nouns through spacy
    terms = [token.text for token in doc if token.pos_ in {"NOUN", "PROPN"} and len(token.text) > 2]
    return terms