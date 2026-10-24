!pip install -q gradio
import gradio as gr

def chatbot(message, history):
    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! Welcome to Business Chatbot."
    elif "profit" in msg:
        return "Profit = Selling Price - Cost Price."
    elif "discount" in msg:
        return "Discount = Original Price × Discount % / 100."
    elif "sales" in msg:
        return "Promote products online and offer discounts."
    elif "price" in msg:
        return "Selling Price = Cost Price + Profit."
    else:
        return "Ask me about profit, discount, sales, or price!"

gr.ChatInterface(
    chatbot,
    title="Business Assistant Chatbot",
    description="A simple chatbot for basic business questions."
).launch(share=True)
