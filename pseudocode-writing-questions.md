# Pseudocode-writing questions

Solve on paper first. IDs W001–W020 are easy, W021–W040 medium, W041–W060 hard. Use the README contract. For each: specify the input domain, write an algorithm, dry-run the supplied sample, state time/space complexity and test one boundary. These are original exercises.

## W001 — Swap two values

Write pseudocode to swap two integers using a temporary variable. Demonstrate a=4,b=9.

## W002 — Rotate three values

Rotate (a,b,c) to (c,a,b). Demonstrate (1,2,3).

## W003 — Quotient and remainder

For integer a and nonzero integer b, print truncation-toward-zero quotient and remainder. Demonstrate a=-17,b=5.

## W004 — Even or odd

Classify any integer n as even or odd. Demonstrate n=-7.

## W005 — Largest of three

Find the largest of three integers including ties. Demonstrate (7,7,2).

## W006 — Grade bands

Given a valid integer mark 0..100, print A for >=80, B for >=60, C for >=40, F otherwise. Demonstrate 60.

## W007 — Leap year

Implement Gregorian leap-year rules for a positive integer year: divisible by 400, or by 4 but not 100. Demonstrate 1900.

## W008 — Sum from one to n

Using a loop, sum 1 through nonnegative n. Demonstrate n=5.

## W009 — Odd-number sum

Sum the positive odd numbers at most nonnegative n with a step of two. Demonstrate n=8.

## W010 — Countdown

Print integers from nonnegative n down to zero, one per line. Demonstrate n=3.

## W011 — Multiplication table

Print k*n for k=1..5, one per line. Demonstrate n=3.

## W012 — Count decimal digits

Count digits of a nonnegative integer, treating zero as one digit. Demonstrate n=1002.

## W013 — Digit sum

Find sum of decimal digits of nonnegative n. Demonstrate n=405.

## W014 — Reverse an integer

Reverse decimal digits numerically for nonnegative n. Demonstrate n=120.

## W015 — Numeric palindrome

Determine whether nonnegative n reads the same forwards and backwards. Demonstrate n=1221.

## W016 — Iterative factorial

Compute n! for integer n>=0 without recursion. Demonstrate n=5.

## W017 — Fibonacci term

Compute F_n for n>=0, F0=0,F1=1, using constant auxiliary space. Demonstrate n=7.

## W018 — Euclidean GCD

Compute GCD of two nonnegative integers, defining GCD(0,0)=0. Demonstrate (48,18).

## W019 — Array sum

Sum a possibly empty integer array. Demonstrate [3,-2,7].

## W020 — Linear search

Return the first index of target or -1 if absent in any integer array. Demonstrate A=[4,9,4],target=4.

## W021 — Maximum array value

Return the largest value of a nonempty integer array. Demonstrate [-8,-2,-5].

## W022 — Second distinct largest

Find the second distinct largest value, or print NONE if fewer than two distinct values exist. Use sorting for clarity; demonstrate [5,5,2,8,8].

## W023 — Reverse array in place

Reverse any array using two indices and O(1) extra space. Demonstrate [1,2,3,4,5].

## W024 — Count occurrences

Count exact occurrences of target in a possibly empty array. Demonstrate [2,3,2,2],target=2.

## W025 — Vowel count

Count ASCII vowels in a string ignoring case. Demonstrate "Zeus AI". LOWER returns a lowercase copy; IS_IN tests membership.

## W026 — String reversal

Build reversed ASCII text without a reverse builtin. Demonstrate "code".

## W027 — String palindrome

Check exact, case-sensitive palindrome with two pointers. Demonstrate "abca".

## W028 — Trial-division prime

Test primality for integer n>=0 using divisors up to sqrt(n). Demonstrate n=29.

## W029 — Prime count in a range

Count primes in inclusive [2,n], n>=0. Demonstrate n=10.

## W030 — Armstrong test

For nonnegative n, test whether n equals the sum of each digit raised to the number of digits. Demonstrate 153; POWER is integer exponentiation.

## W031 — Least common multiple

Compute LCM of nonnegative a,b using GCD, with LCM=0 if either input is 0. Demonstrate (12,18).

