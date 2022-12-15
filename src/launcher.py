from src.solver import AI_wordle_solver

""" Where you can launch wordle game """

TURN_LIMIT = 6


def normal_play(game, wordlist):
    
    for t in range(1, TURN_LIMIT+1):
        end_turn = 0
        while end_turn == 0:
            guess = input(f"Turn: {t} Input your 5 letters word guess: ")

            if len(guess) != 5 or wordlist.word_in_list(guess):
                print ("\n[!] This word doesn't exist or len too long\n")
                continue

            end_turn = 1
            game.change_result(guess)
            print (f"Result: {game.result}\n")

            if game.is_winning():
                print ("Congrats, you win !")
                return 1

    print (f"You lost ! The word was {guess}")


def AI_play(game, wordlist):
    algo = AI_wordle_solver(wordlist)

    for t in range(1, TURN_LIMIT+1):
        guess = algo.make_guess()
        game.change_result(guess)

        if game.is_winning():
            break

    return {"Win": game.is_winning(), "Result": game.result, "Turn": t}