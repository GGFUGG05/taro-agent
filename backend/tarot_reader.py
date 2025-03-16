"""
Tarot card reader functionality
"""
import random
from tarot_database import get_all_cards, get_spread_interpretation
from copy import deepcopy
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TarotReader:
    """
    A class to handle Tarot card readings
    """
    def __init__(self):
        logger.debug("Initializing TarotReader")
        self.all_cards = get_all_cards()
        logger.debug(f"Loaded {len(self.all_cards)} cards")
        if not self.all_cards:
            raise ValueError("Failed to initialize tarot deck - no cards loaded")
        
        # Verify we have the expected number of cards (78 total)
        expected_cards = 78
        if len(self.all_cards) != expected_cards:
            raise ValueError(f"Invalid deck size: expected {expected_cards} cards but got {len(self.all_cards)}")
        
    def shuffle_deck(self):
        """Shuffle the deck of cards"""
        shuffled_deck = self.all_cards.copy()
        random.shuffle(shuffled_deck)
        return shuffled_deck
        
    def draw_cards(self, deck, num_cards=3, allow_reversals=True):
        """
        Draw a specified number of cards from the deck
        
        Args:
            deck (list): The shuffled deck to draw from
            num_cards (int): Number of cards to draw
            allow_reversals (bool): Whether cards can be reversed
            
        Returns:
            list: The drawn cards with possible reversals
        """
        if num_cards > len(deck):
            raise ValueError(f"Cannot draw {num_cards} cards from a deck of {len(deck)} cards")
            
        drawn_cards = []
        for i in range(num_cards):
            card = deepcopy(deck[i])  # Make a deep copy to avoid modifying the original
            
            # Determine if card is reversed
            if allow_reversals and random.random() < 0.5:
                card["is_reversed"] = True
            else:
                card["is_reversed"] = False
                
            drawn_cards.append(card)
            
        return drawn_cards
        
    def three_card_reading(self, spread_type="past-present-future", allow_reversals=True):
        """
        Perform a three-card Tarot reading
        
        Args:
            spread_type (str): Type of three-card spread
                Options: "past-present-future", "situation-obstacle-advice"
            allow_reversals (bool): Whether cards can appear reversed
            
        Returns:
            dict: The reading results including cards and interpretation
        """
        try:
            # Define positions based on spread type
            if spread_type == "past-present-future":
                positions = ["Past", "Present", "Future"]
            elif spread_type == "situation-obstacle-advice":
                positions = ["Situation", "Obstacle", "Advice"]
            else:
                raise ValueError(f"Unknown spread type: {spread_type}")
            
            # Shuffle and draw cards
            shuffled_deck = self.shuffle_deck()
            if not shuffled_deck:
                raise ValueError("Failed to shuffle deck - deck is empty")
            
            drawn_cards = self.draw_cards(shuffled_deck, 3, allow_reversals)
            if len(drawn_cards) != 3:
                raise ValueError(f"Expected 3 cards but got {len(drawn_cards)}")
            
            # Get the interpretation
            interpretation = get_spread_interpretation(drawn_cards, positions, allow_reversals)
            if not interpretation:
                raise ValueError("Failed to generate interpretation")
            
            return {
                "spread_type": spread_type,
                "positions": positions,
                "cards": drawn_cards,
                "allow_reversals": allow_reversals,
                "interpretation": interpretation
            }
        except Exception as e:
            # Log the error for debugging
            print(f"Error in three_card_reading: {str(e)}")
            raise