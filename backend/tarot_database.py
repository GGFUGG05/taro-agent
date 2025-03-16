"""
Tarot card database with upright and reversed meanings
"""

TAROT_CARDS = {
    "major_arcana": [
        {
            "name": "The Fool",
            "number": 0,
            "arcana": "Major",
            "suit": None,
            "img": "the_fool.jpg",
            "upright": "New beginnings, innocence, spontaneity, free spirit",
            "reversed": "Recklessness, risk-taking, inconsideration, carelessness"
        },
        {
            "name": "The Magician",
            "number": 1,
            "arcana": "Major",
            "suit": None,
            "img": "the_magician.jpg",
            "upright": "Manifestation, resourcefulness, power, inspired action",
            "reversed": "Manipulation, poor planning, untapped talents, trickery"
        },
        {
            "name": "The High Priestess",
            "number": 2,
            "arcana": "Major",
            "suit": None,
            "img": "the_high_priestess.jpg",
            "upright": "Intuition, sacred knowledge, divine feminine, subconsciousness",
            "reversed": "Secrets, disconnected from intuition, withdrawal, silence"
        },
        {
            "name": "The Empress",
            "number": 3,
            "arcana": "Major",
            "suit": None,
            "img": "the_empress.jpg",
            "upright": "Femininity, beauty, nature, nurturing, abundance",
            "reversed": "Creative block, dependence, emptiness, lack of growth"
        },
        {
            "name": "The Emperor",
            "number": 4,
            "arcana": "Major",
            "suit": None,
            "img": "the_emperor.jpg",
            "upright": "Authority, structure, control, fatherhood, power",
            "reversed": "Domination, excessive control, rigidity, inflexibility"
        },
        {
            "name": "The Hierophant",
            "number": 5,
            "arcana": "Major",
            "suit": None,
            "img": "the_hierophant.jpg",
            "upright": "Tradition, conformity, morality, ethics, education",
            "reversed": "Rebellion, subversiveness, freedom, personal beliefs"
        },
        {
            "name": "The Lovers",
            "number": 6,
            "arcana": "Major",
            "suit": None,
            "img": "the_lovers.jpg",
            "upright": "Love, harmony, relationships, unity, choices",
            "reversed": "Self-love, disharmony, imbalance, misalignment of values"
        },
        {
            "name": "The Chariot",
            "number": 7,
            "arcana": "Major",
            "suit": None,
            "img": "the_chariot.jpg",
            "upright": "Control, willpower, success, action, determination",
            "reversed": "Self-discipline, opposition, lack of direction, aggression"
        },
        {
            "name": "Strength",
            "number": 8,
            "arcana": "Major",
            "suit": None,
            "img": "strength.jpg",
            "upright": "Courage, persuasion, influence, compassion, inner strength",
            "reversed": "Self-doubt, weakness, insecurity, low confidence"
        },
        {
            "name": "The Hermit",
            "number": 9,
            "arcana": "Major",
            "suit": None,
            "img": "the_hermit.jpg",
            "upright": "Soul-searching, introspection, solitude, inner guidance",
            "reversed": "Isolation, loneliness, withdrawal, rejection"
        },
        {
            "name": "Wheel of Fortune",
            "number": 10,
            "arcana": "Major",
            "suit": None,
            "img": "wheel_of_fortune.jpg",
            "upright": "Good luck, karma, life cycles, destiny, turning point",
            "reversed": "Bad luck, resistance to change, breaking cycles, misfortune"
        },
        {
            "name": "Justice",
            "number": 11,
            "arcana": "Major",
            "suit": None,
            "img": "justice.jpg",
            "upright": "Justice, fairness, truth, cause and effect, law",
            "reversed": "Unfairness, lack of accountability, dishonesty, injustice"
        },
        {
            "name": "The Hanged Man",
            "number": 12,
            "arcana": "Major",
            "suit": None,
            "img": "the_hanged_man.jpg",
            "upright": "Surrender, letting go, new perspective, suspension",
            "reversed": "Indecision, delay, resistance, stalling, needless sacrifice"
        },
        {
            "name": "Death",
            "number": 13,
            "arcana": "Major",
            "suit": None,
            "img": "death.jpg",
            "upright": "End of cycle, beginnings, change, transformation, transition",
            "reversed": "Resistance to change, inability to move on, stagnation"
        },
        {
            "name": "Temperance",
            "number": 14,
            "arcana": "Major",
            "suit": None,
            "img": "temperance.jpg",
            "upright": "Balance, moderation, patience, purpose, meaning",
            "reversed": "Imbalance, excess, self-healing, re-alignment, impatience"
        },
        {
            "name": "The Devil",
            "number": 15,
            "arcana": "Major",
            "suit": None,
            "img": "the_devil.jpg",
            "upright": "Bondage, addiction, sexuality, materialism, playfulness",
            "reversed": "Releasing limiting beliefs, exploring dark thoughts, detachment"
        },
        {
            "name": "The Tower",
            "number": 16,
            "arcana": "Major",
            "suit": None,
            "img": "the_tower.jpg",
            "upright": "Sudden change, upheaval, chaos, revelation, awakening",
            "reversed": "Personal transformation, fear of change, avoiding disaster"
        },
        {
            "name": "The Star",
            "number": 17,
            "arcana": "Major",
            "suit": None,
            "img": "the_star.jpg",
            "upright": "Hope, spirituality, renewal, inspiration, serenity",
            "reversed": "Lack of faith, despair, self-trust, disconnection, discouragement"
        },
        {
            "name": "The Moon",
            "number": 18,
            "arcana": "Major",
            "suit": None,
            "img": "the_moon.jpg",
            "upright": "Illusion, fear, anxiety, subconscious, intuition",
            "reversed": "Release of fear, repressed emotion, inner confusion, unhappiness"
        },
        {
            "name": "The Sun",
            "number": 19,
            "arcana": "Major",
            "suit": None,
            "img": "the_sun.jpg",
            "upright": "Positivity, fun, warmth, success, vitality",
            "reversed": "Inner child, feeling down, overly optimistic, temporary depression"
        },
        {
            "name": "Judgment",
            "number": 20,
            "arcana": "Major",
            "suit": None,
            "img": "judgment.jpg",
            "upright": "Judgment, rebirth, inner calling, reflection, reckoning",
            "reversed": "Self-doubt, lack of self-awareness, failure to learn lessons"
        },
        {
            "name": "The World",
            "number": 21,
            "arcana": "Major",
            "suit": None,
            "img": "the_world.jpg",
            "upright": "Completion, achievement, travel, fulfillment, wholeness",
            "reversed": "Lack of completion, shortcuts, delays, emptiness"
        }
    ],
    "minor_arcana": {
        "wands": [
            {
                "name": "Ace of Wands",
                "number": 1,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "ace_of_wands.jpg",
                "upright": "Inspiration, new opportunities, creativity, potential",
                "reversed": "Delays, lack of motivation, self-doubt, creative block"
            },
            {
                "name": "Two of Wands",
                "number": 2,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "two_of_wands.jpg",
                "upright": "Planning, making decisions, leaving home, exploration",
                "reversed": "Fear of change, playing it safe, poor planning, obstacles"
            },
            {
                "name": "Three of Wands",
                "number": 3,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "three_of_wands.jpg",
                "upright": "Expansion, foresight, overseas opportunities, progress",
                "reversed": "Obstacles, delays, frustration, lack of cooperation"
            },
            {
                "name": "Four of Wands",
                "number": 4,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "four_of_wands.jpg",
                "upright": "Celebration, harmony, homecoming, reunion, community",
                "reversed": "Lack of support, instability, discord, incomplete celebrations"
            },
            {
                "name": "Five of Wands",
                "number": 5,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "five_of_wands.jpg",
                "upright": "Conflict, competition, tension, disagreement, diversity",
                "reversed": "Avoiding conflict, cooperation, harmonious resolution"
            },
            {
                "name": "Six of Wands",
                "number": 6,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "six_of_wands.jpg",
                "upright": "Victory, public recognition, progress, self-confidence",
                "reversed": "Failure, egotism, lack of recognition, overconfidence"
            },
            {
                "name": "Seven of Wands",
                "number": 7,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "seven_of_wands.jpg",
                "upright": "Challenge, competition, perseverance, standing your ground",
                "reversed": "Giving up, exhaustion, overwhelmed, retreating from challenge"
            },
            {
                "name": "Eight of Wands",
                "number": 8,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "eight_of_wands.jpg",
                "upright": "Speed, action, air travel, movement, quick decisions",
                "reversed": "Delays, frustration, setbacks, internal disputes, slowing down"
            },
            {
                "name": "Nine of Wands",
                "number": 9,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "nine_of_wands.jpg",
                "upright": "Resilience, courage, persistence, test of faith, boundaries",
                "reversed": "Self-doubt, giving up too soon, failure to prepare, exhaustion"
            },
            {
                "name": "Ten of Wands",
                "number": 10,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "ten_of_wands.jpg",
                "upright": "Burden, responsibility, hard work, stress, achievement",
                "reversed": "Failure to delegate, overly dependant, burnt out, overcommitted"
            },
            {
                "name": "Page of Wands",
                "number": 11,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "page_of_wands.jpg",
                "upright": "Inspiration, enthusiasm, discovery, energy, adventurous",
                "reversed": "Lack of direction, procrastination, inconsistency, hastiness"
            },
            {
                "name": "Knight of Wands",
                "number": 12,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "knight_of_wands.jpg",
                "upright": "Energy, passion, adventure, impulsiveness, self-confidence",
                "reversed": "Haste, scattered energy, frustration, delays, temperamental"
            },
            {
                "name": "Queen of Wands",
                "number": 13,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "queen_of_wands.jpg",
                "upright": "Exuberance, warmth, confidence, independence, social butterfly",
                "reversed": "Demanding, jealous, controlling, smothering, intolerant"
            },
            {
                "name": "King of Wands",
                "number": 14,
                "arcana": "Minor",
                "suit": "Wands",
                "img": "king_of_wands.jpg",
                "upright": "Leadership, vision, entrepreneur, honor, courage",
                "reversed": "Impulsive, domineering, recklessness, ruthless, unforgiving"
            }
        ],
        "cups": [
            {
                "name": "Ace of Cups",
                "number": 1,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "ace_of_cups.jpg",
                "upright": "New love, overflowing emotions, creativity, intuition",
                "reversed": "Blocked creativity, emotional void, emptiness, self-love"
            },
            {
                "name": "Two of Cups",
                "number": 2,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "two_of_cups.jpg",
                "upright": "Partnership, mutual attraction, union, connection, close bonds",
                "reversed": "Imbalanced relationship, disconnection, misunderstanding"
            },
            {
                "name": "Three of Cups",
                "number": 3,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "three_of_cups.jpg",
                "upright": "Celebration, friendship, creativity, community, collaboration",
                "reversed": "Overindulgence, group disconnect, gossip, isolation"
            },
            {
                "name": "Four of Cups",
                "number": 4,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "four_of_cups.jpg",
                "upright": "Apathy, contemplation, disconnection, meditation, re-evaluation",
                "reversed": "Clarity, awakening, new possibilities, epiphany, depression"
            },
            {
                "name": "Five of Cups",
                "number": 5,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "five_of_cups.jpg",
                "upright": "Loss, grief, disappointment, sadness, regret",
                "reversed": "Acceptance, moving on, finding peace, forgiveness"
            },
            {
                "name": "Six of Cups",
                "number": 6,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "six_of_cups.jpg",
                "upright": "Nostalgia, childhood memories, innocence, joy, healing",
                "reversed": "Stuck in the past, unrealistic memories, naive, homesick"
            },
            {
                "name": "Seven of Cups",
                "number": 7,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "seven_of_cups.jpg",
                "upright": "Choices, fantasy, illusion, wishful thinking, imagination",
                "reversed": "Lack of clarity, disorganized, confused, overwhelmed by choices"
            },
            {
                "name": "Eight of Cups",
                "number": 8,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "eight_of_cups.jpg",
                "upright": "Walking away, disillusionment, abandoning ship, leaving behind",
                "reversed": "Avoidance, fear of change, fear of loss, staying in a bad situation"
            },
            {
                "name": "Nine of Cups",
                "number": 9,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "nine_of_cups.jpg",
                "upright": "Contentment, satisfaction, gratitude, emotional fulfillment",
                "reversed": "Dissatisfaction, materialism, self-indulgence, overindulgence"
            },
            {
                "name": "Ten of Cups",
                "number": 10,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "ten_of_cups.jpg",
                "upright": "Divine love, harmony, partnership, alignment of values, joy",
                "reversed": "Broken family, domestic disagreement, unhappiness, misalignment"
            },
            {
                "name": "Page of Cups",
                "number": 11,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "page_of_cups.jpg",
                "upright": "Creative opportunities, intuitive messages, curiosity, possibility",
                "reversed": "Creative blocks, emotional immaturity, insecurity, escapism"
            },
            {
                "name": "Knight of Cups",
                "number": 12,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "knight_of_cups.jpg",
                "upright": "Messenger, romance, following your heart, artistic, reflective",
                "reversed": "Moodiness, disappointment, unrealistic expectations, illusion"
            },
            {
                "name": "Queen of Cups",
                "number": 13,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "queen_of_cups.jpg",
                "upright": "Compassion, calm, comfort, nurturing, emotional security",
                "reversed": "Insecurity, co-dependency, overwhelm, needy, sensitive"
            },
            {
                "name": "King of Cups",
                "number": 14,
                "arcana": "Minor",
                "suit": "Cups",
                "img": "king_of_cups.jpg",
                "upright": "Emotional balance, leadership, compassion, diplomacy, counsel",
                "reversed": "Emotionally manipulative, selfish, moody, withdrawn, cold"
            }
        ],
        "swords": [
            {
                "name": "Ace of Swords",
                "number": 1,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "ace_of_swords.jpg",
                "upright": "Clarity, breakthrough, mental strength, truth, intellectual power",
                "reversed": "Confusion, brutality, chaos, misuse of power, mental cloudiness"
            },
            {
                "name": "Two of Swords",
                "number": 2,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "two_of_swords.jpg",
                "upright": "Difficult choices, stalemate, impasse, balance, avoidance",
                "reversed": "Disillusion, indecision, confusion, breakthrough, clarity"
            },
            {
                "name": "Three of Swords",
                "number": 3,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "three_of_swords.jpg",
                "upright": "Heartbreak, emotional pain, sorrow, grief, hurt",
                "reversed": "Healing, reconciliation, forgiveness, recovery, letting go"
            },
            {
                "name": "Four of Swords",
                "number": 4,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "four_of_swords.jpg",
                "upright": "Rest, recovery, contemplation, recuperation, sanctuary",
                "reversed": "Re-entry, lack of progress, restlessness, burnout, exhaustion"
            },
            {
                "name": "Five of Swords",
                "number": 5,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "five_of_swords.jpg",
                "upright": "Conflict, defeat, winning at all costs, betrayal, hostility",
                "reversed": "Forgiveness, reconciliation, desire to rebuild, making amends"
            },
            {
                "name": "Six of Swords",
                "number": 6,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "six_of_swords.jpg",
                "upright": "Transition, moving forward, personal growth, positive change",
                "reversed": "Unresolved issues, resisting transition, stagnation, backsliding"
            },
            {
                "name": "Seven of Swords",
                "number": 7,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "seven_of_swords.jpg",
                "upright": "Betrayal, deception, strategy, sneakiness, getting away with something",
                "reversed": "Confession, conscience, regret, exposure, remorse"
            },
            {
                "name": "Eight of Swords",
                "number": 8,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "eight_of_swords.jpg",
                "upright": "Imprisonment, restriction, limitation, self-imposed barriers",
                "reversed": "Freedom, self-awareness, empowerment, overcoming obstacles"
            },
            {
                "name": "Nine of Swords",
                "number": 9,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "nine_of_swords.jpg",
                "upright": "Anxiety, worry, fear, depression, nightmares, despair",
                "reversed": "Hope, inner strength, health, pushing through, acceptance"
            },
            {
                "name": "Ten of Swords",
                "number": 10,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "ten_of_swords.jpg",
                "upright": "Painful endings, betrayal, backstabbing, defeat, crisis",
                "reversed": "Recovery, regeneration, resistance, inevitable end, survival"
            },
            {
                "name": "Page of Swords",
                "number": 11,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "page_of_swords.jpg",
                "upright": "Curiosity, thirst for knowledge, new ideas, studious, vigilance",
                "reversed": "Deception, manipulation, lack of clarity, gossip, cynicism"
            },
            {
                "name": "Knight of Swords",
                "number": 12,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "knight_of_swords.jpg",
                "upright": "Action, assertiveness, direct, hasty, intellectual, impulsive",
                "reversed": "Volatile, reckless, oppressive, argumentative, no direction"
            },
            {
                "name": "Queen of Swords",
                "number": 13,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "queen_of_swords.jpg",
                "upright": "Independent, unbiased, clear, perceptive, honest, strong",
                "reversed": "Cold, callous, bitter, malicious, manipulative, uncompromising"
            },
            {
                "name": "King of Swords",
                "number": 14,
                "arcana": "Minor",
                "suit": "Swords",
                "img": "king_of_swords.jpg",
                "upright": "Mental clarity, intellectual power, authority, truth",
                "reversed": "Manipulative, tyrannical, abusive, coldness, corrupted"
            }
        ],
        "pentacles": [
            {
                "name": "Ace of Pentacles",
                "number": 1,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "ace_of_pentacles.jpg",
                "upright": "New opportunities, prosperity, abundance, manifestation, potential",
                "reversed": "Lost opportunity, bad investments, missed chances, scarcity"
            },
            {
                "name": "Two of Pentacles",
                "number": 2,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "two_of_pentacles.jpg",
                "upright": "Balance, adaptability, time management, multitasking, prioritizing",
                "reversed": "Imbalance, disorganization, overwhelmed, messiness, burnout"
            },
            {
                "name": "Three of Pentacles",
                "number": 3,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "three_of_pentacles.jpg",
                "upright": "Teamwork, collaboration, mastery, accomplishment, recognition",
                "reversed": "Lack of teamwork, disorganized, competition, poor workmanship"
            },
            {
                "name": "Four of Pentacles",
                "number": 4,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "four_of_pentacles.jpg",
                "upright": "Security, control, conservatism, scarcity, frugality",
                "reversed": "Generosity, giving, financial insecurity, overprotective"
            },
            {
                "name": "Five of Pentacles",
                "number": 5,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "five_of_pentacles.jpg",
                "upright": "Financial hardship, poverty, insecurity, worry, isolation",
                "reversed": "Recovery, repairing finances, overcoming hardship, spiritual focus"
            },
            {
                "name": "Six of Pentacles",
                "number": 6,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "six_of_pentacles.jpg",
                "upright": "Charity, generosity, sharing, giving and receiving, gratitude",
                "reversed": "Power imbalances, dependency, selfishness, debts, strings attached"
            },
            {
                "name": "Seven of Pentacles",
                "number": 7,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "seven_of_pentacles.jpg",
                "upright": "Long-term success, perseverance, diligence, patience, investment",
                "reversed": "Impatience, wasted efforts, lack of rewards, laziness, meagerness"
            },
            {
                "name": "Eight of Pentacles",
                "number": 8,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "eight_of_pentacles.jpg",
                "upright": "Apprenticeship, education, quality, engagement, skill development",
                "reversed": "Shortcuts, perfectionism, lack of growth, poorly executed work"
            },
            {
                "name": "Nine of Pentacles",
                "number": 9,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "nine_of_pentacles.jpg",
                "upright": "Luxury, self-sufficiency, independence, freedom, garden of delights",
                "reversed": "Codependency, superficiality, façade, living beyond means"
            },
            {
                "name": "Ten of Pentacles",
                "number": 10,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "ten_of_pentacles.jpg",
                "upright": "Wealth, family, establishment, inheritance, permanence",
                "reversed": "Family disputes, financial failure, unstable foundations"
            },
            {
                "name": "Page of Pentacles",
                "number": 11,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "page_of_pentacles.jpg",
                "upright": "Manifestation, financial opportunity, study, diligence, scholarship",
                "reversed": "Lack of focus, procrastination, impractical, dreaminess"
            },
            {
                "name": "Knight of Pentacles",
                "number": 12,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "knight_of_pentacles.jpg",
                "upright": "Patience, responsibility, hard work, reliability, productivity",
                "reversed": "Boredom, laziness, rigidity, perfectionism, obsessiveness"
            },
            {
                "name": "Queen of Pentacles",
                "number": 13,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "queen_of_pentacles.jpg",
                "upright": "Nurturing, practical, providing, abundance, financial security",
                "reversed": "Selfish, greedy, materialistic, neglectful, stingy"
            },
            {
                "name": "King of Pentacles",
                "number": 14,
                "arcana": "Minor",
                "suit": "Pentacles",
                "img": "king_of_pentacles.jpg",
                "upright": "Wealth, success, leadership, stability, business acumen",
                "reversed": "Financially corrupt, poor money management, greedy, stubborn"
            }
        ]
    }
}

