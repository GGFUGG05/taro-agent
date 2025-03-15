import { useState, useRef, useEffect } from 'react';
import styles from '../styles/Home.module.css';

export default function TaroChat() {
  const [question, setQuestion] = useState('');
  const [context, setContext] = useState('');
  const [conversations, setConversations] = useState([]);
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
      
      const response = await fetch('/api/proxy', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          question, 
          context,
          conversation_history: conversationHistory
        }),
      });
      
      if (!response.ok) {
        throw new Error('Failed to get response from Taro');
      }
      
      const data = await response.json();
      
      // Add Taro's response to conversation
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
        { role: 'assistant', content: 'Sorry, there was an error processing your request.' }
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
            <p>Ask Taro a question to start a conversation!</p>
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
                  <span className={styles.typing}>Taro is thinking...</span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
        )}
      </div>
      
      <div className={styles.inputArea}>
        <form onSubmit={handleSubmit} className={styles.form}>
          <div className={styles.inputGroup}>
            <textarea
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              className={styles.textarea}
              placeholder="Ask Taro a question..."
              rows={3}
              required
            />
          </div>
          
          <button type="submit" className={styles.button} disabled={loading || !question.trim()}>
            {loading ? 'Sending...' : 'Send'}
          </button>
        </form>
      </div>
      
      <div className={styles.contextArea}>
        <div className={styles.inputGroup}>
          <label htmlFor="context">Additional context (optional):</label>
          <textarea
            id="context"
            value={context}
            onChange={(e) => setContext(e.target.value)}
            className={styles.contextTextarea}
            rows={2}
          />
        </div>
      </div>
    </div>
  );
}