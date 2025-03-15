from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Taro Agent API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaroRequest(BaseModel):
    question: str
    context: str = ""
    conversation_history: list = []

class TaroResponse(BaseModel):
    answer: str

@app.get("/")
async def root():
    return {"message": "Welcome to the Taro Agent API"}

@app.post("/api/taro", response_model=TaroResponse)
async def taro_agent(request: TaroRequest):
    try:
        # Create a system message defining the Taro agent's behavior
        system_message = """
        You are a Taro Augur, an ancient oracle skilled in the art of taro divination. 
        You guide users in interpreting taro readings, revealing hidden insights, and providing wisdom for their queries. 
        Your responses should be mystical yet clear, blending traditional taro symbolism with intuitive interpretation. 
        Be respectful and insightful, helping the user understand the deeper meanings behind their draws. If the user is unfamiliar with taro, gently introduce them to the practice. Never force predictions but instead offer interpretations that empower the user to reflect and decide their path.
        """
        
        # Create the messages array for the ChatGPT API
        messages = [
            {"role": "system", "content": system_message}
        ]
        
        # Add context if provided
        if request.context:
            messages.append({"role": "system", "content": f"Additional context: {request.context}"})
        
        # Add conversation history
        if request.conversation_history:
            messages.extend(request.conversation_history)
        
        # Add the user's question
        messages.append({"role": "user", "content": request.question})
        
        # Call the OpenAI API
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",  # or whichever model you prefer
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        # Extract and return the assistant's response
        answer = response.choices[0].message.content
        return TaroResponse(answer=answer)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)