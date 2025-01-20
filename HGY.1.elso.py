import random

def random_gyumik():
    gyumolcsok = ["alma", "körte", "szilva", "barack", "málna", "füge", "eper"]
    return [random.choice(gyumolcsok) for _ in range(30)]
