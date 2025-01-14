import argparse
from query_chemistry import query_chemistry_related

def main():
    # Parse CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Process the query
    response = query_chemistry_related(query_text)
    print(response)


if __name__ == "__main__":
    main()