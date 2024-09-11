import gradio as gr
import ollama


def ollama_chat(message, history):
    messages = []

    if len(history) > 0:
        for element in history:
            history_user_message = {
                'role': 'user',
                'content': element[0]
            }
            history_assistant_message = {
                'role': 'assistant',
                'content': element[1]
            }
            messages.append(history_user_message)
            messages.append(history_assistant_message)

    chat_message = {
        'role': 'user',
        'content': message
    }
    messages.append(chat_message)

    stream = ollama.chat(
        model='llama3',
        messages=messages,
        stream=True
    )

    partial_message = ""
    for chunk in stream:
        if len(chunk['message']['content']) != 0:
            partial_message = partial_message + chunk['message']['content']
            yield partial_message


gr.ChatInterface(
    ollama_chat,
    chatbot=gr.Chatbot(),
    title="Jan's Private AI Assistant",
    retry_btn=None,
    undo_btn="Undo",
    clear_btn="Clear",
    # multimodal=True,
).launch()
