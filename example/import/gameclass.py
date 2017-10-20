class character_stat:
    def __init__(self):
        self.m_hp = "0"
        self.m_mp = "0"

    def set_all(self, hp, mp):
        self.m_hp = hp
        self.m_mp = mp

    def print(self):
        print("HP : ", self.m_hp)
        print("MP : ", self.m_mp)