## W032 — Count triangular visits

Count pairs (i,j) with 1<=j<=i<=n using nested loops. Demonstrate n=4.

## W033 — Rows of stars

Print a left-aligned triangle of n rows, row i containing i stars. Demonstrate n=3.

## W034 — Matrix sum

Sum a rectangular integer matrix with at least one row; rows may have zero columns. Demonstrate [[1,2,3],[4,5,6]].

## W035 — Main diagonal sum

Sum the main diagonal of a square matrix. Demonstrate [[1,2],[3,4]].

## W036 — Transpose a rectangle

Build a new transpose of a rectangular matrix with >=1 row and >=1 column. Demonstrate [[1,2,3],[4,5,6]].

## W037 — Bubble sort

Sort an integer array ascending in place using adjacent swaps. Demonstrate [3,1,2].

## W038 — Selection sort

Sort ascending in place by selecting the smallest remaining value. Demonstrate [4,2,3,1].

## W039 — Binary search

Search an ascending integer array for target; return any matching index or -1. Demonstrate [2,5,8,11],target=11.

## W040 — Recursive factorial

Write a recursive factorial for n>=0 with a correct base case. Demonstrate n=4.

## W041 — Recursive digit sum

Compute digit sum recursively for nonnegative n. Demonstrate 204.

## W042 — Recursive GCD

Write recursive Euclid for nonnegative a,b. Demonstrate (81,27).

## W043 — Recursive palindrome

Check an ASCII string using recursive inward-moving indices. Demonstrate "radar".

## W044 — Fast exponentiation

Compute base^exp for integer base and exp>=0 using repeated squaring. Define 0^0=1 in this exercise. Demonstrate 3^5.

## W045 — Set-bit count

Count 1 bits of a nonnegative integer using x AND (x-1). Demonstrate x=13.

## W046 — Power of two

Test whether nonnegative x is a positive power of two using a bitwise condition. Demonstrate x=16.

## W047 — Unique unpaired element

Every integer in the array occurs twice except one that occurs once. Find the unique value using XOR. Inputs are nonnegative; demonstrate [4,1,4,7,1].

## W048 — Toggle a selected bit

Toggle bit k (zero=least significant) of nonnegative x using XOR; k>=0. Demonstrate x=10,k=1.

## W049 — Prefix sums

Build prefix array P of length n+1 with P[0]=0 and P[i+1]=sum A[0..i]. Demonstrate [2,-1,4].

## W050 — Fixed-window maximum sum

For array A and valid 1<=k<=LENGTH(A), find maximum sum of any contiguous k-element window. Demonstrate [2,-1,3,4],k=2.

## W051 — Remove sorted duplicates

Return a new array containing one copy of each value of sorted input. Demonstrate [1,1,2,2,3].

## W052 — Merge sorted arrays

Merge two ascending arrays into one ascending array, retaining duplicates. Demonstrate [1,4] and [2,3,4].

## W053 — Pair sum in sorted array

Given ascending array and target, determine if two distinct positions sum to target using two pointers. Demonstrate [1,2,4,7],target=9.

## W054 — Insertion sort

Sort ascending in place with a shifting insertion sort. Demonstrate [3,1,2].

## W055 — Balanced parentheses

For text containing only ( and ), determine if parentheses are balanced using a counter. Demonstrate "(()())".

## W056 — Maximum subarray sum

For nonempty integer array, find maximum sum of a nonempty contiguous subarray. Demonstrate [-2,3,-1,4,-5].

## W057 — Recursive Fibonacci calls

Return F_n recursively for n>=0; then explain why this version is slower than iteration. Demonstrate n=5.

## W058 — Unique diagonal sum

For a square matrix sum both diagonals counting any shared center once. Demonstrate [[1,2,3],[4,5,6],[7,8,9]].

## W059 — First occurrence by binary search

Return the leftmost index of target in a sorted array, or -1. Demonstrate [1,2,2,2,4],target=2.

## W060 — Recursive subset-sum decision

Given nonnegative array A and nonnegative target, decide if some subset sums to target. Empty subset allowed. Demonstrate [3,5,7],target=10.
