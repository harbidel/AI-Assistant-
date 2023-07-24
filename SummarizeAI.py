# import dependecies
import openai
import streamlit as st

# set the GPT-3 api key
openai.api_key = st.secrets['pass']

st.header("Summarizer App using OpenAI + Streamlit")

article_text = st.text_area("Enter your text which you want to summarize")
temp = st.slider("temparature", 0.0,1.0,0.5)

if len(article_text) > 100:
    if st.button("Generate Summary"):
        # Use GPT-3 to generate a summary of the article
        response = openai.Completion.create(
            engine = "text-curie-001",
            prompt = "Please summarize this scientific article for me in a few sentences : " + article_text,
            max_token = 516,
            temperature = temp
        )

        # Print the summary generated

        res = response["choices"][0]["text"]
        st.info(res)

        st.download_button("Download Result", res)
else:
    st.warning("The sentence is not long enough!")