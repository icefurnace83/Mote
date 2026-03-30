import time
import random
import os
tick_rate                   = 5
hunger_chance               = 0.2
sadness_chance              = 0.15
poop_rate                   = 2
poop_chance                 = 0.3
too_many_poops              = 2
too_many_poops_sick_chance  = 0.25
maximum_poops               = 4
chance_to_get_sick          = 0.4
neglected_when_sick_chance  = 0.3
maximum_care_mistakes       = 10
default_naugtiness          = 0.05
maximum_hunger              = 4
maximum_happiness           = 4
ASCII_ART = {
    "Egg": r"""
    (oo)
    (__)
    """,
    "Baby": r"""
    (o_o)
    <)__)>
    """,
    "Child": r"""
     ^_^
     /|\
     / \
    """,
    "Teen (Champ)": r"""
    (^‿^)
    /|_|\
     | |
    """,
    "Teen (Chump)": r"""
    (>_<)
    <)_)>
     / \
    """,
    "Adult (Chill)": r"""
    (⌐■_■)
    |██|
    /  \
    """,
    "Adult (Charming)": r"""
    (*▽)
     <))\
     / \
    """,
    "Adult (Cheeky)": r"""
    (¬‿¬)
    \|_/
     | |
    """,
    "Adult (Silly)": r"""
    ( @w@)
    /)_(\
    (   )
    """,
    "Adult (Wobbly)": r"""
    (°ロ°)
    /| \~
     ~  ~
    """,
    "Adult (Cranky)": r"""
    (ಠ_ಠ)
    /||\
     ||
    """,
    "Dead": r"""
    [RIP]
    /__\
     ||
    """
}
BEHAVIOR_MODIFIERS = {
    "Teen (Chump)":     {"discipline_gain": -2, "misbehave_chance": 0.3},
    "Adult (Chill)":    {"discipline_gain": 2,  "misbehave_chance": 0.01},
    "Adult (Charming)": {"discipline_gain": 1,  "misbehave_chance": 0.05, "play_bonus": 1},
    "Adult (Cheeky)":   {"discipline_gain": -1, "misbehave_chance": 0.25, "play_bonus": 2},
    "Adult (Silly)":    {"discipline_gain": 0,  "misbehave_chance": 0.15, "play_bonus": 2},
    "Adult (Wobbly)":   {"discipline_gain": 0,  "misbehave_chance": 0.2},
    "Adult (Cranky)":   {"discipline_gain": 2,  "misbehave_chance": 0.3, "refuses_play": True}
}
class Mote:
    def __init__(self):
        self.reset()
    def reset(self):
        self.ticks = 0
        self.stage = "Egg"
        self.age = 0
        self.hunger = 4
        self.happiness = 4
        self.poop = 0
        self.sick = False
        self.misbehaving = False
        self.care_mistakes = 0
        self.attention_flag = False
        self.evolution_timer = 0
        self.alive = True
    def ai(self):
        if not self.alive:
            return
        self.ticks += 1
        if self.ticks >= tick_rate:
            self.age += 1
            self.evolution_timer += 1
            self.ticks = 0
        if random.random() <= hunger_chance:
            self.hunger = max(0, self.hunger - 1)
        if random.random() <= sadness_chance:
            self.happiness = max(0, self.happiness - 1)
        if self.ticks % poop_rate == 0:
            if random.random() <= poop_chance:
                self.poop += 1
        if self.poop >= too_many_poops and random.random() <= too_many_poops_sick_chance:
            self.sick = True
        if self.poop >= maximum_poops or self.hunger <=0 or self.happiness <= 0:
            if random.random() <= chance_to_get_sick:
                self.sick = True
        if self.sick and random.random() <= neglected_when_sick_chance:
            self.care_mistakes += 1
        if self.care_mistakes >= maximum_care_mistakes:
            self.stage = "Dead"
            self.alive = False
            return
        form = BEHAVIOR_MODIFIERS.get(self.stage, {})
        chance_to_be_naughty = form.get("misbehave_chance", default_naugtiness)
        if random.random() < chance_to_be_naughty:
            self.misbehaving = True
        self.attention_flag = any([
            self.hunger < maximum_hunger,
            self.happiness < maximum_happiness,
            self.poop > 0,
            self.sick,
            self.misbehaving,
        ])
        self.check_evolution()
    def check_evolution(self):
        years_in_stage = {
            "Egg": 2,
            "Baby": 4,
            "Child": 7,
            "Teen (Champ)": 8,
            "Teen (Chump)": 15,
            "Adult (Chill)": 30,
            "Adult (Cheeky)": 15,
        }
        if self.evolution_timer >= years_in_stage.get(self.stage, 999):
            prev = self.stage
            if self.stage == "Egg":
                self.stage = "Baby"
            elif self.stage == "Baby":
                self.stage = "Child"
            elif self.stage == "Child":
                if self.care_mistakes <= 1:
                    self.stage = "Teen (Champ)"
                else:
                    self.stage = "Teen (Chump)"
            elif self.stage.startswith("Teen"):
                if self.stage == "Teen (Champ)":
                    self.stage = "Adult (Chill)" if self.care_mistakes <= 4 else "Adult (Charming)"
                else:
                    self.stage = "Adult (Cheeky)" if self.care_mistakes <= 2 else "Adult (Silly)"
            elif self.stage.startswith("Adult"):
                if self.stage == "Adult (Chill)":
                    self.stage = "Adult (Wobbly)"
                elif self.stage == "Adult (Cheeky)": self.stage = "Adult (Cranky)"
            self.evolution_timer = 0
            show_flash_text(self.stage)
    def render(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("------------------------------")
        print(f"{self.name} — {self.stage} — {self.age} years")
        print("------------------------------")
        print(ASCII_ART.get(self.stage, "(._.)"))
        print("------------------------------")
        print(f"Hunger:     {'●'*self.hunger + '○'*(maximum_hunger - self.hunger)}")
        print(f"Happiness:  {'●'*self.happiness + '○'*(maximum_happiness - self.happiness)}")
        print(f"Poop:       {self.poop}")
        print(f"Sick:       {'Yes' if self.sick else 'No'}")
        print(f"Misbehaving:{'Yes' if self.misbehaving else 'No'}")
        print(f"Attention:  {'Yes' if self.attention_flag else 'No'}")
        print("------------------------------")
    def interact(self, choice):
        form = BEHAVIOR_MODIFIERS.get(self.stage, {})
        if choice == "7":
            print("Resetting Mote...")
            self.reset()
            time.sleep(1)
        if not self.alive:
            print("Your Mote has passed. Press [7] to Reset.")
            time.sleep(2)
            return
        if choice == "1":
            if self.hunger < maximum_hunger:
                self.hunger += 1
                self.attention_flag = False
        elif choice == "2":
            if form.get("refuses_play"):
                print("This Mote refuses to play.")
                time.sleep(1)
                return
            if not self.misbehaving:
                bonus = form.get("play_bonus", 1)
                self.happiness = min(maximum_happiness, self.happiness + bonus)
                self.attention_flag = False
        elif choice == "3":
            self.poop = 0
            self.attention_flag = False
        elif choice == "4":
            if self.sick:
                self.sick = False
                self.attention_flag = False
        elif choice == "5":
            if self.misbehaving:
                gain = form.get("discipline_gain", 1)
                self.misbehaving = False
                self.attention_flag = False
                print(f"Disciplined! Gained {gain} respect.")
                time.sleep(1)
        elif choice == "6":
             show_stats_screen()
def main():
    little_friend = Mote()
    little_friend.name = input("> What is your Mote's name? ")
    game_is_running = True
    little_friend.render()
    while game_is_running:
        print("[1] Feed  [2] Play  [3] Toilet")
        print("[4] Medicine  [5] Discipline  [6] Stats")
        print("[7] Reset  [Q] Quit")
        choice = input("> Choose action: ").strip().upper()
        if choice == "Q":
            game_is_running = False
        little_friend.interact(choice)
        little_friend.ai()
        little_friend.render()
        time.sleep(0.5)
def show_flash_text(stage):
    frame1 = f"* {stage} *"
    frame2 = " "
    for _ in range(3):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" * 5 + frame1.center(40))
        time.sleep(0.3)
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" * 5 + frame2.center(40))
        time.sleep(0.3)
def show_under_construction_flash():
    frame1 = r"""
    *-*-*-*-*-*-*-*-*-*-*-
    - UNDER CONSTRUCTION *
    *-*-*-*-*-*-*-*-*-*-*-
    """
    frame2 = r"""
    -*-*-*-*-*-*-*-*-*-*-*
    * UNDER CONSTRUCTION -
    -*-*-*-*-*-*-*-*-*-*-*
    """
    for _ in range(6):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" * 5 + frame1.center(40))
        time.sleep(0.3)
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" * 5 + frame2.center(40))
        time.sleep(0.3)
def show_stats_screen():
    show_under_construction_flash()
if __name__ == "__main__":
    main()