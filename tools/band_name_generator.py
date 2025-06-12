from smolagents import tool
import random

@tool
def generate_band_name(first_name: str) -> str:
    """Generates a random band name using the provided first name as inspiration.
    
    Args:
        first_name: The first name to use as inspiration for the band name
    """
    
    adjectives = [
        "Cosmic", "Electric", "Mystic", "Savage", "Silent", 
        "Neon", "Quantum", "Midnight", "Crystal", "Thunder"
    ]
    
    nouns = [
        "Dragons", "Warriors", "Prophets", "Wolves", "Riders",
        "Pirates", "Bandits", "Knights", "Wizards", "Rebels"
    ]
    
    # Generate the band name using the first name and random elements
    band_name = f"{random.choice(adjectives)} {first_name}'s {random.choice(nouns)}"
    
    return f"Your generated band name is: {band_name}" 