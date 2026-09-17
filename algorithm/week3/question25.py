def guess_number_game(secret: int, guess: int) -> str:
    if guess == secret:
        return "Correct";

    elif guess < secret:
        return "Too Low";

    else:
        return "Too High"
