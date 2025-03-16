# The Tarot Oracle 🔮

A modern web application that provides interactive tarot card readings with AI-powered interpretations. This project combines traditional tarot wisdom with modern technology to deliver insightful and personalized readings.

## Features ✨

- **Interactive Tarot Readings**: Get three-card readings with beautiful card animations
- **Multiple Spread Types**:
  - Past, Present, Future
  - Situation, Obstacle, Advice
- **Reversible Cards**: Option to include reversed card meanings for deeper insights
- **Progressive Reveal**: Dramatic card reveal sequence with smooth animations
- **AI Interpretation**: Get detailed interpretations of your reading
- **Interactive Chat**: Discuss your reading with an AI assistant for deeper understanding

## Tech Stack 🛠️

### Frontend
- Next.js
- React
- Axios for API calls
- CSS Modules for styling
- Modern animation techniques

### Backend
- Python
- FastAPI
- AI integration for interpretations
- Comprehensive tarot card database

## Getting Started 🚀

### Prerequisites
- Node.js (v14 or higher)
- Python (v3.8 or higher)
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/GGFUGG05/tarot-agent.git
cd tarot-agent
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# In frontend/.env.local
NEXT_PUBLIC_API_URL=http://localhost:8000

# Create backend/.env
# Add your open-ai key here
```

### Running the Application

1. Start the backend server:
```bash
cd backend
uvicorn main:app --reload
```

2. Start the frontend development server:
```bash
cd frontend
npm run dev
```

3. Open your browser and navigate to `http://localhost:3000`

## Usage 📖

1. Enter your question in the input field
2. (Optional) Add additional context about your situation
3. Select your preferred spread type
4. Choose whether to allow reversed cards
5. Click "Get Reading" to receive your tarot reading
6. Watch as the cards are revealed one by one
7. Read through the interpretations and insights
8. Use the chat feature to explore your reading further

## Card Animations 🎴

The application features a sophisticated card reveal sequence:
1. All cards appear face-down simultaneously
2. Cards flip one by one with smooth animations
3. Card meanings and interpretations fade in progressively
4. Chat interface becomes available for deeper discussion


## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Future Enhancements 🚀

- Additional spread types
- Save reading history
- Share readings
- Mobile app version
- More detailed card interpretations
- Custom card deck themes
