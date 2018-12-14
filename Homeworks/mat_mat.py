# ASSIGNMENT NAME: HW02 Part 2
# NAME: Chance Cardona
# EMAIL: ccardona@mines.edu
# DATE: 9/3/2018
# DESCRIPTION: Matrix Matrix Multiplication
# Given an nxm and an mxp matrix returns the nxp matrix product.
# GRADING NOTES:
# OTHER NOTES: Uses lists, not numpy. Use Matrix of form 
#   [[2,1,2],[3,3,2],[1,1,2]].
#   and vector just a list of numbers. It checks for proper input, 
#   and should guide you for the most part.


# WOw much print according to format.
def printMatrix(M):
    outprint = "["
    for i in range(len(M)):
        for j in range(len(M[0])):
            outprint += str(M[i][j]) + " "
        outprint += "\n"
    outprint = outprint[:-2] + "]"
    print(outprint)

def mxm(A, B):
    arr = []
    # Does the Iterative algorithm found on the matrix mult algorithm
    # page on wikipedia. I know I could have just done the mat_vec
    # for each column, but its hard accessing by column the way i did the lists.
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[0])):
                sum += A[i][k]*B[k][j]
            row.append(sum)
        arr.append(row)
    return arr

def mat_mat(A, B):
    try:
        # len(matrix) is the # of rows
        # len(matrix[0]) is the # of columns
        # Access with matrix[row][col]

        # checks that A and B are square matrices
        if len(A[0]) == len(B):
            printMatrix(mxm(A,B))
        else:
            print("Dimensions do not line up. Use nxm and mxp matrices respectively.")
    except:
        print("Error. Improper matrix's entered. Use [[1,2],[3,4]] style matrices.")
    return


if __name__ == '__main__':
    A = [[1,2,3],[4,3,1]]
    B = [[2,3,2,2],[1,4,2,6],[8,1,4,6]]
    mat_mat(A, B)