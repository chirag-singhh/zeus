# Error-detection questions

There are 75 original programs. Each violates its stated task on some valid input. Locate the fault, classify it (syntax, type, logic, runtime, boundary or termination), explain a failing execution, write complete corrected code, and test a boundary. A sample can mask a fault: check the whole input contract. Use the README neutral conventions; all code in this file is Pseudocode.

## E001 — Swap two values — program review

**Required behavior:** Write pseudocode to swap two integers using a temporary variable. Demonstrate a=4,b=9.

```text
Pseudocode — faulty
a ← 4
b ← 9
temp ← b
a ← b
b ← temp
PRINT a, b
```

Identify and repair the fault. Give a failing input and a verification example.

## E002 — Rotate three values — program review

**Required behavior:** Rotate (a,b,c) to (c,a,b). Demonstrate (1,2,3).

```text
Pseudocode — faulty
a ← 1
b ← 2
c ← 3
temp ← c
c ← a
b ← a
a ← temp
PRINT a, b, c
```

Identify and repair the fault. Give a failing input and a verification example.

## E003 — Quotient and remainder — program review

**Required behavior:** For integer a and nonzero integer b, print truncation-toward-zero quotient and remainder. Demonstrate a=-17,b=5.

```text
Pseudocode — faulty
a ← (−17)
b ← 5
q ← DIVIDE_TRUNC(a, b)
r ← (a + (q * b))
PRINT q, r
```

Identify and repair the fault. Give a failing input and a verification example.

## E004 — Even or odd — program review

**Required behavior:** Classify any integer n as even or odd. Demonstrate n=-7.

```text
Pseudocode — faulty
n ← (−7)
IF (REMAINDER_TRUNC(n, 2) ≠ 0) THEN
    PRINT "even"
ELSE
    PRINT "odd"
END IF
```

Identify and repair the fault. Give a failing input and a verification example.

## E005 — Largest of three — program review

**Required behavior:** Find the largest of three integers including ties. Demonstrate (7,7,2).

```text
Pseudocode — faulty
a ← 7
b ← 7
c ← 2
best ← 0
IF (b > best) THEN
    best ← b
END IF
IF (c > best) THEN
    best ← c
END IF
PRINT best
```

Identify and repair the fault. Give a failing input and a verification example.

## E006 — Grade bands — program review

**Required behavior:** Given a valid integer mark 0..100, print A for >=80, B for >=60, C for >=40, F otherwise. Demonstrate 60.

```text
Pseudocode — faulty
mark ← 60
IF (mark ≥ 80) THEN
    PRINT "A"
ELSE
    IF (mark > 60) THEN
        PRINT "B"
    ELSE
        IF (mark ≥ 40) THEN
            PRINT "C"
        ELSE
            PRINT "F"
        END IF
    END IF
END IF
```

Identify and repair the fault. Give a failing input and a verification example.

## E007 — Leap year — program review

**Required behavior:** Implement Gregorian leap-year rules for a positive integer year: divisible by 400, or by 4 but not 100. Demonstrate 1900.

```text
Pseudocode — faulty
year ← 1900
leap ← (((year MOD 400) = 0) AND (((year MOD 4) = 0) AND ((year MOD 100) ≠ 0)))
PRINT leap
```

Identify and repair the fault. Give a failing input and a verification example.

## E008 — Sum from one to n — program review

**Required behavior:** Using a loop, sum 1 through nonnegative n. Demonstrate n=5.

```text
Pseudocode — faulty
n ← 5
s ← 0
FOR i ← 1 TO (n − 1) STEP 1
    s ← (s + i)
END FOR
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E009 — Odd-number sum — program review

**Required behavior:** Sum the positive odd numbers at most nonnegative n with a step of two. Demonstrate n=8.

```text
Pseudocode — faulty
n ← 8
s ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    s ← (s + i)
END FOR
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E010 — Countdown — program review

**Required behavior:** Print integers from nonnegative n down to zero, one per line. Demonstrate n=3.

```text
Pseudocode — faulty
n ← 3
FOR i ← n TO (0 + 1) STEP (−1)
    PRINT i
END FOR
```

Identify and repair the fault. Give a failing input and a verification example.

## E011 — Multiplication table — program review

**Required behavior:** Print k*n for k=1..5, one per line. Demonstrate n=3.

```text
Pseudocode — faulty
n ← 3
FOR k ← 1 TO (6 − 1) STEP 1
    PRINT (k + n)
END FOR
```

