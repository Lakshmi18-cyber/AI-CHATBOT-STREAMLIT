from rest_framework.decorators import api_view
from rest_framework.response import Response
import google.generativeai as genai

# Configure API KEY
genai.configure(api_key="GOOGLE API KEY")

# New Working Model
model = genai.GenerativeModel("gemini-3.8-flash")

chat_history = []


@api_view(["POST"])
def chatbot(request):
    try:
        user_message = request.data.get("message")

        if not user_message:
            return Response({
                "response": "Please enter message"
            })

        # Save user message
        chat_history.append(
            {
                "role": "user",
                "parts": [user_message]
            }
        )

        # Generate response
        response = model.generate_content(chat_history)
        bot_reply = response.text

        # Save bot reply
        chat_history.append(
            {
                "role": "model",
                "parts": [bot_reply]
            }
        )

        return Response({
            "response": bot_reply
        })

    except Exception as e:
        print("ERROR:", str(e))
        return Response({
            "response": str(e)
        })