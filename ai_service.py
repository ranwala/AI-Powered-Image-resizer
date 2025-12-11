import json

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class AIService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    def analyse_image(self, base64_encoded_image):

        messages = [
            SystemMessage(content="You are an image analysis assistant."),
            HumanMessage(
                content=[
                    {"type": "text", "text": """
                    Look at the image and answer the question.
                    
                    Respond ONLY with valid JSON in this exact format:
                    
                    {"people_present": true}
                    
                    No explanations. No extra text.
                    """},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_encoded_image}"}
                    }
                ]
            )
        ]

        try:
            response = self.llm.invoke(messages)
            json_response = json.loads(response.content)
            return json_response['people_present']
        except Exception as e:
            print(e)