Identify and repair the fault. Give a failing input and a verification example.

## E012 — Count decimal digits — program review

**Required behavior:** Count digits of a nonnegative integer, treating zero as one digit. Demonstrate n=1002.

```text
Pseudocode — faulty
n ← 1002
count ← 0
WHILE (n ≥ 10)
    count ← (count + 1)
    n ← (n DIV 10)
END WHILE
PRINT count
```

Identify and repair the fault. Give a failing input and a verification example.

## E013 — Digit sum — program review

**Required behavior:** Find sum of decimal digits of nonnegative n. Demonstrate n=405.

```text
Pseudocode — faulty
n ← 405
s ← 0
WHILE (n > 0)
    s ← (n MOD 10)
    n ← (n DIV 10)
END WHILE
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E014 — Reverse an integer — program review

**Required behavior:** Reverse decimal digits numerically for nonnegative n. Demonstrate n=120.

```text
Pseudocode — faulty
n ← 120
r ← 0
WHILE (n > 0)
    r ← (r + (n MOD 10))
    n ← (n DIV 10)
END WHILE
PRINT r
```

Identify and repair the fault. Give a failing input and a verification example.

## E015 — Numeric palindrome — program review

**Required behavior:** Determine whether nonnegative n reads the same forwards and backwards. Demonstrate n=1221.

```text
Pseudocode — faulty
n ← 1221
original ← n
r ← 0
WHILE (n > 0)
    r ← ((r * 10) + (n MOD 10))
    n ← (n DIV 10)
END WHILE
PRINT (r = n)
```

Identify and repair the fault. Give a failing input and a verification example.

## E016 — Iterative factorial — program review

**Required behavior:** Compute n! for integer n>=0 without recursion. Demonstrate n=5.

```text
Pseudocode — faulty
n ← 5
p ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    p ← (p * i)
END FOR
PRINT p
```

Identify and repair the fault. Give a failing input and a verification example.

## E017 — Fibonacci term — program review

**Required behavior:** Compute F_n for n>=0, F0=0,F1=1, using constant auxiliary space. Demonstrate n=7.

```text
Pseudocode — faulty
n ← 7
a ← 0
b ← 1
FOR i ← 0 TO (n − 1) STEP 1
    nxt ← (a + b)
    a ← b
    b ← (a + b)
END FOR
PRINT a
```

Identify and repair the fault. Give a failing input and a verification example.

## E018 — Euclidean GCD — program review

**Required behavior:** Compute GCD of two nonnegative integers, defining GCD(0,0)=0. Demonstrate (48,18).

```text
Pseudocode — faulty
a ← 48
b ← 18
WHILE (b ≠ 0)
    r ← (a MOD b)
    a ← b
    b ← (a MOD b)
END WHILE
PRINT a
```

Identify and repair the fault. Give a failing input and a verification example.

## E019 — Array sum — program review

**Required behavior:** Sum a possibly empty integer array. Demonstrate [3,-2,7].

```text
Pseudocode — faulty
A ← [3, (−2), 7]
s ← 0
FOR i ← 0 TO ((LENGTH(A) + 1) − 1) STEP 1
    s ← (s + A[i])
END FOR
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E020 — Linear search — program review

**Required behavior:** Return the first index of target or -1 if absent in any integer array. Demonstrate A=[4,9,4],target=4.

```text
Pseudocode — faulty
A ← [4, 9, 4]
target ← 4
found ← (−1)
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] = target) THEN
        found ← i
        // no action
    END IF
END FOR
PRINT found
```

Identify and repair the fault. Give a failing input and a verification example.

## E021 — Maximum array value — program review

**Required behavior:** Return the largest value of a nonempty integer array. Demonstrate [-8,-2,-5].

```text
Pseudocode — faulty
A ← [(−8), (−2), (−5)]
best ← 0
FOR i ← 1 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] > best) THEN
        best ← A[i]
    END IF
END FOR
PRINT best
```

Identify and repair the fault. Give a failing input and a verification example.

## E022 — Second distinct largest — program review

**Required behavior:** Find the second distinct largest value, or print NONE if fewer than two distinct values exist. Use sorting for clarity; demonstrate [5,5,2,8,8].

```text
Pseudocode — faulty
A ← [5, 5, 2, 8, 8]
B ← SORTED(A)
answer ← "NONE"
IF (LENGTH(B) ≥ 2) THEN
    largest ← B[(LENGTH(B) − 1)]
    i ← (LENGTH(B) − 2)
    WHILE (i ≥ 0)
        IF (B[i] = largest) THEN
            answer ← B[i]
            BREAK
        END IF
        i ← (i − 1)
    END WHILE
END IF
PRINT answer
```

