//import logo from "./logo.svg";
import "./App.css";
import React, { useState } from "react";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isSending, setIsSending] = useState(false);

  const sendMessage = async () => {
    if (!input) return;

    setIsSending(true);

    const userMessage = { text: input, sender: "user" };

    setInput("");

    setMessages((prevMessages) => [...prevMessages, userMessage]);

    setTimeout(() => {
      const botMessage = { text: "This is a dummy response.", sender: "bot" };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
      setIsSending(false);
    }, 1000); // 1-second delay

    try {
      // This sends input to the backend
      const response = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: input }), // Send the user input
      });

      const data = await response.json();
      console.log("API Response:", data); // Log the API response to debug s

      // This is the model's response
      const botMessage = { text: data.response, sender: "bot" };

      // Update messages with the user's message and bot's response
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error("Error sending message:", error);
    } finally {
      setIsSending(false);
    }
  };

  // Clear all messages
  const clearChat = () => {
    setMessages([]); // Clear the messages array
  };

  return (
    <div className="chat-container">
      <div className="title-section">
        <h1>HA-GPT Chatbot</h1>
        <h2>HyperActive - Generating Pre-training Transformer Chatbot</h2>
        <button className="clear-button" onClick={clearChat}>
          Clear Chat
        </button>
      </div>
      <div className="messages">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.sender === "user" ? "user" : "bot"}`}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)} // Update input state
          onKeyDown={(e) => e.key === "Enter" && sendMessage()} // Send message on Enter
          placeholder="Type your message..."
        />
        <button onClick={sendMessage} disabled={isSending}>
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
