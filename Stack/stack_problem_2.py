"""
Craig Wright
CSE 212
Spring 2021

Its 2458 and inflation is at ridiculous levels never seen before in the history of the Milky Way galaxy. You have an
annual salary of $27,200,843.04 which is now average for the middle class. You get paid $1,133,368.46 bi-monthly plus
any bonuses or overtime you earned during that period.

You have kept track of your paychecks for the first 5 months of the year by adding them to an array. (It doesn't make
the most sense, but intergalactic law now requires this strange format.) The problem is that January's statements are at
the front of the array. To make things more confusing and annoying, federal law in 2458 prohibits the reading of arrays
from the beginning for some bureaucratic reason that we don't pretend to understand.

To keep in line with the laws and avoid space jail, create a program that will use stack memory and functions to reverse
your statements so that they can be printed out in chronological order (reverse of what they are now).
"""


def reorder_statements(list_to_reorder):
    # TODO: add your code here
    pass


def print_statement(list_to_display):
    for counter in range(len(list_to_display)):
        item = None  # TODO: Replace 'None" with your code

        # Formats the string with the data from the tuple.
        print(f"Your {item[0]} statement records ${item[1]} in earnings.")


# Tuple -->(Month and statement number, earned amount).
statements = [('Jan1', 1133599.99), ('Jan2', 1137896.01), ('Feb1', 1200000.02), ('Feb2', 1133369.03),
              ('Mar2', 1133400.04), ('Apr1', 1133389.05), ('Apr2', 1730336.06), ('May1', 1135368.07),
              ('May2', 1144432.08)]

# Reorder the statements.
new_statements = reorder_statements(statements)

# Display the statements.
print_statement(new_statements)

# Verify output:
# Your Jan1 statement records $1133599.99 in earnings.
# Your Jan2 statement records $1137896.01 in earnings.
# Your Feb1 statement records $1200000.02 in earnings.
# Your Feb2 statement records $1133369.03 in earnings.
# Your Mar2 statement records $1133400.04 in earnings.
# Your Apr1 statement records $1133389.05 in earnings.
# Your Apr2 statement records $1730336.06 in earnings.
# Your May1 statement records $1135368.07 in earnings.
# Your May2 statement records $1144432.08 in earnings.
