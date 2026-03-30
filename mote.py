#FIRST USE: comment
#FIRST USE: import
#FIRST USE: function
#FIRST USE: variable
#FIRST USE: integer
#FIRST USE: float
#FIRST USE: global and local variables


import time                                                             # import the time module so we can use the *time.sleep() function
import random                                                           # import the random module so we can use the *random.random() function
import os                                                               # import the os module so we can use the *os.system() function and the *os.name variable
                                                                        # *more details provided later


tick_rate                   = 5                                         # create a global variable called tick_rate and make it an integer equal to 5
hunger_chance               = 0.2                                       # create a global variable called maximum_hunger and make it a float equal to 0.2
sadness_chance              = 0.15                                      # create a global variable called sadness_chance and make it a float equal to 0.15
poop_rate                   = 2                                         # create a global variable called poop_rate and make it an integer equal to 2
poop_chance                 = 0.3                                       # create a global variable called poop_chance and make it a float equal to to 0.3
too_many_poops              = 2                                         # create a global variable called too_many_poops and make it an integer equal to 2
too_many_poops_sick_chance  = 0.25                                      # create a global variable too_many_poops_sick_chance and make it a float equal to 0.25
maximum_poops               = 4                                         # create a global variable called maximum_poops and make it an integer equal to 4
chance_to_get_sick          = 0.4                                       # create a global variable called chance_to_get_sick and make it a float equal to 0.4
neglected_when_sick_chance  = 0.3                                       # create a global variable called neglected_when_sick_chance and make it a float equal to 0.3
maximum_care_mistakes       = 10                                        # create a global variable called maximum_care_mistakes and make it an integer equal to 10
default_naugtiness          = 0.05                                      # create a global variable called default_naugtiness and make it an integer equal to 10
maximum_hunger              = 4                                         # create a global variable called maximum_hunger and make it an integer equal to 4
maximum_happiness           = 4                                         # create a global variable called maximum_happiness and make it an integer equal to 4



#FIRST USE: dictionary
#FIRST USE: =
#FIRST USE: dictionary keys
#FIRST USE: indentation
#FIRST USE: string
#FIRST USE: raw string
ASCII_ART = {                                                           # create a dictionary to set the ascii art for each Mote evolution
                                                                        # contains the Mote's different evolution names as keys and raw strings
                                                                        # depicting the ascii artwork that will be displayed as the values
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
#<https://en.wikipedia.org/wiki/List_of_Unicode_characters>
}


#FIRST USE: nested dictionary
#FIRST USE: boolean

BEHAVIOR_MODIFIERS = {                                                  # create a dictionary with evolution names as keys and with nested 
                                                                        # dictionaries containing multiple key : value pairs to modify how
                                                                        # different stages of evolution are simulated.


    "Teen (Chump)":     {"discipline_gain": -2, "misbehave_chance": 0.3},
    "Adult (Chill)":    {"discipline_gain": 2,  "misbehave_chance": 0.01},
    "Adult (Charming)": {"discipline_gain": 1,  "misbehave_chance": 0.05, "play_bonus": 1},
    "Adult (Cheeky)":   {"discipline_gain": -1, "misbehave_chance": 0.25, "play_bonus": 2},
    "Adult (Silly)":    {"discipline_gain": 0,  "misbehave_chance": 0.15, "play_bonus": 2},
    "Adult (Wobbly)":   {"discipline_gain": 0,  "misbehave_chance": 0.2},
    "Adult (Cranky)":   {"discipline_gain": 2,  "misbehave_chance": 0.3, "refuses_play": True}
}

#FIRST USE: class
class Mote:                                                             # create a class called Mote
                                                                        # it will be a template that contains all the functions and
                                                                        # variables needed to interact with, simulate and render a Mote object

#FIRST USE: def
#FIRST USE: __init__
#FIRST USE: self
#FIRST USE: parameter
    def __init__(self):                                                 # create a function within Mote that will be named __init__
                                                                        # when called it will pass it self as a parameter
                                                                        # it will be called when a new Mote is created
                                                                        # it will call the function contained in the Mote class that is
                                                                        # named reset
