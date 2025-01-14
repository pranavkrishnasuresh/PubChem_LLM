import ollama

PROMPT_TEMPLATE = """
You will be answering a chemistry related question. Be detailed and confident, answer the question based on the following context from PubChem.:

{context}

---

Answer the following question based on context provided prior, focus the answer on chemistry basis: {question}
"""


def generate_llm_response(context: str, question: str):
    """
    Use the LLM to generate a response based on the context and question.
    """
    try:
        prompt = PROMPT_TEMPLATE.format(context=context, question=question)

        # Call the Ollama Server Locally with the given model and prompt
        response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])

        return response['message']['content']
    except Exception as e:
        return f"Error during LLM invocation: {e}"