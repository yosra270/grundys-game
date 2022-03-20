from decision_rules.minimax import play
from decision_rules.minimax_alpha_beta_prunning import play_ab


def main():
    print("Which algorithm would you like to choose :")

    print("\n\t1/ MINIMAX")
    print("\t2/ Alpha Beta")    

    algorithm = int(input("\n_ : "))

    if algorithm ==1 :
        play()
    else:
        play_ab()

if __name__ == '__main__':
    main()