#FIRST USE: calling a function
        self.reset()                                                    # call the Mote's function named reset, it will take care
                                                                        # of setting up all of the Mote's data


    def reset(self):                                                    # create a function within Mote that will be named reset
                                                                        # it will pass it self as a parameter when
                                                                        # it is called (unless another is specified)
                                                                        # it will be called when a Mote is reset and
                                                                        # set all of the Mote's variables to default values

        self.ticks = 0                                                  # set the Mote's ticks value to the integer 0
        self.stage = "Egg"                                              # set the Mote's stage value to the string "Egg"
        self.age = 0                                                    # set the Mote's age value to the integer 0
        self.hunger = 4                                                 # set the Mote's hunger value to the integer 4
        self.happiness = 4                                              # set the Mote's happiness value to the integer 4
        self.poop = 0                                                   # set the Mote's poop value to the integer 0
        self.sick = False                                               # set the Mote's sick value to the boolean False
        self.misbehaving = False                                        # set the Mote's misbehaving value to the boolean False
        self.care_mistakes = 0                                          # set the Mote's care mistakes value to the integer 0
        self.attention_flag = False                                     # set the Mote's attention_flag value to the boolean False
        self.evolution_timer = 0                                        # set the Mote's evolution_timer value to the integer 0
        self.alive = True                                               # set the Mote's alive value to the boolean True


    def ai(self):                                                       # create a function within Mote that will be named ai
                                                                        # when called it will pass it self as a parameter when
                                                                        # it is called (unless another is specified)
                                                                        # it will be called every loop of the program and
                                                                        # run through our Mote's ai logic

#FIRST USE: if
#FIRST USE: not
#FIRST USE: return
        if not self.alive:                                              # if the Mote is not alive:
            return                                                      # exit this function immediately , no need to go further

#FIRST USE: +=
        self.ticks += 1                                                 # increase the Mote's tick value by 1

#FIRST USE: >=
        if self.ticks >= tick_rate:                                     # if the Mote's tick value is higher than or equal to the
                                                                        # global variable named tick_rate:
            self.age += 1                                               # increase the Mote's age value by 1
            self.evolution_timer += 1                                   # increase the Mote's evolution_timer value by 1
            self.ticks = 0                                              # reset the Mote's tick value to 0

#FIRST USE: random.random
#FIRST USE: <=

        if random.random() <= hunger_chance:                            # if the number returned by the function random in the 
                                                                        # imported module random (that is between 0 and 1) is
                                                                        # less than the global variable named hunger_chance:
#FIRST USE: max
            self.hunger = max(0, self.hunger - 1)                       # set the Mote's hunger value to be equal to:
                                                                        # the larger of 0 or the Mote's hunger value -1
                                                                        # *note* using max keeps the returned value from ever
                                                                        # being lower than 0

        if random.random() <= sadness_chance:                           # if the number returned by the function random in the 
                                                                        # imported module random (that is between 0 and 1) is less
                                                                        # than the global variable named sadness_chance
                                                                        
            self.happiness = max(0, self.happiness - 1)                 # set the Mote's happiness value to be equal to:
                                                                        # the larger of 0 or the Mote's happiness value -1
                                                                        # *note* using max keeps the returned value from ever
                                                                        # being lower than 0

#FIRST USE: modulo
#FIRST USE: ==
        if self.ticks % poop_rate == 0:                                 # if the Mote's tick number divided by the global variable
                                                                        # poop_rate has a remainder of 0: (once every poop_rate ticks)
                                                                        
            if random.random() <= poop_chance:                          # if the number returned by the function random in the 
                                                                        # imported module random (that is between 0 and 1) is less than
                                                                        # the global variable named poop_chance
                                                                        
                self.poop += 1                                          # increase the Mote's poop value by 1

#FIRST USE: and
        if self.poop >= too_many_poops and random.random() <= too_many_poops_sick_chance:
                                                                        # if the motes poop value is larger than or equal the global
                                                                        # variable named too_many_poops and the number returned by
                                                                        # the function random in the  imported module random (that
                                                                        # is between 0 and 1) is less than the global variable named
                                                                        # too_many_poops_sick_chance:
                                                                        
            self.sick = True                                            # set the Mote's sick value to True

#FIRST USE: or
        if self.poop >= maximum_poops or self.hunger <=0 or self.happiness <= 0:
                                                                        # if the motes poop value is larger than or equal to the 
                                                                        # global variable named maximum_poops
                                                                        # or the Mote's hunger is less than or equal to 0
                                                                        # or the Mote's happiness value is less than or equal to 0:
                                                                        
            if random.random() <= chance_to_get_sick:                   # if a number returned by the function random in the 
                                                                        # imported module random (that is between 0 and 1) is less
                                                                        # than the global variable named chance_to_get_sick
                                                                        
                self.sick = True                                        # set the Mote's sick value to equal True

        if self.sick and random.random() <= neglected_when_sick_chance: # if a random number between 0 and 1 is less than the global variable
                                                                        # neglected_when_sick_chance
                                                                        
            self.care_mistakes += 1                                     # increase the Mote's care_mistakes value by 1

        if self.care_mistakes >= maximum_care_mistakes:                 # if Mote's care mistakes is grater than or equal to the global variable
                                                                        # maximum_care_mistakes:
            
            self.stage = "Dead"                                         # change the Mote's stage value to equal "Dead"
            self.alive = False                                          # change the Mote's alive value to equal False
            return                                                      # exit this function immediately , no need to go further

