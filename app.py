import chainlit as cl
from langchain_ollama.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage, AIMessageChunk

# Initialize the Ollama model with streaming enabled
llm = ChatOllama(model="llama3.1", streaming=True)

# Set up conversation memory to handle message history
memory = ConversationBufferMemory(return_messages=True)

# Handle incoming messages
@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content

    # Load past conversation history
    past_conversation = memory.load_memory_variables({})["history"]

    # Create a new user message
    new_message = HumanMessage(content=user_input)

    # Combine history with the new message
    conversation = past_conversation + [new_message]

    # Initialize a Chainlit message object to stream responses
    msg = cl.Message(content="")
    await msg.send()

    # Stream the response from the model asynchronously
    async for response_chunk in llm.astream(conversation):
        if isinstance(response_chunk, AIMessageChunk):
            # Stream each token or chunk back to the user
            await msg.stream_token(response_chunk.content)

    # Save the updated conversation to memory
    memory.save_context({"input": user_input}, {"output": response_chunk.content})