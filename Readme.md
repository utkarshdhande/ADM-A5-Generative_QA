# Generative QA using RAG

We have build a Streamlit application which answers to any questions related to Gaming Laptops using Generative QA

## Installation

Here are the libraries required to run the project:

1. !pip install pytube -q
2. !pip install git+https://github.com/openai/whisper.git -q
3. !pip install -qU openai pinecone-client datasets tqdm

## Usage

1. Clone the repository.
2. Install the libraries by referring requirements.txt file.
3. Run the file 'Streamlit_GenerativeQA.py' and enter the questions related to gaming laptop.

## Streamlit app

[Streamlit App](https://utkarshdhande-adm-a5-generative-q-streamlit-generativeqa-nz4qg2.streamlit.app/)


## Execution

Whisper model is used to transcribe YouTube videos related to Gamig Laptop reviews. The transcriptions are then coverted to vector embeddings. The vector embeddings are stored in Pinecone database. When the user makes any query, the query is converted into vector embeddings using the same model, which is used the pinecone database. The pinecone database returns a response of matching/similar text transriptions from videos.


## Contact

[Utkarsh Dhande](https://github.com/utkarshdhande) and [Parva Shah](https://github.com/parvashah-create)