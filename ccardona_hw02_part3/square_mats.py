# ASSIGNMENT NAME: HW02 Part 2
# NAME: Chance Cardona
# EMAIL: ccardona@mines.edu
# DATE: 9/3/2018
# DESCRIPTION: Square Matrices
# Given 2 NxN matrices, returns their product.
# GRADING NOTES:
# OTHER NOTES: Uses lists, not numpy. Use Matrix of form 
#   [[2,1,2],[3,3,2],[1,1,2]].
#   and vector just a list of numbers. It checks for proper input, 
#   and should guide you for the most part.

##############################################################################

##############################################################################
from mat_mat import printMatrix, mxm

def square_mats(A, B):
    try:
        # len(matrix) is the # of rows
        # len(matrix[0]) is the # of columns
        # Access with matrix[row][col]

        # checks that A and B are square matrices, then just calls the 
        # general matrix multiplication algorithm. Otherwise says to 
        # use the general.
        if len(A[0]) == len(B[0]) and len(A) == len(B) and len(A) == len(A[0]):
            printMatrix(mxm(A, B))
        else:
            print("Dimensions do not line up. Use 2 mxm matrices. Or try mat_mat function.")
    except:
        print("Error. Improper matrix's entered. Use [[1,2],[3,4]] style matrices.")
    return

if __name__ == '__main__':
    A = [[2,4,1],[1,3,2],[6,1,3]]
    B = [[5,3,1],[2,2,2],[1,3,1]]
    square_mats(A, B)