Identify and repair the fault. Give a failing input and a verification example.

## E023 — Reverse array in place — program review

**Required behavior:** Reverse any array using two indices and O(1) extra space. Demonstrate [1,2,3,4,5].

```text
Pseudocode — faulty
A ← [1, 2, 3, 4, 5]
l ← 0
r ← (LENGTH(A) − 1)
WHILE (l < r)
    temp ← A[l]
    A[l] ← A[r]
    A[r] ← temp
    l ← (l + 1)
    r ← (r + 1)
END WHILE
PRINT A
```

Identify and repair the fault. Give a failing input and a verification example.

## E024 — Count occurrences — program review

**Required behavior:** Count exact occurrences of target in a possibly empty array. Demonstrate [2,3,2,2],target=2.

```text
Pseudocode — faulty
A ← [2, 3, 2, 2]
target ← 2
count ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] ≠ target) THEN
        count ← (count + 1)
    END IF
END FOR
PRINT count
```

Identify and repair the fault. Give a failing input and a verification example.

## E025 — Vowel count — program review

**Required behavior:** Count ASCII vowels in a string ignoring case. Demonstrate "Zeus AI". LOWER returns a lowercase copy; IS_IN tests membership.

```text
Pseudocode — faulty
s ← "Zeus AI"
s ← s
count ← 0
FOR i ← 0 TO (LENGTH(s) − 1) STEP 1
    IF (s[i] IS_IN "aeiou") THEN
        count ← (count + 1)
    END IF
END FOR
PRINT count
```

Identify and repair the fault. Give a failing input and a verification example.

## E026 — String reversal — program review

**Required behavior:** Build reversed ASCII text without a reverse builtin. Demonstrate "code".

```text
Pseudocode — faulty
s ← "code"
r ← ""
FOR i ← (LENGTH(s) − 1) TO (0 + 1) STEP (−1)
    r ← (r + s[i])
END FOR
PRINT r
```

Identify and repair the fault. Give a failing input and a verification example.

## E027 — String palindrome — program review

**Required behavior:** Check exact, case-sensitive palindrome with two pointers. Demonstrate "abca".

```text
Pseudocode — faulty
s ← "abca"
l ← 0
r ← (LENGTH(s) − 1)
ok ← TRUE
WHILE (l < r)
    IF (s[l] = s[r]) THEN
        ok ← FALSE
        BREAK
    END IF
    l ← (l + 1)
    r ← (r − 1)
END WHILE
PRINT ok
```

Identify and repair the fault. Give a failing input and a verification example.

## E028 — Trial-division prime — program review

**Required behavior:** Test primality for integer n>=0 using divisors up to sqrt(n). Demonstrate n=29.

```text
Pseudocode — faulty
n ← 29
prime ← (n ≥ 2)
d ← 2
WHILE (prime AND ((d * d) < n))
    IF ((n MOD d) = 0) THEN
        prime ← FALSE
    END IF
    d ← (d + 1)
END WHILE
PRINT prime
```

Identify and repair the fault. Give a failing input and a verification example.

## E029 — Prime count in a range — program review

**Required behavior:** Count primes in inclusive [2,n], n>=0. Demonstrate n=10.

```text
Pseudocode — faulty
n ← 10
count ← 0
FOR x ← 2 TO ((n + 1) − 1) STEP 1
    prime ← FALSE
    d ← 2
    WHILE (prime AND ((d * d) ≤ x))
        IF ((x MOD d) = 0) THEN
            prime ← FALSE
        END IF
        d ← (d + 1)
    END WHILE
    IF prime THEN
        count ← (count + 1)
    END IF
END FOR
PRINT count
```

Identify and repair the fault. Give a failing input and a verification example.

## E030 — Armstrong test — program review

**Required behavior:** For nonnegative n, test whether n equals the sum of each digit raised to the number of digits. Demonstrate 153; POWER is integer exponentiation.

```text
Pseudocode — faulty
n ← 153
original ← n
digits ← 1
t ← n
WHILE (t ≥ 10)
    digits ← (digits + 1)
    t ← (t DIV 10)
END WHILE
s ← 0
WHILE (n > 0)
    digit ← (n MOD 10)
    s ← (s + POWER(digit, 2))
    n ← (n DIV 10)
END WHILE
PRINT (s = original)
```

