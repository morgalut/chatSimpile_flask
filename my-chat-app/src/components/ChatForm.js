// ChatForm.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ChatForm = () => {
    const [message, setMessage] = useState('');
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        const fetchMessages = async () => {
            try {
                const response = await axios.get('http://localhost:5000/get_messages');
                setMessages(response.data.messages || []);
            } catch (error) {
                console.error('Error:', error);
            }
        };

        fetchMessages();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/send_message', { message });
            console.log(response.data);
            // After sending the message, fetch the updated list of messages
            const updatedResponse = await axios.get('http://localhost:5000/get_messages');
            setMessages(updatedResponse.data.messages || []);
            setMessage('');
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} />
                <button type="submit">Send</button>
            </form>
            <ul>
                {messages.map((msg, index) => (
                    <li key={index}>{msg}</li>
                ))}
            </ul>
        </div>
    );
};

export default ChatForm;
