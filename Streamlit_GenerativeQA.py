import streamlit as st
import pandas as pd
import pinecone
import openai

# Open AI

openai.api_key = st.secrets['openai_api']
embed_model = "text-embedding-ada-002"

def complete(prompt):
    # query text-davinci-003
    res = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return res['choices'][0]['text'].strip()

def retrieve(query):
    limit = 4000
    res = openai.Embedding.create(
        input=[query],
        engine=embed_model
    )

    # retrieve from Pinecone
    xq = res['data'][0]['embedding']

    # get relevant contexts
    res = index.query(xq, top_k=4, include_metadata=True)
    contexts = [x['metadata']['text'] for x in res['matches']]


    # build our prompt with the retrieved contexts included

    prompt_answer = (
        f"\n\nQuestion: {query} \n Answer:"
    )
    # append contexts until hitting limit
    for i in range(1, len(contexts)):
        if len("\n\n---\n\n".join(contexts[:i])) >= limit:
            prompt = (
                prompt_answer
            )
            break
        elif i == len(contexts)-1:
            prompt = (
                prompt_answer
            )
    return prompt



# Pinecone

index_name = 'openai-youtube-transcriptions'

# initialize connection to pinecone (get API key at app.pinecone.io)
pinecone.init(api_key=st.secrets['pinecone_api'],
              environment="us-west4-gcp"
             )

index = pinecone.Index(index_name)



# Define the app's interface
st.title("Gaming Laptop uaing generative Q&A")
st.header("Question of any gaming laptop")

# Take the user's input query
query = st.text_input("Your question?")

run = st.button('Search')
# Process the user's query and display the results
if query and run:
    query_with_contexts = retrieve(query)

    st.write(query_with_contexts)
    answer = complete(query_with_contexts)
    st.write(f'**:green[{answer}]**')
