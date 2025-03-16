import { useState } from 'react';
import styles from '../styles/TarotCard.module.css';

export default function TarotCard({ card }) {
  const [flipped, setFlipped] = useState(false);
  const isReversed = card.reversed;
  
  // Simplified card back pattern 
  const cardBack = (
    <div className={styles.cardBack}>
      <div className={styles.pattern}>
        <div className={styles.circle}></div>
        <div className={styles.star}></div>
      </div>
    </div>
  );
  
  // Card front with name and simplified visualization
  const cardFront = (
    <div className={styles.cardFront}>
      <h3 className={styles.cardName}>{card.name}</h3>
      <div className={styles.cardInfo}>
        <p className={styles.cardArcana}>{card.arcana} Arcana</p>
        {card.suit && <p className={styles.cardSuit}>Suit of {card.suit}</p>}
      </div>
      <div className={styles.cardSymbol}>
        {getCardSymbol(card)}
      </div>
      {isReversed && <div className={styles.reversedLabel}>Reversed</div>}
    </div>
  );
  
  return (
    <div 
      className={`
        ${styles.card} 
        ${isReversed ? styles.reversed : ''} 
        ${flipped ? styles.flipped : ''}
      `}
      onClick={() => setFlipped(!flipped)}
    >
      <div className={styles.cardInner}>
        {flipped ? cardFront : cardBack}
      </div>
    </div>
  );
}

function getCardSymbol(card) {
  // Get a symbol based on the card type to display a simple visualization
  if (card.arcana === "Major") {
    // Symbols for major arcana cards
    const majorSymbols = {
      "The Fool": "👣",
      "The Magician": "∞",
      "The High Priestess": "☽",
      "The Empress": "♀",
      "The Emperor": "♂",
      "The Hierophant": "⚜",
      "The Lovers": "❤",
      "The Chariot": "⚡",
      "Strength": "🦁",
      "The Hermit": "🔆",
      "Wheel of Fortune": "⚙",
      "Justice": "⚖",
      "The Hanged Man": "🙃",
      "Death": "🦴",
      "Temperance": "⚱",
      "The Devil": "😈",
      "The Tower": "🏢",
      "The Star": "⭐",
      "The Moon": "🌙",
      "The Sun": "☀",
      "Judgment": "📯",
      "The World": "🌍"
    };
    
    return majorSymbols[card.name] || "★";
  } else {
    // Symbols for minor arcana based on suit
    const suitSymbols = {
      "Wands": "🔥",
      "Cups": "💧",
      "Swords": "💨",
      "Pentacles": "🌿"
    };
    
    // For court cards, add a person emoji
    if (["Page", "Knight", "Queen", "King"].some(court => card.name.includes(court))) {
      return `${suitSymbols[card.suit]} 👤`;
    }
    
    // For numbered cards, add the number
    const number = card.name.split(" ")[0];
    if (["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"].includes(number)) {
      return `${suitSymbols[card.suit]} ${getNumberSymbol(number)}`;
    }
    
    return suitSymbols[card.suit] || "★";
  }
}

function getNumberSymbol(numberWord) {
  const numberMap = {
    "Ace": "1",
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5",
    "Six": "6",
    "Seven": "7",
    "Eight": "8",
    "Nine": "9",
    "Ten": "10"
  };
  
  return numberMap[numberWord] || numberWord;
}