Identify and repair the fault. Give a failing input and a verification example.

## E031 — Least common multiple — program review

**Required behavior:** Compute LCM of nonnegative a,b using GCD, with LCM=0 if either input is 0. Demonstrate (12,18).

```text
Pseudocode — faulty
a ← 12
b ← 18
x ← a
y ← b
WHILE (y ≠ 0)
    r ← (x MOD y)
    x ← y
    y ← r
END WHILE
IF ((a = 0) AND (b ≠ 0)) THEN
    answer ← 0
ELSE
    answer ← ((a DIV x) * b)
END IF
PRINT answer
```

Identify and repair the fault. Give a failing input and a verification example.

## E032 — Count triangular visits — program review

**Required behavior:** Count pairs (i,j) with 1<=j<=i<=n using nested loops. Demonstrate n=4.

```text
Pseudocode — faulty
n ← 4
count ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    FOR j ← 1 TO ((n + 1) − 1) STEP 1
        count ← (count + 1)
    END FOR
END FOR
PRINT count
```

Identify and repair the fault. Give a failing input and a verification example.

## E033 — Rows of stars — program review

**Required behavior:** Print a left-aligned triangle of n rows, row i containing i stars. Demonstrate n=3.

```text
Pseudocode — faulty
n ← 3
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    row ← "*"
    FOR j ← 0 TO (i − 1) STEP 1
        row ← (row + "*")
    END FOR
    PRINT row
END FOR
```

Identify and repair the fault. Give a failing input and a verification example.

## E034 — Matrix sum — program review

**Required behavior:** Sum a rectangular integer matrix with at least one row; rows may have zero columns. Demonstrate [[1,2,3],[4,5,6]].

```text
Pseudocode — faulty
M ← [[1, 2, 3], [4, 5, 6]]
s ← 0
FOR r ← 0 TO (LENGTH(M) − 1) STEP 1
    FOR c ← 0 TO (LENGTH(M) − 1) STEP 1
        s ← (s + M[r][c])
    END FOR
END FOR
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E035 — Main diagonal sum — program review

**Required behavior:** Sum the main diagonal of a square matrix. Demonstrate [[1,2],[3,4]].

```text
Pseudocode — faulty
M ← [[1, 2], [3, 4]]
s ← 0
FOR i ← 0 TO (LENGTH(M) − 1) STEP 1
    s ← (s + M[i][0])
END FOR
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E036 — Transpose a rectangle — program review

**Required behavior:** Build a new transpose of a rectangular matrix with >=1 row and >=1 column. Demonstrate [[1,2,3],[4,5,6]].

```text
Pseudocode — faulty
M ← [[1, 2, 3], [4, 5, 6]]
T ← []
FOR c ← 0 TO (LENGTH(M[0]) − 1) STEP 1
    row ← []
    FOR r ← 0 TO (LENGTH(M) − 1) STEP 1
        APPEND(row, M[c][r])
    END FOR
    APPEND(T, row)
END FOR
PRINT T
```

Identify and repair the fault. Give a failing input and a verification example.

## E037 — Bubble sort — program review

**Required behavior:** Sort an integer array ascending in place using adjacent swaps. Demonstrate [3,1,2].

```text
Pseudocode — faulty
A ← [3, 1, 2]
FOR end ← (LENGTH(A) − 1) TO (0 + 1) STEP (−1)
    FOR j ← 0 TO ((end + 1) − 1) STEP 1
        IF (A[j] > A[(j + 1)]) THEN
            temp ← A[j]
            A[j] ← A[(j + 1)]
            A[(j + 1)] ← temp
        END IF
    END FOR
END FOR
PRINT A
```

Identify and repair the fault. Give a failing input and a verification example.

## E038 — Selection sort — program review

**Required behavior:** Sort ascending in place by selecting the smallest remaining value. Demonstrate [4,2,3,1].

```text
Pseudocode — faulty
A ← [4, 2, 3, 1]
FOR i ← 0 TO ((LENGTH(A) − 1) − 1) STEP 1
    best ← 0
    FOR j ← (i + 1) TO (LENGTH(A) − 1) STEP 1
        IF (A[j] < A[best]) THEN
            best ← j
        END IF
    END FOR
    temp ← A[i]
    A[i] ← A[best]
    A[best] ← temp
END FOR
PRINT A
```

Identify and repair the fault. Give a failing input and a verification example.

## E039 — Binary search — program review

**Required behavior:** Search an ascending integer array for target; return any matching index or -1. Demonstrate [2,5,8,11],target=11.

