class Record:

    def __init__(self, name, price, item_type):
        self.name = name
        self.price = price
        self.item_type = item_type


def total_cost_with_tax(state, records):
    ma_tax = 1.0625
    me_tax = 1.055
    cost = 0.00

    for i in records:
        if state.lower() == '':
            print("Cannot be empty.")
            raise SyntaxError
        elif state.lower() == 'ma' or state.lower() == 'me' or state.lower() == 'nh':
            if i.price > 0:
                if i.item_type.lower() == "wic eligible food":
                    cost += i.price
                elif i.item_type.lower() == "everything else":
                    if state.lower() == 'ma':
                        cost += (i.price * ma_tax)
                    elif state.lower() == 'me':
                        cost += (i.price * me_tax)
                    elif state.lower() == 'nh':
                        cost += i.price
                elif i.item_type.lower() == "clothing":
                    if state.lower() == 'ma':
                        if i.price > 175:
                            taxed = i.price - 175
                            untaxed = i.price - taxed
                            cost += (taxed * ma_tax) + untaxed
                        else:
                            cost += i.price
                    elif state.lower() == 'me':
                        cost += (i.price * me_tax)
                    elif state.lower() == 'nh':
                        cost += i.price
                elif i.item_type.lower() == '':
                    print("Cannot be empty.")
                    raise SyntaxError
                else:
                    print("invalid type, so no cost was returned. State must be 'Clothing', 'Wic Eligible Food', "
                          "or 'everything else'.")
                    raise ValueError
            elif i.price < 0:
                print("Price cannot be negative.")
                raise ValueError
            else:
                print("Price must be entered with numbers or decimals (i.e. '10' or '1.99')")
                raise TypeError
        else:
            print("invalid state, so no cost was returned. State must be 'MA', 'ME', or 'NH'.")
            raise ValueError
    print("\nTotal cost:")
    cost = round(cost, 2)
    print(cost)
    return cost
