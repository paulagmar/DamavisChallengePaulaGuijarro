# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:48:13 2023

@author: PaulaGuijarroMartinez
"""

# =============DEFINE TEST USED====================
# Change this code for new tests
def testLabyrinth(test_number):
    if test_number == 1:
        return [
            [".",".",".",".",".",".",".",".","."],
            ["#",".",".",".","#",".",".",".","."],
            [".",".",".",".","#",".",".",".","."],
            [".","#",".",".",".",".",".","#","."],
            [".","#",".",".",".",".",".","#","."]
        ]
    elif test_number == 2:
        return [
            [".",".",".",".",".",".",".",".","."],
            ["#",".",".",".","#",".",".","#","."],
            [".",".",".",".","#",".",".",".","."],
            [".","#",".",".",".",".",".","#","."],
            [".","#",".",".",".",".",".","#","."]
        ]
    elif test_number == 3:
        return [
            [".",".","."],
            [".",".","."],
            [".",".","."]
        ]
    elif test_number == 4:
        return [
            [".",".",".",".",".",".",".",".",".","."],
            [".","#",".",".",".",".","#",".",".","."],
            [".","#",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".","#",".",".",".",".",".",".",".","."],
            [".","#",".",".",".","#",".",".",".","."],
            [".",".",".",".",".",".","#",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."]
        ]
    else:
        raise ValueError("Invalid test number.")

