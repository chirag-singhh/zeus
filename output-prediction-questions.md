# Output-prediction questions

Original practice: O001–O020 easy, O021–O060 medium, O061–O100 mixed boundary and language traps. Use the README contract for neutral code. Java snippets belong inside main; C snippets are complete programs. Choose one option and write your own variable table before checking.

## O001 — Multiplication before addition

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

## O002 — Left-associative subtraction

Predict the exact output. **Language: Pseudocode**.

```text
x ← ((20 − 6) − 3)
PRINT x
```

**A.** ```text
17
```

**B.** ```text
14
```

**C.** ```text
9
```

**D.** ```text
11
```

## O003 — Integer quotient and remainder

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

## O004 — Signed truncation

Predict the exact output. **Language: Pseudocode**.

```text
a ← (−23)
q ← DIVIDE_TRUNC(a, 4)
r ← (a − (q * 4))
PRINT q, r
```

**A.** ```text
-6 1
```

**B.** ```text
-5 3
```

**C.** ```text
-5 -3
```

**D.** ```text
-6 -3
```

## O005 — Assignment uses old values

Predict the exact output. **Language: Pseudocode**.

```text
x ← 3
y ← (x + 2)
x ← (y * 2)
PRINT x, y
```

**A.** ```text
10 10
```

**B.** ```text
6 5
```

**C.** ```text
5 10
```

**D.** ```text
10 5
```

## O006 — Temporary swap

Predict the exact output. **Language: Pseudocode**.

```text
a ← 2
b ← 8
t ← a
a ← b
b ← t
PRINT a, b
```

**A.** ```text
8 8
```

**B.** ```text
8 2
```

**C.** ```text
2 8
```

**D.** ```text
2 2
```

## O007 — Nested boundary condition

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

## O008 — Independent IF blocks

Predict the exact output. **Language: Pseudocode**.

```text
x ← 6
s ← 0
IF (x > 3) THEN
    s ← (s + 1)
END IF
IF ((x MOD 2) = 0) THEN
    s ← (s + 2)
END IF
PRINT s
```

**A.** ```text
1
```

**B.** ```text
2
```

**C.** ```text
0
```

**D.** ```text
3
```

## O009 — Only one alternative

Predict the exact output. **Language: Pseudocode**.

```text
x ← 7
IF (x > 4) THEN
    PRINT "A"
ELSE
    IF (x > 2) THEN
        PRINT "B"
    ELSE
        PRINT "C"
    END IF
END IF
```

**A.** ```text
A
```

**B.** ```text
B
```

**C.** ```text
A
B
```

**D.** ```text
C
```

## O010 — Conditional expression

Predict the exact output. **Language: Pseudocode**.

```text
x ← 4
y ← 9
z ← (x IF (x > y) ELSE y)
PRINT z
```

**A.** ```text
9
```

**B.** ```text
4
```

**C.** ```text
13
```

**D.** ```text
FALSE
```

## O011 — Inclusive step-two loop

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

## O012 — Descending loop

Predict the exact output. **Language: Pseudocode**.

```text
s ← 0
FOR i ← 6 TO (0 + 1) STEP (−2)
    s ← (s + i)
END FOR
PRINT s
```

**A.** ```text
10
```

**B.** ```text
12
```

**C.** ```text
6
```

**D.** ```text
14
```

## O013 — Skipped FOR body

Predict the exact output. **Language: Pseudocode**.

```text
s ← 9
FOR i ← 5 TO (3 − 1) STEP 1
    s ← 0
END FOR
PRINT s
```

**A.** ```text
0
```

**B.** ```text
9
```

**C.** ```text
5
```

**D.** ```text
3
```

## O014 — Doubling loop

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

## O015 — Halving loop

Predict the exact output. **Language: Pseudocode**.

```text
n ← 19
count ← 0
WHILE (n > 0)
    n ← (n DIV 2)
    count ← (count + 1)
END WHILE
PRINT count
```

