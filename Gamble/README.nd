# Casino Dice Game

A terminal-based dice betting game built in Python, developed as part of my Python learning journey (post-CS50P).

This project is a **programming simulation using fictional points** — not a real-money gambling application.

## Versions

- **V1** — My earliest version of this project. Simple but buggy: had a negative-value bug in the loss calculation and treated ties as wins. Kept in the repo as a snapshot of where I started.
- **V2** *(current)* — A full rebuild from scratch with corrected logic, proper input validation, and cleanly separated functions. See below for rules and design.

The goal of keeping both versions is to track my progress as I learn — V2 isn't a patch on V1, it's a redesign using what I've learned since.

## How to Play

Run the script and follow the prompts each round:

1. Enter your wager (minimum 10 points, maximum your current balance).
2. Enter a number from 1–12.
3. Choose your bet: `Higher`, `Lower`, or `Equal`.
4. A die is rolled (1–12). Win or lose points based on the outcome.
5. Keep playing until your balance drops below 10, or you choose to stop.

## Rules

- **Starting balance:** 1000 points
- **Wager:** min 10, max = current balance
- **Dice:** `random.randint(1, 12)`

### Betting Choices

| Choice | Wins if |
|--------|---------|
| Higher | dice > your number |
| Lower  | dice < your number |
| Equal  | dice == your number |

If you choose Higher or Lower and the dice lands exactly on your number, it's a push — no win, no loss.

### Payout Table

The payout multiplier scales with how unlikely your bet is (fewer winning outcomes = bigger payout):

| Winning outcomes (p) | Multiplier |
|-----------------------|------------|
| 10–12                 | 1.25x      |
| 7–9                   | 1.5x       |
| 6                     | 2x         |
| 3–5                   | 3x         |
| 2                     | 5x         |
| 1                     | 10x        |

Payout on a win: `balance += wager * multiplier`
Loss: `balance -= wager`

## Design Notes

The game logic is split into small, single-responsibility functions:

- `probability_calc()` — counts possible winning outcomes for a given bet
- `wager_percentage()` — maps winning outcomes to a payout multiplier
- `bet_validation()` — checks if a betting choice/number combo is legal
- `wager_validation()` — checks if a wager amount is legal for the current balance
- `check_result()` — determines win/loss for a given roll
- `update_balance()` — applies the win/loss to the balance

This structure keeps calculation, validation, and game flow separate, making the code easier to test, debug, and extend.

## Status

V2 is playable end-to-end. Possible future improvements (V3 candidates): high score tracking, round statistics, refined UX for input errors.
