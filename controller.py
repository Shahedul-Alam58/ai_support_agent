from ai_router import detect_intent
from handlers.track_handler import track_handler
from handlers.refund_handler import refund_handler
from handlers.complaint_handler import complaint_handler

def route_request(user_input):
    try:
        intent = detect_intent(user_input)

        if intent == "track":
            return track_handler(user_input)
        elif intent == "refund":
            return refund_handler(user_input)
        elif intent == "complaint":
            return complaint_handler(user_input)
        else:
            return "Sorry, I couldn't understand your request."

    except:
        return "AI service is busy. Please try again."