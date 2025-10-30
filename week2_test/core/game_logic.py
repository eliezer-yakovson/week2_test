from core.player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int:
    total = 0
    for c in hand:
        r = c["rank"]
        if r.isdigit():
            total += int(r)
        elif r in ("J", "Q", "K"):
            total += 10
        else:
            total += eleven_or_one(hand)
    return total

def eleven_or_one(hand: list[dict])-> int:
    count_a = 0
    s=0
    for c in hand:
        r = c["rank"]
        if r.isdigit():
            s += int(r)
        elif r in ("J", "Q", "K"):
            s += 10
        else: count_a += 1
    if count_a == 1 and s + 11 <= 21:
        return 11
    return 1
        
def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].extend([deck.pop(0), deck.pop(0)])
    dealer["hand"].extend([deck.pop(0), deck.pop(0)])
    print(f"Player value: {calculate_hand_value(player['hand'])}")
    print(f"Dealer value: {calculate_hand_value(dealer['hand'])}")
    print("")

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        v = calculate_hand_value(dealer["hand"])
        if v > 21:
            print(f"Dealer busted ({v})")
            return False
        if v >= 17:
            print(f"Dealer stands ({v})")
            return True
        dealer["hand"].append(deck.pop(0))
        print(f"Dealer hits ({calculate_hand_value(dealer['hand'])})")

def player_play(deck: list[dict], player: dict) -> bool:
    while True:
        v = calculate_hand_value(player["hand"])
        if v > 21:
            print(f"Player busted ({v}). Dealer wins.")
            return False
        a = ask_player_action()
        if a == "H":
            player["hand"].append(deck.pop(0))
            v = calculate_hand_value(player["hand"])
            print(f"Player hits ({v})")
        else:
            print("Player stands.")
            return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    print("=== Blackjack ===")
    deal_two_each(deck, player, dealer)
    player_ok = player_play(deck, player)
    dealer_ok = dealer_play(deck, dealer)
    pv = calculate_hand_value(player["hand"])
    dv = calculate_hand_value(dealer["hand"])
    print("=== Final ===")
    print(f"Player: {pv}, Dealer: {dv}")
    if not player_ok:
        print("Dealer wins.")
    elif not dealer_ok:
        print("Player wins.")
    elif pv > dv:
        print("Player wins.")
    elif dv > pv:
        print("Dealer wins.")
    else:
        print("Tie.")

