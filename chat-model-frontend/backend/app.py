from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


app = Flask(__name__)
CORS(app)

# Define the paths where the model and tokenizer are saved
#gpt_model_path = r"backend/gpt_model_3"
#gpt_model_path = r"C:\Users\User\Documents\AAI Masters Program\AAI 520\FinalProject\GenAI-Chatbot\chat-model-frontend\backend\gpt_model_3"
#gpt_tokenizer_path = r"backend/gpt_tokenizer_3"
#gpt_tokenizer_path = r"C:\Users\User\Documents\AAI Masters Program\AAI 520\FinalProject\GenAI-Chatbot\chat-model-frontend\backend\gpt_tokenizer_3"

# model = GPT2LMHeadModel.from_pretrained(gpt_model_path)
# tokenizer = GPT2Tokenizer.from_pretrained(gpt_tokenizer_path)
model = GPT2LMHeadModel.from_pretrained('aaronmram/AAI-520-final')
tokenizer = GPT2Tokenizer.from_pretrained('aaronmram/AAI-520-final')

model.eval()

# # Check for GPU availability and move the model to the appropriate device
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)

# Define fallback responses
fallback_responses = [
    "I'm not sure how to respond to that.",
    "Can you please rephrase your question?",
    "That's an interesting point! Tell me more.",
    "I'm still learning. Can you clarify?",
    "I don't have the answer to that right now.",
    "That's a good question! Let me think about it."
]

# Helper function to ensure punctuation


def ensure_punctuation(input_text):
    if input_text and input_text[-1] not in ['.', '!', '?']:
        return input_text + '.'
    return input_text

# Helper function to strip echoed input from response


def strip_echo(user_input, response):
    user_input_lower = user_input.lower()
    if user_input_lower in response.lower():
        response_cleaned = response.replace(user_input, '').strip()
        return response_cleaned
    return response


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')

    # Ensure the input has punctuation
    user_input = ensure_punctuation(user_input)

    # Tokenize the input
    inputs = tokenizer(user_input, return_tensors="pt",
                       padding=True, truncation=True, max_length=100)
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    # Generate a response
    with torch.no_grad():
        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=100,
            temperature=0.3,   # Increase randomness
            top_k=50,          # Limit to top 50 predictions
            top_p=0.7,        # Nucleus sampling with p=0.95
            do_sample=True     # Enable sampling
        )

    # Decode and clean the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Clean the response to avoid unwanted tokens
    response_cleaned = response.strip()
    response_cleaned = response_cleaned.replace(
        '[USER]', '').replace('[BOT]', '').replace('SEP', '').strip()

    # Strip echoed parts from the response
    response_cleaned = strip_echo(user_input, response_cleaned)

    # Use a fallback if the response is empty or nonsensical
    if not response_cleaned or "I'm sorry" in response_cleaned:
        response_cleaned = fallback_responses[0]  # Default fallback

    # Return the response to the frontend
    return jsonify({'response': response_cleaned})


if __name__ == '__main__':
    app.run(port=5000, debug=True)


# model = GPT2LMHeadModel.from_pretrained(gpt_model_path)
# tokenizer = GPT2Tokenizer.from_pretrained(gpt_tokenizer_path)


# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     user_message = data.get('message')

#     bot_response = f"Bot received: {user_message}"

#     return jsonify({'response': bot_response})


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