#FIRST USE: get
        form = BEHAVIOR_MODIFIERS.get(self.stage, {})                   # make a variable named form and make it equal to the 
                                                                        # dictionary from within BEHAVIOR_MODIFIERS that has
                                                                        # the same name as the the Mote's stage. If there is no
                                                                        # dictionary with the same name as the the Mote's stage
                                                                        # within the dictionary named form then make the variable
                                                                        # named form equal to a blank dictionary

        chance_to_be_naughty = form.get("misbehave_chance", default_naugtiness)
                                                                        # make a variable called chance_to_be_naughty and make it equal to the
                                                                        # variable named misbehave_chance within the form dictionary that 
                                                                        # was just made. If there is no variable called chance_to_be_naughty within
                                                                        # the dictionary named form then make it equal default_naugtiness

        if random.random() < chance_to_be_naughty:                      # if a random number is smaller than chance_to_be_naughty:
            self.misbehaving = True                                     # set Mote's misbehaving value to True

#FIRST USE: any
        self.attention_flag = any([
            self.hunger < maximum_hunger,                               # check if the Mote's hunger value is less than the global maximum_hunger
            self.happiness < maximum_happiness,                         # check if the Mote's happiness value is less than the global maximum_happiness
            self.poop > 0,                                              # check if the Mote's poop value is greater than then 0
            self.sick,                                                  # check if the Mote's sick value is True
            self.misbehaving,                                           # check if the Mote's misbehaving is True
        ])                                                              # if any of these things are True than set the motes attention_flag to the value True


        self.check_evolution()                                          # call the Mote's check_evolution function (*created next*)


    def check_evolution(self):                                          # create a function within Mote that will be named check_evolution
                                                                        # it will pass it self as a parameter when
                                                                        # it is called (unless another is specified)
                                                                        # it will be called every loop of the program and
                                                                        # run through our Mote evolution logic

        years_in_stage = {                                              # creates a dictionary named years_in_stage
                                                                        # with evolution stage name as keys and years they stay
                                                                        # that stage as values

            "Egg": 2,                                                   # the Mote is an egg for 2 years
            "Baby": 4,                                                  # the Mote is a baby for 4 years
            "Child": 7,                                                 # the Mote is a child for 7 years
            "Teen (Champ)": 8,                                          # the Mote is a Teen (Champ) for 7 years
            "Teen (Chump)": 15,                                         # the Mote is a Teen (Chump) 15 years
            "Adult (Chill)": 30,                                        # the Mote is an Adult (Chill) for 30 years
            "Adult (Cheeky)": 15,                                       # the Mote is an Adult (Cheeky) for 15 years
        }

        if self.evolution_timer >= years_in_stage.get(self.stage, 999): # if the Mote's evolution_timer is larger than or
                                                                        # equal to the threshold matching the Mote's stage:
                                                                        # (If there is no threshold matching the Mote's
                                                                        # stage then if the evolution_timer is larger than 999)

            prev = self.stage                                           # even if we aren't going to use it, we may as well
                                                                        # create a variable called prev and store the Mote's
                                                                        # current stage here.

            if self.stage == "Egg":                                     # if the Mote's stage is "egg":
                self.stage = "Baby"                                     # change the Mote's stage to "baby"

#FIRST USE: elif
            elif self.stage == "Baby":                                  # else if the Mote's stage is "egg":
                self.stage = "Child"                                    # change the Mote's stage to "child"


            elif self.stage == "Child":                                 # else if the Mote's stage is "child"

#FIRST USE: else
                if self.care_mistakes <= 1:                              # if care_mistakes are less than or equal to 1:
                
                    self.stage = "Teen (Champ)"                         # set the Mote's stage to "Teen (Champ)"
                    
                else:
                    self.stage = "Teen (Chump)"                         # else: set the set the Mote's stage to "Teen (Chump)"
                                                                        
                                                                        
                                                                        

#FIRST USE: startswith
            elif self.stage.startswith("Teen"):                         # else if the Mote's stage starts with "Teen"

                if self.stage == "Teen (Champ)":                        # if Mote's stage is "Teen (Champ)":