```text
Pseudocode — faulty
A ← [2, 5, 8, 11]
target ← 11
lo ← 0
hi ← (LENGTH(A) − 1)
found ← (−1)
WHILE (lo ≤ hi)
    mid ← (lo + ((hi − lo) DIV 2))
    IF (A[mid] = target) THEN
        found ← mid
        BREAK
    END IF
    IF (A[mid] < target) THEN
        lo ← mid
    ELSE
        hi ← (mid − 1)
    END IF
END WHILE
PRINT found
```

Identify and repair the fault. Give a failing input and a verification example.

## E040 — Recursive factorial — program review

**Required behavior:** Write a recursive factorial for n>=0 with a correct base case. Demonstrate n=4.

```text
Pseudocode — faulty
FUNCTION fact(n)
    IF (n ≤ 1) THEN
        RETURN 0
    END IF
    RETURN (n * fact((n − 1)))
END FUNCTION
PRINT fact(4)
```

Identify and repair the fault. Give a failing input and a verification example.

## E041 — Recursive digit sum — program review

**Required behavior:** Compute digit sum recursively for nonnegative n. Demonstrate 204.

```text
Pseudocode — faulty
FUNCTION digits(n)
    IF (n = 0) THEN
        RETURN 1
    END IF
    RETURN ((n MOD 10) + digits((n DIV 10)))
END FUNCTION
PRINT digits(204)
```

Identify and repair the fault. Give a failing input and a verification example.

## E042 — Recursive GCD — program review

**Required behavior:** Write recursive Euclid for nonnegative a,b. Demonstrate (81,27).

```text
Pseudocode — faulty
FUNCTION gcd(a, b)
    IF (a = 0) THEN
        RETURN a
    END IF
    RETURN gcd(b, (a MOD b))
END FUNCTION
PRINT gcd(81, 27)
```

Identify and repair the fault. Give a failing input and a verification example.

## E043 — Recursive palindrome — program review

**Required behavior:** Check an ASCII string using recursive inward-moving indices. Demonstrate "radar".

```text
Pseudocode — faulty
FUNCTION pal(s, l, r)
    IF (l ≥ r) THEN
        RETURN TRUE
    END IF
    IF (s[l] ≠ s[r]) THEN
        RETURN FALSE
    END IF
    RETURN pal(s, (l + 1), (r + 1))
END FUNCTION
s ← "radar"
PRINT pal(s, 0, (LENGTH(s) − 1))
```

Identify and repair the fault. Give a failing input and a verification example.

## E044 — Fast exponentiation — program review

**Required behavior:** Compute base^exp for integer base and exp>=0 using repeated squaring. Define 0^0=1 in this exercise. Demonstrate 3^5.

```text
Pseudocode — faulty
base ← 3
exp ← 5
result ← 1
WHILE (exp > 0)
    IF ((exp MOD 2) = 1) THEN
        result ← (result * base)
    END IF
    base ← (base * base)
    exp ← (exp * 2)
END WHILE
PRINT result
```

Identify and repair the fault. Give a failing input and a verification example.

## E045 — Set-bit count — program review

**Required behavior:** Count 1 bits of a nonnegative integer using x AND (x-1). Demonstrate x=13.

```text
Pseudocode — faulty
x ← 13
count ← 0
WHILE (x > 0)
    x ← (x BIT_OR (x − 1))
    count ← (count + 1)
END WHILE
PRINT count
```

Identify and repair the fault. Give a failing input and a verification example.

## E046 — Power of two — program review

**Required behavior:** Test whether nonnegative x is a positive power of two using a bitwise condition. Demonstrate x=16.

```text
Pseudocode — faulty
x ← 16
answer ← ((x > 1) AND ((x BIT_AND (x − 1)) = 0))
PRINT answer
```

Identify and repair the fault. Give a failing input and a verification example.

## E047 — Unique unpaired element — program review

**Required behavior:** Every integer in the array occurs twice except one that occurs once. Find the unique value using XOR. Inputs are nonnegative; demonstrate [4,1,4,7,1].

```text
Pseudocode — faulty
A ← [4, 1, 4, 7, 1]
answer ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    answer ← (answer BIT_OR A[i])
END FOR
PRINT answer
```

Identify and repair the fault. Give a failing input and a verification example.

## E048 — Toggle a selected bit — program review

**Required behavior:** Toggle bit k (zero=least significant) of nonnegative x using XOR; k>=0. Demonstrate x=10,k=1.

