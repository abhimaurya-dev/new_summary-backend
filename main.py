import os
import uvicorn
from app.main import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    port = int(os.getenv("PORT")) 
    print(f"Starting server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)