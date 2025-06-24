from smolagents import tool
import random

@tool
def generate_chord_progression(key: str) -> str:
    """Generates a musical chord progression in a specified key.
    Args:
        key: The musical key (e.g., 'C', 'Am', 'F#')
    Returns:
        A string containing the chord progression
    """
    # Common chord progressions (Roman numerals)
    progressions = {
        'major': [
            ['I', 'IV', 'V', 'I'],
            ['I', 'vi', 'IV', 'V'],
            ['ii', 'V', 'I', 'IV'],
            ['I', 'V', 'vi', 'IV'],
            ['I', 'IV', 'vi', 'V'],
            ['ii', 'V', 'I', 'vi']
        ],
        'minor': [
            ['i', 'iv', 'v', 'i'],
            ['i', 'VI', 'VII', 'i'],
            ['i', 'iv', 'v', 'VI'],
            ['i', 'VII', 'VI', 'v'],
            ['i', 'III', 'VII', 'VI'],
            ['i', 'iv', 'III', 'VI']
        ]
    }

    # Comprehensive chord mappings for all keys
    chord_mappings = {
        # Major Keys
        'C':  ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'],
        'G':  ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#dim'],
        'D':  ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#dim'],
        'A':  ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#dim'],
        'E':  ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#dim'],
        'B':  ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim'],
        'F#': ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'E#dim'],
        'C#': ['C#', 'D#m', 'E#m', 'F#', 'G#', 'A#m', 'B#dim'],
        'F':  ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim'],
        'Bb': ['Bb', 'Cm', 'Dm', 'Eb', 'F', 'Gm', 'Adim'],
        'Eb': ['Eb', 'Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Ddim'],
        'Ab': ['Ab', 'Bbm', 'Cm', 'Db', 'Eb', 'Fm', 'Gdim'],
        'Db': ['Db', 'Ebm', 'Fm', 'Gb', 'Ab', 'Bbm', 'Cdim'],
        'Gb': ['Gb', 'Abm', 'Bbm', 'Cb', 'Db', 'Ebm', 'Fdim'],
        'Cb': ['Cb', 'Dbm', 'Ebm', 'Fb', 'Gb', 'Abm', 'Bbdim'],
        
        # Enharmonic equivalents
        'F#': ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'E#dim'],
        'Gb': ['Gb', 'Abm', 'Bbm', 'Cb', 'Db', 'Ebm', 'Fdim'],
        'C#': ['C#', 'D#m', 'E#m', 'F#', 'G#', 'A#m', 'B#dim'],
        'Db': ['Db', 'Ebm', 'Fm', 'Gb', 'Ab', 'Bbm', 'Cdim']
    }

    # Clean input and check if minor
    key = key.strip()
    is_minor = key.endswith('m')
    base_key = key[:-1] if is_minor else key

    # Validate key
    if base_key not in chord_mappings:
        return f"Invalid key. Supported keys are: {', '.join(sorted(chord_mappings.keys()))} (add 'm' for minor)"

    # Get progression pattern
    progression_type = 'minor' if is_minor else 'major'
    pattern = random.choice(progressions[progression_type])

    # Convert roman numerals to actual chords
    roman_to_index = {
        'i': 0, 'ii': 1, 'iii': 2, 'iv': 3, 'v': 4, 'vi': 5, 'vii': 6,
        'I': 0, 'II': 1, 'III': 2, 'IV': 3, 'V': 4, 'VI': 5, 'VII': 6
    }
    
    chords = chord_mappings[base_key]
    result = []
    
    for numeral in pattern:
        idx = roman_to_index[numeral.lower()]
        result.append(chords[idx])

    return f"Chord progression in {key}: {' - '.join(result)}"
#this is the end of the code also an edit to the file to work on git