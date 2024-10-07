#Game question

def solve_riddle(riddle):
    print(riddle)
    answer = input("Gib deine Antwort ein: ").strip().lower()
    if answer == "Feuer":
        return True
    else:
        print("Das ist nicht richtig. Versuche es noch einmal.")
        return False

#End of the game

def end_game():
    print("Danke fürs Spielen! Auf Wiedersehen!")