**A.** ```text
4
```

**B.** ```text
6
```

**C.** ```text
5
```

**D.** ```text
19
```

## O016 — Decrement before accumulation

Predict the exact output. **Language: Pseudocode**.

```text
i ← 5
s ← 0
WHILE (i > 0)
    i ← (i − 1)
    s ← (s + i)
END WHILE
PRINT s
```

**A.** ```text
10
```

**B.** ```text
15
```

**C.** ```text
5
```

**D.** ```text
14
```

## O017 — BREAK before addition

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

## O018 — CONTINUE skips evens

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

## O019 — WHILE update before CONTINUE

Predict the exact output. **Language: Pseudocode**.

```text
i ← 0
s ← 0
WHILE (i < 5)
    i ← (i + 1)
    IF (i = 3) THEN
        CONTINUE
    END IF
    s ← (s + i)
END WHILE
PRINT s
```

**A.** ```text
12
```

**B.** ```text
15
```

**C.** ```text
9
```

**D.** ```text
Does not terminate
```

## O020 — Rectangular nested loop

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

## O021 — Triangular loop

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

## O022 — Inner BREAK only

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

## O023 — Dependent step increments

Predict the exact output. **Language: Pseudocode**.

```text
count ← 0
FOR i ← 1 TO (5 − 1) STEP 1
    j ← i
    WHILE (j ≤ 4)
        count ← (count + 1)
        j ← (j + i)
    END WHILE
END FOR
PRINT count
```

**A.** ```text
8
```

**B.** ```text
10
```

**C.** ```text
16
```

**D.** ```text
7
```

## O024 — Array accumulation

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

## O025 — Array mutation feeds next step

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

## O026 — Array alias

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

## O027 — Array copy

Predict the exact output. **Language: Pseudocode**.

```text
A ← [3, 4]
B ← COPY(A)
B[1] ← 9
PRINT A, B
```

**A.** ```text
[3, 9] [3, 9]
```

**B.** ```text
[3, 4] [3, 4]
```

**C.** ```text
[3, 9] [3, 4]
```

**D.** ```text
[3, 4] [3, 9]
```

## O028 — First matching index

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

## O029 — Last matching index

Predict the exact output. **Language: Pseudocode**.

```text
A ← [5, 2, 5]
answer ← (−1)
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] = 5) THEN
        answer ← i
    END IF
END FOR
PRINT answer
```

**A.** ```text
0
```

**B.** ```text
1
```

**C.** ```text
2
```

**D.** ```text
3
```

## O030 — One bubble pass

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

## O031 — Selection minimum index

Predict the exact output. **Language: Pseudocode**.

```text
A ← [8, 3, 7, 2]
best ← 0
FOR i ← 1 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] < A[best]) THEN
        best ← i
    END IF
END FOR
PRINT best, A[best]
```

**A.** ```text
2 3
```

**B.** ```text
3 2
```

**C.** ```text
1 3
```

**D.** ```text
2 2
```

## O032 — Binary search successful

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

## O033 — String reverse loop

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

## O034 — Character filtering

Predict the exact output. **Language: Pseudocode**.

```text
s ← "banana"
count ← 0
FOR i ← 0 TO (LENGTH(s) − 1) STEP 1
    IF (s[i] = "a") THEN
        count ← (count + 1)
    END IF
END FOR
PRINT count
```

**A.** ```text
2
```

**B.** ```text
4
```

**C.** ```text
6
```

**D.** ```text
3
```

## O035 — End-exclusive slice

Predict the exact output. **Language: Pseudocode**.

```text
s ← "zeus"
PRINT SLICE(s, 1, 3)
```

**A.** ```text
eu
```

**B.** ```text
eus
```

**C.** ```text
ze
```

**D.** ```text
us
```

## O036 — String concatenation

Predict the exact output. **Language: Pseudocode**.

