from PHGN311TestLib import ASSERT_EQUALS_IrI, ASSERT_EQUALS_IrS, ASSERT_EQUALS_SrI, ASSERT_EQUALS_SrS
import argparse

parser = argparse.ArgumentParser(description="Run test cases for HW02 part 1. Run specific parts or all parts")
parser.add_argument("-p", "--part", type=int, choices=[0,1,3,5], nargs='+', default=[0],
                    help="run test cases for specific Euler problem (1, 3, 5). Choose 0 or ignore parameter to run all parts")
part = parser.parse_args().part

#*****************************************************************************
# BEGIN test cases --- DO NOT EDIT -- EDITING WILL RESULT IN A ZERO SCORE
#*****************************************************************************
if __name__ == '__main__':
    print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")
    print("\n\033[1;32m*** START TEST CASES ***\033[0m")
    print("\033[1;32m___________________________________________________________________________________________________\033[0m")

    if 0 in part or 1 in part:
        from problem1 import multiples_3_5
        # -- Problem 1 --
        print("\n\033[1;32m[TESTING] Problem 1: multiples_3_5\033[0m\n")
        if  ASSERT_EQUALS_IrI(0, 0, multiples_3_5, 30)!=-1:
            ASSERT_EQUALS_IrI(1, 0, multiples_3_5, 30)
            ASSERT_EQUALS_IrI(3, 0, multiples_3_5, 30)
            ASSERT_EQUALS_IrI(5, 3, multiples_3_5, 30)
            ASSERT_EQUALS_IrI(6, 8, multiples_3_5, 30)
            ASSERT_EQUALS_IrI(10, 23, multiples_3_5, 30)
            ASSERT_EQUALS_IrI(100, 2318, multiples_3_5, 30)
            ASSERT_EQUALS_IrI(1000, 233168, multiples_3_5, 30)
            ASSERT_EQUALS_IrI(1234567, 355636612814, multiples_3_5, 30)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")

    if 0 in part or 3 in part:
        from problem3 import largest_prime_factor
        # -- Problem 3 --
        print("\n\033[1;32m[TESTING] Problem 3: largest_prime_factor\033[0m\n")
        if ASSERT_EQUALS_IrI(0, 0, largest_prime_factor, 30)!=-1:
           ASSERT_EQUALS_IrI(1, 1, largest_prime_factor, 30)
           ASSERT_EQUALS_IrI(12, 3, largest_prime_factor, 30)
           ASSERT_EQUALS_IrI(17, 17, largest_prime_factor, 30)
           ASSERT_EQUALS_IrI(100, 5, largest_prime_factor, 30)
           ASSERT_EQUALS_IrI(600851475143, 6857, largest_prime_factor, 120)
           ASSERT_EQUALS_IrI(6008514751431, 3516509, largest_prime_factor, 120)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")


    if 0 in part or 5 in part:
        from problem5 import smallest_multiple
        # -- Problem 5 --
        print("\n\033[1;32m[TESTING] Problem 5: smallest_multiple\033[0m\n")
        if ASSERT_EQUALS_IrI(0, 0, smallest_multiple, 30)!=-1:
           ASSERT_EQUALS_IrI(1, 1, smallest_multiple, 30)
           ASSERT_EQUALS_IrI(3, 6, smallest_multiple, 30)
           ASSERT_EQUALS_IrI(10, 2520, smallest_multiple, 30)
           ASSERT_EQUALS_IrI(17, 12252240, smallest_multiple, 30)
           ASSERT_EQUALS_IrI(20, 232792560, smallest_multiple, 60)
           ASSERT_EQUALS_IrI(22, 232792560, smallest_multiple, 120)
           ASSERT_EQUALS_IrI(23, 5354228880, smallest_multiple, 240)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")
        print("\033[1;32m___________________________________________________________________________________________________\033[0m")
        print("\n\033[1;32m*** END TEST CASES ***\033[0m")
        print("\033[1;32m___________________________________________________________________________________________________\033[0m\n\n")
#*****************************************************************************
# END test cases
#*****************************************************************************
