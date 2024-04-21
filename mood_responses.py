def mood_response(mood):
  
    if mood.lower() == "happy":
        return "Great to hear that you're happy!"
    elif mood.lower() == "sad":
        return "I'm sorry to hear that you're feeling sad. Is there anything I can do to cheer you up?"
    elif mood.lower() == "angry":
        return "Take a deep breath and try to relax. Anger doesn't solve anything."
    elif mood.lower() == "calm":
        return "It's good to hear that you're feeling calm. Enjoy the tranquility!"
    else:
        return "I'm not sure how to respond to that mood. But remember, whatever you're feeling, it's okay."
