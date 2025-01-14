# import requests

# PUBCHEM_API_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

# def fetch_pubchem_data(terms):
#     """
#     Query PubChem for each term and gather the resulting context.
#     """
#     context = []
#     for term in terms:
#         term_type = infer_term_type(term)
#         if not term_type:
#             print(f"Skipping term '{term}': Unable to infer type.")
#             continue

#         try:
#             url = construct_pubchem_url(term, term_type)
#             response = requests.get(url, timeout=10)  # Set a timeout to avoid hanging
#             response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
#             descriptions = extract_pubchem_descriptions(response.json())
#             if descriptions:
#                 context.append(f"**{term}**: {descriptions}")
#         except requests.exceptions.RequestException as e:
#             print(f"Error querying PubChem for term '{term}': {e}")
#         except ValueError as e:
#             print(f"Error processing response for term '{term}': {e}")
#     return "\n\n".join(context)



# def infer_term_type(term: str):
#     """
#     Infer the type of the term (e.g., compound name, formula, CID).
#     """
#     if term.isdigit():
#         return "cid"  # Assume term is a PubChem CID
#     elif len(term) <= 5 and all(c.isalpha() or c.isdigit() for c in term):
#         return "formula"  # Assume term is a chemical formula
#     else:
#         return "name"  # Default to compound name


# def construct_pubchem_url(term: str, term_type: str):
#     """
#     Construct the PubChem API URL based on the term type.
#     """
#     if term_type == "cid":
#         return f"{PUBCHEM_API_BASE}/compound/cid/{term}/description/JSON"
#     elif term_type == "formula":
#         return f"{PUBCHEM_API_BASE}/compound/formula/{term}/description/JSON"
#     elif term_type == "name":
#         return f"{PUBCHEM_API_BASE}/compound/name/{term}/description/JSON"
#     else:
#         raise ValueError(f"Unsupported term type: {term_type}")


# def extract_pubchem_descriptions(data):
#     """
#     Extract descriptions from the PubChem API response.
#     """
#     try:
#         descriptions = [
#             item.get("Description", "")
#             for item in data["InformationList"]["Information"]
#             if "Description" in item
#         ]
#         return " ".join(descriptions) if descriptions else None
#     except KeyError:
#         return None


import requests

PUBCHEM_API_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

def fetch_pubchem_data(terms):
    """
    For each term, brute-force all possible 'description' endpoints:
      - /compound/cid/<term>/description/JSON
      - /compound/formula/<term>/description/JSON
      - /compound/name/<term>/description/JSON
    
    Gather any descriptions returned by PubChem.
    """
    context = []
    for term in terms:
        # We'll try all three endpoints for every single term
        endpoints = [
            f"{PUBCHEM_API_BASE}/compound/cid/{term}/description/JSON",
            f"{PUBCHEM_API_BASE}/compound/formula/{term}/description/JSON",
            f"{PUBCHEM_API_BASE}/compound/name/{term}/description/JSON",
        ]

        for url in endpoints:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                descriptions = extract_pubchem_descriptions(response.json())
                if descriptions:
                    # Track which endpoint succeeded, purely for debugging or clarity
                    # You can remove the endpoint label if you don’t need it.
                    label = url.replace(PUBCHEM_API_BASE, "")
                    context.append(f"**Term**: {term}\n**Endpoint**: {label}\n{descriptions}")
            except requests.exceptions.RequestException as e:
                # This includes timeouts, connection errors, and all HTTP errors
                print(f"Error querying PubChem for term '{term}' at '{url}': {e}")
            except ValueError as e:
                # JSON decoding or other data processing errors
                print(f"Error processing response for term '{term}' at '{url}': {e}")

    # Join everything into one big string, separated by blank lines
    return "\n\n".join(context)


def extract_pubchem_descriptions(data):
    """
    Extract 'Description' fields from the PubChem API response.
    """
    try:
        # data["InformationList"]["Information"] is typically a list,
        # each item can contain a "Description" field.
        descriptions = [
            item.get("Description", "")
            for item in data["InformationList"]["Information"]
            if "Description" in item
        ]
        return " ".join(descriptions) if descriptions else None
    except KeyError:
        # If the expected fields aren't found in the JSON, just return None.
        return None
