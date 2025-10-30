def ask_player_action() -> str:
    while True:
        c = input("Your move? (H=hit, S=stand): ").strip().upper()
        if c in ("H", "S"):
            return c
        print("Enter H or S only.")
