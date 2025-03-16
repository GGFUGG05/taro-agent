from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
from tarot_reader import TarotReader
import json
from typing import List, Optional

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Tarot Reader API")

# Initialize the Tarot reader
tarot_reader = TarotReader()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TarotRequest(BaseModel):
    spread_type: str = "past-present-future"
    allow_reversals: bool = True
    question: Optional[str] = None
    additional_context: Optional[str] = None

class TarotResponse(BaseModel):
    spread_type: str
    positions: List[str]
    cards: List[dict]
    allow_reversals: bool
    interpretation: dict
    ai_interpretation: Optional[str] = None

class TarotChatRequest(BaseModel):
    reading_result: dict
    question: str
    conversation_history: list = []

class TarotChatResponse(BaseModel):
    answer: str

@app.get("/")
async def root():
    return {"message": "Welcome to the Tarot Reader API"}

@app.post("/api/tarot/reading", response_model=TarotResponse)
async def get_tarot_reading(request: TarotRequest):
    try:

        # Perform the Tarot reading
        reading_result = tarot_reader.three_card_reading(
            spread_type=request.spread_type,
            allow_reversals=request.allow_reversals
        )
        
        # Generate an AI interpretation if a question was provided
        if request.question:
            ai_interpretation = await generate_ai_interpretation(
                reading_result, 
                request.question,
                request.additional_context
            )
            reading_result["ai_interpretation"] = ai_interpretation

            print(f"AI interpretation generated successfully")
        
        return reading_result
    
    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/tarot/chat", response_model=TarotChatResponse)
async def chat_about_reading(request: TarotChatRequest):
    try:
        # Create the messages array for the ChatGPT API
        messages = [
            {"role": "system", "content": get_tarot_system_prompt()}
        ]
        
        # Add reading result as context
        reading_context = format_reading_for_chat(request.reading_result)
        messages.append({"role": "system", "content": f"Tarot reading context: {reading_context}"})
        
        # Add conversation history
        if request.conversation_history:
            messages.extend(request.conversation_history)
        
        # Add the user's question
        messages.append({"role": "user", "content": request.question})
        
        # Call the OpenAI API
        try:
            # Using the new client format for OpenAI
            client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model="gpt-4",  # or whichever model you prefer
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            answer = response.choices[0].message.content
        except AttributeError:
            # Fallback to older API format if the above fails
            response = await openai.ChatCompletion.acreate(
                model="gpt-4",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            answer = response.choices[0].message.content
            
        return TarotChatResponse(answer=answer)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def generate_ai_interpretation(reading_result, question, additional_context=None):
    """Generate an AI interpretation of the Tarot reading"""
    try:
        # Format the reading for the AI
        reading_context = format_reading_for_chat(reading_result)
        
        # Create the messages array for the ChatGPT API
        messages = [
            {"role": "system", "content": get_tarot_system_prompt()},
            {"role": "system", "content": f"Tarot reading context: {reading_context}"}
        ]
        
        # Add additional context if provided
        if additional_context:
            messages.append({"role": "system", "content": f"Additional context: {additional_context}"})
        
        # Add the user's question
        prompt = f"I've done a {reading_result['spread_type']} tarot reading and want your interpretation about this question: {question}"
        messages.append({"role": "user", "content": prompt})
        
        # Call the OpenAI API
        try:
            # Using the new client format for OpenAI
            client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                temperature=0.7,
                max_tokens=800
            )
            answer = response.choices[0].message.content
        except AttributeError:
            # Fallback to older API format if the above fails
            response = await openai.ChatCompletion.acreate(
                model="gpt-4",
                messages=messages,
                temperature=0.7,
                max_tokens=800
            )
            answer = response.choices[0].message.content
            
        return answer
    
    except Exception as e:
        print(f"Error generating AI interpretation: {str(e)}")
        return f"I couldn't generate an interpretation. Error: {str(e)}"

def format_reading_for_chat(reading_result):
    """Format the reading result for the AI chat context"""
    spread_type = reading_result["spread_type"]
    positions = reading_result["positions"]
    cards = reading_result["cards"]
    interpretation = reading_result["interpretation"]
    
    # Format cards info
    cards_info = []
    for i, card in enumerate(cards):
        position = positions[i]
        reversed_text = "(Reversed)" if card.get("reversed", False) else ""
        card_info = f"{position}: {card['name']} {reversed_text}"
        cards_info.append(card_info)
    
    # Format card interpretations
    card_interpretations = []
    for card_interp in interpretation["cards"]:
        card_interpretations.append(f"{card_interp['position']} - {card_interp['card']}: {card_interp['meaning']}")
    
    # Format the overall narrative and insights
    narrative = interpretation["narrative"]
    insights = "\n".join([f"- {insight}" for insight in interpretation["insights"]])
    
    # Combine everything into a readable format
    formatted_reading = f"""
Spread Type: {spread_type}
Cards:
{chr(10).join(cards_info)}

Card Interpretations:
{chr(10).join(card_interpretations)}

Overall Narrative:
{narrative}

Actionable Insights:
{insights}
"""
    
    return formatted_reading

def get_tarot_system_prompt():
    """Get the system prompt for Tarot interpretations"""
    return """
You are an experienced Tarot reader with deep knowledge of card meanings, symbolism, and interpretation techniques. Your role is to provide insightful, thoughtful Tarot interpretations based on the cards presented.

Guidelines:
1. Provide authentic interpretations based on traditional Tarot meanings
2. Consider card positions and their significance in the spread
3. Take reversed cards into account when applicable
4. Look for patterns, suit concentrations, and interactions between cards
5. Be sensitive and respectful while being honest about challenging cards
6. Frame interpretations in a way that empowers the querent
7. Avoid making absolute predictions about the future
8. Respect that Tarot is a tool for reflection and guidance, not fortune-telling
9. When discussing Major Arcana cards, emphasize their significance as important life lessons or significant forces
10. Provide actionable insights when possible

Remember that your interpretation should weave together the meaning of individual cards into a cohesive narrative that addresses the querent's question or situation.
"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)