# Functions to work with the database
def get_all_cards():
    """Return a flat list of all tarot cards"""
    all_cards = []
    
    # Add major arcana
    all_cards.extend(TAROT_CARDS["major_arcana"])
    
    # Add minor arcana
    for suit in TAROT_CARDS["minor_arcana"]:
        all_cards.extend(TAROT_CARDS["minor_arcana"][suit])
    
    return all_cards

def get_card_by_name(name):
    """Find a card by its name"""
    all_cards = get_all_cards()
    for card in all_cards:
        if card["name"] == name:
            return card
    return None

def generate_narrative(card_interpretations, stats):
    """Generate a cohesive narrative based on the cards and their positions"""
    narrative = "Your reading reveals "
    
    # First, check for significant patterns
    if stats["major_arcana_count"] >= 2:
        narrative += "significant forces at work in your life. "
    
    # Identify the dominant suit, if any
    dominant_suit = None
    max_count = 0
    for suit, count in stats["suits"].items():
        if count > max_count:
            max_count = count
            dominant_suit = suit
    
    if max_count >= 2:
        suit_meanings = {
            "Wands": "creativity and passion",
            "Cups": "emotions and relationships",
            "Swords": "thoughts and challenges",
            "Pentacles": "material concerns and practical matters"
        }
        narrative += f"There is a strong emphasis on {suit_meanings[dominant_suit]} in your current situation. "
    
    # Connect the cards in a story
    if len(card_interpretations) >= 3:
        past = card_interpretations[0]
        present = card_interpretations[1]
        future = card_interpretations[2]
        
        narrative += f"{past['card']} in your {past['position']} has led to your current situation with {present['card']}. "
        narrative += f"This is leading toward {future['card']} in your future. "
    
    # Look for contrasting energies
    has_contrasting_energies = False
    contrasting_pairs = [
        (["The Tower", "Death", "Ten of Swords"], ["The Sun", "The Star", "Ten of Cups"]),
        (["The Chariot", "Knight of Wands"], ["The Hanged Man", "Four of Swords"]),
        (["The Hermit"], ["Three of Cups", "The Lovers"])
    ]
    
    for pair in contrasting_pairs:
        group1_found = any(card["card"].split(" (")[0] in pair[0] for card in card_interpretations)
        group2_found = any(card["card"].split(" (")[0] in pair[1] for card in card_interpretations)
        
        if group1_found and group2_found:
            has_contrasting_energies = True
            break
    
    if has_contrasting_energies:
        narrative += "There are contrasting energies at play, suggesting a period of transition or internal conflict. "
    
    return narrative.strip()

