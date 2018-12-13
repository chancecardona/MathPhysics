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

    if 0 in part or 16 in part:
        from problem16 import power_digit_sum
        # -- Problem 1 --
        print("\n\033[1;32m[TESTING] Problem 16: power digit sum\033[0m\n")
        ASSERT_EQUALS_IrI(1000, 1366, power_digit_sum, 30)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")

    if 0 in part or 20 in part:
        from problem20 import factorial_digit_sum
        # -- Problem 1 --
        print("\n\033[1;32m[TESTING] Problem 20: factorial digit sum\033[0m\n")
        ASSERT_EQUALS_IrI(100, 648, factorial_digit_sum, 30)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")

    if 0 in part or 25 in part:
        from problem25 import nth_digit_fibonacci
        # -- Problem 5 --
        print("\n\033[1;32m[TESTING] Problem 25: nth digit fibonacci\033[0m\n")
        ASSERT_EQUALS_IrI(1000, 4782, nth_digit_fibonacci, 120)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")
        print("\033[1;32m___________________________________________________________________________________________________\033[0m")
        print("\n\033[1;32m*** END TEST CASES ***\033[0m")
        print("\033[1;32m___________________________________________________________________________________________________\033[0m\n\n")
#*****************************************************************************
# END test cases
#*****************************************************************************
