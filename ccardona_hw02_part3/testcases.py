from PHGN311TestLib import ASSERT_EQUALS_IrI, ASSERT_EQUALS_IrS, ASSERT_EQUALS_SrI, ASSERT_EQUALS_SrS
import argparse

parser = argparse.ArgumentParser(description="Run test cases for HW02 part 2. Run specific parts or all parts")
parser.add_argument("-p", "--part", type=int, choices=[0,7,9], nargs='+', default=[0],
                    help="run test cases for specific Euler problem (7, 9). Choose 0 or ignore parameter to run all parts")
part = parser.parse_args().part

#*****************************************************************************
# BEGIN test cases --- DO NOT EDIT -- EDITING WILL RESULT IN A ZERO SCORE
#*****************************************************************************
if __name__ == '__main__':
    print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")
    print("\n\033[1;32m*** START TEST CASES ***\033[0m")
    print("\033[1;32m___________________________________________________________________________________________________\033[0m")

    if 0 in part or 7 in part:
        from problem7 import nth_prime
        # -- Problem 1 --
        print("\n\033[1;32m[TESTING] Problem 7: nth prime\033[0m\n")
        ASSERT_EQUALS_IrI(10001, 104743, nth_prime, 60)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")


    if 0 in part or 9 in part:
        from problem9 import triplet
        # -- Problem 5 --
        print("\n\033[1;32m[TESTING] Problem 9: \033[0m\n")
        ASSERT_EQUALS_IrI(1000, 31875000, triplet, 30)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")
        print("\033[1;32m___________________________________________________________________________________________________\033[0m")
        print("\n\033[1;32m*** END TEST CASES ***\033[0m")
        print("\033[1;32m___________________________________________________________________________________________________\033[0m\n\n")
#*****************************************************************************
# END test cases
#*****************************************************************************
