from time import sleep

widthMax = 43
padding = 50

"""
Function to create Christmas Tree
"""


def christmas_tree(msg, year):
    # to add tree leaves
    for leaf in range(widthMax):
        # print leaf only for ODD numbers
        if leaf % 2 != 0:
            # "X" = represent leaf, String formatting for center align in total width
            print(f'{"X" * leaf:^{widthMax + padding}}')

    # stem of the tree
    for stem in range(2):
        if stem % 2 != 0:
            print(f'{"X" * (stem * 2):^{widthMax + padding}}')
        if stem % 2 != 0:
            print(f'{"X" * (stem * 2):^{widthMax + padding}}')
            print(f'{msg.upper():^{widthMax + padding}}')
            print(f'{year:^{widthMax + padding}}')

    print('')
    print('')
    print('')


"""
main starts here
"""

if __name__ == "__main__":
    for i in range(5):
        christmas_tree("Merry Christmas", "2020")
        sleep(1)
