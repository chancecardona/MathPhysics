from PHGN311TestLib import ASSERT_EQUALS_IrI, ASSERT_EQUALS_IrS, ASSERT_EQUALS_SrI, ASSERT_EQUALS_SrS
import argparse
from part1 import factorial, sum_nums
from part2 import time_conversion, count_vowels
from part3 import palindrome, is_power_of_two

parser = argparse.ArgumentParser(description="Run test cases for HW01. Run specific parts or all parts")
parser.add_argument("-p", "--part", type=int, choices=[0,1,2,3], nargs='+', default=[0],
                    help="run test cases for specific part of HW. Choose 0 or ignore parameter to run all parts")
part = parser.parse_args().part

#*****************************************************************************
# BEGIN test cases --- DO NOT EDIT -- EDITING WILL RESULT IN A ZERO SCORE
#*****************************************************************************
if __name__ == '__main__':
    print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")
    print("\n\033[1;32m*** START TEST CASES ***\033[0m")
    print("\033[1;32m___________________________________________________________________________________________________\033[0m")

    if 0 in part or 1 in part:
        # -- Problem 1 --
        print("\n\033[1;32m[TESTING] Problem 1: factorial\033[0m\n")
        if  ASSERT_EQUALS_IrI(0, 1, factorial)!=-1:
            ASSERT_EQUALS_IrI(1, 1, factorial)
            ASSERT_EQUALS_IrI(5, 120, factorial)
            ASSERT_EQUALS_IrI(10, 3628800, factorial)
            ASSERT_EQUALS_IrI(15, 1307674368000, factorial)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")

        # -- Problem 2 --
        print("\n\033[1;32m[TESTING] Problem 2: sum_nums\033[0m\n")
        if ASSERT_EQUALS_IrI(0, 0, sum_nums)!=-1:
           ASSERT_EQUALS_IrI(1, 1, sum_nums)
           ASSERT_EQUALS_IrI(2, 3, sum_nums)
           ASSERT_EQUALS_IrI(100, 5050, sum_nums)
           ASSERT_EQUALS_IrI(8202018, 33636553737171, sum_nums)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")

    if 0 in part or 2 in part:
        # -- Problem 3 --
        print("\n\033[1;32m[TESTING] Problem 3: time_conversion\033[0m\n")
        if ASSERT_EQUALS_IrS(0, "00:00:00", time_conversion)!=-1:
           ASSERT_EQUALS_IrS(60, "00:01:00", time_conversion)
           ASSERT_EQUALS_IrS(999, "00:16:39", time_conversion)
           ASSERT_EQUALS_IrS(3600, "01:00:00", time_conversion)
           ASSERT_EQUALS_IrS(3670, "01:01:10", time_conversion)
           ASSERT_EQUALS_IrS(87127, "24:12:07", time_conversion)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")

        # -- Problem 4 --
        print("\n\033[1;32m[TESTING] Problem 4: count_vowels\033[0m\n")
        if ASSERT_EQUALS_SrI("hello", 2, count_vowels)!=-1:
           ASSERT_EQUALS_SrI("sequoia", 5, count_vowels)
           ASSERT_EQUALS_SrI("hmmm", 0, count_vowels)
           ASSERT_EQUALS_SrI("oooooooooooooooooooo", 20, count_vowels)
           ASSERT_EQUALS_SrI("this one has spaces wow", 7, count_vowels)
           ASSERT_EQUALS_SrI("oth3r r@ndom $()(}))", 2, count_vowels)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")

    if 0 in part or 3 in part:
        # -- Problem 5 --
        print("\n\033[1;32m[TESTING] Problem 5: palindrome\033[0m\n")
        if ASSERT_EQUALS_SrS("tacocat", True, palindrome)!=-1:
           ASSERT_EQUALS_SrS("hello", False, palindrome)
           ASSERT_EQUALS_SrS("racecar", True, palindrome)
           ASSERT_EQUALS_SrS("a dog a panic in a pagoda", True, palindrome)
           ASSERT_EQUALS_SrS("hey now you're an all star", False, palindrome)
           ASSERT_EQUALS_SrS("a", True, palindrome)
           ASSERT_EQUALS_SrS("abba", True, palindrome)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")

        # -- Problem 6 --
        print("\n\033[1;32m[TESTING] Problem 6: is_power_of_two\033[0m\n")
        if ASSERT_EQUALS_IrS(1, True, is_power_of_two)!=-1:
           ASSERT_EQUALS_IrS(20, False, is_power_of_two)
           ASSERT_EQUALS_IrS(1024, True, is_power_of_two)
           ASSERT_EQUALS_IrS(4096, True, is_power_of_two)
           ASSERT_EQUALS_IrS(-42, False, is_power_of_two)
           ASSERT_EQUALS_IrS(0, False, is_power_of_two)
        print("\n\033[1;32m___________________________________________________________________________________________________\033[0m")
        print("\033[1;32m___________________________________________________________________________________________________\033[0m")
        print("\n\033[1;32m*** END TEST CASES ***\033[0m")
        print("\033[1;32m___________________________________________________________________________________________________\033[0m\n\n")
#*****************************************************************************
# END test cases
#*****************************************************************************
