from google import genai
import time
import re
client = genai.Client(api_key="AIzaSyAveiNEwkG6sSuH4i2MJ95fa39KKT3TEP0")





def detect_intent(user_input):
    text = user_input.lower()

    # Keyword fallback
    if "track" in text or "where is my order" in text:
        return "track"
    elif "refund" in text or "money back" in text:
        return "refund"
    elif "complaint" in text or "problem" in text or "issue" in text:
        return "complaint"

    # AI detection (optional)
    prompt = f"""
    Classify this customer support message into one of these categories:

    track
    refund
    complaint
    unknown

    Message: {user_input}

    Return only the category name.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        intent = response.text.strip().lower()
        # Normalize AI output
        if "track" in intent:
            return "track"
        elif "refund" in intent:
            return "refund"
        elif "complaint" in intent:
            return "complaint"
        else:
            return "unknown"
    except:
        return "unknown"