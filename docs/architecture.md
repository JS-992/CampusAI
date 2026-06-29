# CampusAI - Architecture

## Tech Stack

### Frontend

* **React** – User Interface
* **Tailwind CSS** – Styling
* **Axios** – API Communication

---

### Backend

* **FastAPI** – REST API Backend
* **Python** – Core Programming Language

---

### AI Layer

* **LangChain** – RAG Pipeline
* **OpenAI API** *(Initial LLM)*
* *(Can later replace with Llama/Gemma/Mistral)*

---

### Document Processing

* **PyMuPDF** – PDF Text Extraction
* **python-pptx** – PPT Text Extraction

---

### Vector Database

* **ChromaDB**

  * Stores document embeddings
  * Performs semantic search

---

### Database

* **PostgreSQL**

  * User data
  * Subjects
  * Regulations
  * Uploaded files
  * Quiz history

---

### Development Tools

* **Cursor** – AI Code Editor
* **Git & GitHub** – Version Control
* **Postman / Swagger UI** – API Testing

---

# High-Level Architecture

```
                     Student

                        │

                        ▼

                React Frontend

                        │
                  Axios Requests

                        ▼

               FastAPI Backend

        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼

PostgreSQL Database              AI Pipeline

(User Data, Subjects,        PDF/PPT Processing
Materials, Quizzes)                  │
                                     ▼
                              Extract Text
                                     │
                                     ▼
                                Chunk Text
                                     │
                                     ▼
                              Create Embeddings
                                     │
                                     ▼
                                 ChromaDB
                                     │
                                     ▼
                          Retrieve Relevant Chunks
                                     │
                                     ▼
                               OpenAI / LLM
                                     │
                                     ▼
                              Generate Response
                                     │
                                     ▼
                              FastAPI Response
                                     │
                                     ▼
                              React Frontend
```

---

# Project Workflow

```
Upload PDF/PPT
        │
        ▼
Extract Text
        │
        ▼
Split into Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store in ChromaDB
        │
        ▼
Student asks a question
        │
        ▼
Retrieve relevant chunks
        │
        ▼
LLM generates answer
        │
        ▼
Display response
```

---

# Folder Overview

```
CampusAI/

backend/
frontend/
database/
datasets/
docs/

```

---

# Future Enhancements

* Local LLM Support
* OCR for scanned PDFs
* Voice Assistant
* Attendance Predictor
* GATE Preparation Module
* Video Lesson Generator
* Mobile Application

---
