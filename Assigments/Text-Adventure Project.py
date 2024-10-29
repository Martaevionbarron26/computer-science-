def start_your_sports_career():
    print("This is your start to your football career where will your career go?")
    print("1. QB")
    print("2. WR")
  #picking what position you want to play

    choice = input("> ")
   
   
    if choice == "1":
        QB_Career()
    elif choice == "2":
        WR_Career()
    else:
        print("Invalid choice. try again.")
        start_your_sports_career()
# srarting your career

def QB_Career():
    print("Nice i see you want to be a quater back we can make that happen")
    print("What type of player are you?")
    print("1. Impolsive QB")
    print("2. Filed Genrater QB")
    print("3. Scrambler QB")
    Player_Build = input("> ")

    if Player_Build == "1":
        impolsive_QB()
    elif Player_Build == "2":
        Gunslingers_QB()
    elif Player_Build == "3":
        Scrambler_QB()
    else:
        print("Invalid choice, try agin.")
        QB_Career()
    
    first_NFL_game_for_QB()
    # Chose what buils you want to be.
def WR_Career():
    print("I see you chose wide reciver we can make that happen")
    print("what type of player are you?")
    print("1. Deep treat WR")
    print("2. Rout runner WR")
    print("3. Pysical WR")
    Player_Build = input("> ")

    if Player_Build == "1":
        deept_treat_WR()
    elif Player_Build == "2":
        route_runner_WR()
    elif Player_Build == "3":
        physical_WR()
    else:
        print("Invalid choice, try again")
        WR_Career()
    
    first_nfl_game_for_WR()
#chose you biuld
def impolsive_QB():
    print("I see you chose impolsive QB your player will be like Cam newton now its time to play you have been drafthed to the vikings.")
# who your player build will be like 
def Gunslingers_QB():
    print("I see that you chose gunslinger QB your player build will be like Aaron Rodgers But know its time to play you have been drafthed to the steelers.")
# who your player build will be like 
def Scrambler_QB():
    print("I see that you chose scrambler QB your player will be like Mike Vick but now its time to play you have been drafthed to the chargers.")
# who your player build will be like 



def deept_treat_WR():
    print("I see you want you chose deep threat WR your player will be like Tyreek Hill but know its time to play you have been drafthed to the giants.")
#what olayer you are going to be like 
def route_runner_WR():
    print("I see you chose route runner WR your player will be like Antiono Brown but know its time to play you have been drafthed to the panthers.")
#what olayer you are going to be like 
def physical_WR():
    print("I see you chose Physical WR your player will be like Aj Brown  but now its time to play you have been drafthed to the cardinals")
#what olayer you are going to be like 


def first_NFL_game_for_QB():
    print("Its your first nfl game and coach wanted to suprise you for doing good at pratice but im going to spill it for you you are going to start this game so don't go out there scared this is your game.")
    print("also make sure to wear your your rib protecter!")
    print("1. Wear your rib protecter and go out looking like a scrub LOW CHANCE of getting injerd")
    print("2. Don't wear your rib protecter and go out with drip HIGH CHANCE of getting injerd")
#first gameye
    choice = input("> ")
    if choice == ("1"):
        your_fine_walk_it_off()

    elif choice == ("2"):
        your_career_is_over()
    
    else:
        print("Invalid choice, try again.")




def your_fine_walk_it_off():
    print("Luckly you put rib protecter on he hit you so hard we thoght you diead but walk it off you will be fine.")
    right_choice_QB()

def your_career_is_over():
    print("Well Next time lisen to coach now your career is over your perlized.")

    try_again = input("Want to try again?")

    if try_again == "yes":
        start_your_sports_career()



def first_nfl_game_for_WR():
    print("Its your first nfl game and coach wanted to suprise you for doing good at pratice but im going to spill it for you you are going to start this game so don't go out there scared this is your game.")
    print("Make sure you wear your arm brace!")
    print("1. Wear your arm rib protecter and look like a scrub LOW CHANCE of getting injerd")
    print("2. Don't wear your rib protecter and have drip HIGH CHANCE of getting injerd")
#first game
    choice = input("> ")
    if choice == "1":
        get_up_you_will_be_fine()
    elif choice == "2":
        just_like_that_your_done()
    else:
        print("invalid choice, try again")
        first_nfl_game_for_WR

def get_up_you_will_be_fine():
    print("Good thing you not hard headed get up you will be fine.")
    good_your_back()

def just_like_that_your_done():
    print("Just like that you just ruiend your career next time listen.")

    try_again = input("Want to try again?")

    if try_again == "yes":
        start_your_sports_career()

def right_choice_QB():
    print("I see that you have made the right decision that hit was pretty hard but these are your options.")
    print("1. Take an week to condition and shake back")
    print("or")
    print("2. play the next game while hurt")

    choice = input("> ")

    if choice == "1":
        good_your_back_helthey()
    
    elif choice == "2":
        not_again()
    else:
        print("Invalid chose, try again.")
        right_choice_QB()

def good_your_back_helthey():
    print("Good your back healthey coach is ready to start you again.")
    first_wild_card_game_QB()

def not_again():
    print("Your hurt again coch is going to trade you if you get hurt again")

    try_again = input("Want to try again?")
    if try_again == "yes":
        start_your_sports_career()
#Got answer rong try again

def good_your_back_WR():
    print("I see that you have mahe the right decision that hit was pretty hard but these are your options.")
    print("1. Take an week to condition and shake back")
    print("or")
    print("2. play the next game while hurt")
#your back from injery reserve 
    choice = input("> ")
    if choice == "1":
        good_your_back()

    elif choice == "2":
        you_cant_be_foreal()
    else:
        print("Invalid choice, try again.")
        good_your_back_WR() # did not pick the choices you have

