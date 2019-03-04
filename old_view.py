import os
class View():

    def welcome_screen(self):
        print('Welcome to Terminal Trader!')
        print()
        print('Please make a selection - choose 1, 2, or 3')
        print()
        print('1. create account')
        print('2. login')
        print('3. quit')
        print()
        return input()


    def get_username(self):
        print()
        print("Please enter a username:")
        print()
        return input()

    def add_balance(self):
        print()
        print('How much would you like to add to your account?')
        print()
        return input()

    def get_password(self):
        print()
        print('Please enter a password')
        print()
        return input()

    def confirm_password(self):
        print()
        print('Please confirm your password')
        print()
        return input("Press the 'Return' key when complete\n")

    def improper_password(self):
        print()
        print('Passwords do not match! Please try again')
        print()

    def improper_balance(self):
        print()
        print('Balance is invalid - please enter only a numeric positive value')
        print()

    def improper_selection(self):
        print()
        print('Please try again - choose from available options')
        print()

    def goodbye(self):
        print()
        print('Thank you - Goodbye!')
        print()

    def logged_in_screen(self, username, balance):
        print()
        print("Hello {username}".format(username))
        print('Your current balance is {balance}'.format(balance))
        print()
        print('Main Menu: ')
        print()
        print('\t1. see positions')
        print('\t2. deposit money')
        print('\t3. look up stock price')
        print('\t4. buy stock')
        print('\t5. sell stock')
        print('\t6. trade history')
        print('\t7. logout')
        print('\t8. logout and quit')
        print('\t9. Top traded stocks')
        return input()

    def positions(self, account, user_position):
        print()
        print('Here are the positions for {account.username}: '.format(account.username))
        print()
        print('Ticker: {user_position.ticker}, Shares: {user_position.shares}'.format(user_position.ticker, user_position.shares))

    def deposit_funds(self):
        print()
        print('How much woud you like to deposit?')
        print()
        return input()

    def request_ticker_symbol(self):
        print()
        print('Please enter a ticker symbol')
        print()
        return input()

    def return_ticker_symbol_price(self, ticker_response):
        print('Current price for {ticker_response[0]} is {ticker_response[1]}'.format(ticker_response[0], ticker_response[1]))

    def improper_ticker(self):
        print('Invalid ticker supplied - please try again')

    def select_trade_option(self, username):
        print()
        print('Select trade option for {username}'.format(username))
        print('a) View all trade history')
        print('b) View trade history by ticker')
        print('c) Go back to the homepage')
        return input()

    def show_trades(self, username, trade):
        print()
        print('Ticker: {trade.ticker} Volume: {trade.volume} Price: {trade.price}'.format(trade.ticker, trade.volume, trade.price))

    def get_shares(self, current_price):
        print()
        print("Please provide number of shares you'd like to buy")
        print("Current price for {current_price[0]} is {current_price[1]}".format(current_price[0], current_price[1]))
        return input()

    def sell_shares(self):
        print()
        print('How many shares would you like to sell?')
        return input()

    def clearscreen(self):
        os.system('clear')

    def wups(self):
        print("Guess you don't have enough!!!")
    def insufficient_funds(self):
        print('You have insufficient funds for this transaction')
    def sell_shares_amount(self):
        print()
        print('How may shares would you like to sell?')
        return input()