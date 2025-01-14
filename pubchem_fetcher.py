import requests

PUBCHEM_API_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

def fetch_pubchem_data(terms):
    """
      - /compound/cid/<term>/description/JSON
      - /compound/formula/<term>/description/JSON
      - /compound/name/<term>/description/JSON
    """
    context = []
    for term in terms:
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
                    label = url.replace(PUBCHEM_API_BASE, "")
                    context.append(f"**Term**: {term}\n**Endpoint**: {label}\n{descriptions}")
            except requests.exceptions.RequestException as e:
                # print(f"Error querying PubChem for term '{term}' at '{url}': {e}")
                pass
            except ValueError as e:
                # print(f"Error processing response for term '{term}' at '{url}': {e}")
                pass

    return "\n\n".join(context)


def extract_pubchem_descriptions(data):
    """
    Extract 'Description' fields from the PubChem API response.
    """
    try:
        descriptions = [
            item.get("Description", "")
            for item in data["InformationList"]["Information"]
            if "Description" in item
        ]
        return " ".join(descriptions) if descriptions else None
    except KeyError:
        return None