#FIRST USE: ternary operator
                    self.stage = "Adult (Chill)" if self.care_mistakes <= 4 else "Adult (Charming)"
                                                                        # if care_mistakes are less than or equal to 1:
                                                                        # set the Mote's stage to "Adult (Chill)"
                                                                        # else set the Mote's stage to "Adult (Charming)"
                                                                        
                else:                                                   # else:
                    self.stage = "Adult (Cheeky)" if self.care_mistakes <= 2 else "Adult (Silly)"
                                                                        # if care_mistakes are less than or equal to 1:
                                                                        # set the Mote's stage to "Adult (Cheeky)"
                                                                        # else set the Mote's stage to "Adult (Silly)"

            elif self.stage.startswith("Adult"):                        # else if the Mote's stage starts with "Adult"

                if self.stage == "Adult (Chill)":                       # if Mote's stage is "Adult (Chill)":
                    self.stage = "Adult (Wobbly)"                       # set the Mote's stage to "Adult (Chill)"

                elif self.stage == "Adult (Cheeky)": self.stage = "Adult (Cranky)"
                                                                        # TIP (you can check and set some shorter statements in one line)
                                                                        # else if Mote's stage is "Adult (Chill)": set the Mote's stage to "Adult (Cranky)"

            self.evolution_timer = 0                                    # set the Mote's evolution timer to 0 since it just evolved

            show_flash_text(self.stage)                                 # call the show_flash_text function and pass the Mote's
                                                                        # stage as an argument


    def render(self):                                                   # create a function within Mote that will be called render
                                                                        # it will pass it self as a parameter when
                                                                        # it is called (unless another is specified)
                                                                        # it will draw the Mote's name, ascii art and some other 
                                                                        # variables to the screen
                                                                        # it will be called every loop of the program and
                                                                        # run through our Mote render routine
#FIRST USE: os.system
#FIRST USE: os.name
#FIRST USE: clear screen
        os.system("cls" if os.name == "nt" else "clear")                # clear the screen, but first check what the operating system is
                                                                        # if operating system name is "nt": pass "cls" to the system function in the os module
                                                                        # else: pass "clear" to the system function in the os module

                                                                        # another way to think of this: if using windows call os.system("cls")
                                                                        # otherwise call os.system("clear")

#FIRST USE: print
#FIRST USE: String Formatting with F-Strings
        print("------------------------------")                         # display a string containing a row of 30 - characters

        print(f"{self.name} — {self.stage} — {self.age} years")         # display a formatted string starting on a new line with
                                                                        # the Mote's name then " - " then the Mote's stage 
                                                                        # then " - " and then Mote's age and then " years"

        print("------------------------------")                         # display a string containing a row of 30 "-" characters

        print(ASCII_ART.get(self.stage, "(._.)"))                       # from the dictionary named ASCII_ART check if there is a
                                                                        # dictionary key with the same name as the Mote's stage
                                                                        # if there is display it, other wise display "(._.)"

        print("------------------------------")                         # display a string containing a row of 30 "-" characters
        
        print(f"Hunger:     {'●'*self.hunger + '○'*(maximum_hunger - self.hunger)}") 
                                                                        # display an ammount of '●' that is equal to the Mote's hunger
                                                                        # of '●' and an ammount of '○' that is equal to the result of the
                                                                        # global maximum_hunger minus the Mote's hunger

        print(f"Happiness:  {'●'*self.happiness + '○'*(maximum_happiness - self.happiness)}")
                                                                        # display an ammount of '●' that is equal to the Mote's happiness
                                                                        # of '●' and an ammount of '○' that is equal to the result of the
                                                                        # global maximum_happiness minus the Mote's happiness

        print(f"Poop:       {self.poop}")                               # display the Mote's poop value

        print(f"Sick:       {'Yes' if self.sick else 'No'}")            # display 'Yes' if the Mote is sick variable is True else display 'No'

        print(f"Misbehaving:{'Yes' if self.misbehaving else 'No'}")     # display 'Yes' if the Mote's misbehaving variable is True else display 'No'

        print(f"Attention:  {'Yes' if self.attention_flag else 'No'}")  # display 'Yes' if the Mote is attention_flag variable is True else display 'No'

        print("------------------------------")                         # display a string containing a row of 30 "-" characters


    def interact(self, choice):                                         # create a function within Mote that will be called interact
                                                                        # it will pass it self as a parameter when
                                                                        # it is called (unless another is specified)
                                                                        # it will also be passed a variable named choice that is an
                                                                        # argument
                                                                        # it will draw the Mote's name, ascii art and some other 
                                                                        # variables to the screen
                                                                        # it will be called every loop of the program and
                                                                        # process what happens to the Mote after the player makes
                                                                        # a choice

        form = BEHAVIOR_MODIFIERS.get(self.stage, {})                   # make a variable named form and make it equal to the 
                                                                        # dictionary from within BEHAVIOR_MODIFIERS that has
                                                                        # the same name as the the Mote's stage. If there is no
                                                                        # dictionary with the same name as the the Mote's stage
                                                                        # within the dictionary named form then make the variable
                                                                        # named form equal to a blank dictionary

        if choice == "7": #reset Mote                                   # if the variable named choice that was passed when this
                                                                        # function was called is equal to 7:
                                                                        
            print("Resetting Mote...")                                  # display a string containing Resetting Mote...

            self.reset()                                                # call the Mote's reset function

