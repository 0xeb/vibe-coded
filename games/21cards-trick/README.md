# 21 Cards Magic Trick

Interactive simulator and game for the classic 21-card magic trick. Modernized from the original [lallousx86/21cards-trick](https://github.com/lallousx86/21cards-trick).

| | |
|---|---|
| **Type** | Interactive HTML5 game / mathematical puzzle |
| **Original** | [lallousx86/21cards-trick](https://github.com/lallousx86/21cards-trick) |

## Modes

- **Play** -- Experience the trick as a spectator. Pick a card mentally, click its column three times, and watch the reveal.
- **How It Works** -- Learn the math behind the convergence: the shuffle table, position narrowing, and an interactive tracker.
- **Simulator** -- Watch all 21 cards converge to position 11 after three rounds.

## Usage

Open `21cards-trick.html` directly in any modern browser. No server required.

## How the Trick Works

You deal 21 cards into 3 columns of 7. The spectator picks a card and tells you which column it's in. You gather the columns, placing the chosen column **in the middle**. Re-deal and repeat **three times**. The card is now at position 11 -- the exact middle.

The math: each round narrows the card's possible position by a factor of ~3 (21 → 7 → 3 → 1). The shuffle table `[[1,0,2], [0,1,2], [0,2,1]]` ensures the chosen column always ends up in the middle third.

## Credits

Original simulator by Elias Bachaalany. Modernized interactive version with play mode, math explainer, and convergence simulator.
