import json

# Define your openings here
openings = [
    # E4 Openings
    {"name": "Sicilian Defense", "pgn": "1. e4 c5", "tag": "e4"},
    {"name": "French Defense", "pgn": "1. e4 e6", "tag": "e4"},
    {"name": "Caro-Kann Defense", "pgn": "1. e4 c6", "tag": "e4"},
    {"name": "Ruy Lopez", "pgn": "1. e4 e5 2. Nf3 Nc6 3. Bb5", "tag": "e4"},
    {"name": "Italian Game", "pgn": "1. e4 e5 2. Nf3 Nc6 3. Bc4", "tag": "e4"},
    {"name": "Scandinavian Defense", "pgn": "1. e4 d5", "tag": "e4"},
    
    # D4 Openings
    {"name": "Queen's Gambit", "pgn": "1. d4 d5 2. c4", "tag": "d4"},
    {"name": "London System", "pgn": "1. d4 d5 2. Bf4", "tag": "d4"},
    {"name": "King's Indian Defense", "pgn": "1. d4 Nf6 2. c4 g6", "tag": "d4"},
    
    # Flank
    {"name": "English Opening", "pgn": "1. c4", "tag": "flank"}
]

output_cards = []

# Generate IDs starting from 100
current_id = 100

for op in openings:
    current_id += 1
    
    # 1. Create White View
    output_cards.append({
        "id": current_id,
        "front": op["name"],
        "back": op["pgn"],
        "pgn": op["pgn"],
        "tag": op["tag"],
        "orientation": "white"
    })
    
    # 2. Create Black View
    # We append '0' to the ID to make it unique (e.g. 101 becomes 1010)
    # or just multiply by 10
    black_id = int(str(current_id) + "0")
    
    output_cards.append({
        "id": black_id,
        "front": op["name"],
        "back": op["pgn"],
        "pgn": op["pgn"],
        "tag": op["tag"],
        "orientation": "black"
    })

# Save to file
with open("cards.json", "w") as f:
    json.dump(output_cards, f, indent=2)

print(f"Success! Generated {len(output_cards)} cards (White & Black views) in cards.json")
