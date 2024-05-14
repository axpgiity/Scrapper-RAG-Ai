import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph
st.title("This is an Ai Web Scrapper")
st.caption("Powered by OpenAI for Glance")
open_ai_Access_token= st.text_input("OpenAi Access Token" , type="password")
#A radio button created using StreamLit
if open_ai_Access_token:
    model=st.radio(
        "Select gpt Model",
        ["gpt-3.5-turbo","gpt 4"],
        index=0,
    )
    #Configuring Graph to a Dictionary of "llm":which itself contains a dictionary of api_key and selected model.
    graph_config={
        "llm":{
            "api_key":open_ai_Access_token,
            "model":model,
        },
    }
    #code to Scrape the Site
    #to create a text fielf use st.text_input(" ")  | st is an alias for streamlit package(imported)
    url = st.text_input("Enter the URL of the website to be Scraped")
    #request user_promt 
    user_promt = st.text_input("Enter Your Request")
    #now pass the url(as source), prompt(as prompt), graph_config(as the config of the model) in the SmartScraperGraph constructor (imported)
    #creating an object of SmartScraperGraph
    smart_scraper_graph = SmartScraperGraph(
    prompt= user_promt,
    source= url,
    config= graph_config
    )
    if st.button("Scrape"):
      result=smart_scraper_graph.run()
      st.write(result)