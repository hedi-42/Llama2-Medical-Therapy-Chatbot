# Medical Chatbot  

A secure and private medical chatbot that helps users access accurate medical information. It processes medical documents locally and uses AI to provide relevant answers to user queries.  

---

## **Table of Contents**  
1. [Introduction](#introduction)  
2. [Technologies Used](#technologies-used)  
3. [Installation Instructions](#installation-instructions)  
4. [How to Run the Project](#how-to-run-the-project)  
5. [Folder Structure](#folder-structure)  

---

## **Introduction**  

This project is a local, AI-powered medical chatbot that retrieves context from medical PDFs and provides personalized answers. Built with privacy in mind, all data processing happens locally to ensure user data remains secure.  

### **Features**  
- Retrieves and analyzes medical documents in PDF format.  
- Uses embeddings and a vector database (FAISS) for fast search.  
- Responds to medical queries with AI-powered advice.  

---

## **Technologies Used**  

- **Python**: Programming language.  
- **LangChain**: For managing LLM-based workflows.  
- **FAISS**: Vector database for fast similarity search.  
- **Chainlit**: Framework for building conversational UIs.  
- **Hugging Face Sentence Transformers**: For embedding generation.  
- **Llama 2**: Language model for generating responses.  

---

## **Installation Instructions**  

1. **Clone the Repository**:  
    ```bash
    git clone https://github.com/yourusername/medical-chatbot.git
    cd medical-chatbot
    ```

2. **Create a Virtual Environment**:  
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:  
    - On Windows:  
        ```bash
        venv\Scripts\activate
        ```  
    - On Mac/Linux:  
        ```bash
        source venv/bin/activate
        ```  

4. **Install Dependencies**:  
    ```bash
    pip install -r requirements.txt
    ```

---

## **How to Run the Project**  

### **Step 1: Serve the PDF Files**  
Navigate to the `data` folder and serve the PDFs using Python's HTTP server:  
    ```
    cd data
    python -m http.server 8001
    ```

### **Step 2: Process the Medical Documents**  
Go back to the project root folder and run the ingestion script to create the vector database:  
    ```
    cd ..
    python ingest.py
    ```

### **Step 3: Start the Chatbot**  
Run the chatbot with Chainlit:  
    ```
    chainlit run model.py -w
    ```

## **Notes**  
- Ensure the `data` folder contains relevant PDFs before running the ingestion script.  
- The chatbot runs locally, so no data is sent to external servers.  
- For questions or contributions, feel free to open an issue or a pull request.

---

**Enjoy using the Medical Chatbot!** 😊  
