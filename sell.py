#  Get the last col of underlying
def get_lastcol():
  last_col = []
  i = -52
  while i <= 52:
    last_col.append(1.1**i)
    i += 2
  return last_col


# Get the underlying tree
def get_underlying_tree():
    tree = []
    last_col = get_lastcol()
    tree.append(last_col)
    period = 52
    while period > 0:
        previous_period = []
        for j in range(len(last_col) - 1):
            previous_period.append((1.1 * last_col[j] + last_col[j + 1]/1.1)/2)
        tree.append(previous_period)
        last_col = previous_period
        period -= 1
    return tree

#  Get the last col of underlying
def get_payoff_last():
    payoff_last = []
    l = get_lastcol()
    for i in l:
        payoff_last.append(max(1 - i, 0))
    return payoff_last

# Get the payoff tree
def get_payoff_tree():
    tree = []
    last_col = get_payoff_last()
    tree.append(last_col)
    period = 52
    p = 10/21
    while period > 0:
        previous_period = []
        for j in range(len(last_col) - 1):
            previous_period.append((1-p)*last_col[j] + p*last_col[j+1])
        tree.append(previous_period)
        last_col = previous_period
        period -= 1
    return tree
# Helper function to calculate case 1
def case1_helper(underlying, payoff, K):
    if underlying - K > 0:
        return max(underlying - K, 0) + payoff
    else:
        return -100


# Case1 for 2 Swing
def get_all_case1s():
    undertree = get_underlying_tree()
    payofftree = get_payoff_tree()
    case1tree = []
    for i in range(len(undertree)):
        each = []
        for j in range(len(undertree[i])):
            each.append(case1_helper(undertree[i][j], payofftree[i][j], 1))
        case1tree.append(each)
    return case1tree


# 2 Swing option tree
def get_all_case2():
    case2tree = []
    payofftree = get_payoff_tree()
    last_col = payofftree[0]
    case2tree.append(last_col)
    case1tree = get_all_case1s()
    for i in range(1, len(payofftree)):
        previous = []
        for j in range(len(payofftree[i])):
            case2 = (11/21) * last_col[j]+ (10/21)*last_col[j+1]
            case1 = case1tree[i][j]
            previous.append(max(case1, case2))
        last_col = previous
        case2tree.append(last_col)
    return case2tree


# Get case1 for 3 Swing
def get_case1tree_3th():
    undertree = get_underlying_tree()
    payofftree = get_all_case2()
    case1tree = []
    for i in range(len(undertree)):
        each = []
        for j in range(len(undertree[i])):
            each.append(case1_helper(undertree[i][j], payofftree[i][j], 1))
        case1tree.append(each)
    return case1tree


# Get 3 Swing
def get_3swing_option():
    Swing = []
    Swing_2 = get_all_case2()
    last_col = Swing_2[0]
    Swing.append(last_col)
    last_col = Swing_2[1]
    Swing.append(last_col)
    case1tree = get_case1tree_3th()
    for i in range(2, len(Swing_2)):
        previous = []
        for j in range(len(Swing_2[i])):
            case2 = (11 / 21) * last_col[j] + (10 / 21) * last_col[j + 1]
            case1 = case1tree[i][j]
            previous.append(max(case1, case2))
        last_col = previous
        Swing.append(last_col)
    return Swing


# Get case1 for 4 Swing option
def get_case1_4th():
    undertree = get_underlying_tree()
    payofftree = get_3swing_option()
    case1tree = []
    for i in range(len(undertree)):
        each = []
        for j in range(len(undertree[i])):
            each.append(case1_helper(undertree[i][j], payofftree[i][j], 1))
        case1tree.append(each)
    return case1tree


# Get the 4 Swing option
def get_4Swing_option():
    indicator = []
    Swing = []
    Swing_3 = get_3swing_option()
    last_col = Swing_3[0]
    Swing.append(last_col)
    indicator.append([1]*len(last_col))
    Swing.append(Swing_3[1])
    indicator.append([1] * len(Swing_3[1]))
    Swing.append(Swing_3[2])
    indicator.append([1]*len(Swing_3[2]))
    last_col = Swing_3[2]
    case1tree = get_case1_4th()
    for i in range(3, len(Swing_3)):
        indicator_line = []
        previous = []
        for j in range(len(Swing_3[i])):
            case2 = (11 / 21) * last_col[j] + (10 / 21) * last_col[j + 1]
            case1 = case1tree[i][j]
            # previous.append(max(case1, case2))
            # if previous
            if round(case1, 3) > round(case2, 3):
                previous.append(case1)
                indicator_line.append(1)
            elif case1 == case2:
                previous.append(case2)
                indicator_line.append('indif')
            else:
                previous.append(case2)
                indicator_line.append(0)
        last_col = previous
        Swing.append(last_col)
        indicator.append(indicator_line)
    return Swing, indicator
def check_helper(array):
    for i in range(len(array)):
        print(array[i])
# Helper function to calculate each probability
# def calculate_probability(node1, node2):
#     return (node2)
if __name__ == '__main__':
  # print(get_prices(2))
  # print(get_lastcol())
  # print(get_payoff_last())
  tree = get_payoff_tree()
  check_helper(tree)
  # for i in range(len(tree)):
  #     print(tree[i])
  # undertree = get_underlying_tree()
  # for i in range(len(undertree)):
  #     print(undertree[i])

  # case1tree = get_all_case1s()
  # check_helper(case1tree)
  # payoff = get_payoff_tree()
  # check_helper(payoff)
  # swing2 = get_all_case2()
  # check_helper(swing2)
  # swing3 = get_3swing_option()
  # check_helper(swing3)
  #swing4 = get_4Swing_option()
  #check_helper(swing4[0])
  #check_helper(swing4[1])