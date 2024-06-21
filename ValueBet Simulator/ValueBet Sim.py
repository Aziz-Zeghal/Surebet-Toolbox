import csv
import pandas as pd
import random
import matplotlib.pyplot as plt

import csv
import pandas as pd
import random

def multiple_sim(file_path, bankroll_size, stack_size, num_simulations):
    # Load text file
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        info = []
        for row in reader:
            value_odd = row[0][0:5]
            true_prob = round((float(row[0][-2:]) + float(row[1][0])*0.1)/100, 3)
            surevaluation = float(row[1][-2:] + '.' + row[2].replace('%', ''))
            info.append((float(value_odd), true_prob, surevaluation))
    
    # Convert list to pandas dataframe
    data = pd.DataFrame(info, columns=['value_odd', 'true_prob', 'surevaluation'])
    
    # Initialize variables
    results = {'num_simulations': num_simulations,
               'bets_placed': [],
               'bankroll_final': [],
               'profit_total': [],
               'winning_simulations': 0}
    
    for i in range(num_simulations):
        # Add a new column to the dataframe to track the bankroll after each bet
        data['bankroll'] = bankroll_size

        # Initialize variables
        bankroll = bankroll_size
        bets_placed = 0
        total_profit = 0

        # Iterate through each row in the data
        for index, row in data.iterrows():
            # Calculate the bet size based on the stack size
            bet_size = stack_size

            # Place the bet
            bankroll -= bet_size
            bets_placed += 1

            # Determine if the bet wins or loses
            if random.uniform(0, 1) < row['true_prob']:
                # Bet wins
                outcome = "won"
                profit = bet_size * row['value_odd']
                total_profit += profit - bet_size
                bankroll += profit
            else:
                # Bet loses
                outcome = "lost"
                profit = -bet_size
                total_profit += profit

            # Update the bankroll column in the dataframe
            data.at[index, 'bankroll'] = bankroll

            # Stop the simulation if the bankroll is depleted
            if bankroll <= 0:
                break

        # Save the simulation results
        results['bets_placed'].append(bets_placed)
        results['bankroll_final'].append(bankroll)
        results['profit_total'].append(total_profit)
        
        # Check if the end bankroll is greater than or equal to the starting bankroll
        if bankroll >= bankroll_size:
            results['winning_simulations'] += 1
        
        # Print the final bankroll for this simulation
        print(f"Simulation {i+1} final bankroll: {bankroll:.4f}")

    # Calculate the statistics and print the results
    win_rate = results['winning_simulations'] / num_simulations
    profit_mean = sum(results['profit_total']) / num_simulations
    profit_std = (sum((x - profit_mean)**2 for x in results['profit_total']) / (num_simulations - 1))**0.5
    print(f"\nWin rate: {win_rate:.2%}")
    print(f"Average profit: {profit_mean:.2f}")
    print(f"Profit standard deviation: {profit_std:.2f}")



def simulate_value_betting(file_path, bankroll_size, stack_size):
    # Load text file
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        info = []
        for row in reader:
            value_odd = row[0][0:5]
            true_prob = round((float(row[0][-2:]) + float(row[1][0])*0.1)/100, 3)
            surevaluation = float(row[1][-2:] + '.' + row[2].replace('%', ''))
            info.append((float(value_odd), true_prob, surevaluation))
    
    # Convert list to pandas dataframe
    data = pd.DataFrame(info, columns=['value_odd', 'true_prob', 'surevaluation'])
    
    # Add a new column to the dataframe to track the bankroll after each bet
    data['bankroll'] = bankroll_size
    
    # Initialize variables
    bankroll = bankroll_size
    bets_placed = 0
    total_profit = 0
    bankroll_history = []
    
    # Iterate through each row in the data
    for index, row in data.iterrows():
        # Calculate the bet size based on the stack size
        bet_size = stack_size
        
        # Place the bet
        bankroll -= bet_size
        bets_placed += 1
        
        # Determine if the bet wins or loses
        if random.uniform(0, 1) < row['true_prob']:
            # Bet wins
            outcome = "won"
            profit = bet_size * row['value_odd']
            total_profit += profit - bet_size
            bankroll += profit
        else:
            # Bet loses
            outcome = "lost"
            profit = -bet_size
            total_profit += profit
        
        # Update the bankroll column in the dataframe
        data.at[index, 'bankroll'] = bankroll
        bankroll_history.append(bankroll)
        #print(f"BET {bets_placed}: {bet_size} @ {row['value_odd']} ({row['true_prob']:.2f}), {outcome}")

        # Stop the simulation if the bankroll is depleted
        if bankroll <= 0:
            break
    
    # Calculate and return the results
    print(f"Bets placed: {bets_placed}\nBankroll: {bankroll:.3f}€\nTotal profit: {total_profit:.3f} €")

    win_rate = bets_placed / len(data)
    plt.plot(bankroll_history)
    plt.xlabel('Bet')
    plt.ylabel('Bankroll (€)')
    plt.show()


def print_file(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            value_odd = row[0][0:5]
            true_prob = round((float(row[0][-2:]) + float(row[1][0])*0.1)/100, 3)
            surevaluation = float(row[1][-2:] + '.' + row[2].replace('%', ''))
            data.append((value_odd, true_prob, surevaluation))
            print(value_odd, true_prob, surevaluation)

#print_file("bet_data.txt")
#simulate_value_betting("bet_dataBIG.txt", 100, 4)
multiple_sim("bet_dataBIG.txt", 100, 3, 300)