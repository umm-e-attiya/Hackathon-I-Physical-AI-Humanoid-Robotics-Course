// ChatWidget.jsx
import React, { useState } from "react";
import axios from "axios";

export default function ChatWidget() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    // Add user's message to chat
    const userMessage = { sender: "user", text: input };
    setMessages([...messages, userMessage]);
    setLoading(true);

    try {
      // Call backend /ask endpoint
      const response = await axios.post("http://127.0.0.1:8000/ask", {prompt,});

      const results = response.data.results; // List of SearchResult
      let botText = "";

      if (results.length === 0) {
        botText = "Sorry, I couldn't find an answer.";
      } else {
        // Concatenate top results content
        botText = results.map((r) => r.content).join("\n\n");
      }

      const botMessage = { sender: "bot", text: botText };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      console.error(err);
      const botMessage = {
        sender: "bot",
        text: "There was an error connecting to the backend.",
      };
      setMessages((prev) => [...prev, botMessage]);
    } finally {
      setInput("");
      setLoading(false);
    }
  };

  return (
    <div className="chat-widget">
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={msg.sender === "user" ? "message user" : "message bot"}
          >
            {msg.text}
          </div>
        ))}
        {loading && <div className="message bot">Bot is typing...</div>}
      </div>
      <div className="chat-input">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          placeholder="Ask me something..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
      <style jsx>{`
        .chat-widget {
          width: 350px;
          border: 1px solid #ccc;
          border-radius: 8px;
          padding: 10px;
          font-family: sans-serif;
        }
        .chat-messages {
          height: 300px;
          overflow-y: auto;
          margin-bottom: 10px;
        }
        .message {
          padding: 6px 10px;
          border-radius: 6px;
          margin-bottom: 6px;
          max-width: 80%;
        }
        .message.user {
          background-color: #d1e7ff;
          align-self: flex-end;
        }
        .message.bot {
          background-color: #f1f1f1;
          align-self: flex-start;
        }
        .chat-input {
          display: flex;
        }
        .chat-input input {
          flex: 1;
          padding: 6px 8px;
          border: 1px solid #ccc;
          border-radius: 4px;
        }
        .chat-input button {
          margin-left: 6px;
          padding: 6px 12px;
          border: none;
          background-color: #007bff;
          color: white;
          border-radius: 4px;
          cursor: pointer;
        }
      `}</style>
    </div>
  );
}

