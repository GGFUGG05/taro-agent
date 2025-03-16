import { useState, useEffect } from 'react';
import axios from 'axios';
import styles from '../styles/TarotReading.module.css';
import TarotCard from './TarotCard';
import TarotChat from './TarotChat';

export default function TarotReading() {
  const [question, setQuestion] = useState('');
  const [context, setContext] = useState('');
  const [spreadType, setSpreadType] = useState('past-present-future');
  const [allowReversals, setAllowReversals] = useState(true);
  const [reading, setReading] = useState(null);
  const [loading, setLoading] = useState(false);
  const [conversations, setConversations] = useState([]);
  const [showChat, setShowChat] = useState(false);

  const spreadTypes = {
    'past-present-future': 'Past, Present, Future',
    'situation-obstacle-advice': 'Situation, Obstacle, Advice'
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
        const response = await axios.post('http://localhost:8000/api/tarot/reading', {
            spread_type: spreadType,
            allow_reversals: allowReversals,
            question: question,
            additional_context: context
        });
      
        const data = response.data;
        
        setReading(data);
        setShowChat(false);
        
        // Reset conversations when a new reading is performed
        setConversations([]);
        
        // Add AI interpretation as first message if available
        if (data.ai_interpretation) {
            setConversations([
                { role: 'assistant', content: data.ai_interpretation }
            ]);
            setShowChat(true);
        }
    } catch (error) {
        console.error('Error:', error);
        if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.error('Response data:', error.response.data);
            console.error('Response status:', error.response.status);
            console.error('Response headers:', error.response.headers);
            alert(`Error ${error.response.status}: ${error.response.data.detail || 'Failed to get Tarot reading'}`);
        } else if (error.request) {
            // The request was made but no response was received
            console.error('Request error:', error.request);
            alert('No response received from server. Please try again.');
        } else {
            // Something happened in setting up the request that triggered an Error
            console.error('Error message:', error.message);
            alert('There was an error getting your Tarot reading. Please try again.');
        }
    } finally {
        setLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Taro Tarot Reader</h1>
      
      <div className={styles.readingForm}>
        <form onSubmit={handleSubmit}>
          <div className={styles.formGroup}>
            <label htmlFor="question">Your Question</label>
            <input
              type="text"
              id="question"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="What would you like guidance on?"
              className={styles.input}
            />
          </div>
          
          <div className={styles.formGroup}>
            <label htmlFor="context">Additional Context (optional)</label>
            <textarea
              id="context"
              value={context}
              onChange={(e) => setContext(e.target.value)}
              placeholder="Any additional details about your situation..."
              className={styles.textarea}
              rows={3}
            />
          </div>
          
          <div className={styles.formRow}>
            <div className={styles.formGroup}>
              <label htmlFor="spreadType">Spread Type</label>
              <select
                id="spreadType"
                value={spreadType}
                onChange={(e) => setSpreadType(e.target.value)}
                className={styles.select}
              >
                {Object.entries(spreadTypes).map(([value, label]) => (
                  <option key={value} value={value}>{label}</option>
                ))}
              </select>
            </div>
            
            <div className={styles.formGroup}>
              <label className={styles.checkboxLabel}>
                <input
                  type="checkbox"
                  checked={allowReversals}
                  onChange={(e) => setAllowReversals(e.target.checked)}
                  className={styles.checkbox}
                />
                Allow Reversed Cards
              </label>
            </div>
          </div>
          
          <button 
            type="submit" 
            className={styles.button}
            disabled={loading || !question.trim()}
          >
            {loading ? 'Shuffling Cards...' : 'Get Reading'}
          </button>
        </form>
      </div>
      
      {reading && (
        <div className={styles.readingResult}>
          <h2 className={styles.readingTitle}>
            {spreadTypes[reading.spread_type]} Spread
          </h2>
          
          <div className={styles.cardsContainer}>
            {reading.cards.map((card, index) => (
              <div key={index} className={styles.cardPosition}>
                <h3 className={styles.positionTitle}>{reading.positions[index]}</h3>
                <TarotCard card={card} />
              </div>
            ))}
          </div>
          
          <div className={styles.interpretation}>
            <h3>Card Meanings</h3>
            {reading.interpretation.cards.map((card, index) => (
              <div key={index} className={styles.cardMeaning}>
                <h4>{card.position}: {card.card}</h4>
                <p>{card.meaning}</p>
              </div>
            ))}
            
            <h3>Overall Interpretation</h3>
            <p>{reading.interpretation.narrative}</p>
            
            <h3>Insights</h3>
            <ul className={styles.insights}>
              {reading.interpretation.insights.map((insight, index) => (
                <li key={index}>{insight}</li>
              ))}
            </ul>
            
            <div className={styles.chatToggle}>
              <button 
                className={styles.toggleButton}
                onClick={() => setShowChat(!showChat)}
              >
                {showChat ? 'Hide Chat' : 'Discuss Your Reading'}
              </button>
            </div>
            
            {showChat && (
              <TarotChat 
                reading={reading} 
                conversations={conversations}
                setConversations={setConversations}
              />
            )}
          </div>
        </div>
      )}
    </div>
  );
}