import streamlit as st


# title
st.title("Streamlit Code Base")

# remarks
st.markdown("""
             Remember to set the following in your .streamlit/secrets.toml file:
             * OPENAI_API_KEY
            * PINECONE_API_KEY, PINECONE_API_ENV, PINECONE_INDEX_NAME
            * If using EMAIL, SENDGRID_API_KEY
            * If using Dataframe, DATAFRAME_CSV as the URL for the corresponding CSV file 
            * If using the Quiz App, QUIZ_CSV as the name of the CSV file with Quiz data....
             """)