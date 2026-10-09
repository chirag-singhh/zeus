# Timed mixed mock assessments

Three original **60-minute** practice tests, **30 questions** each. The mix/timing is a training design, not a claimed Zeus pattern. All questions are reproduced in full so you can work from this file alone. Selected bank questions are deliberately reused for assessment: avoid reading the keys first. The three mocks do not reuse a bank item with each other.

**Suggested 60-minute split:** 18 minutes output prediction, 16 minutes debugging, 17 minutes writing, 6 minutes reasoning, 3 minutes review. If a problem stalls, mark it and return. Use paper; no running code during the timed attempt. Java fragments belong inside main. Read the README conventions before starting.

# Mock 1 — 60 minutes, 30 questions, 48 points

## M1-Q01 — Output prediction: Multiplication before addition

Predict the exact output. **Language: Pseudocode**.

```text
x ← (4 + (3 * 2))
PRINT x
```

**A.** ```text
10
```

**B.** ```text
14
```

**C.** ```text
11
```

**D.** ```text
8
```

## M1-Q02 — Output prediction: Integer quotient and remainder

Predict the exact output. **Language: Pseudocode**.

```text
a ← 23
PRINT (a DIV 4), (a MOD 4)
```

**A.** ```text
5 2
```

**B.** ```text
5 3
```

**C.** ```text
6 3
```

**D.** ```text
5.75 0
```

## M1-Q03 — Output prediction: Nested boundary condition

Predict the exact output. **Language: Pseudocode**.

```text
x ← 0
IF (x ≥ 0) THEN
    IF (x > 0) THEN
        PRINT "P"
    ELSE
        PRINT "Z"
    END IF
ELSE
    PRINT "N"
END IF
```

**A.** ```text
P
```

**B.** ```text
N
```

**C.** ```text
P
Z
```

**D.** ```text
Z
```

## M1-Q04 — Output prediction: Inclusive step-two loop

Predict the exact output. **Language: Pseudocode**.

```text
s ← 0
FOR i ← 1 TO (8 − 1) STEP 2
    s ← (s + i)
END FOR
PRINT s
```

**A.** ```text
9
```

**B.** ```text
25
```

**C.** ```text
12
```

**D.** ```text
16
```

## M1-Q05 — Output prediction: Doubling loop

Predict the exact output. **Language: Pseudocode**.

```text
i ← 1
s ← 0
WHILE (i ≤ 8)
    s ← (s + i)
    i ← (i * 2)
END WHILE
PRINT s, i
```

**A.** ```text
7 8
```

**B.** ```text
15 8
```

**C.** ```text
15 16
```

**D.** ```text
31 32
```

## M1-Q06 — Output prediction: BREAK before addition

Predict the exact output. **Language: Pseudocode**.

```text
s ← 0
FOR i ← 1 TO (7 − 1) STEP 1
    IF (i = 4) THEN
        BREAK
    END IF
    s ← (s + i)
END FOR
PRINT s
```

**A.** ```text
10
```

**B.** ```text
21
```

**C.** ```text
6
```

**D.** ```text
3
```

## M1-Q07 — Output prediction: Rectangular nested loop

Predict the exact output. **Language: Pseudocode**.

```text
count ← 0
FOR i ← 0 TO (3 − 1) STEP 1
    FOR j ← 0 TO (2 − 1) STEP 1
        count ← (count + 1)
    END FOR
END FOR
PRINT count
```

**A.** ```text
5
```

**B.** ```text
3
```

**C.** ```text
6
```

**D.** ```text
9
```

## M1-Q08 — Output prediction: Array accumulation

Predict the exact output. **Language: Pseudocode**.

```text
A ← [2, 5, 1]
s ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    s ← (s + A[i])
END FOR
PRINT s
```

**A.** ```text
7
```

**B.** ```text
8
```

**C.** ```text
3
```

**D.** ```text
5
```

## M1-Q09 — Output prediction: First matching index

Predict the exact output. **Language: Pseudocode**.

```text
A ← [5, 2, 5]
answer ← (−1)
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] = 5) THEN
        answer ← i
        BREAK
    END IF
END FOR
PRINT answer
```

**A.** ```text
0
```

**B.** ```text
2
```

**C.** ```text
1
```

**D.** ```text
-1
```

## M1-Q10 — Output prediction: String reverse loop

Predict the exact output. **Language: Pseudocode**.

