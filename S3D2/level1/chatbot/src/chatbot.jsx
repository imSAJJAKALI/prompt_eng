import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Chatbot.css'; // You can create a CSS file for styling

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    // Initialize the conversation with a welcome message from the chatbot
    setMessages([
      { text: 'Welcome! How can I assist you today?', type: 'chatbot' },
    ]);
  }, []);

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleSendMessage = async () => {
    if (inputText.trim() === '') return;

    // Create a new message object with the user's input
    const newUserMessage = {
      text: inputText,
      type: 'user',
    };

    // Add the user's message to the chat
    setMessages([...messages, newUserMessage]);
    setInputText('');

    // Send the user's message to OpenAI and receive a response
    setIsLoading(true);

    try {
      const response = await axios.post(
        'https://api.openai.com/v1/engines/davinci/completions',
        {
          prompt: `User: ${inputText}`,
          max_tokens: 50,
        },
        {
          headers: {
            'Authorization': 'Bearer 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', // Replace with your OpenAI API key
            'Content-Type': 'application/json',
          },
        }
      );

      // Extract the chatbot's response from the API response
      const chatbotResponse = response.data.choices[0].text;

      // Create a new message object with the chatbot's response
      const newChatbotMessage = {
        text: chatbotResponse,
        type: 'chatbot',
      };

      // Add the chatbot's response to the chat
      setMessages([...messages, newChatbotMessage]);
    } catch (error) {
      console.error('OpenAI API error:', error);
      // Handle API errors gracefully
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <h1>ChatGPT Chatbot</h1>
      </div>
      <div className="chatbot-messages">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${message.type === 'user' ? 'user' : 'chatbot'}`}
          >
            {message.text}
          </div>
        ))}
        {isLoading && (
          <div className="message chatbot">Chatbot is typing...</div>
        )}
      </div>
      <div className="chatbot-input">
        <input
          type="text"
          placeholder="Type your question..."
          value={inputText}
          onChange={handleInputChange}
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
