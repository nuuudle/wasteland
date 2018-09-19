#oregon trail kopi??? idfk
import time
import random

#------------------------------------------
m_name = "..."
m_atk = 10
m_hp = 100
m_def = 20
#------------------------------------------
p_name = "Connor"
p_atk = 10
p_hp = 100
p_def = 20
#------------------------------------------

def game_start_chardev():
    print("Stranger" + ": What's up nigger.")
    time.sleep(1.5)
    print("Stranger" + ": Nice wagon you got there, mind if I join ya?")
    time.sleep(0.5)
    #print("--------------------------------------------")

    answer_game_start = input("(Press Y for 'yes' and N for 'no')")
    if answer_game_start == "N" or "n":
        print("Stranger" + ": Nice")
        print("The stranger hops on the seat beside you.")
    elif answer_game_start == "Y" or "y":
        print("Stranger" + ": Meh, still joining you, it gets lonely out on the wasteland.")
        print("The stranger hops on the seat beside you.")
    else:
        print("(That's not a valid command.)")

    time.sleep(1)
    print("A couple of minutes of silence goes by.")
    time.sleep(0.5)

    print(p_name + ": By the way, what's your name? Mine's Connor.")
    m_name = input("(What's your name?)")

    time.sleep(0.5)
    print(p_name + ": So, {} is your name huh, good to know.".format(m_name))





game_start_chardev()
