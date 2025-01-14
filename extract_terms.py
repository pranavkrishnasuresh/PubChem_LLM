import spacy

# Initialize SpaCy NLP model
nlp = spacy.load("en_core_web_sm")


def extract_chemistry_terms(query_text: str):
    """
    Extract chemistry-related terms from the query using SpaCy.
    """
    doc = nlp(query_text)
    # Filter for potential chemistry-related terms (e.g., nouns, proper nouns)
    terms = [token.text for token in doc if token.pos_ in {"NOUN", "PROPN"} and len(token.text) > 2]
    return terms
