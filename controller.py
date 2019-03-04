from app.account import Account
from app.view import View
from app.util import get_price
from app.util import top_traded
import time

view = View()

def run ():
    welcome_homepage()

def welcome_homepage():
    while True:
        selection = view.welcome_screen()
        if selection not in ['1','2','3']:
            view.improper_selection()
            continue

        if selection == '1':
            username, balance, password, confirm_password = view.get_username(), view.add_balance(), view.get_password(), view.confirm_password()

            if password != confirm_password:
                view.improper_password()
                continue
            if not balance.isdigit() or int(balance) < 0:
                view.improper_balance()
                continue

            account = Account(username = username, balance = balance)
            hashed_pw = Account.set_password(account, password)
            
            account.save()
            logged_in_homepage(account)
            return
        elif selection == '2':
            username, password = view.get_username(), view.get_password()
            logged_in_account = Account.login(username=username, password=password)

            if logged_in_account:
                logged_in_homepage(logged_in_account)
                return
            else:
                print('Invalid credentials supplied')
                continue
        elif selection == '3':
            view.goodbye()
            return

def logged_in_homepage(account):

    while True:
        print(account.username, account.balance)
        selection = view.logged_in_screen(account.username, account.balance)

        if selection not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            view.improper_selection()
            time.sleep(3)

        if selection == '1':
            Account.get_positions(account)

        elif selection == '2':
            deposit = view.deposit_funds()
            if not deposit.isdigit() or int(deposit) < 1:
                view.improper_balance()
                time.sleep(3)
            else:
                account.balance = int(account.balance) + int(deposit)
                account.save()
                continue

        elif selection == '3':
            ticker_request = view.request_ticker_symbol()
            ticker_response = get_price(ticker_request)
            if type(ticker_response) == list:
                view.return_ticker_symbol_price(ticker_response)
                time.sleep(2)
            else:
                view.improper_ticker()
                time.sleep(3)

        elif selection == '4':
            ticker = view.request_ticker_symbol()
            current_price = get_price(ticker)
            share_amount = view.get_shares(current_price)
            if share_amount:
                try:
                    Account.buy(account, ticker, share_amount, current_price)
                except ValueError:
                    view.insufficient_funds()
            else:
                view.improper_ticker()
                time.sleep(3)

        # elif selection == '5':
        #   Account.get_positions(account)
        #   # time.sleep(3)
        #   ticker_to_sell = view.sell_shares()
        #   has_stock = get_price(ticker_to_sell)
        #   print(has_stock)
        #   amount = view.sell_shares_amount()
        #   current_price = get_price(ticker_to_sell)
        #   if has_stock:
        #       Account.sell(account, ticker_to_sell, amount, current_price)
        #   else:
        #       view.improper_ticker()
        #       time.sleep(3)

        elif selection == '5':
            Account.get_positions(account)
            ticker = view.request_ticker_symbol()
            shares = int(view.sell_shares())

            try:
                Account.sell(account, ticker, shares)
            except ValueError:
                view.wups()
                time.sleep(3)
            # view.clearscreen()

        elif selection == '6':
            selection = view.select_trade_option(account.username)

            if len(selection) != 1 or selection.lower() not in ['a', 'b', 'c']:
                view.improper_selection()
                time.sleep(3)
            elif selection.lower() == 'a':
                account_trades = Account.get_trades(account)
                for trade in account_trades:
                    view.show_trades(account.username, trade)
                    time.sleep(1)
            elif selection.lower() == 'b':
                ticker_symbol = view.request_ticker_symbol()
                account_trades_by_ticker = Account.trades_for(account, ticker_symbol)

                if account_trades_by_ticker:
                    for trade in account_trades_by_ticker:
                        view.show_trades(account.username, trade)
                        time.sleep(3)

                else:
                    view.improper_ticker()
                    time.sleep(3)
            elif selection.lower() == 'c':
                continue
        elif selection == '7':
            view.goodbye()
            welcome_homepage()
            return
        elif selection == '8':
            view.goodbye()
            return
        elif selection == '9':
            top_traded('https://api.iextrading.com/1.0/stock/market/batch?symbols=aapl,fb&types=quote,news,chart&range=1m&last=5')
            time.sleep(3)

"""TODO
    develop the view for the login screen and the controller option for it
    see the below for inspiration"""

"""
Sample execution

Welcome to Terminal Trader!

    1. create account
    2. login
    3. quit

Your choice: 2

Main Menu:

    1. see balance & positions
    2. deposit money
    3. look up stock price
    4. buy stock
    5. sell stock
    6. trade history

etc.

you should have useful output if a user inputs a stock that does not exist

you should not allow a user to spend money they don't have or sell shares they don't have

your display of positions or trades should be well-formatted, don't
just print a python list
"""