def generate_insights(card_interpretations, stats):
    """Generate actionable insights based on the reading"""
    insights = []
    
    # Generate specific insights based on card combinations
    if len(card_interpretations) >= 3:
        past = card_interpretations[0]
        present = card_interpretations[1]
        future = card_interpretations[2]
        
        # Example insight based on past and present
        past_card_name = past["card"].split(" (")[0]
        present_card_name = present["card"].split(" (")[0]
        future_card_name = future["card"].split(" (")[0]
        
        is_past_reversed = "(Reversed)" in past["card"]
        is_present_reversed = "(Reversed)" in present["card"]
        is_future_reversed = "(Reversed)" in future["card"]
        
        # Create personalized insight based on the specific cards
        insight = f"Your {past_card_name}{' (Reversed)' if is_past_reversed else ''} in the past has influenced your current experience of {present_card_name}{' (Reversed)' if is_present_reversed else ''}. "
        
        # Add action suggestion based on future card
        if is_future_reversed:
            insight += f"To overcome the challenges of {future_card_name} Reversed in your future, consider "
        else:
            insight += f"To embrace the energy of {future_card_name} in your future, try "
        
        # Add specific action based on the future card
        if "Swords" in future_card_name:
            insight += "approaching situations with clarity and direct communication."
        elif "Cups" in future_card_name:
            insight += "opening yourself to emotional connections and creative inspiration."
        elif "Wands" in future_card_name:
            insight += "pursuing your passions and taking inspired action."
        elif "Pentacles" in future_card_name:
            insight += "focusing on practical matters and building stable foundations."
        elif future_card_name in ["The Fool", "The Sun", "The Star"]:
            insight += "embracing new beginnings with optimism and faith."
        elif future_card_name in ["The Tower", "Death", "The Moon"]:
            insight += "surrendering to necessary changes and trusting the process of transformation."
        else:
            insight += "reflecting on the specific meaning of this card and how it relates to your situation."
        
        insights.append(insight)
    
    # Add a general insight based on the overall spread
    if stats["major_arcana_count"] >= 2:
        insights.append("The presence of multiple Major Arcana cards suggests this is a significant time in your life with important lessons and experiences. Pay attention to the themes they represent.")
    
    return insights