```text
s ← "abc"
r ← ""
FOR i ← (LENGTH(s) − 1) TO ((−1) + 1) STEP (−1)
    r ← (r + s[i])
END FOR
PRINT r
```

**A.** ```text
cba
```

**B.** ```text
abc
```

**C.** ```text
bc
```

**D.** ```text
cab
```

## M1-Q11 — Output prediction: Bitwise AND

Predict the exact output. **Language: Pseudocode**.

```text
a ← 13
b ← 10
PRINT (a BIT_AND b)
```

**A.** ```text
7
```

**B.** ```text
15
```

**C.** ```text
23
```

**D.** ```text
8
```

## M1-Q12 — Output prediction: Guard division with AND

Predict the exact output. **Language: Pseudocode**.

```text
d ← 0
PRINT ((d ≠ 0) AND ((12 DIV d) > 1))
```

**A.** ```text
FALSE
```

**B.** ```text
TRUE
```

**C.** ```text
Runtime error
```

**D.** ```text
0
```

## M1-Q13 — Error detection: Swap two values — program review

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

## M1-Q14 — Error detection: Grade bands — program review

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

## M1-Q15 — Error detection: Sum from one to n — program review

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

## M1-Q16 — Error detection: Count decimal digits — program review

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

## M1-Q17 — Error detection: Array sum — program review

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

## M1-Q18 — Error detection: Maximum array value — program review

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

## M1-Q19 — Error detection: Trial-division prime — program review

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

## M1-Q20 — Error detection: Binary search — program review

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

## M1-Q21 — Pseudocode writing: Even or odd

Classify any integer n as even or odd. Demonstrate n=-7.

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M1-Q22 — Pseudocode writing: Sum from one to n

Using a loop, sum 1 through nonnegative n. Demonstrate n=5.

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M1-Q23 — Pseudocode writing: Digit sum

Find sum of decimal digits of nonnegative n. Demonstrate n=405.

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M1-Q24 — Pseudocode writing: Array sum

Sum a possibly empty integer array. Demonstrate [3,-2,7].

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M1-Q25 — Pseudocode writing: Linear search

Return the first index of target or -1 if absent in any integer array. Demonstrate A=[4,9,4],target=4.

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M1-Q26 — Logical reasoning: Chain of implications

P implies Q; Q implies R. R is FALSE. Which must be true?

A. P is FALSE
B. P is TRUE
C. Q is TRUE
D. P cannot be determined

## M1-Q27 — Logical reasoning: Sets and existence

All widgets are devices. Some widgets are blue. What necessarily follows?

A. All devices are widgets
B. Some blue things are devices
C. All blue things are widgets
D. No device is blue

## M1-Q28 — Logical reasoning: Three-person ordering

A,B,C occupy distinct positions 1,2,3. A is before B. C is not first. Who must be first?

A. A
B. B
C. C
D. Cannot determine

## M1-Q29 — Logical reasoning: Data sufficiency: exact integer

x is an integer. Is its exact value determined? Statement I: x is even. Statement II: 1<x<5. Choose the sufficiency result.

A. I alone; II not
B. II alone; I not
C. Together only
D. Not even together

## M1-Q30 — Logical reasoning: Specified sequence rule

The sequence is defined by a_n=n*n+1 for n=1,2,… . Its first five terms are 2,5,10,17,26. What is the sixth?

A. 35
B. 36
C. 37
D. 38

# Mock 2 — 60 minutes, 30 questions, 48 points

## M2-Q01 — Output prediction: CONTINUE skips evens

Predict the exact output. **Language: Pseudocode**.

```text
s ← 0
FOR i ← 1 TO (7 − 1) STEP 1
    IF ((i MOD 2) = 0) THEN
        CONTINUE
    END IF
    s ← (s + i)
END FOR
PRINT s
```

**A.** ```text
12
```

**B.** ```text
9
```

**C.** ```text
21
```

**D.** ```text
6
```

## M2-Q02 — Output prediction: Triangular loop

Predict the exact output. **Language: Pseudocode**.

```text
count ← 0
FOR i ← 1 TO (5 − 1) STEP 1
    FOR j ← 0 TO (i − 1) STEP 1
        count ← (count + 1)
    END FOR
END FOR
PRINT count
```

**A.** ```text
10
```

**B.** ```text
16
```

**C.** ```text
6
```

**D.** ```text
8
```

## M2-Q03 — Output prediction: Inner BREAK only

