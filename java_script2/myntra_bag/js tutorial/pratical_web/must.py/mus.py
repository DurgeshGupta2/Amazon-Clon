import textwrap
import google.generativeai as genai
from IPython.display import display, Markdown

def to_markdown(text):
    return Markdown(textwrap.indent(text.replace('.', '*'), '> ', predicate=lambda _: True))

def configure_generative_ai(api_key):
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"Error configuring generative AI: {e}")

def generate_and_display_content(prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        display(to_markdown(response.text))
        return response.text
    except Exception as e:
        print(f"Error generating content: {e}")
        return None

# Replace 'YOUR_API_KEY' with your actual API key
api_key = "YOUR_API_KEY"  # Replace with your API key for the Gemini API

# Configuration
configure_generative_ai(api_key)

# Model Usage
while True:
    conversation_history = ""
    while True:
        prompt = input("You: ")
        if prompt.lower() == 'exit':
            print("Goodbye!")
            break
        elif prompt.lower() == 'clear':
            conversation_history = ""
            print("Conversation cleared.")
        else:
            conversation_history += "\n" + prompt
            conversation_history = generate_and_display_content(conversation_history)
            if conversation_history is None:
                break
