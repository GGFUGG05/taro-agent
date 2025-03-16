// pages/api/proxy/chat.js
export default async function handler(req, res) {
    if (req.method !== 'POST') {
      return res.status(405).json({ message: 'Method not allowed' });
    }
  
    try {
      const response = await fetch(`${process.env.BACKEND_URL}/api/tarot/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(req.body),
      });
  
      const data = await response.json();
  
      if (!response.ok) {
        throw new Error(data.detail || 'Failed to get response from backend');
      }
  
      return res.status(200).json(data);
    } catch (error) {
      console.error('Proxy error:', error);
      return res.status(500).json({ message: 'Internal server error', error: error.message });
    }
  }