Predict the exact output. **Language: Pseudocode**.

```text
count ← 0
FOR i ← 0 TO (3 − 1) STEP 1
    FOR j ← 0 TO (4 − 1) STEP 1
        IF (j = 2) THEN
            BREAK
        END IF
        count ← (count + 1)
    END FOR
END FOR
PRINT count
```

**A.** ```text
2
```

**B.** ```text
12
```

**C.** ```text
6
```

**D.** ```text
9
```

## M2-Q04 — Output prediction: Array mutation feeds next step

Predict the exact output. **Language: Pseudocode**.

```text
A ← [1, 2, 3, 4]
FOR i ← 1 TO (LENGTH(A) − 1) STEP 1
    A[i] ← (A[i] + A[(i − 1)])
END FOR
PRINT A
```

**A.** ```text
[1, 3, 6, 10]
```

**B.** ```text
[1, 3, 5, 7]
```

**C.** ```text
[1, 2, 3, 4]
```

**D.** ```text
[10, 6, 3, 1]
```

## M2-Q05 — Output prediction: Array alias

Predict the exact output. **Language: Pseudocode**.

```text
A ← [3, 4]
B ← A
B[1] ← 9
PRINT A, B
```

**A.** ```text
[3, 9] [3, 9]
```

**B.** ```text
[3, 4] [3, 9]
```

**C.** ```text
[3, 9] [3, 4]
```

**D.** ```text
[9, 4] [9, 4]
```

## M2-Q06 — Output prediction: One bubble pass

Predict the exact output. **Language: Pseudocode**.

```text
A ← [4, 1, 3, 2]
FOR j ← 0 TO ((LENGTH(A) − 1) − 1) STEP 1
    IF (A[j] > A[(j + 1)]) THEN
        t ← A[j]
        A[j] ← A[(j + 1)]
        A[(j + 1)] ← t
    END IF
END FOR
PRINT A
```

**A.** ```text
[1, 2, 3, 4]
```

**B.** ```text
[4, 3, 2, 1]
```

**C.** ```text
[1, 4, 2, 3]
```

**D.** ```text
[1, 3, 2, 4]
```

## M2-Q07 — Output prediction: Binary search successful

Predict the exact output. **Language: Pseudocode**.

```text
A ← [1, 4, 6, 9, 12]
lo ← 0
hi ← 4
answer ← (−1)
WHILE (lo ≤ hi)
    mid ← (lo + ((hi − lo) DIV 2))
    IF (A[mid] = 9) THEN
        answer ← mid
        BREAK
    END IF
    IF (A[mid] < 9) THEN
        lo ← (mid + 1)
    ELSE
        hi ← (mid − 1)
    END IF
END WHILE
PRINT answer
```

**A.** ```text
2
```

**B.** ```text
4
```

**C.** ```text
3
```

**D.** ```text
-1
```

## M2-Q08 — Output prediction: Matrix row total

Predict the exact output. **Language: Pseudocode**.

```text
M ← [[2, 1], [3, 4]]
s ← 0
FOR c ← 0 TO (2 − 1) STEP 1
    s ← (s + M[1][c])
END FOR
PRINT s
```

**A.** ```text
3
```

**B.** ```text
7
```

**C.** ```text
10
```

**D.** ```text
5
```

## M2-Q09 — Output prediction: Scalar parameter value

Predict the exact output. **Language: Pseudocode**.

```text
FUNCTION change(x)
    x ← (x + 5)
    RETURN x
END FUNCTION
a ← 2
b ← change(a)
PRINT a, b
```

**A.** ```text
7 7
```

**B.** ```text
2 2
```

**C.** ```text
7 2
```

**D.** ```text
2 7
```

## M2-Q10 — Output prediction: Recursive factorial trace

Predict the exact output. **Language: Pseudocode**.

```text
FUNCTION f(n)
    IF (n ≤ 1) THEN
        RETURN 1
    END IF
    RETURN (n * f((n − 1)))
END FUNCTION
PRINT f(4)
```

**A.** ```text
10
```

**B.** ```text
16
```

**C.** ```text
4
```

**D.** ```text
24
```

## M2-Q11 — Output prediction: Eight-bit complement

Predict the exact output. **Language: Pseudocode**.

```text
PRINT BIT_NOT8(5)
```

**A.** ```text
-6
```

**B.** ```text
251
```

**C.** ```text
5
```

**D.** ```text
250
```

