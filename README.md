# HA-GPT: HyperActive Generating Pre-trained Transformer Chatbot

## Project Overview
HA-GPT is an AI-powered chatbot application that uses GPT-2 to engage in multi-turn conversations, adapt to context, and provide human-like responses. The chatbot is trained on the Cornell Movie Dialogue Corpus and hosted on Hugging Face. The application consists of a Python Flask backend, a ReactJS frontend, and is deployed online for easy interaction.

### Features:
- **Multi-turn Conversations**: Maintains the context of conversation across multiple turns.
- **Real-time Interaction**: Chat with the AI in real-time using a simple web-based interface.
- **Hugging Face Model Integration**: GPT-2 model fine-tuned and stored on Hugging Face for efficient deployment.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Model Details](#model-details)
4. [Frontend](#frontend)
5. [Backend](#backend)
6. [Links](#links)
7. [Contributing](#contributing)
8. [License](#license)

## Installation

### Prerequisites
Ensure you have the following tools installed on your system:
- Node.js
- Python 3.x
- Flask
- Hugging Face transformers
- ReactJS

### Steps to Run Locally

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Aaron-m-ram/GenAI-Chatbot.git
    cd chat-model-frontend
    ```

2. **Install Frontend Dependencies**:
    ```bash
    npm install
    ```

3. **Start the Frontend**:
    ```bash
    npm start
    ```

4. **Navigate to Backend Folder**:
    ```bash
    cd ../chat-model-backend
    ```

5. **Set Up a Python Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

6. **Install Backend Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

7. **Run the Flask Backend**:
    ```bash
    flask run
    ```

Now, open your browser and navigate to `http://localhost:3000` to interact with the chatbot.

## Model Details
The chatbot uses the GPT-2 model fine-tuned on the Cornell Movie Dialogue Corpus. This model generates context-aware responses, helping the chatbot maintain coherent conversations. The model itself is stored on the hugging face website due to size.

#### Hugging Face Model:
- **Link**: [HA-GPT on Hugging Face](https://huggingface.co/aaronmram/AAI-520-final/tree/main)

## Frontend
The frontend is built using ReactJS and provides a simple, responsive interface for users to chat with the chatbot.

- **Key Features**:
  - Real-time message display.
  - Chatbox for sending messages.
  - Clear chat button for resetting conversations.

The code for the frontend is located in `App.js` and manages the communication between the user and the backend using a simple fetch API call.

## Backend
The backend is implemented using Python Flask. It connects to the Hugging Face GPT-2 model and generates responses for the chatbot.

- **Key Features**:
  - API endpoints for sending user queries and receiving responses from the model.
  - Integration with Hugging Face GPT-2 model.
  
The backend serves the React frontend and handles the logic for processing user input and generating chatbot responses.

For more details on the backend logic, see the `app.py` file.

## Links
- **Live Website**: [HA-GPT Web Application](https://ha-gpt-06cfd0ebfba4.herokuapp.com/)
- **Hugging Face Model**: [HA-GPT Model on Hugging Face](https://huggingface.co/aaronmram/AAI-520-final/tree/main)

## Contributing
Contributions are welcome! Feel free to fork this repository, submit pull requests, or open issues for bugs and feature requests.
