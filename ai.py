def simple_ai_response(user_input):
    if "hallo" in user_input.lower():
        return "Hallo! Wie kann ich dir helfen?"
    elif "wetter" in user_input.lower():
        return "Ich kann das Wetter leider nicht vorhersagen, aber du kannst auf wetter.com nachschauen."
    else:
        return "Das habe ich leider nicht verstanden."
