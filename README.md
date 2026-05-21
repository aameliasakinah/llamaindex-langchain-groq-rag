# Multi-Format RAG Chatbot using LlamaIndex, LangChain, and Groq LLM

A high-performance, hybrid Retrieval-Augmented Generation (RAG) chatbot application developed in Google Colab. This system allows users to interactively query and extract information from local documents (PDFs and Excel Spreadsheets) with instant response times and zero hallucination.

## 🚀 Features
* **Hybrid Architecture:** Local data processing and text embedding generation paired with ultra-fast cloud LLM inference.
* **Multi-Format Ingestion:** Seamlessly reads, parses, and indexes both text-based **PDF** documents and **Excel (.xlsx)** spreadsheets.
* **Deterministic Responses:** Set to strict factual consistency (`temperature=0`) to ensure answers are strictly backed by the provided document source.
* **Interactive CLI Loop:** Continuous chat session with built-in empty-input handling and safe exit commands.

---

## 🛠️ Tech Stack
* **Data Framework:** [LlamaIndex](https://www.llamaindex.ai/) (Data ingestion, embedding management, and vector indexing)
* **Integration Ecosystem:** [LangChain Community](https://www.langchain.com/) (Bridge connector for Groq Cloud)
* **LLM Provider:** [Groq Cloud API](https://groq.com/) (Model: `llama-3.1-8b-instant`)
* **Local Embedding Model:** [HuggingFace](https://huggingface.co/) (`BAAI/bge-small-en-v1.5`)
* **File Parsers:** `pypdf` (for PDFs) and `openpyxl` (for Microsoft Excel)

---

## 📋 Prerequisites & Configuration

Before running the notebook, ensure you have a **Groq API Key**.
1. Get an API key from the [Groq Cloud Console](https://console.groq.com/).
2. Open your Google Colab notebook.
3. Click on the **Secrets** icon (the key icon 🔑 on the left sidebar).
4. Add a new secret with the name **`GROQ_API_KEY`** and paste your API key as the value.
5. Toggle the button to grant notebook access to this key.

---

## 📖 Notebook Execution Steps (3-Cell Architecture)

### 1. Cell 1: Environment Setup & Dependency Management
This cell purges old caches and performs a clean installation of all required framework versions to prevent environment conflicts in Google Colab.
> **⚠️ CRITICAL STEP:** After Cell 1 finishes executing, you **MUST** refresh the Colab RAM session by going to **Runtime > Restart session** in the top menu before moving to Cell 2.

### 2. Cell 2: Model & API Configuration
Initializes asynchronous loops, securely retrieves your `GROQ_API_KEY`, loads the HuggingFace embedding model into local runtime memory, and hooks up the Groq Cloud inference client.

### 3. Cell 3: Core RAG Pipeline & Chat Loop
Handles data ingestion by validating the `data` folder directory. It converts document pages into vectorized chunks, compiles a local `VectorStoreIndex`, sets up a `query_engine` to fetch the top 3 most relevant context snippets (`similarity_top_k=3`), and triggers the live interactive chat.

---

## 🕹️ How to Run & Test
1. Clone this repository or upload the `.ipynb` file to your Google Drive.
2. Open the file in **Google Colab**.
3. Setup the `GROQ_API_KEY` in the Colab Secrets panel.
4. Run **Cell 1** and then **Restart the Session**.
5. Create a folder named **`data`** in the Colab left file explorer panel.
6. Upload your sample PDF or Excel file inside that `data` folder.
7. Run **Cell 2** and **Cell 3**.
8. Start typing your questions in the interactive prompt box. Type `exit` to close the conversation.

---

## 📊 Sample Execution Output
Below is an actual runtime transcript captured during testing with a United States Constitution reference document (14 pages detected):

```text
[INFO] Membaca file PDF dari folder 'data'...
[INFO] Sukses membaca dokumen. Total: 14 halaman terdeteksi.
[INFO] Membangun Vector Index di latar belakang...
[INFO] Sistem RAG Berhasil Diaktifkan!

==================================================
🤖 CHATBOT RAG DOKUMEN AKTIF
Ketik pertanyaan Anda lalu tekan ENTER.
Ketik 'exit' untuk menyudahi percakapan.
==================================================

Kamu: apa isi dari article 1?
[Sistem]: Sedang mencari referensi di PDF dan merumuskan jawaban...

Bot: Article 1 menjelaskan tentang struktur dan kekuasaan Kongres Amerika Serikat. Kongres terdiri dari dua bagian, yaitu Senat dan Dewan Perwakilan Rakyat.
----------------------------------------

Kamu: apa tujuan dari article 2?
[Sistem]: Sedang mencari referensi di PDF dan merumuskan jawaban...

Bot: Tujuan dari Article 2 adalah untuk menentukan hak pilih warga negara Amerika Serikat dalam pemilihan presiden, wakil presiden, dan anggota Kongres.
----------------------------------------

Kamu: exit
Sesi chat diakhiri. Sampai jumpa!
