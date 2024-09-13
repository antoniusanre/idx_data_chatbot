
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
import streamlit as st
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import SystemMessage, trim_messages
from operator import itemgetter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


model = ChatGroq(model="llama3-8b-8192")

trimmer = trim_messages(
    max_tokens=65,
    strategy="last",
    token_counter=model,
    include_system=True,
    allow_partial=False,
    start_on="human",
)
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability in {language}.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

config = {"configurable": {"session_id": "tes"}}
chain = (RunnablePassthrough.assign(messages=itemgetter("messages") | trimmer) | prompt|model)

with_message_history = RunnableWithMessageHistory(chain, get_session_history, input_messages_key="messages")

config = {"configurable": {"session_id": "abc20"}}

st.title("🤵:red[Personal] Assistant")
if "memory" not in st.session_state:
    st.session_state.memory = []

def generate_response(input_text):
    response = with_message_history.invoke(
        {
            "messages": st.session_state.memory + [HumanMessage(content=input_text)],
            "language": "English",
        },
        config=config,
    )
    st.session_state.memory.append(HumanMessage(content = input_text))
    st.info(response.content)
    return response.content

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


response = None
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    stream = None
    try:
        with st.chat_message("assistant"):
            stream = generate_response(prompt)
            st.session_state.messages.append({"role": "assistant", "content": stream})
    except:
        st.warning("I'm sorry there's an error while processing your query. I can help you with other queries.")