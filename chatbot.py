from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()


initial_messages =[
    {"role": "system", "content": "You are a trip planner in dubai. you are an expertin dubai tourism locations, food, events, hotels etc. you are able to guide users to plan their vacations to dubai.you should  respond professionally. you are name is DubAI, short name D.AI . response shouldn't be exceed 200.Always ask questions to user and help them to plan the trip.finally give a day wise itinerary. deal with user professionally "},
        {
            "role": "assistant",
            "content": "Hello,I am DubAI,your expert trip planner .How can i help you?."
        }
    
]

def get_response_from_llm(messages):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
        
    
    )

    return completion.choices[0].message.content


if "messages" not in st.session_state:
    st.session_state.messages = initial_messages
    
    
st.title("Dubai Trip Assistant")


for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
user_message=st.chat_input("Enter your message")
if user_message:
    new_message={
            "role": "user",
            "content": user_message
        }
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
            st.markdown(new_message["content"])
    
    response=get_response_from_llm(st.session_state.messages)
    if response:
        response_message={
            "role": "assistant",
            "content": response
        }
        st.session_state.messages.append(response_message)
        with st.chat_message(response_message["role"]):
            st.markdown(response_message["content"])
    