```text
s ← ""
FOR i ← 1 TO (4 − 1) STEP 1
    s ← (s + STRING(i))
END FOR
PRINT s
```

**A.** ```text
6
```

**B.** ```text
321
```

**C.** ```text
123
```

**D.** ```text
1 2 3
```

## O037 — Matrix row total

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

## O038 — Secondary diagonal

Predict the exact output. **Language: Pseudocode**.

```text
M ← [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s ← 0
FOR i ← 0 TO (3 − 1) STEP 1
    s ← (s + M[i][(2 − i)])
END FOR
PRINT s
```

**A.** ```text
25
```

**B.** ```text
45
```

**C.** ```text
12
```

**D.** ```text
15
```

## O039 — Scalar parameter value

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

## O040 — Array parameter mutation

Predict the exact output. **Language: Pseudocode**.

```text
FUNCTION change(A)
    A[0] ← (A[0] + 5)
    RETURN A[0]
END FUNCTION
a ← [2, 3]
b ← change(a)
PRINT a, b
```

**A.** ```text
[2, 3] 7
```

**B.** ```text
[7, 3] 2
```

**C.** ```text
[2, 3] 2
```

**D.** ```text
[7, 3] 7
```

## O041 — Nested function calls

Predict the exact output. **Language: Pseudocode**.

```text
FUNCTION twice(x)
    RETURN (x * 2)
END FUNCTION
PRINT (twice(twice(3)) + 1)
```

**A.** ```text
7
```

**B.** ```text
12
```

**C.** ```text
14
```

**D.** ```text
13
```

## O042 — Early RETURN

Predict the exact output. **Language: Pseudocode**.

```text
FUNCTION f(x)
    IF (x > 0) THEN
        RETURN x
    END IF
    RETURN (−x)
END FUNCTION
PRINT f((−4)), f(3)
```

**A.** ```text
-4 3
```

**B.** ```text
4 -3
```

**C.** ```text
-4 -3
```

**D.** ```text
4 3
```

## O043 — Recursive factorial trace

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

## O044 — Print on descent

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

## O045 — Print on return

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

## O046 — Two recursive branches

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

## O047 — Recursive halving

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

## O048 — Bitwise AND

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

## O049 — Bitwise OR and XOR

Predict the exact output. **Language: Pseudocode**.

```text
a ← 5
b ← 3
PRINT (a BIT_OR b), (a BIT_XOR b)
```

**A.** ```text
6 7
```

**B.** ```text
1 6
```

**C.** ```text
7 6
```

**D.** ```text
7 1
```

## O050 — Eight-bit complement

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

## O051 — Shift then addition

Predict the exact output. **Language: Pseudocode**.

```text
x ← 3
PRINT ((x SHL 2) + 1), (13 SHR 1)
```

**A.** ```text
16 6
```

**B.** ```text
7 6
```

**C.** ```text
13 7
```

**D.** ```text
13 6
```

## O052 — XOR cancellation

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

## O053 — Clear set bits

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

## O054 — Guard division with AND

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

## O055 — OR skips call side effect

Predict the exact output. **Language: Pseudocode**.

```text
FUNCTION mark()
    PRINT "called"
    RETURN FALSE
END FUNCTION
PRINT (TRUE OR mark())
```

**A.** ```text
called
TRUE
```

**B.** ```text
called
FALSE
```

**C.** ```text
FALSE
```

**D.** ```text
TRUE
```

## O056 — De Morgan evaluation

Predict the exact output. **Language: Pseudocode**.

```text
p ← TRUE
q ← FALSE
PRINT (NOT (p AND q)), ((NOT p) OR (NOT q))
```

**A.** ```text
FALSE FALSE
```

**B.** ```text
TRUE FALSE
```

**C.** ```text
FALSE TRUE
```

**D.** ```text
TRUE TRUE
```

## O057 — Digit extraction order

Predict the exact output. **Language: Pseudocode**.

