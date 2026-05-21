!pip uninstall -y langchain langchain-core langchain-community langchain-groq llama-index llama-index-core
!pip cache purge
!pip install -q llama-index llama-index-core llama-index-embeddings-huggingface llama-index-llms-langchain llama-index-readers-file langchain-community langchain-groq pypdf nest_asyncio
!pip install -q llama-index llama-index-core llama-index-embeddings-huggingface llama-index-llms-langchain llama-index-readers-file langchain-community langchain-groq pypdf nest_asyncio openpyxl

import os
import nest_asyncio
from google.colab import userdata
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from langchain_groq import ChatGroq

nest_asyncio.apply()

GROQ_API_KEY = userdata.get("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
print("[INFO] Memuat HuggingFace Embedding Lokal (BAAI/bge-small-en-v1.5)...")

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)
print("[INFO] Menghubungkan ke Groq Cloud LLM (llama-3.1-8b-instant)...")

Settings.llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant",
    temperature=0
)
print("\n🎉 [SUKSES] Seluruh konfigurasi model siap digunakan!")

import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

if not os.path.exists("data") or len(os.listdir("data")) == 0:
    os.makedirs("data", exist_ok=True)
    print("PERINGATAN: Folder 'data' kosong atau tidak ditemukan.")
    print("Silakan upload file PDF Anda ke dalam folder 'data' di panel kiri Google Colab terlebih dahulu, lalu jalankan ulang cell ini.")
else:
    print("[INFO] Membaca file PDF dari folder 'data'...")
    documents = SimpleDirectoryReader("data").load_data()
    print(f"[INFO] Sukses membaca dokumen. Total: {len(documents)} halaman terdeteksi.")
    print("[INFO] Membangun Vector Index di latar belakang...")

    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(similarity_top_k=3)
    print("[INFO] Sistem RAG Berhasil Diaktifkan!")
    print("\n" + "="*50)
    print("🤖 CHATBOT RAG DOKUMEN AKTIF")
    print("Ketik pertanyaan Anda lalu tekan ENTER.")
    print("Ketik 'exit' untuk menyudahi percakapan.")
    print("="*50 + "\n")

    while True:
        question = input("Kamu: ").strip()
        if question.lower() == 'exit':
            print("Sesi chat diakhiri. Sampai jumpa!")
            break
        if not question:
            continue
        print("\n[Sistem]: Sedang mencari referensi di PDF dan merumuskan jawaban...")
        try:
            response = query_engine.query(question)
            print(f"\nBot: {response}")
            print("\n" + "-"*40 + "\n")
        except Exception as e:
            print(f"\n[ERROR]: Terjadi kendala komunikasi dengan API: {e}\n")

