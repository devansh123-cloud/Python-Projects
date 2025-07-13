score = 0  # Global score

def play():
    global score  # Use existing global
    score += 10   # Add 10 points
    print("Score is now:", score)

play()
play()