```text
n ← 407
s ← 0
WHILE (n > 0)
    s ← (s + (n MOD 10))
    n ← (n DIV 10)
END WHILE
PRINT s
```

**A.** ```text
407
```

**B.** ```text
7
```

**C.** ```text
4
```

**D.** ```text
11
```

## O058 — Numeric reversal drops zeros

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

## O059 — Euclid state

Predict the exact output. **Language: Pseudocode**.

```text
a ← 35
b ← 15
WHILE (b ≠ 0)
    r ← (a MOD b)
    a ← b
    b ← r
END WHILE
PRINT a, b
```

**A.** ```text
5 0
```

**B.** ```text
15 5
```

**C.** ```text
0 5
```

**D.** ```text
5 5
```

## O060 — Negative-only maximum

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

## O061 — Boundary sequence 0/5/2

Predict the exact output. **Language: Pseudocode**.

```text
s ← ""
FOR i ← 0 TO (5 − 1) STEP 2
    IF (s ≠ "") THEN
        s ← (s + " ")
    END IF
    s ← (s + STRING(i))
END FOR
IF (s = "") THEN
    s ← "EMPTY"
END IF
PRINT s
```

**A.** ```text
0
```

**B.** ```text
0 2 4
```

**C.** ```text
0 2 4 5
```

**D.** ```text
Does not terminate
```

## O062 — Boundary sequence 5/-1/-2

Predict the exact output. **Language: Pseudocode**.

```text
s ← ""
FOR i ← 5 TO ((−1) + 1) STEP (−2)
    IF (s ≠ "") THEN
        s ← (s + " ")
    END IF
    s ← (s + STRING(i))
END FOR
IF (s = "") THEN
    s ← "EMPTY"
END IF
PRINT s
```

**A.** ```text
5
```

**B.** ```text
5 3 1
```

**C.** ```text
5 3 1 -1
```

**D.** ```text
Does not terminate
```

## O063 — Boundary sequence 3/3/1

Predict the exact output. **Language: Pseudocode**.

```text
s ← ""
FOR i ← 3 TO (3 − 1) STEP 1
    IF (s ≠ "") THEN
        s ← (s + " ")
    END IF
    s ← (s + STRING(i))
END FOR
IF (s = "") THEN
    s ← "EMPTY"
END IF
PRINT s
```

**A.** ```text
3
```

**B.** ```text
Does not terminate
```

**C.** ```text
No output
```

**D.** ```text
EMPTY
```

## O064 — Boundary sequence 8/1/-3

Predict the exact output. **Language: Pseudocode**.

```text
s ← ""
FOR i ← 8 TO (1 + 1) STEP (−3)
    IF (s ≠ "") THEN
        s ← (s + " ")
    END IF
    s ← (s + STRING(i))
END FOR
IF (s = "") THEN
    s ← "EMPTY"
END IF
PRINT s
```

**A.** ```text
8
```

**B.** ```text
8 5 2
```

**C.** ```text
8 5 2 1
```

**D.** ```text
Does not terminate
```

## O065 — Digit count boundary n=0

Predict the exact output. **Language: Pseudocode**.

```text
n ← 0
count ← 1
WHILE (n ≥ 10)
    count ← (count + 1)
    n ← (n DIV 10)
END WHILE
PRINT count
```

**A.** ```text
0
```

**B.** ```text
2
```

**C.** ```text
3
```

**D.** ```text
1
```

## O066 — Digit count boundary n=1

Predict the exact output. **Language: Pseudocode**.

```text
n ← 1
count ← 1
WHILE (n ≥ 10)
    count ← (count + 1)
    n ← (n DIV 10)
END WHILE
PRINT count
```

**A.** ```text
0
```

**B.** ```text
1
```

**C.** ```text
2
```

**D.** ```text
3
```

## O067 — Digit count boundary n=10

Predict the exact output. **Language: Pseudocode**.

```text
n ← 10
count ← 1
WHILE (n ≥ 10)
    count ← (count + 1)
    n ← (n DIV 10)
END WHILE
PRINT count
```