```text
Pseudocode — faulty
x ← 10
k ← 1
mask ← (1 SHL k)
answer ← (x BIT_OR mask)
PRINT answer
```

Identify and repair the fault. Give a failing input and a verification example.

## E049 — Prefix sums — program review

**Required behavior:** Build prefix array P of length n+1 with P[0]=0 and P[i+1]=sum A[0..i]. Demonstrate [2,-1,4].

```text
Pseudocode — faulty
A ← [2, (−1), 4]
P ← [0]
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    APPEND(P, A[i])
END FOR
PRINT P
```

Identify and repair the fault. Give a failing input and a verification example.

## E050 — Fixed-window maximum sum — program review

**Required behavior:** For array A and valid 1<=k<=LENGTH(A), find maximum sum of any contiguous k-element window. Demonstrate [2,-1,3,4],k=2.

```text
Pseudocode — faulty
A ← [2, (−1), 3, 4]
k ← 2
window ← 0
FOR i ← 0 TO (k − 1) STEP 1
    window ← (window + A[i])
END FOR
best ← 0
FOR i ← k TO (LENGTH(A) − 1) STEP 1
    window ← ((window − A[(i − k)]) + A[i])
    IF (window > best) THEN
        best ← window
    END IF
END FOR
PRINT best
```

Identify and repair the fault. Give a failing input and a verification example.

## E051 — Remove sorted duplicates — program review

**Required behavior:** Return a new array containing one copy of each value of sorted input. Demonstrate [1,1,2,2,3].

```text
Pseudocode — faulty
A ← [1, 1, 2, 2, 3]
B ← []
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF ((i = 0) AND (A[i] ≠ A[(i − 1)])) THEN
        APPEND(B, A[i])
    END IF
END FOR
PRINT B
```

Identify and repair the fault. Give a failing input and a verification example.

## E052 — Merge sorted arrays — program review

**Required behavior:** Merge two ascending arrays into one ascending array, retaining duplicates. Demonstrate [1,4] and [2,3,4].

```text
Pseudocode — faulty
A ← [1, 4]
B ← [2, 3, 4]
i ← 0
j ← 0
C ← []
WHILE ((i < LENGTH(A)) AND (j < LENGTH(B)))
    IF (A[i] ≤ B[j]) THEN
        APPEND(C, A[i])
        i ← (i + 1)
    ELSE
        APPEND(C, B[j])
        j ← (j + 1)
    END IF
END WHILE
WHILE (i < LENGTH(A))
    APPEND(C, A[i])
    i ← (i + 1)
END WHILE
WHILE (j < LENGTH(A))
    APPEND(C, B[j])
    j ← (j + 1)
END WHILE
PRINT C
```

Identify and repair the fault. Give a failing input and a verification example.

## E053 — Pair sum in sorted array — program review

**Required behavior:** Given ascending array and target, determine if two distinct positions sum to target using two pointers. Demonstrate [1,2,4,7],target=9.

```text
Pseudocode — faulty
A ← [1, 2, 4, 7]
target ← 9
l ← 0
r ← (LENGTH(A) − 1)
found ← FALSE
WHILE (l < r)
    s ← (A[l] + A[r])
    IF (s = target) THEN
        found ← TRUE
        BREAK
    END IF
    IF (s < target) THEN
        r ← (r − 1)
    ELSE
        r ← (r − 1)
    END IF
END WHILE
PRINT found
```

Identify and repair the fault. Give a failing input and a verification example.

## E054 — Insertion sort — program review

**Required behavior:** Sort ascending in place with a shifting insertion sort. Demonstrate [3,1,2].

```text
Pseudocode — faulty
A ← [3, 1, 2]
FOR i ← 1 TO (LENGTH(A) − 1) STEP 1
    key ← A[i]
    j ← (i − 1)
    WHILE ((j ≥ 0) AND (A[j] > key))
        A[(j + 1)] ← A[j]
        j ← (j − 1)
    END WHILE
    A[j] ← key
END FOR
PRINT A
```

Identify and repair the fault. Give a failing input and a verification example.

## E055 — Balanced parentheses — program review

**Required behavior:** For text containing only ( and ), determine if parentheses are balanced using a counter. Demonstrate "(()())".

```text
Pseudocode — faulty
s ← "(()())"
balance ← 0
ok ← TRUE
FOR i ← 0 TO (LENGTH(s) − 1) STEP 1
    IF (s[i] = "(") THEN
        balance ← (balance + 1)
    ELSE
        balance ← (balance − 1)
    END IF
    IF (balance > LENGTH(s)) THEN
        ok ← FALSE
        BREAK
    END IF
END FOR
PRINT (ok AND (balance = 0))
```

