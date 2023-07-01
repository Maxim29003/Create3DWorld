from app import app
from dotenv import load_dotenv
from config import PORT

if __name__ == '__main__':
    load_dotenv()
    app.run(port=PORT)
