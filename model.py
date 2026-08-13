"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
def expected_value(values, probabilities):
    # return the expected value of the discrete distribution (values, probabilities).
    return float(np.dot(values, probabilities))

# Step 2 - one_reroll_die_value
def one_reroll_die_value(sides):
    # return {'value': expected winnings under optimal reroll policy, 'reroll_faces': sorted faces to reroll}

    faces = list(range(1, sides + 1))
    uniform_prob = [1/sides] * sides

    # expected value of the uniform distribution
    # clsoed form solution: reroll_value = (sides + 1) / 2
    reroll_value = expected_value(faces, uniform_prob) 
    
    reroll_faces = []
    optimal_winnings = []

    for face in faces:
        if reroll_value > face:
            reroll_faces.append(face)
            optimal_winnings.append(reroll_value)
        else:
            optimal_winnings.append(face)


    return {
        "value" : expected_value(optimal_winnings, uniform_prob),
        "reroll_faces" : reroll_faces
    }

# Step 3 - pay_per_reroll_die_game
import numpy as np

def pay_per_reroll_die_game(sides, reroll_cost):
    # return {'threshold': t, 'value': V} for the pay-per-reroll die game under the optimal threshold policy.

    treshes = list(range(sides+1))

    v = []
    for t in treshes:
        v.append( (t + sides) / 2 - ( (t - 1) / (sides - t +1) * reroll_cost) )

    t = np.argmax(v)

    return {'threshold': t, 'value': max(v)}

# Step 4 - red_black_card_game_value
from functools import lru_cache

def red_black_card_game_value(num_red, num_black):
    # return {'value': expected payout under optimal stopping, 'stop_now': whether to stop immediately}.

    @lru_cache(maxsize=None)
    def V(r, b):

        if r == 0 and b == 0:
            return 0.0

        if r == 0:
            return 0.0

        if b == 0:
            return float(r)

        # Value of continuing
        cont = (
            r / (r + b) * (1 + V(r - 1, b))
            + b / (r + b) * (-1 + V(r, b - 1))
        )

        return max(0.0, cont)

    # initial state
    r = num_red
    b = num_black

    if r == 0 and b == 0:
        cont = 0.0

    elif r == 0:
        cont = -1.0

    elif b == 0:
        cont = r

    else:
        cont = (
            r / (r + b) * (1 + V(r - 1, b))
            + b / (r + b) * (-1 + V(r, b - 1))
        )

    value = max(0.0, cont)
    stop_now = (cont <= 0.0)

    return {
        'value': value,
        'stop_now': stop_now
    }

# Step 5 - make_quotes (not yet solved)
# TODO: implement

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