## M2-Q12 — Output prediction: Negative-only maximum

Predict the exact output. **Language: Pseudocode**.

```text
A ← [(−4), (−9), (−2)]
best ← A[0]
FOR i ← 1 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] > best) THEN
        best ← A[i]
    END IF
END FOR
PRINT best
```

**A.** ```text
0
```

**B.** ```text
-9
```

**C.** ```text
-2
```

**D.** ```text
-4
```

## M2-Q13 — Error detection: Leap year — program review

**Required behavior:** Implement Gregorian leap-year rules for a positive integer year: divisible by 400, or by 4 but not 100. Demonstrate 1900.

```text
Pseudocode — faulty
year ← 1900
leap ← (((year MOD 400) = 0) AND (((year MOD 4) = 0) AND ((year MOD 100) ≠ 0)))
PRINT leap
```

Identify and repair the fault. Give a failing input and a verification example.

## M2-Q14 — Error detection: Fibonacci term — program review

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

## M2-Q15 — Error detection: Second distinct largest — program review

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

## M2-Q16 — Error detection: Vowel count — program review

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

## M2-Q17 — Error detection: Matrix sum — program review

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

## M2-Q18 — Error detection: Transpose a rectangle — program review

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

## M2-Q19 — Error detection: Power of two — program review

**Required behavior:** Test whether nonnegative x is a positive power of two using a bitwise condition. Demonstrate x=16.

```text
Pseudocode — faulty
x ← 16
answer ← ((x > 1) AND ((x BIT_AND (x − 1)) = 0))
PRINT answer
```

Identify and repair the fault. Give a failing input and a verification example.

## M2-Q20 — Error detection: Remove sorted duplicates — program review

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

## M2-Q21 — Pseudocode writing: Reverse array in place

Reverse any array using two indices and O(1) extra space. Demonstrate [1,2,3,4,5].

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M2-Q22 — Pseudocode writing: String palindrome

Check exact, case-sensitive palindrome with two pointers. Demonstrate "abca".

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M2-Q23 — Pseudocode writing: Trial-division prime

Test primality for integer n>=0 using divisors up to sqrt(n). Demonstrate n=29.

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M2-Q24 — Pseudocode writing: Bubble sort

Sort an integer array ascending in place using adjacent swaps. Demonstrate [3,1,2].

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M2-Q25 — Pseudocode writing: Binary search

Search an ascending integer array for target; return any matching index or -1. Demonstrate [2,5,8,11],target=11.

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M2-Q26 — Logical reasoning: Count satisfying assignments

How many assignments of Boolean P,Q make (P OR Q) AND NOT(P AND Q) true?

A. 1
B. 2
C. 3
D. 4

## M2-Q27 — Logical reasoning: Four-person ordering count

A,B,C,D occupy distinct positions. A is before B, B before C, and D is last. How many orders satisfy all constraints?

A. 0
B. 1
C. 2
D. 6

## M2-Q28 — Logical reasoning: Grid-path counting

A path consists of exactly two R moves and two D moves, in any order. How many different move strings are possible?

A. 4
B. 6
C. 8
D. 12

## M2-Q29 — Logical reasoning: Digit constraints

A two-digit number has digit sum 9; its tens digit exceeds its units digit by 3. What is the number?

A. 36
B. 54
C. 63
D. 72

## M2-Q30 — Logical reasoning: Sufficiency of a yes/no answer

n is a positive integer. Is n divisible by 6? I: n is odd. II: n is divisible by 3. Which information determines the answer?

A. I alone; II not
B. II alone; I not
C. Together only
D. Not even together

# Mock 3 — 60 minutes, 30 questions, 48 points

## M3-Q01 — Output prediction: Print on descent

Predict the exact output. **Language: Pseudocode**.

```text
FUNCTION f(n)
    IF (n = 0) THEN
        RETURN 0
    END IF
    PRINT n
    RETURN f((n − 1))
END FUNCTION
f(3)
```

**A.** ```text
1
2
3
```

**B.** ```text
3
2
1
0
```

**C.** ```text
0
1
2
3
```

**D.** ```text
3
2
1
```

## M3-Q02 — Output prediction: Print on return

Predict the exact output. **Language: Pseudocode**.

```text
FUNCTION f(n)
    IF (n = 0) THEN
        RETURN 0
    END IF
    f((n − 1))
    PRINT n
    RETURN n
END FUNCTION
f(3)
```