**A.** ```text
1
```

**B.** ```text
3
```

**C.** ```text
4
```

**D.** ```text
2
```

## O068 — Digit count boundary n=1001

Predict the exact output. **Language: Pseudocode**.

```text
n ← 1001
count ← 1
WHILE (n ≥ 10)
    count ← (count + 1)
    n ← (n DIV 10)
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
5
```

**D.** ```text
6
```

## O069 — Prime boundary n=1

Predict the exact output. **Language: Pseudocode**.

```text
n ← 1
prime ← (n ≥ 2)
d ← 2
WHILE (prime AND ((d * d) ≤ n))
    IF ((n MOD d) = 0) THEN
        prime ← FALSE
    END IF
    d ← (d + 1)
END WHILE
PRINT prime, d
```

**A.** ```text
No output
```

**B.** ```text
Runtime error
```

**C.** ```text
FALSE 2
```

**D.** ```text
Does not terminate
```

## O070 — Prime boundary n=2

Predict the exact output. **Language: Pseudocode**.

```text
n ← 2
prime ← (n ≥ 2)
d ← 2
WHILE (prime AND ((d * d) ≤ n))
    IF ((n MOD d) = 0) THEN
        prime ← FALSE
    END IF
    d ← (d + 1)
END WHILE
PRINT prime, d
```

**A.** ```text
No output
```

**B.** ```text
Runtime error
```

**C.** ```text
Does not terminate
```

**D.** ```text
TRUE 2
```

## O071 — Prime boundary n=9

Predict the exact output. **Language: Pseudocode**.

```text
n ← 9
prime ← (n ≥ 2)
d ← 2
WHILE (prime AND ((d * d) ≤ n))
    IF ((n MOD d) = 0) THEN
        prime ← FALSE
    END IF
    d ← (d + 1)
END WHILE
PRINT prime, d
```

**A.** ```text
No output
```

**B.** ```text
FALSE 4
```

**C.** ```text
Runtime error
```

**D.** ```text
Does not terminate
```

## O072 — Prime boundary n=17

Predict the exact output. **Language: Pseudocode**.

```text
n ← 17
prime ← (n ≥ 2)
d ← 2
WHILE (prime AND ((d * d) ≤ n))
    IF ((n MOD d) = 0) THEN
        prime ← FALSE
    END IF
    d ← (d + 1)
END WHILE
PRINT prime, d
```

**A.** ```text
TRUE 2
```

**B.** ```text
TRUE 5
```

**C.** ```text
FALSE 2
```

**D.** ```text
FALSE 5
```

## O073 — Fibonacci state after 0 updates

Predict the exact output. **Language: Pseudocode**.

```text
a ← 0
b ← 1
FOR i ← 0 TO (0 − 1) STEP 1
    t ← (a + b)
    a ← b
    b ← t
END FOR
PRINT a, b
```

**A.** ```text
1 0
```

**B.** ```text
1 2
```

**C.** ```text
0 1
```

**D.** ```text
-1 0
```

## O074 — Fibonacci state after 1 updates

Predict the exact output. **Language: Pseudocode**.

```text
a ← 0
b ← 1
FOR i ← 0 TO (1 − 1) STEP 1
    t ← (a + b)
    a ← b
    b ← t
END FOR
PRINT a, b
```

**A.** ```text
1 1
```

**B.** ```text
2 2
```

**C.** ```text
0 0
```

**D.** ```text
0
```

## O075 — Fibonacci state after 4 updates

Predict the exact output. **Language: Pseudocode**.

```text
a ← 0
b ← 1
FOR i ← 0 TO (4 − 1) STEP 1
    t ← (a + b)
    a ← b
    b ← t
END FOR
PRINT a, b
```

**A.** ```text
5 3
```

**B.** ```text
4 6
```

**C.** ```text
2 4
```

**D.** ```text
3 5
```

