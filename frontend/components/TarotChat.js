import { useState, useRef, useEffect } from 'react';
import styles from '../styles/TarotChat.module.css';

export default function TarotChat({ reading, conversations, setConversations }) {
  const [question, setQuestion] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [conversations]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!question.trim()) return;
    
    // Add user message to conversation
    setConversations([...conversations, { role: 'user', content: question }]);
    setLoading(true);
    
    try {
      const conversationHistory = conversations.map(msg => ({
        role: msg.role,
        content: msg.content
      }));
      
      const response = await fetch('/api/proxy/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          reading_result: reading,
          question,
          conversation_history: conversationHistory
        }),
      });
      
      if (!response.ok) {
        throw new Error('Failed to get response from Tarot reader');
      }
      
      const data = await response.json();
      
      // Add Tarot reader's response to conversation
      setConversations([
        ...conversations, 
        { role: 'user', content: question },
        { role: 'assistant', content: data.answer }
      ]);
      
      // Clear input field
      setQuestion('');
    } catch (error) {
      console.error('Error:', error);
      setConversations([
        ...conversations,
        { role: 'user', content: question },
        { role: 'assistant', content: 'Sorry, there was an error processing your request. Please try asking again.' }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.chatContainer}>
      <div className={styles.chatArea}>
        {conversations.length === 0 ? (
          <div className={styles.emptyChat}>
            <p>Ask a question about your Tarot reading</p>
          </div>
        ) : (
          <div className={styles.messages}>
            {conversations.map((msg, index) => (
              <div 
                key={index} 
                className={`${styles.message} ${msg.role === 'user' ? styles.userMessage : styles.assistantMessage}`}
              >
                <div className={styles.messageContent}>
                  {msg.content}
                </div>
              </div>
            ))}
            {loading && (
              <div className={`${styles.message} ${styles.assistantMessage}`}>
                <div className={styles.messageContent}>
                  <span className={styles.typing}>Reading the cards...</span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
        )}
      </div>
      
      <div className={styles.inputArea}>
        <form onSubmit={handleSubmit} className={styles.form}>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            className={styles.input}
            placeholder="Ask about your reading..."
            disabled={loading}
          />
          
          <button 
            type="submit" 
            className={styles.button} 
            disabled={loading || !question.trim()}
          >
            Send
          </button>
        </form>
      </div>
    </div>
  );
}