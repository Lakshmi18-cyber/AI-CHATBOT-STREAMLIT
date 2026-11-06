# AI Chatbot using Django, Streamlit and Google Gemini API

A chatbot application with a Django REST backend that talks to the Google Gemini API and a Streamlit frontend for the chat interface.

## Tools Used
- Python
- Django and Django REST Framework
- Streamlit
- Google Gemini API (Google AI Studio)

## Project Structure
- `backend/chatbotapiproject/`: Django project with the `aiapp` app that contains the chatbot API
- `frontend/streamlitapp.py`: Streamlit chat interface

## How to Run
1. Install the libraries: `pip install -r requirements.txt`
2. Get a free API key from Google AI Studio and add it in the backend code (or set it as an environment variable named `GOOGLE_API_KEY`)
3. Start the backend: `cd backend/chatbotapiproject` then `python manage.py runserver`
4. Start the frontend: `cd frontend` then `streamlit run streamlitapp.py`

## Note
The API key is not included in this repository. Add your own key to run the project.

## Author
Lakshmi | BSc Computer Science
GitHub: [Lakshmi18-cyber](https://github.com/Lakshmi18-cyber)
