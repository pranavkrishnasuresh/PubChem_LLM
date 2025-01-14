**PubChem Knowledge-Enabled LLM**

**1. Clone the Repository**

git clone https://github.com/pranavkrishnasuresh/PubChem_LLM.git

cd PubChem_LLM

**2. Set Up a Python Environment**

Create a new Python virtual environment:
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

**3. Install Dependencies**

Install the required packages using requirements.txt:
pip install -r requirements.txt

**4. Start the Ollama Server**

Ensure the Ollama server is running:
ollama start

**5. Run the Code**

python3 main.py "Your chemistry question here"



**How it Works:**

**Question Parsing:**
The input question is processed to identify nouns and proper nouns using NLP techniques.

**Chemistry Term Identification:**
The extracted terms are checked to find relevant chemistry-related keywords.

**PubChem API Query:**
Identified terms are queried through the PubChem REST API to gather relevant chemical data and context.

**Context-Based Analysis:**
The collected information is fed into the Ollama LLM, which provides a detailed, context-aware response to your question.
