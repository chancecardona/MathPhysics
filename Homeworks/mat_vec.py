# ASSIGNMENT NAME: HW02 Part 2
# NAME: Chance Cardona
# EMAIL: ccardona@mines.edu
# DATE: 9/3/2018
# DESCRIPTION: Matrix Times a Vector.
# Given a matrix and a vector, returns the product of these (a vector) Ax = b
# GRADING NOTES:
# OTHER NOTES: Uses lists, not numpy. Use Matrix of form 
#   [[2,1,2],[3,3,2],[1,1,2]].
#   and vector just a list of numbers. It checks for proper input, 
#   and should guide you for the most part.

# does the dot product given 2 vectors.
def dotproduct(a, b):
    sum = 0
    for i in range(len(a)):
        sum += a[i]*b[i] 
    return sum

# Actual math part. Done this way so I could always use in the future
# if I needed to import this function without printing.
def mxv(matrix, vector):
    # does the dot product for each row in the matrix with the vector
    arr = []
    for i in range(len(matrix)):
        arr.append(dotproduct(matrix[i], vector))
    return arr

def printVec(v):
    outprint = "["
    for i in range(len(v)):
        outprint += str(v[i]) + "\n"
    outprint = outprint[:-1] + "]" 
    print(outprint)

#mostly just input sanitizing. Also prints according to format.
def mat_vec(matrix, vector):
    try:
        # len(matrix) is the # of rows
        # len(matrix[0]) is the # of columns
        # Access with matrix[row][col]
        if len(matrix[0]) == len(vector):
            # does the dot product for each row in the matrix with the vector
            printVec(mxv(matrix, vector))
        else:
            print("Dimensions do not line up. Use an mxn matrix and and nx1 vector.")
    except:
        print("Error. Improper matrix or vector entered. Use [[1,2],[3,4]] style matrices.")
    return

if __name__ == '__main__':
    A = [[2,1,2],[3,3,2],[1,1,2]]
    B = [2,3,2]
    mat_vec(A, B)

    # code making sure the try excepts work properly.
    # x = [1,2,3,4]
    # b = ["a", "b", 7]
    # mat_vec(A, x)
    # mat_vec(x, b)
