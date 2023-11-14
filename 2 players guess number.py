def guess():

    import random
    main_num = random.randint(0, 100)
    print(main_num)

    player1 = str(input("Enter The First Player Name : "))
    player2 = str(input("Enter The Second Player Name : "))
    
    while 1:
        
        player1_num = int(input("Enter The First Player Guess Number : "))
        player2_num = int(input("Enter The Second Player Guess Number : "))

        if player1_num == player2_num == main_num:
            print(f"Both {player1} and {player2} are Win.")
            break

        if player1_num == main_num:
            print(f"{player1} Wins.")
            print(f"{player2} Lose.")
            break

        if player2_num == main_num:
            print(f"{player2} Wins.")
            print(f"{player1} Lose.")
            break

        if player1_num > main_num:
            print(f"{player1_num} is Too Large.")

        if player2_num > main_num:
            print(f"{player2_num} is Too Large.")

        if player1_num < main_num:
            print(f"{player1_num} is Too Small.")

        if player2_num < main_num:
            print(f"{player2_num} is Too Small.")

        else:
            pass

guess()