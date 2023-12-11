Card Probability Script

#### Overview
This Python script is designed to simulate the drawing of a card from a standard deck of 52 playing cards. It randomly selects a card, identifies whether it is a face card (Jack, Queen, King), and calculates the probability of drawing a face card from the deck. This script can be used for educational purposes, games, or any application where understanding the probability of drawing a face card is useful.

#### Features
- **Random Card Generation**: Randomly selects a card from a standard deck.
- **Face Card Identification**: Determines if the selected card is a Jack, Queen, or King.
- **Probability Calculation**: Calculates the probability of drawing a face card from the deck.

#### Requirements
- Python 3.x

#### How to Run the Script
1. Ensure Python 3.x is installed on your system.
2. Save the script to a file.
3. Run the script using Python interpreter:
   ```
   python filename.py
   ```

#### Code Explanation
- `generate_card()`: This function creates a standard deck of cards and selects one card randomly.
- `is_image_card(card)`: This function checks if the given card is a face card (Jack, Queen, King).
- The script then prints the randomly selected card and whether it is a face card.
- It also calculates and prints the probability of drawing a face card from a standard deck, which is pre-calculated as approximately 23.08%.

#### Example Output
```
Opponent's card: Queen of Hearts
Is image card: True
Probability of image card: 23.08
```

#### Customization
You can modify the `suits` and `ranks` lists in the `generate_card` function to customize the deck (e.g., adding Jokers or using a different card set).

#### Disclaimer
This script is for educational and entertainment purposes and is not meant for gambling or betting applications.

#### License
This script is provided "as is", without warranty of any kind, express or implied. You are free to use, modify, and distribute it as needed.