**A.** ```text
3
2
1
```

**B.** ```text
1
2
3
```

**C.** ```text
0
1
2
3
```

**D.** ```text
3
```

## M3-Q03 — Output prediction: Two recursive branches

Predict the exact output. **Language: Pseudocode**.

```text
FUNCTION f(n)
    IF (n ≤ 1) THEN
        RETURN n
    END IF
    RETURN (f((n − 1)) + f((n − 2)))
END FUNCTION
PRINT f(5)
```

**A.** ```text
5
```

**B.** ```text
8
```

**C.** ```text
3
```

**D.** ```text
15
```

## M3-Q04 — Output prediction: Recursive halving

Predict the exact output. **Language: Pseudocode**.

```text
FUNCTION f(n)
    IF (n = 0) THEN
        RETURN 0
    END IF
    RETURN (1 + f((n DIV 2)))
END FUNCTION
PRINT f(10)
```

**A.** ```text
4
```

**B.** ```text
3
```

**C.** ```text
5
```

**D.** ```text
10
```

## M3-Q05 — Output prediction: XOR cancellation

Predict the exact output. **Language: Pseudocode**.

```text
A ← [6, 2, 6, 9, 2]
x ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    x ← (x BIT_XOR A[i])
END FOR
PRINT x
```

**A.** ```text
0
```

**B.** ```text
25
```

**C.** ```text
6
```

**D.** ```text
9
```

## M3-Q06 — Output prediction: Clear set bits

Predict the exact output. **Language: Pseudocode**.

```text
x ← 14
count ← 0
WHILE (x > 0)
    x ← (x BIT_AND (x − 1))
    count ← (count + 1)
END WHILE
PRINT count
```

**A.** ```text
3
```

**B.** ```text
4
```

**C.** ```text
2
```

**D.** ```text
14
```

## M3-Q07 — Output prediction: Numeric reversal drops zeros

Predict the exact output. **Language: Pseudocode**.

```text
n ← 1200
r ← 0
WHILE (n > 0)
    r ← ((r * 10) + (n MOD 10))
    n ← (n DIV 10)
END WHILE
PRINT r
```

**A.** ```text
0021
```

**B.** ```text
21
```

**C.** ```text
1200
```

**D.** ```text
12
```

## M3-Q08 — Output prediction: Parity-filtered triangle n=2

Predict the exact output. **Language: Pseudocode**.

```text
count ← 0
FOR i ← 1 TO (3 − 1) STEP 1
    FOR j ← 1 TO ((i + 1) − 1) STEP 1
        IF (((i + j) MOD 2) = 0) THEN
            count ← (count + 1)
        END IF
    END FOR
END FOR
PRINT count
```

**A.** ```text
3
```

**B.** ```text
2
```

**C.** ```text
1
```

**D.** ```text
4
```

## M3-Q09 — Output prediction: Java left-to-right increments

Predict the exact output. **Language: Java**.

```java
int x=2;
int y=x++ + ++x;
System.out.println(y+" "+x);
```

**A.** ```text
5 4
```

**B.** ```text
7 4
```

**C.** ```text
Undefined behavior
```

**D.** ```text
6 4
```

## M3-Q10 — Output prediction: Java AND short-circuit

Predict the exact output. **Language: Java**.

```java
int x=0;
boolean flag=(x!=0) && (++x>0);
System.out.println(flag+" "+x);
```

**A.** ```text
true 1
```

**B.** ```text
false 0
```

**C.** ```text
false 1
```

**D.** ```text
Runtime error
```

## M3-Q11 — Output prediction: Python double unary plus

Predict the exact output. **Language: Python**.

```python
x = 4
y = ++x
print(x, y)
```

**A.** ```text
5 5
```

**B.** ```text
4 5
```

**C.** ```text
4 4
```

**D.** ```text
Syntax error
```

## M3-Q12 — Output prediction: C do-while runs once

Predict the exact output. **Language: C**.

```c
#include <stdio.h>
int main(void) {
    int x=0;
    do { x++; } while(x<0);
    printf("%d\n",x);
    return 0;
}
```

**A.** ```text
1
```

**B.** ```text
0
```

**C.** ```text
2
```

**D.** ```text
Does not terminate
```

## M3-Q13 — Error detection: Least common multiple — program review

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

## M3-Q14 — Error detection: Recursive palindrome — program review

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

## M3-Q15 — Error detection: Fast exponentiation — program review

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