#FIRST USE: time.sleep
            time.sleep(1)                                               # call the sleep function from within the time module
                                                                        # and pass the argument 1 (waits for 1 second)

        if not self.alive:                                              # if the Mote's alive variable is not equal to True:

            print("Your Mote has passed. Press [7] to Reset.")          # display a string containing Your Mote has passed. Press [7] to Reset.

            time.sleep(2)                                               # call the sleep function from within the time module
                                                                        # and pass the argument ,3 (*waits for 2 seconds)

            return                                                      # exit this function immediately , no need to go further

        if choice == "1": # feed                                        # if the variable named choice that was passed when this
                                                                        # function was called is equal to 1:

            if self.hunger < maximum_hunger:                            # if the Mote's hunger value is larger than the global
                                                                        # global variable maximum hunger:

                self.hunger += 1                                        # increase the Mote's hunger value by 1

                self.attention_flag = False                             # set the Mote's attention_flag value to False

        elif choice == "2": # play                                      # if the variable named choice that was passed when this
                                                                        # function was called is equal to 2:

            if form.get("refuses_play"):                                # if there is a key named refuses_play within the
                                                                        # dictionary named form that is paired with a value that
                                                                        # is equal to True then:
                                                                        # *note* no other value is needed here, if there is no key
                                                                        # named refuses_play within the dictionary or if the
                                                                        # key named refuses_play within the dictionary is equal to
                                                                        # any value other than True this if condition will not be
                                                                        # processed
 
                print("This Mote refuses to play.")                     # display a string containing This Mote refuses to play.

                time.sleep(1)                                           # call the sleep function from within the time module
                                                                        # and pass the argument 1 (waits for 1 second)

                return                                                  # exit this function immediately , no need to go further

            if not self.misbehaving:                                    # if the Mote's misbehaving value is not equal to True:

                bonus = form.get("play_bonus", 1)                       # create a variable named bonus and set it to be equal to
                                                                        # the value paired with the key named play_bonus in the dictionary named form.
                                                                        # if no key named play_bonus is in the dictionary named form
                                                                        # then set the variable named bonus to be equal to 1
#FIRST USE: min
                self.happiness = min(maximum_happiness, self.happiness + bonus)
                                                                        # set the Mote's happiness value to be equal to the
                                                                        # smaller of:
                                                                        # the global variable maximum_happiness or
                                                                        # the Mote's happiness + bonus
                                                                        # *note* using min keeps the returned value from ever being
                                                                        # larger than the global maximum_happiness value

                self.attention_flag = False                             # set the Mote's attention_flag value to be equal to False

        elif choice == "3": # toilet                                    # if the variable named choice that was passed when this
                                                                        # function was called is equal to 3 then:

            self.poop = 0                                               # set the Mote's poop value to equal 0

            self.attention_flag = False                                 # set the Mote's attention_flag to equal False

        elif choice == "4": # medicine                                  # if the variable named choice that was passed when this
                                                                        # function was called is equal to 4 then:

            if self.sick:                                               # if the Mote's sick value is equal to True

                self.sick = False                                       # set the Mote's sick value to be equal to False

                self.attention_flag = False                             # set the Mote's attention_flag value to be equal to False

        elif choice == "5": # discipline                                # if the variable named choice that was passed when this
                                                                        # function was called is equal to 5 then:

            if self.misbehaving:                                        # if the Mote's misbehaving value is equal to True:

                gain = form.get("discipline_gain", 1)                   # create a variable named gain and set it to be equal to
                                                                        # the value paired with the key named discipline_gain in
                                                                        # the dictionary named form. if no key named discipline_gain
                                                                        # is in the dictionary named form then set the variable named
                                                                        # gain to be equal to 1

                self.misbehaving = False                                # set the Mote's misbehaving value to be equal to False

                self.attention_flag = False                             # set the Mote's attention_flag value to be equal to False

                print(f"Disciplined! Gained {gain} respect.")           # display a formatted string containing "Disciplined! Gained " 
                                                                        # and then the value stored in the variable gain 
                                                                        # and then " respect."

                time.sleep(1)                                           # call the sleep function from within the time module
                                                                        # and pass the argument 1 (waits for 1 second)
                
        elif choice == "6": # stats                                     # if the variable named choice that was passed when this
                                                                        # function was called is equal to 6 then:
                                                                        
             show_stats_screen()                                        # call the show_stats_screen function
                                                                        #


