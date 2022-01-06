genesis_block = {
    'previos_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        : sender: The sender of the coins.
        : recipient: THe recipient of the coins.
        : amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = '-'.join(([str(last_block[key]) for key in last_block]))
    print(hashed_block)

    block = {
        'previos_hash': 'XYZ',
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of users."""
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount) # можно без скобок если больше 1 переменной

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_element():
    for block in blockchain:
        print('Outputting Block')
        print(block)


def verify_chain():
    # block_index = 1
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    # for block in blockchain:
    #     if block == blockchain[0]:
    #         continue
    #     if block[0] == blockchain[block_index -1]:
    #         pass
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


while True:
    print('Please choose:')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Маnipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_element()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list')
    # if not verify_chain():
    #     print('Invalid blockchain!')
    #     break


print('Done!')
