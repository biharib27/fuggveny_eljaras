import random
def random_gyumik(hossz=30):
    gyumolcsok = ["alma", "körte", "szilva", "barack", "málna", "füge", "eper"]
    return [random.choice(gyumolcsok) for _ in range(hossz)]