#FIRST USE: main
def main():                                                             # create a global function that will be named main
                                                                        # this function will be the entry point

#FIRST USE: object

    # Create a type of Mote called little_friend will be used in the simulation
    little_friend = Mote()                                              # create an object of the Mote class that is named little_friend
                                                                        # (*note* this object is the instance of the Mote class
                                                                        # that will be simulated using all the data and functions contained
                                                                        # within the Mote class during the game loop)
#FIRST USE: input
    # Ask what the little_friend's name should be
    little_friend.name = input("> What is your Mote's name? ")          # display a string containing "> What is your Mote's name? "
                                                                        # and sets the variable named name within the little_friend object
                                                                        #  to whatever the player has typed before pressing enter



##############
## THE GAME ##
#########################################################################
#                                                                       #
#   SET THE GAME TO START                                               #
#   ---------------------                                               #
#                                                                       #
    game_is_running = True                                              # create a variable name game_is_running and set it to equal True
#                                                                       # (*note* this is the main game loop)
#                                                                       #
#   DRAW TO THE SCREEN ONE TIME BEFORE DOING ANYTHING ELSE              #
#   ------------------------------------------------------              #
#                                                                       #
    little_friend.render()                                              # call the render function that is within the little_friend object
#                                                                       # (*note* this will "draw" the default state of little_friend to 
##################                                                      # the screen one before any player input)
# THE GAME LOOP ##                                                      #
#########################################################################
#FIRST USE: while                                                       #
    while game_is_running:                                              # while game_is_running is equal to True: do the following:
                                                                        # (*note* anything in this while loop is part of the game loop
                                                                        # and will be ran sequentially in a never ending loop until
#                                                                       # the variable named game_is_running is no longer equal to True)
#       (1) GET THE PLAYER's INPUT                                      #
#       --------------------------                                      # "draw" our very simple HUD (Heads Up Display)
        print("[1] Feed  [2] Play  [3] Toilet")                         # display a string containing "[1] Feed  [2] Play  [3] Toilet" 
        print("[4] Medicine  [5] Discipline  [6] Stats")                # display a string containing "[4] Medicine  [5] Discipline  [6] Stats" 
        print("[7] Reset  [Q] Quit")                                    # display a string containing "[7] Reset  [Q] Quit" 
#                                                                       #
                                                                        # get the player's input (*note* this is the game's "controls")
#FIRST USE: strip                                                       #
#FIRST USE: upper                                                       #
        choice = input("> Choose action: ").strip().upper()             # display a string containing "> Choose action: "
#                                                                       # and create a variable named choice that is equal to what
#                                                                       # the player has typed before pressing enter
#                                                                       # after the spaces have been stripped from the start and end
#                                                                       # and all the letters have been made upper case
#       (2) CHECK IF THE PLAYER WANTS TO QUIT                           #
#       -------------------------------------                           #
        if choice == "Q":                                               # if the variable named choice is equal to the string "Q":
            game_is_running = False                                     # set the variable named game_is_running to be equal to False
#                                                                       # (*note* this will exit the game)
#       (3) RUN PLAYER CONTOL LOGIC                                     #
#       ---------------------------                                     #                                                                        
        little_friend.interact(choice)                                  # call the interact function that is within the little_friend object
                                                                        # (*note* this will run through the game logic that happens
                                                                        # after the player presses a key)
#       (4) RUN AI LOGIC                                                #
#       ----------------                                                #   
        little_friend.ai()                                              # call the ai function that is within the little_friend object
                                                                        # (*note* this will run through the ai logic and update the
                                                                        # all of the little_friend object's variables)
#       (5) RENDER GAME TO SCREEN                                       #
#       -------------------------                                       #  
        little_friend.render()                                          # call the render function that is within the little_friend object
                                                                        # (*note* this will "draw" the current state of little_friend to
                                                                        # the screen)
#       (6) WAIT TO PREVENT SCREEN FLICKER                              #
#       ----------------------------------                              #  
        time.sleep(0.5)                                                 # call the sleep function from within the time module
                                                                        # and pass the argument .5 (waits for half of a second)
