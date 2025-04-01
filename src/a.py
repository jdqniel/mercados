"""Script to identify animals in images using Google's Gemini model."""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

def main():
    """Main function to process the image and get animal identification."""
    foto = "fotos/1.jpg"

    # Load environment variables and initialize the model
    load_dotenv()
    llm = init_chat_model("gemini-2.0-flash", model_provider="google-genai")
    
    # Get response from the model
    response = llm.invoke("Necesito que me ayudes a identificar el tipo de animal que esta en la foto: foto_bs64")
    print(response)

    
if __name__ == "__main__":
    main()