def good_your_back():
    print("Good your back healthey coach is ready to start you again.")
    first_wild_card_game_Wr()
#made the right choice 
def you_cant_be_foreal():
    print("Your hurt again coch is going to trade you if you get hurt again")
#bad choice 
    try_again = input("Want to try agian?")
    if try_again == "yes":
        first_nfl_game_for_WR() #picked worng answer if you wnat to play again type yes



def first_wild_card_game_QB():
    print("You have been doing great this season your leading the leage in yards")
    print("But its time to show your real talent you in the playoffs now so it's time to realy lock in.")
    print("1. wear an arm sleeve get better trowing threw the game")
    print("2. wear an leg sleeve better speed threw the game.")
    #Boost your player
    choice = input("> ")
    if choice == "1":
        arm_sleeve()

    elif choice == "2":
        leg_sleeve()

    else:
        print("Invalid choice, try again")
        first_wild_card_game_QB() # picked the rong answer so try again

def arm_sleeve():
    print("Your chose arm sleve low chance of trowing picks.")
    in_wild_card_game_QB() # to run the code 
    #Boost for picking arm sleeve

def leg_sleeve():
    print("Your chose leg sleeve you faster than every one in this game.")
    in_wild_card_game_QB() # to run the code
    #boost for picking leg sleeve

def first_wild_card_game_Wr():
      print("You have been doing great this season your leading the leage in receptions.")
      print("But its time to show your real talent you in the playoffs now so it's time to realy lock in pick what you want to wear in game boost your game play.")
      print("1. Wear gloves better cathing")
      print("2. Wear leg sleeve for better relese")

      choice = input("> ")
      if choice == "1":
          gloves()

      elif choice == "2":
          leg()
      else:
          print("Invalid choice, try again")
          first_wild_card_game_Wr()
        

def gloves():
    print("you chose gloves any ball that come your way will get caught but now its time to get in the game.")
    in_wild_card_game_WR() # run the code
def leg():
    print("you chose leg sleeve on a streak you will all ways beat your oppenet but now its time to get in the game.")
    in_wild_card_game_WR() # run the code

def in_wild_card_game_QB():
    print("your in the 4th quarter with 20 sec left score to make it to the next playoff round")
    print("Throw the the ball on 4th and 5 and win the or run")
    print("1. run")
    print("2. pass")

    choice = input("> ")
    if choice == "1":
        run()

    elif choice == "2":
        pass_()
    else:
        print("Invalid choice, try again")
        in_wild_card_game_QB()

def run():
    print("You chose to scramble high risk come with high reward you scored the game winning TOUCHDOWN")
    week_before_the_super_bowl() # run code
    #Chose to run the ball 


def pass_():
    print("You choses to pass the ball you scared me and coach with that pass but it was an TOUCHDOWN")
    week_before_the_super_bowl() # run code
     #Chose to pass the ball

def in_wild_card_game_WR():
    print("your in the 4th quarter with 20 sec left score to make it to the next playoff round")
    print("Run an zig rout on the 5 yard line or run an fade ball in headtap for game ")
    print("1. Head tap")
    print("2. zig")

    choice = input("> ")
    if choice == "1":
        HEAD_TAP()
    elif choice == "2":
        omg()
    else:
        print("Invalid choice, try again,")
        in_wild_card_game_WR()

def HEAD_TAP():
    print("OMG he just HEAD TAP him for game your the goat.")
    week_before_the_super_bowl() # run code
def omg():
    ("OMG he just cooked him for game can you sighn my jersey.")
    week_before_the_super_bowl() # run code


def week_before_the_super_bowl():
    print("Its the week before the super bowl and your scared your not good enogh and you know someone who sells steroids.")
    print("1. Take roids and get max attrubuties.")
    print("or")
    print("2. dont take roids")

    choice = input("> ")
    if choice == "1":
        max_()
    elif choice == "2":
        regular()
    else:
        print("Invalid choice, try again.")
        week_before_the_super_bowl()

def max_():
    print("Your maxed out on all your stats in super bowl game.")
    super_bowl_game_Both()

def regular():
    print("stats stay same but huge boost to confidence.")
    super_bowl_game_Both() # Code to run for qb and wr



def super_bowl_game_Both(): #for wr and qb
    print("Its the big day show why you will be one of the greatest.")
    print("Its 4th in 1 3sec lrfth on the clock.")
    print("1. Tush push")
    print("or")
    print("2. rpo")
    
    choice = input("> ")
    if choice == "1":
        tush_Push()
    elif choice == "2":
        rpo()
    else:
        print("Invalid choice, try again")
        super_bowl_game_Both()



def tush_Push():
    print("Is he in LETSSS go we won the super bowl")
    you_won_the_super_bowl() #Run the end game code 


def rpo():
    print("OMG that was risky but he is in Tuchdown.")
    you_won_the_super_bowl() #Run the end game code 


def you_won_the_super_bowl():
    print("you won there an afther party you down to come.")
    print("go to the afthere party.")
    print("or")
    print("go celebrate with family.")

    choice = input("> ")
    if choice == "1":
        go()

    elif choice == "2":
        go_with_fam()
    else:
        print("Invalid choice, try again.")
        you_won_the_super_bowl()

def go():
    print("you went to the club had a fun time but afther you were out side in got crossed in an cross fire and got hit in the head.")

    try_again = input("Want to try again?")
    if try_again == "yes":
        you_won_the_super_bowl()


def go_with_fam():
    print("You went with with you family and had a great night and for the next five years you were doing great and won 4 more super bowls and the best to ever do it the end.")
    



start_your_sports_career()