## O076 — Fibonacci state after 6 updates

Predict the exact output. **Language: Pseudocode**.

```text
a ← 0
b ← 1
FOR i ← 0 TO (6 − 1) STEP 1
    t ← (a + b)
    a ← b
    b ← t
END FOR
PRINT a, b
```

**A.** ```text
13 8
```

**B.** ```text
9 14
```

**C.** ```text
8 13
```

**D.** ```text
7 12
```

## O077 — Search edge [], target 1

Predict the exact output. **Language: Pseudocode**.

```text
A ← []
target ← 1
found ← (−1)
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] = target) THEN
        found ← i
        BREAK
    END IF
END FOR
PRINT found
```

**A.** ```text
-1
```

**B.** ```text
0
```

**C.** ```text
-2
```

**D.** ```text
1
```

## O078 — Search edge [3], target 3

Predict the exact output. **Language: Pseudocode**.

```text
A ← [3]
target ← 3
found ← (−1)
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] = target) THEN
        found ← i
        BREAK
    END IF
END FOR
PRINT found
```

**A.** ```text
1
```

**B.** ```text
-1
```

**C.** ```text
2
```

**D.** ```text
0
```

## O079 — Search edge [2, 2, 2], target 2

Predict the exact output. **Language: Pseudocode**.

```text
A ← [2, 2, 2]
target ← 2
found ← (−1)
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] = target) THEN
        found ← i
        BREAK
    END IF
END FOR
PRINT found
```

**A.** ```text
1
```

**B.** ```text
0
```

**C.** ```text
-1
```

**D.** ```text
2
```

## O080 — Search edge [1, 4, 7], target 5

Predict the exact output. **Language: Pseudocode**.

```text
A ← [1, 4, 7]
target ← 5
found ← (−1)
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] = target) THEN
        found ← i
        BREAK
    END IF
END FOR
PRINT found
```

**A.** ```text
0
```

**B.** ```text
-1
```

**C.** ```text
-2
```

**D.** ```text
1
```

## O081 — Parity-filtered triangle n=1

Predict the exact output. **Language: Pseudocode**.

```text
count ← 0
FOR i ← 1 TO (2 − 1) STEP 1
    FOR j ← 1 TO ((i + 1) − 1) STEP 1
        IF (((i + j) MOD 2) = 0) THEN
            count ← (count + 1)
        END IF
    END FOR
END FOR
PRINT count
```

**A.** ```text
1
```

**B.** ```text
2
```

**C.** ```text
0
```

**D.** ```text
3
```

## O082 — Parity-filtered triangle n=2

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

## O083 — Parity-filtered triangle n=3

Predict the exact output. **Language: Pseudocode**.

```text
count ← 0
FOR i ← 1 TO (4 − 1) STEP 1
    FOR j ← 1 TO ((i + 1) − 1) STEP 1
        IF (((i + j) MOD 2) = 0) THEN
            count ← (count + 1)
        END IF
    END FOR
END FOR
PRINT count
```

**A.** ```text
4
```

**B.** ```text
5
```

**C.** ```text
3
```

**D.** ```text
6
```

## O084 — Parity-filtered triangle n=4

Predict the exact output. **Language: Pseudocode**.

```text
count ← 0
FOR i ← 1 TO (5 − 1) STEP 1
    FOR j ← 1 TO ((i + 1) − 1) STEP 1
        IF (((i + j) MOD 2) = 0) THEN
            count ← (count + 1)
        END IF
    END FOR
END FOR
PRINT count
```

**A.** ```text
7
```

**B.** ```text
5
```

**C.** ```text
6
```

**D.** ```text
8
```

## O085 — Java postfix then prefix

Predict the exact output. **Language: Java**.

```java
int x=4;
int a=x++;
int b=++x;
System.out.println(a+" "+b+" "+x);
```

**A.** ```text
5 6 6
```

**B.** ```text
4 5 6
```

