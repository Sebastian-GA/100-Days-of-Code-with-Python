logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

card_symbols = ["♠", "♦", "♥", "♣"]


def ascii_card(symbol, value):
    if value == "?":
        return [
            '┌─────────┐',
            '│░░░░░░░░░│',
            '│░░░░░░░░░│',
            '│░░░░░░░░░│',
            '└─────────┘'
        ]

    symbol = card_symbols[symbol]
    if len(value) == 1:
        value = " " + value
    return [
        '┌─────────┐',
        '│{}       │'.format(value),
        '│    {}    │'.format(symbol),
        '│       {}│'.format(value),
        '└─────────┘'
    ]