Identify and repair the fault. Give a failing input and a verification example.

## E056 — Maximum subarray sum — program review

**Required behavior:** For nonempty integer array, find maximum sum of a nonempty contiguous subarray. Demonstrate [-2,3,-1,4,-5].

```text
Pseudocode — faulty
A ← [(−2), 3, (−1), 4, (−5)]
ending ← A[0]
best ← 0
FOR i ← 1 TO (LENGTH(A) − 1) STEP 1
    ending ← MAX(A[i], (ending + A[i]))
    best ← MAX(best, ending)
END FOR
PRINT best
```

Identify and repair the fault. Give a failing input and a verification example.

## E057 — Recursive Fibonacci calls — program review

**Required behavior:** Return F_n recursively for n>=0; then explain why this version is slower than iteration. Demonstrate n=5.

```text
Pseudocode — faulty
FUNCTION fib(n)
    IF (n ≤ 1) THEN
        RETURN 1
    END IF
    RETURN (fib((n − 1)) + fib((n − 2)))
END FUNCTION
PRINT fib(5)
```

Identify and repair the fault. Give a failing input and a verification example.

## E058 — Unique diagonal sum — program review

**Required behavior:** For a square matrix sum both diagonals counting any shared center once. Demonstrate [[1,2,3],[4,5,6],[7,8,9]].

```text
Pseudocode — faulty
M ← [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n ← LENGTH(M)
s ← 0
FOR i ← 0 TO (n − 1) STEP 1
    s ← (s + M[i][i])
    IF (i = ((n − 1) − i)) THEN
        s ← (s + M[i][((n − 1) − i)])
    END IF
END FOR
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E059 — First occurrence by binary search — program review

**Required behavior:** Return the leftmost index of target in a sorted array, or -1. Demonstrate [1,2,2,2,4],target=2.

```text
Pseudocode — faulty
A ← [1, 2, 2, 2, 4]
target ← 2
lo ← 0
hi ← (LENGTH(A) − 1)
answer ← (−1)
WHILE (lo ≤ hi)
    mid ← (lo + ((hi − lo) DIV 2))
    IF (A[mid] ≥ target) THEN
        IF (A[mid] = target) THEN
            answer ← mid
        END IF
        lo ← (mid + 1)
    ELSE
        lo ← (mid + 1)
    END IF
END WHILE
PRINT answer
```

Identify and repair the fault. Give a failing input and a verification example.

## E060 — Recursive subset-sum decision — program review

**Required behavior:** Given nonnegative array A and nonnegative target, decide if some subset sums to target. Empty subset allowed. Demonstrate [3,5,7],target=10.

```text
Pseudocode — faulty
FUNCTION possible(A, i, target)
    IF (target < 0) THEN
        RETURN TRUE
    END IF
    IF (i = LENGTH(A)) THEN
        RETURN FALSE
    END IF
    IF ((A[i] ≤ target) AND possible(A, (i + 1), (target − A[i]))) THEN
        RETURN TRUE
    END IF
    RETURN possible(A, (i + 1), target)
END FUNCTION
A ← [3, 5, 7]
PRINT possible(A, 0, 10)
```

Identify and repair the fault. Give a failing input and a verification example.

## E061 — Swap two values — grammar/type review

**Required behavior:** Write pseudocode to swap two integers using a temporary variable. Demonstrate a=4,b=9.

```text
Pseudocode — faulty
a ← 4
b ← 9
temp = a
a ← b
b ← temp
PRINT a, b
```

Identify and repair the fault. Give a failing input and a verification example.

## E062 — Even or odd — grammar/type review

**Required behavior:** Classify any integer n as even or odd. Demonstrate n=-7.

```text
Pseudocode — faulty
n ← (−7)
IF (REMAINDER_TRUNC(n, 2) = 0)
    PRINT "even"
ELSE
    PRINT "odd"
END IF
```

Identify and repair the fault. Give a failing input and a verification example.

## E063 — Largest of three — grammar/type review

**Required behavior:** Find the largest of three integers including ties. Demonstrate (7,7,2).

```text
Pseudocode — faulty
a ← 7
b ← 7
c ← 2
best ← a
IF (b > best) THEN
    best ← b
END FOR
IF (c > best) THEN
    best ← c
