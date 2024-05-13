# def money_made(num_shares, purchase_share_price, current_share_price):
"""
num_shares is the number of shares of a stock that we purchased.
purchase_share_price is the price of each of those shares.
current_share_price is the current share price.
Return the amount of money we have earned on the stock.
"""
def money_made(num_shares, purchase_share_price, current_share_price):
    """
    Calculate the profit or loss from buying and then selling stock.

    Parameters:
    num_shares (int): The number of shares of a stock that were purchased.
    purchase_share_price (float): The price per share at the time of purchase.
    current_share_price (float): The current price per share.

    Returns:
    float: The total profit or loss.
    """
    # Calculate the profit or loss per share
    profit_per_share = current_share_price - purchase_share_price
    
    # Calculate total profit or loss
    total_profit = profit_per_share * num_shares
    
    return total_profit

profit = money_made(1888, 34.17, 52.12)
print(profit)