def get_spread_interpretation(cards, positions, allow_reversals=True):
    """
    Generate an interpretation for a spread of cards
    
    Args:
        cards (list): List of card dictionaries
        positions (list): List of position names (e.g., ["Past", "Present", "Future"])
        allow_reversals (bool): Whether cards can appear reversed
        
    Returns:
        dict: Interpretation data including individual card meanings and overall narrative
    """
    # Validate inputs
    if not cards or not positions:
        raise ValueError("Cards and positions must not be empty")
    if len(cards) != len(positions):
        raise ValueError(f"Number of cards ({len(cards)}) must match number of positions ({len(positions)})")
    
    # Count card types for pattern recognition
    card_stats = {
        "major_arcana_count": 0,
        "suits": {
            "Wands": 0,
            "Cups": 0,
            "Swords": 0,
            "Pentacles": 0
        }
    }
    
    # Build individual card interpretations
    card_interpretations = []
    
    for i, card in enumerate(cards):
        position = positions[i]
        is_reversed = card.get("is_reversed", False)
        
        # Update statistics
        if card["arcana"] == "Major":
            card_stats["major_arcana_count"] += 1
        elif card["suit"]:
            card_stats["suits"][card["suit"]] += 1
        
        # Get meaning based on orientation
        meaning = card["reversed"] if is_reversed else card["upright"]
        
        # Create interpretation for this card
        card_interpretation = {
            "position": position,
            "card": f"{card['name']}{' (Reversed)' if is_reversed else ''}",
            "meaning": meaning,
            "interpretation": f"In the {position} position, {card['name']}{' (Reversed)' if is_reversed else ''} suggests {meaning}."
        }
        
        card_interpretations.append(card_interpretation)
    
    # Generate overall narrative based on card combinations and patterns
    narrative = generate_narrative(card_interpretations, card_stats)
    
    # Generate actionable insights
    insights = generate_insights(card_interpretations, card_stats)
    
    return {
        "cards": card_interpretations,
        "narrative": narrative,
        "insights": insights,
        "stats": card_stats
    }