## M3-Q16 — Error detection: Fixed-window maximum sum — program review

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

## M3-Q17 — Error detection: Insertion sort — program review

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

## M3-Q18 — Error detection: Balanced parentheses — program review

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

## M3-Q19 — Error detection: Sum from one to n — grammar/type review

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

## M3-Q20 — Error detection: Array sum — grammar/type review

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

## M3-Q21 — Pseudocode writing: Fast exponentiation

Compute base^exp for integer base and exp>=0 using repeated squaring. Define 0^0=1 in this exercise. Demonstrate 3^5.

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M3-Q22 — Pseudocode writing: Prefix sums

Build prefix array P of length n+1 with P[0]=0 and P[i+1]=sum A[0..i]. Demonstrate [2,-1,4].

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M3-Q23 — Pseudocode writing: Fixed-window maximum sum

For array A and valid 1<=k<=LENGTH(A), find maximum sum of any contiguous k-element window. Demonstrate [2,-1,3,4],k=2.

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M3-Q24 — Pseudocode writing: First occurrence by binary search

Return the leftmost index of target in a sorted array, or -1. Demonstrate [1,2,2,2,4],target=2.

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M3-Q25 — Pseudocode writing: Recursive subset-sum decision

Given nonnegative array A and nonnegative target, decide if some subset sums to target. Empty subset allowed. Demonstrate [3,5,7],target=10.

Write pseudocode, show a dry run, handle the stated domain and give complexity.

## M3-Q26 — Logical reasoning: Converse trap

Every successful submission passes validation. Submission S passes validation. What follows about whether S is successful?

A. It is certainly successful
B. It is certainly unsuccessful
C. It may be successful or unsuccessful
D. No submission can succeed

## M3-Q27 — Logical reasoning: Three-Boolean count

How many assignments of P,Q,R make (P AND Q) OR R true?

A. 3
B. 4
C. 5
D. 6

## M3-Q28 — Logical reasoning: Repair an invariant

A loop intends to maintain s=sum of all elements already visited. Which update preserves the invariant when visiting A[i]?

A. s ← A[i]
B. s ← s + A[i]
C. s ← s * A[i]
D. s ← i + 1

## M3-Q29 — Logical reasoning: Growth reasoning

For n>=1, an outer loop runs n times. Each inner loop starts j=1 and repeatedly doubles j while j<=n. What is the total time for O(1) work in each inner visit?

A. O(n)
B. O(log n)
C. O(n log(n+1))
D. O(n²)

## M3-Q30 — Logical reasoning: Boolean constraint puzzle

A,B,C indicate attendance. If A attends, B does not. If B attends, C attends. Given B attends, what must be true?

A. A attends; C attends
B. A does not attend; C attends
C. A attends; C does not attend
D. A and C both absent

## Practice scoring rubric

This rubric is for these mocks only. No Zeus scoring or negative-marking policy is assumed.

| Question type | Count per mock | Points each | Maximum |
|---|---:|---:|---:|
| Output prediction | 12 | 1 | 12 |
| Error detection | 8 | 2 | 16 |
| Pseudocode writing | 5 | 3 | 15 |
| Logical reasoning | 5 | 1 | 5 |
| Total | 30 | — | 48 |

- Output/reasoning: 1 for the correct option, 0 otherwise. A trace is required for learning but does not alter the practice MCQ score.
- Error detection: 0.5 for the exact faulty operation, 0.5 for its root cause/counterexample, 0.75 for a correction that meets the full specification, 0.25 for a valid boundary check. Equivalent repairs receive credit.
- Writing: 0.5 for input/domain and initialization, 1.25 for the algorithm, 0.5 for correct boundaries/base cases, 0.5 for a correct dry run, 0.25 for complexity. Equivalent correct algorithms are accepted; they need not match the key text.
- No negative marking in these practice mocks. Blank responses score zero. For an actual assessment, follow its published instructions before guessing.
- Percentage = earned points / 48 * 100. **40–48**: strong practice performance; focus on speed and explaining missed items. **32–39.75**: workable foundations; repair recurring mistakes. **24–31.75**: prioritize loops, arrays and condition tracing. **Below 24**: redo the contract and easy examples before adding difficulty. These bands are self-study diagnostics, not hiring thresholds.
- Keep an error log with ID, mistaken assumption, corrected rule, retry result and time used. Separate knowledge mistakes from calculation and time-management mistakes.
