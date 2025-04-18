import random
from .astrology_systems import classic  # Default astrology system

def analyze_commit_message(message, system="classic"):
    """Analyzes the commit message using the specified astrology system."""
    message_lower = message.lower()
    predictions = []

    if system == "classic":
        rules = classic.get_rules()
        for keyword, readings in rules.items():
            if keyword in message_lower:
                predictions.extend(readings)
    elif system == "software_engineers":
        from .astrology_systems import software_engineers
        rules = software_engineers.get_rules()
        for keyword, readings in rules.items():
            if keyword in message_lower:
                predictions.extend(readings)
    elif system == "mythical_creatures":
        from .astrology_systems import mythical_creatures
        rules = mythical_creatures.get_rules()
        for keyword, readings in rules.items():
            if keyword in message_lower:
                predictions.extend(readings)
    else:
        raise ValueError(f"Unknown astrology system: {system}")

    if not predictions:
        predictions.append(random.choice(get_default_readings()))

    return predictions

def generate_astrological_reading(predictions):
    """Generates a humorous astrological reading based on the analysis."""
    reading = "## The Commit Message Astrologer Says...\n\n"
    reading += "\n".join([f"* {random.choice(prediction)}" for prediction in predictions])
    return reading

def get_default_readings():
    """Provides default readings when no keywords are matched."""
    return [
        "The cosmic energies surrounding this commit are a mystery. Its journey is uncertain.",
        "The celestial bodies offer no strong guidance on this commit. Proceed with caution (or not).",
        "A faint glimmer in the cosmic void suggests... something might happen.",
        "The stars are silent on this matter. Perhaps consult a rubber duck for clarity.",
    ]