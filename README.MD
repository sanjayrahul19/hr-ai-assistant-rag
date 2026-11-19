# HR AI Assistant

An AI-powered HR assistant built with **Python, FastAPI, LangChain, OpenAI and ChromaDB**. It answers HR policy questions using Retrieval-Augmented Generation (RAG) and handles employee-specific queries using custom tools.

This project was built as a hands-on learning project to understand LLM integration, RAG pipelines, vector databases, tool calling and API development.

## Features

- **HR Policy Questions:** Retrieves relevant information from an employee handbook PDF using RAG.
- **Employee Lookup:** Retrieves employee information using a custom tool.
- **Leave Balance:** Calculates remaining casual, sick and earned leave.
- **Leave Eligibility:** Checks leave eligibility based on employee details, leave type and requested dates.
- **LLM Tool Selection:** Uses an LLM to determine which tool is appropriate for a user's question.
- **REST API:** Exposes the assistant through a FastAPI endpoint.
- **Input Validation:** Uses Pydantic to validate incoming API requests.
- **Error Handling:** Handles API processing errors and logs exceptions.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API |
| LangChain | LLM integration and tool calling |
| OpenAI GPT-4.1-mini | Language model |
| OpenAI Embeddings | Text embeddings |
| ChromaDB | Vector database |
| PyPDF | PDF text extraction |
| Pydantic | Data validation |
| python-dotenv | Environment configuration |

## Architecture

The assistant uses two information sources:

1. **Employee Handbook (RAG):** Loads the handbook PDF, splits it into chunks, generates embeddings and stores them in ChromaDB. Relevant chunks are retrieved when a user asks an HR policy question.
2. **Mock Employee Data (Tools):** Uses Python employee records to answer employee lookup, leave balance and leave eligibility questions.

The LLM selects the appropriate tool based on the user's question and generates the final response.

## Project Structure

```text
hr-ai-assistant/
│
├── src/
│   ├── agent/
│   │   └── hr_agent.py
│   │
│   ├── api/
│   │   └── chat.py
│   │
│   ├── data/
│   │   └── mock_employee_data.py
│   │
│   ├── rag/
│   │   ├── document_loader.py
│   │   ├── text_splitter.py
│   │   ├── embedding_model.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── rag_chain.py
│   │   └── rag_tool.py
│   │
│   ├── tools/
│   │   ├── employee_tools.py
│   │   └── leave_tools.py
│   │
│   ├── config.py
│   └── main.py
│
├── data/
│   ├── handbook/
│   │   └── employee_handbook.pdf
│   │
│   └── chroma_db/
│
├── tests/
│
├── .env
├── .gitignore
└── requirements.txt
```

## How It Works

### 1. RAG Pipeline

The employee handbook PDF goes through the following process:

```text
Employee Handbook PDF
        ↓
   PDF Loading
        ↓
   Text Splitting
        ↓
    Embeddings
        ↓
     ChromaDB
        ↓
   Similarity Search
        ↓
 Relevant Documents
        ↓
    LLM Response
```

### 2. Tool Calling

The assistant has four tools:

| Tool | Responsibility |
|---|---|
| `search_employee_handbook` | Searches HR policies in the handbook |
| `get_employee` | Retrieves employee information |
| `calculate_leave_balance` | Calculates remaining leave |
| `check_leave_eligibility` | Checks leave eligibility |

The LLM decides which tool to invoke based on the user's question.

### 3. API Request Flow

```text
User
  ↓
FastAPI Endpoint
  ↓
ChatRequest Validation
  ↓
HR Agent
  ↓
LLM Tool Selection
  ↓
RAG / Employee Tools
  ↓
LLM Generates Answer
  ↓
ChatResponse
  ↓
User
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/hr-ai-assistant-rag.git

cd hr-ai-assistant-rag
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4.1-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
```

Replace `your_openai_api_key` with your OpenAI API key.

**Important:** Never commit your `.env` file or expose your API key.

### 5. Add the Employee Handbook

Place the employee handbook PDF here:

```text
data/handbook/employee_handbook.pdf
```

The handbook used in this project contains fictional HR policies and employee information.

### 6. Run the Application

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

### POST `/api/chat`

Send a question to the HR assistant.

**Request:**

```json
{
  "question": "How many casual leaves are allowed annually?"
}
```

**Response:**

```json
{
  "answer": "Employees are entitled to 12 casual leave days annually."
}
```

### Example Questions

**HR Policy Questions**

- How many casual leaves are allowed annually?
- What are the working hours?
- What are the employee benefits?

**Employee Questions**

- Show employee 101's details.
- What is employee 101's department?

**Leave Management Questions**

- What is employee 101's remaining leave balance?
- Is employee 101 eligible for casual leave?

**Unsupported Policy Questions**

- What is the maternity leave policy?

If the handbook does not contain the requested information, the assistant should not invent a policy.

## Testing

Run individual test modules using Python:

```bash
python -m tests.test_document_loader
python -m tests.test_document_splitter
python -m tests.test_embeddings
python -m tests.test_vector_store
python -m tests.test_retriever
python -m tests.test_rag_tool
python -m tests.test_hr_agent
```

Run the FastAPI application and test the endpoint through Swagger UI at `/docs`.

## Key Concepts Learned

- Integrating a pretrained LLM through the OpenAI API
- Prompt engineering
- Retrieval-Augmented Generation (RAG)
- PDF document loading and text chunking
- Text embeddings and vector similarity search
- ChromaDB vector storage and retrieval
- LangChain custom tools
- LLM-based tool selection
- Pydantic validation
- FastAPI REST API development
- Logging and exception handling

## Limitations

This is a learning project, not a production-ready HR system.

- Employee records are stored in a Python dictionary.
- The employee handbook contains fictional information.
- No authentication or authorization is implemented.
- No real leave application or approval workflow exists.
- Leave calculations exclude public holidays and company-specific rules.
- No persistent conversation memory is implemented.
- The PDF loader does not perform OCR on scanned documents.

## Disclaimer

This project uses fictional employee data and sample HR policies for educational purposes only. It is not intended for actual HR operations.