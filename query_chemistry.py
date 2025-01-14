from extract_terms import extract_chemistry_terms
from pubchem_fetcher import fetch_pubchem_data
from llm_response import generate_llm_response


def query_chemistry_related(query_text: str):
    """
    Parse the question, query PubChem for related terms, and generate an LLM response.
    """
    # Step 1: Parse chemistry-related terms from the question
    chemistry_terms = extract_chemistry_terms(query_text)
    if not chemistry_terms:
        return "No chemistry-related terms found in the query."

    # print(f"Extracted Chemistry Terms: {chemistry_terms}")

    # Step 2: Query PubChem for information on the terms
    pubchem_context = fetch_pubchem_data(chemistry_terms)
    if not pubchem_context:
        return "No relevant information found on PubChem."

    # print(f"Fetched Context from PubChem:\n{pubchem_context}")

    # Step 3: Use the fetched context in the LLM
    response = generate_llm_response(pubchem_context, query_text)
    return response