**C.** ```text
4 6 6
```

**D.** ```text
4 6 5
```

## O086 — Java left-to-right increments

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

## O087 — Java decrements

Predict the exact output. **Language: Java**.

```java
int x=5;
int a=x--;
int b=--x;
System.out.println(a+" "+b+" "+x);
```

**A.** ```text
4 3 3
```

**B.** ```text
5 4 3
```

**C.** ```text
5 3 3
```

**D.** ```text
5 3 4
```

## O088 — Java division sign

Predict the exact output. **Language: Java**.

```java
System.out.println((-7/3)+" "+(-7%3));
```

**A.** ```text
-3 2
```

**B.** ```text
-2 -1
```

**C.** ```text
-2 1
```

**D.** ```text
-3 -1
```

## O089 — Java AND short-circuit

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

## O090 — Java switch fall-through

Predict the exact output. **Language: Java**.

```java
int x=2, s=0;
switch(x) {
  case 1: s+=1; break;
  case 2: s+=2;
  case 3: s+=3; break;
  default: s=0;
}
System.out.println(s);
```

**A.** ```text
2
```

**B.** ```text
3
```

**C.** ```text
0
```

**D.** ```text
5
```

## O091 — Java ternary skips other arm

Predict the exact output. **Language: Java**.

```java
int x=3;
int y=(x>0) ? x++ : ++x;
System.out.println(y+" "+x);
```

**A.** ```text
4 4
```

**B.** ```text
3 5
```

**C.** ```text
3 4
```

**D.** ```text
4 5
```

## O092 — Java logical OR skip

Predict the exact output. **Language: Java**.

```java
int x=1;
boolean flag=(x==1) || (x++>0);
System.out.println(flag+" "+x);
```

**A.** ```text
true 1
```

**B.** ```text
true 2
```

**C.** ```text
false 1
```

**D.** ```text
false 2
```

## O093 — Python floor division

Predict the exact output. **Language: Python**.

```python
print(-7 // 3, -7 % 3)
```

**A.** ```text
-2 -1
```

**B.** ```text
-3 2
```

**C.** ```text
-2 1
```

**D.** ```text
-3 -1
```

## O094 — Python double unary plus

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

## O095 — Python range end excluded

Predict the exact output. **Language: Python**.

```python
s = 0
for i in range(1, 5):
    s += i
print(s)
```

**A.** ```text
15
```

**B.** ```text
6
```

**C.** ```text
10
```

**D.** ```text
5
```

## O096 — Python negative indexing

Predict the exact output. **Language: Python**.

```python
A = [2, 4, 6]
print(A[-1])
```

**A.** ```text
Runtime error
```

**B.** ```text
6
```

**C.** ```text
2
```

**D.** ```text
4
```

## O097 — C increments separated

Predict the exact output. **Language: C**.

```c
#include <stdio.h>
int main(void) {
    int x=3;
    int a=x++;
    int b=++x;
    printf("%d %d %d\n",a,b,x);
    return 0;
}
```

**A.** ```text
4 5 5
```

**B.** ```text
3 4 5
```

**C.** ```text
3 5 5
```

**D.** ```text
Undefined behavior
```

## O098 — C decrement loop

Predict the exact output. **Language: C**.

```c
#include <stdio.h>
int main(void) {
    int s=0,i;
    for(i=4;i>0;i--) s+=i;
    printf("%d %d\n",s,i);
    return 0;
}
```

**A.** ```text
10 0
```

**B.** ```text
6 0
```

**C.** ```text
10 1
```

**D.** ```text
15 0
```

## O099 — C do-while runs once

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

## O100 — C integer division

Predict the exact output. **Language: C**.

```c
#include <stdio.h>
int main(void) {
    printf("%d %d\n",17/5,17%5);
    return 0;
}
```

**A.** ```text
3 2
```

**B.** ```text
3.4 0
```

**C.** ```text
4 2
```

**D.** ```text
3 3
```