#   RETURN TO THE BEGINNING OF THE WHILE LOOP AND REPEAT STEPS 1 to 6   #
#   -----------------------------------------------------------------   #
#                                                                       #
#                                                                       #
#   game loop summary                                                   #
#   -----------------                                                   #
#   process user input  (1) and (2)                                     #
#   update game state   (3) and (4)                                     #
#   render visuals      (5) and (6)                                     #
#########################################################################


#           CHALLENGE 0:
#           ------------
#           find out why computers count from 0

#           CHALLENGE 1:
#           ------------
#           break this program by altering everything you can think of
#           download it again and break that copy as well, it is the
#           practice egg you break before making your omelette

#           CHALLENGE 2:
#           ------------
#           try and deduce how the following 2 functions work


def show_flash_text(stage):
    frame1 = f"* {stage} *"
    frame2 = " "
#FIRST USE: range
    for _ in range(3):
        os.system("cls" if os.name == "nt" else "clear")
#FIRST USE \n
#FIRST USE: center
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

#           CHALLENGE 3:
#           ------------
#           Return to BEHAVIOR_MODIFIERS near the top of this module
#           that was skipped over with no explanation and see if you
#           can work out what each key:value pair in the nested dictionary
#           does and try changing some of them and add stuff to others to alter
#           the personality of the Mote's and change the balance of the game

def show_stats_screen():
    # *unfinished*
    show_under_construction_flash()

#           CHALLENGE 4:
#           ------------
#           complete the *unfinished* show_stats_screen function to show the variable values
#           that you think are important in a fun way that isn't too ugly
#
#           (example)
#           print(f"My name is Mote.name} and I am {Mote.age} years old!")
#
#           remember to remove the call to the show_under_construction_flash
#           when you are finished
#           think of other "stats" might you keep track of?
#           create those stats, change them in fun ways, make them interact with
#           the Mote's other stats


#           CHALLENGE 5:
#           ------------
#           add a "teen (Delinquent)" Mote to the ASCII_ART dictionary
#
#           add an elif condition between the other teen types of Mote
#           inside the check_evolution function within the Mote class
#           and code how it "evolves"
#
#           (*example*)
#           elif self.misbehaving and random.random() < .2: self.stage = "Teen (Delinquent)"
#
#           will evolve a Teen (Delinquent) Mote if it is both naughty and a random number
#           between 0 and 1 is lower than .2 (a child who is misbehaving when it evolves
#           will have a 20% to evolve into a Teen (Delinquent))
#           if you copy and paste it, make sure to use the correct indentation
#
#           add some "personality traits" to the BEHAVIOR_MODIFIERS dictionary
#
#           add it's entry into the years_in_stage dictionary that is inside the
#           check_evolution function within the Mote class (if you want it to evolve)


#           CHALLENGE 6:
#           ------------
#           research what the following lines of code mean
#
if __name__ == "__main__":
    main()

#FIRST USE: multiline comment
"""
DOWNLOAD PYTHON INSTALL MANAGER <https://www.python.org/downloads/>

RUN A PYTHON SCRIPT <https://realpython.com/run-python-scripts/>

SET UP INTEGRATED DEVELOPMENT ENVIRONMENT <user preference, user to research different python IDEs>

VIRTUAL ENVIRONMENT <https://www.geeksforgeeks.org/python/python-virtual-environment/>

INSTALL PYINSTALLER <https://pypi.org/project/pyinstaller/>

COMPILE GAME USING PYINSTALLER <https://pypi.org/project/pyinstaller/>
"""

#FIRST USE: comment <https://www.geeksforgeeks.org/python/python-comments/>

#FIRST USE: import <https://www.geeksforgeeks.org/python/import-module-python/>

#FIRST USE: function <https://www.geeksforgeeks.org/python/python-functions/>

#FIRST USE: variable <https://www.geeksforgeeks.org/python/python-variables/>

#FIRST USE: integer <https://www.geeksforgeeks.org/python/python-numbers/>

#FIRST USE: float <https://www.geeksforgeeks.org/python/python-float-type-and-its-meth>

#FIRST USE: global and local variables <https://www.geeksforgeeks.org/python/global-local-variables-python/>

#FIRST USE: dictionary <https://www.geeksforgeeks.org/python/python-dictionary/>

#FIRST USE: = <https://www.geeksforgeeks.org/computer-science-fundamentals/expressions-in-python/>

#FIRST USE: dictionary keys <https://www.geeksforgeeks.org/python/python-dictionary-keys-method/>

#FIRST USE: indentation <https://www.geeksforgeeks.org/python/indentation-in-python/>

#FIRST USE: string <https://www.geeksforgeeks.org/python/python-string/>

#FIRST USE: raw string <https://www.geeksforgeeks.org/python/python-raw-strings/>