END IF
PRINT best
```

Identify and repair the fault. Give a failing input and a verification example.

## E064 — Sum from one to n — grammar/type review

**Required behavior:** Using a loop, sum 1 through nonnegative n. Demonstrate n=5.

```text
Pseudocode — faulty
n ← 5
s ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    s ← (s + i)
END IF
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E065 — Count decimal digits — grammar/type review

**Required behavior:** Count digits of a nonnegative integer, treating zero as one digit. Demonstrate n=1002.

```text
Pseudocode — faulty
n ← 1002
count ← 1
WHILE (n ≥ 10)
    count ← (count + 1)
    n ← (n DIV 10)

PRINT count
```

Identify and repair the fault. Give a failing input and a verification example.

## E066 — Digit sum — grammar/type review

**Required behavior:** Find sum of decimal digits of nonnegative n. Demonstrate n=405.

```text
Pseudocode — faulty
n ← 405
s ← 0
WHILE (n > 0)
    s ← (s + (n MOD 10)
    n ← (n DIV 10)
END WHILE
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E067 — Array sum — grammar/type review

**Required behavior:** Sum a possibly empty integer array. Demonstrate [3,-2,7].

```text
Pseudocode — faulty
A ← [3, (−2), 7
s ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    s ← (s + A[i])
END FOR
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E068 — String reversal — grammar/type review

**Required behavior:** Build reversed ASCII text without a reverse builtin. Demonstrate "code".

```text
Pseudocode — faulty
s ← "code"
r ← "
FOR i ← (LENGTH(s) − 1) TO ((−1) + 1) STEP (−1)
    r ← (r + s[i])
END FOR
PRINT r
```

Identify and repair the fault. Give a failing input and a verification example.

## E069 — Recursive factorial — grammar/type review

**Required behavior:** Write a recursive factorial for n>=0 with a correct base case. Demonstrate n=4.

```text
Pseudocode — faulty
FUNCTION fact(n
    IF (n ≤ 1) THEN
        RETURN 1
    END IF
    RETURN (n * fact((n − 1)))
END FUNCTION
PRINT fact(4)
```

Identify and repair the fault. Give a failing input and a verification example.

## E070 — Recursive digit sum — grammar/type review

**Required behavior:** Compute digit sum recursively for nonnegative n. Demonstrate 204.

```text
Pseudocode — faulty
FUNCTION digits(n)
    IF (n = 0) THEN
        RETUN 0
    END IF
    RETURN ((n MOD 10) + digits((n DIV 10)))
END FUNCTION
PRINT digits(204)
```

Identify and repair the fault. Give a failing input and a verification example.

## E071 — Recursive GCD — grammar/type review

**Required behavior:** Write recursive Euclid for nonnegative a,b. Demonstrate (81,27).

```text
Pseudocode — faulty
FUNCTION gcd(a, b)
    IF (b = 0) THEN
        RETURN a
    END IF
    RETURN gcd(b, (a MOD b))
END WHILE
PRINT gcd(81, 27)
```

Identify and repair the fault. Give a failing input and a verification example.

## E072 — Toggle a selected bit — grammar/type review

**Required behavior:** Toggle bit k (zero=least significant) of nonnegative x using XOR; k>=0. Demonstrate x=10,k=1.

```text
Pseudocode — faulty
x ← 10
k ← 1
mask ← (1 SHIFT k)
answer ← (x BIT_XOR mask)
PRINT answer
```

Identify and repair the fault. Give a failing input and a verification example.

## E073 — Swap two values — grammar/type review

**Required behavior:** Write pseudocode to swap two integers using a temporary variable. Demonstrate a=4,b=9.

```text
Pseudocode — faulty
a ← 4
b ← 9
temp ← a
a ← b
b ← temp
PRINT a b
```

Identify and repair the fault. Give a failing input and a verification example.

## E074 — Array sum — grammar/type review

**Required behavior:** Sum a possibly empty integer array. Demonstrate [3,-2,7].

```text
Pseudocode — faulty
A ← [3, (−2), 7]
s ← "0"
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    s ← (s + A[i])
END FOR
PRINT s
```

Identify and repair the fault. Give a failing input and a verification example.

## E075 — Even or odd — grammar/type review

**Required behavior:** Classify any integer n as even or odd. Demonstrate n=-7.

```text
Pseudocode — faulty
n ← (−7)
IF n THEN
    PRINT "even"
ELSE
    PRINT "odd"
END IF
```

Identify and repair the fault. Give a failing input and a verification example.