#FIRST USE: nested dictionary <https://www.geeksforgeeks.org/python/python-nested-dictionary/>

#FIRST USE: boolean <https://www.geeksforgeeks.org/python/boolean-data-type-in-python/>

#FIRST USE: class <https://www.geeksforgeeks.org/python/python-classes-and-objects/>

#FIRST USE: def <https://www.geeksforgeeks.org/python/python-def-keyword/>

#FIRST USE: __init__ <https://www.geeksforgeeks.org/python/__init__-in-python/>

#FIRST USE: self <https://www.geeksforgeeks.org/python/self-in-python-class/>

#FIRST USE: parameter <https://www.geeksforgeeks.org/python/deep-dive-into-parameters-and-arguments-in-python/>

#FIRST USE: calling a function <https://www.geeksforgeeks.org/python/how-to-call-a-function-in-python-2/>

#FIRST USE: if <https://www.geeksforgeeks.org/python/python-if-else/>

#FIRST USE: not <https://www.geeksforgeeks.org/python/python-not-keyword/>

#FIRST USE: return <https://www.geeksforgeeks.org/python/python-def-keyword/>        *note* return can return no value

#FIRST USE: += <https://www.geeksforgeeks.org/python/g-fact-21-increment-and-decrement-operators-in-python/>

#FIRST USE: >= <https://www.geeksforgeeks.org/python/relational-operators-in-python/>

#FIRST USE: random.random <https://www.geeksforgeeks.org/python/python-random-module/>

#FIRST USE: <= <https://www.geeksforgeeks.org/python/relational-operators-in-python/>

#FIRST USE: max <https://www.geeksforgeeks.org/python/python-max-function/>

#FIRST USE: modulo <https://www.geeksforgeeks.org/python/what-is-a-modulo-operator-in-python/>

#FIRST USE: == <https://www.geeksforgeeks.org/python/relational-operators-in-python/>

#FIRST USE: and <https://www.geeksforgeeks.org/python/python-logical-operators/>

#FIRST USE: or <https://www.geeksforgeeks.org/python/python-or-operator/>

#FIRST USE: get <https://www.geeksforgeeks.org/python/python-dictionary-get-method/>

#FIRST USE: any <https://www.geeksforgeeks.org/python/python-any-function/>

#FIRST USE: elif <https://www.geeksforgeeks.org/python/python3-if-if-else-nested-if-if-elif-statements/>

#FIRST USE: else <https://www.geeksforgeeks.org/python/python-if-else/>

#FIRST USE: startswith <https://www.geeksforgeeks.org/python/python-string-startswith/>

#FIRST USE: ternary operator <https://www.geeksforgeeks.org/python/ternary-operator-in-python/>

#FIRST USE: os.system <https://www.geeksforgeeks.org/python/python-os-system-method/>

#FIRST USE: os.name <https://www.geeksforgeeks.org/python/os-module-python-examples/>
#                   <https://www.geeksforgeeks.org/python/get-os-name-and-version-in-python/>
                   
#FIRST USE: clear screen <https://www.geeksforgeeks.org/python/clear-screen-python/>

#FIRST USE: print <https://www.geeksforgeeks.org/python/python-output-using-print-function/>

#FIRST USE: String Formatting with F-Strings <https://www.geeksforgeeks.org/python/string-formatting-in-python/>

#FIRST USE: time.sleep <https://www.geeksforgeeks.org/python/sleep-in-python/>

#FIRST USE: min <https://www.geeksforgeeks.org/python/python-min-function/>

#FIRST USE: main <https://www.geeksforgeeks.org/python/python-main-function/>

#FIRST USE: object <https://www.geeksforgeeks.org/python/python-object/>

#FIRST USE: input <https://www.geeksforgeeks.org/python/python-input-function/>

#FIRST USE: while <https://www.geeksforgeeks.org/python/python-while-loop/>

#FIRST USE: strip <https://www.geeksforgeeks.org/python/python-string-strip/>

#FIRST USE: upper <https://www.geeksforgeeks.org/python/python-string-upper/>

#FIRST USE: range <https://www.geeksforgeeks.org/python/python-range-function/>

#FIRST USE \n <https://www.geeksforgeeks.org/python/python-new-line-add-print-a-new-line/>

#FIRST USE: center <https://www.geeksforgeeks.org/python/python-string-center-method/>

#FIRST USE: __name__ <https://www.geeksforgeeks.org/python/__name__-a-special-variable-in-python/>

#FIRST USE: __main__ <https://www.geeksforgeeks.org/python/usage-of-__main__-py-in-python/>

#FIRST USE: multiline comment <https://www.geeksforgeeks.org/python/multiline-comments-in-python/>