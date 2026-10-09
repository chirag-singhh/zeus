# Pseudocode-writing answers

Each solution includes complete pseudocode and a statement-by-statement variable trace. Tables show the state after each listed operation; IF/WHILE rows show the evaluated decision. Function frames have separate local state.

## W001 — Swap two values

```text
Pseudocode
a ← 4
b ← 9
temp ← a
a ← b
b ← temp
PRINT a, b
```

**Sample output**

```text
9 4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 4 | a=4 | — |
| 2 | main | b ← 9 | a=4; b=9 | — |
| 3 | main | temp ← a | a=4; b=9; temp=4 | — |
| 4 | main | a ← b | a=9; b=9; temp=4 | — |
| 5 | main | b ← temp | a=9; b=4; temp=4 | — |
| 6 | main | PRINT | a=9; b=4; temp=4 | 9 4 |

**Why it works:** Preserve a before overwriting it; both original values survive.

**Complexity:** O(1) time, O(1) space

**Boundary checks:** Equal values (5,5) remain (5,5); negatives work unchanged.

## W002 — Rotate three values

```text
Pseudocode
a ← 1
b ← 2
c ← 3
temp ← c
c ← b
b ← a
a ← temp
PRINT a, b, c
```

**Sample output**

```text
3 1 2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 1 | a=1 | — |
| 2 | main | b ← 2 | a=1; b=2 | — |
| 3 | main | c ← 3 | a=1; b=2; c=3 | — |
| 4 | main | temp ← c | a=1; b=2; c=3; temp=3 | — |
| 5 | main | c ← b | a=1; b=2; c=2; temp=3 | — |
| 6 | main | b ← a | a=1; b=1; c=2; temp=3 | — |
| 7 | main | a ← temp | a=3; b=1; c=2; temp=3 | — |
| 8 | main | PRINT | a=3; b=1; c=2; temp=3 | 3 1 2 |

**Why it works:** Saving c allows rightward movement without losing the old values.

**Complexity:** O(1) time and space

**Boundary checks:** (0,0,0) stays unchanged.

## W003 — Quotient and remainder

```text
Pseudocode
a ← (−17)
b ← 5
q ← DIVIDE_TRUNC(a, b)
r ← (a − (q * b))
PRINT q, r
```

**Sample output**

```text
-3 -2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← (−17) | a=-17 | — |
| 2 | main | b ← 5 | a=-17; b=5 | — |
| 3 | main | q ← DIVIDE_TRUNC(a, b) | a=-17; b=5; q=-3 | — |
| 4 | main | r ← (a − (q * b)) | a=-17; b=5; q=-3; r=-2 | — |
| 5 | main | PRINT | a=-17; b=5; q=-3; r=-2 | -3 -2 |

**Why it works:** q truncates toward zero; reconstructing r enforces a=q*b+r. DIVIDE_TRUNC is the contract DIV helper.

**Complexity:** O(1) time and space

**Boundary checks:** a=0,b=5 gives 0 0; a=17,b=-5 gives -3 2; reject b=0.

## W004 — Even or odd

```text
Pseudocode
n ← (−7)
IF (REMAINDER_TRUNC(n, 2) = 0) THEN
    PRINT "even"
ELSE
    PRINT "odd"
END IF
```

**Sample output**

```text
odd
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← (−7) | n=-7 | — |
| 2 | main | IF (REMAINDER_TRUNC(n, 2) = 0) → FALSE | n=-7 | — |
| 3 | main | PRINT | n=-7 | odd |

**Why it works:** Only zero remainder matters, so signed remainder policy does not change parity.

**Complexity:** O(1) time and space

**Boundary checks:** 0 is even; -8 is even.

## W005 — Largest of three

```text
Pseudocode
a ← 7
b ← 7
c ← 2
best ← a
IF (b > best) THEN
    best ← b
END IF
IF (c > best) THEN
    best ← c
END IF
PRINT best
```

**Sample output**

```text
7
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 7 | a=7 | — |
| 2 | main | b ← 7 | a=7; b=7 | — |
| 3 | main | c ← 2 | a=7; b=7; c=2 | — |
| 4 | main | best ← a | a=7; b=7; c=2; best=7 | — |
| 5 | main | IF (b > best) → FALSE | a=7; b=7; c=2; best=7 | — |
| 6 | main | IF (c > best) → FALSE | a=7; b=7; c=2; best=7 | — |
| 7 | main | PRINT | a=7; b=7; c=2; best=7 | 7 |

**Why it works:** Start from a real input value rather than zero; independent comparisons preserve ties.

**Complexity:** O(1) time and space

**Boundary checks:** (-9,-2,-5) gives -2; all equal returns that value.

## W006 — Grade bands

```text
Pseudocode
mark ← 60
IF (mark ≥ 80) THEN
    PRINT "A"
ELSE
    IF (mark ≥ 60) THEN
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

**Sample output**

```text
B
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | mark ← 60 | mark=60 | — |
| 2 | main | IF (mark ≥ 80) → FALSE | mark=60 | — |
| 3 | main | IF (mark ≥ 60) → TRUE | mark=60 | — |
| 4 | main | PRINT | mark=60 | B |

**Why it works:** Descending thresholds mean the first matching band is correct.

**Complexity:** O(1) time and space

**Boundary checks:** 39→F,40→C,79→B,80→A; outside 0..100 is invalid input.

## W007 — Leap year

```text
Pseudocode
year ← 1900
leap ← (((year MOD 400) = 0) OR (((year MOD 4) = 0) AND ((year MOD 100) ≠ 0)))
PRINT leap
```

**Sample output**

```text
FALSE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | year ← 1900 | year=1900 | — |
| 2 | main | leap ← (((year MOD 400) = 0) OR (((year MOD 4) = 0) AND ((year MOD 100) ≠ 0))) | year=1900; leap=FALSE | — |
| 3 | main | PRINT | year=1900; leap=FALSE | FALSE |

**Why it works:** The century exception is overridden only by divisibility by 400.

**Complexity:** O(1) time and space

**Boundary checks:** 2000 TRUE,2024 TRUE,2023 FALSE.

## W008 — Sum from one to n

```text
Pseudocode
n ← 5
s ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    s ← (s + i)
END FOR
PRINT s
```

**Sample output**

```text
15
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 5 | n=5 | — |
| 2 | main | s ← 0 | n=5; s=0 | — |
| 3 | main | FOR visit i | n=5; s=0; i=1 | — |
| 4 | main | s ← (s + i) | n=5; s=1; i=1 | — |
| 5 | main | FOR visit i | n=5; s=1; i=2 | — |
| 6 | main | s ← (s + i) | n=5; s=3; i=2 | — |
| 7 | main | FOR visit i | n=5; s=3; i=3 | — |
| 8 | main | s ← (s + i) | n=5; s=6; i=3 | — |
| 9 | main | FOR visit i | n=5; s=6; i=4 | — |
| 10 | main | s ← (s + i) | n=5; s=10; i=4 | — |
| 11 | main | FOR visit i | n=5; s=10; i=5 | — |
| 12 | main | s ← (s + i) | n=5; s=15; i=5 | — |
| 13 | main | FOR exit | n=5; s=15; i=5 | — |
| 14 | main | PRINT | n=5; s=15; i=5 | 15 |

**Why it works:** The inclusive upper bound includes n. An empty loop handles zero.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** n=0→0; n=1→1.

## W009 — Odd-number sum

```text
Pseudocode
n ← 8
s ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 2
    s ← (s + i)
END FOR
PRINT s
```

**Sample output**

```text
16
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 8 | n=8 | — |
| 2 | main | s ← 0 | n=8; s=0 | — |
| 3 | main | FOR visit i | n=8; s=0; i=1 | — |
| 4 | main | s ← (s + i) | n=8; s=1; i=1 | — |
| 5 | main | FOR visit i | n=8; s=1; i=3 | — |
| 6 | main | s ← (s + i) | n=8; s=4; i=3 | — |
| 7 | main | FOR visit i | n=8; s=4; i=5 | — |
| 8 | main | s ← (s + i) | n=8; s=9; i=5 | — |
| 9 | main | FOR visit i | n=8; s=9; i=7 | — |
| 10 | main | s ← (s + i) | n=8; s=16; i=7 | — |
| 11 | main | FOR exit | n=8; s=16; i=7 | — |
| 12 | main | PRINT | n=8; s=16; i=7 | 16 |

**Why it works:** Visits are 1,3,5,7; n need not itself be visited.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** n=0→0; n=1→1; n=9→25.

## W010 — Countdown

```text
Pseudocode
n ← 3
FOR i ← n TO ((−1) + 1) STEP (−1)
    PRINT i
END FOR
```

**Sample output**

```text
3
2
1
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 3 | n=3 | — |
| 2 | main | FOR visit i | n=3; i=3 | — |
| 3 | main | PRINT | n=3; i=3 | 3 |
| 4 | main | FOR visit i | n=3; i=2 | — |
| 5 | main | PRINT | n=3; i=2 | 2 |
| 6 | main | FOR visit i | n=3; i=1 | — |
| 7 | main | PRINT | n=3; i=1 | 1 |
| 8 | main | FOR visit i | n=3; i=0 | — |
| 9 | main | PRINT | n=3; i=0 | 0 |
| 10 | main | FOR exit | n=3; i=0 | — |

**Why it works:** Negative step must pair with a decreasing bound. Zero is included.

**Complexity:** O(n) time, O(1) auxiliary space

**Boundary checks:** n=0 prints a single 0.

## W011 — Multiplication table

```text
Pseudocode
n ← 3
FOR k ← 1 TO (6 − 1) STEP 1
    PRINT (k * n)
END FOR
```

**Sample output**

```text
3
6
9
12
15
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 3 | n=3 | — |
| 2 | main | FOR visit k | n=3; k=1 | — |
| 3 | main | PRINT | n=3; k=1 | 3 |
| 4 | main | FOR visit k | n=3; k=2 | — |
| 5 | main | PRINT | n=3; k=2 | 6 |
| 6 | main | FOR visit k | n=3; k=3 | — |
| 7 | main | PRINT | n=3; k=3 | 9 |
| 8 | main | FOR visit k | n=3; k=4 | — |
| 9 | main | PRINT | n=3; k=4 | 12 |
| 10 | main | FOR visit k | n=3; k=5 | — |
| 11 | main | PRINT | n=3; k=5 | 15 |
| 12 | main | FOR exit | n=3; k=5 | — |

**Why it works:** k controls the row while n remains constant.

**Complexity:** O(1) time and space for five rows; O(m) if m rows

**Boundary checks:** n=0 prints five zeros; negative n is allowed.

## W012 — Count decimal digits

```text
Pseudocode
n ← 1002
count ← 1
WHILE (n ≥ 10)
    count ← (count + 1)
    n ← (n DIV 10)
END WHILE
PRINT count
```

**Sample output**

```text
4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 1002 | n=1002 | — |
| 2 | main | count ← 1 | n=1002; count=1 | — |
| 3 | main | WHILE (n ≥ 10) → TRUE | n=1002; count=1 | — |
| 4 | main | count ← (count + 1) | n=1002; count=2 | — |
| 5 | main | n ← (n DIV 10) | n=100; count=2 | — |
| 6 | main | WHILE (n ≥ 10) → TRUE | n=100; count=2 | — |
| 7 | main | count ← (count + 1) | n=100; count=3 | — |
| 8 | main | n ← (n DIV 10) | n=10; count=3 | — |
| 9 | main | WHILE (n ≥ 10) → TRUE | n=10; count=3 | — |
| 10 | main | count ← (count + 1) | n=10; count=4 | — |
| 11 | main | n ← (n DIV 10) | n=1; count=4 | — |
| 12 | main | WHILE (n ≥ 10) → FALSE | n=1; count=4 | — |
| 13 | main | PRINT | n=1; count=4 | 4 |

**Why it works:** Starting at one counts the final single-digit value including zero.

**Complexity:** O(d) time, O(1) space, d=digits

**Boundary checks:** 0→1;9→1;10→2.

## W013 — Digit sum

```text
Pseudocode
n ← 405
s ← 0
WHILE (n > 0)
    s ← (s + (n MOD 10))
    n ← (n DIV 10)
END WHILE
PRINT s
```

**Sample output**

```text
9
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 405 | n=405 | — |
| 2 | main | s ← 0 | n=405; s=0 | — |
| 3 | main | WHILE (n > 0) → TRUE | n=405; s=0 | — |
| 4 | main | s ← (s + (n MOD 10)) | n=405; s=5 | — |
| 5 | main | n ← (n DIV 10) | n=40; s=5 | — |
| 6 | main | WHILE (n > 0) → TRUE | n=40; s=5 | — |
| 7 | main | s ← (s + (n MOD 10)) | n=40; s=5 | — |
| 8 | main | n ← (n DIV 10) | n=4; s=5 | — |
| 9 | main | WHILE (n > 0) → TRUE | n=4; s=5 | — |
| 10 | main | s ← (s + (n MOD 10)) | n=4; s=9 | — |
| 11 | main | n ← (n DIV 10) | n=0; s=9 | — |
| 12 | main | WHILE (n > 0) → FALSE | n=0; s=9 | — |
| 13 | main | PRINT | n=0; s=9 | 9 |

**Why it works:** MOD extracts before DIV removes the last digit.

**Complexity:** O(d) time, O(1) space

**Boundary checks:** 0→0;999→27.

## W014 — Reverse an integer

```text
Pseudocode
n ← 120
r ← 0
WHILE (n > 0)
    r ← ((r * 10) + (n MOD 10))
    n ← (n DIV 10)
END WHILE
PRINT r
```

**Sample output**

```text
21
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 120 | n=120 | — |
| 2 | main | r ← 0 | n=120; r=0 | — |
| 3 | main | WHILE (n > 0) → TRUE | n=120; r=0 | — |
| 4 | main | r ← ((r * 10) + (n MOD 10)) | n=120; r=0 | — |
| 5 | main | n ← (n DIV 10) | n=12; r=0 | — |
| 6 | main | WHILE (n > 0) → TRUE | n=12; r=0 | — |
| 7 | main | r ← ((r * 10) + (n MOD 10)) | n=12; r=2 | — |
| 8 | main | n ← (n DIV 10) | n=1; r=2 | — |
| 9 | main | WHILE (n > 0) → TRUE | n=1; r=2 | — |
| 10 | main | r ← ((r * 10) + (n MOD 10)) | n=1; r=21 | — |
| 11 | main | n ← (n DIV 10) | n=0; r=21 | — |
| 12 | main | WHILE (n > 0) → FALSE | n=0; r=21 | — |
| 13 | main | PRINT | n=0; r=21 | 21 |

**Why it works:** Multiply accumulated reversal by ten before adding the next digit. Leading zeros are not stored in an integer.

**Complexity:** O(d) time, O(1) space

**Boundary checks:** 0→0;1000→1.

## W015 — Numeric palindrome

```text
Pseudocode
n ← 1221
original ← n
r ← 0
WHILE (n > 0)
    r ← ((r * 10) + (n MOD 10))
    n ← (n DIV 10)
END WHILE
PRINT (r = original)
```

**Sample output**

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 1221 | n=1221 | — |
| 2 | main | original ← n | n=1221; original=1221 | — |
| 3 | main | r ← 0 | n=1221; original=1221; r=0 | — |
| 4 | main | WHILE (n > 0) → TRUE | n=1221; original=1221; r=0 | — |
| 5 | main | r ← ((r * 10) + (n MOD 10)) | n=1221; original=1221; r=1 | — |
| 6 | main | n ← (n DIV 10) | n=122; original=1221; r=1 | — |
| 7 | main | WHILE (n > 0) → TRUE | n=122; original=1221; r=1 | — |
| 8 | main | r ← ((r * 10) + (n MOD 10)) | n=122; original=1221; r=12 | — |
| 9 | main | n ← (n DIV 10) | n=12; original=1221; r=12 | — |
| 10 | main | WHILE (n > 0) → TRUE | n=12; original=1221; r=12 | — |
| 11 | main | r ← ((r * 10) + (n MOD 10)) | n=12; original=1221; r=122 | — |
| 12 | main | n ← (n DIV 10) | n=1; original=1221; r=122 | — |
| 13 | main | WHILE (n > 0) → TRUE | n=1; original=1221; r=122 | — |
| 14 | main | r ← ((r * 10) + (n MOD 10)) | n=1; original=1221; r=1221 | — |
| 15 | main | n ← (n DIV 10) | n=0; original=1221; r=1221 | — |
| 16 | main | WHILE (n > 0) → FALSE | n=0; original=1221; r=1221 | — |
| 17 | main | PRINT | n=0; original=1221; r=1221 | TRUE |

**Why it works:** Compare reversal with saved original, not consumed n.

**Complexity:** O(d) time, O(1) space

**Boundary checks:** 0 TRUE,10 FALSE,7 TRUE.

## W016 — Iterative factorial

```text
Pseudocode
n ← 5
p ← 1
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    p ← (p * i)
END FOR
PRINT p
```

**Sample output**

```text
120
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 5 | n=5 | — |
| 2 | main | p ← 1 | n=5; p=1 | — |
| 3 | main | FOR visit i | n=5; p=1; i=1 | — |
| 4 | main | p ← (p * i) | n=5; p=1; i=1 | — |
| 5 | main | FOR visit i | n=5; p=1; i=2 | — |
| 6 | main | p ← (p * i) | n=5; p=2; i=2 | — |
| 7 | main | FOR visit i | n=5; p=2; i=3 | — |
| 8 | main | p ← (p * i) | n=5; p=6; i=3 | — |
| 9 | main | FOR visit i | n=5; p=6; i=4 | — |
| 10 | main | p ← (p * i) | n=5; p=24; i=4 | — |
| 11 | main | FOR visit i | n=5; p=24; i=5 | — |
| 12 | main | p ← (p * i) | n=5; p=120; i=5 | — |
| 13 | main | FOR exit | n=5; p=120; i=5 | — |
| 14 | main | PRINT | n=5; p=120; i=5 | 120 |

**Why it works:** The multiplicative identity is 1. The empty product gives 0!=1.

**Complexity:** O(n) time, O(1) space in the unit-cost model

**Boundary checks:** n=0→1; n=1→1; reject negatives.

## W017 — Fibonacci term

```text
Pseudocode
n ← 7
a ← 0
b ← 1
FOR i ← 0 TO (n − 1) STEP 1
    nxt ← (a + b)
    a ← b
    b ← nxt
END FOR
PRINT a
```

**Sample output**

```text
13
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 7 | n=7 | — |
| 2 | main | a ← 0 | n=7; a=0 | — |
| 3 | main | b ← 1 | n=7; a=0; b=1 | — |
| 4 | main | FOR visit i | n=7; a=0; b=1; i=0 | — |
| 5 | main | nxt ← (a + b) | n=7; a=0; b=1; i=0; nxt=1 | — |
| 6 | main | a ← b | n=7; a=1; b=1; i=0; nxt=1 | — |
| 7 | main | b ← nxt | n=7; a=1; b=1; i=0; nxt=1 | — |
| 8 | main | FOR visit i | n=7; a=1; b=1; i=1; nxt=1 | — |
| 9 | main | nxt ← (a + b) | n=7; a=1; b=1; i=1; nxt=2 | — |
| 10 | main | a ← b | n=7; a=1; b=1; i=1; nxt=2 | — |
| 11 | main | b ← nxt | n=7; a=1; b=2; i=1; nxt=2 | — |
| 12 | main | FOR visit i | n=7; a=1; b=2; i=2; nxt=2 | — |
| 13 | main | nxt ← (a + b) | n=7; a=1; b=2; i=2; nxt=3 | — |
| 14 | main | a ← b | n=7; a=2; b=2; i=2; nxt=3 | — |
| 15 | main | b ← nxt | n=7; a=2; b=3; i=2; nxt=3 | — |
| 16 | main | FOR visit i | n=7; a=2; b=3; i=3; nxt=3 | — |
| 17 | main | nxt ← (a + b) | n=7; a=2; b=3; i=3; nxt=5 | — |
| 18 | main | a ← b | n=7; a=3; b=3; i=3; nxt=5 | — |
| 19 | main | b ← nxt | n=7; a=3; b=5; i=3; nxt=5 | — |
| 20 | main | FOR visit i | n=7; a=3; b=5; i=4; nxt=5 | — |
| 21 | main | nxt ← (a + b) | n=7; a=3; b=5; i=4; nxt=8 | — |
| 22 | main | a ← b | n=7; a=5; b=5; i=4; nxt=8 | — |
| 23 | main | b ← nxt | n=7; a=5; b=8; i=4; nxt=8 | — |
| 24 | main | FOR visit i | n=7; a=5; b=8; i=5; nxt=8 | — |
| 25 | main | nxt ← (a + b) | n=7; a=5; b=8; i=5; nxt=13 | — |
| 26 | main | a ← b | n=7; a=8; b=8; i=5; nxt=13 | — |
| 27 | main | b ← nxt | n=7; a=8; b=13; i=5; nxt=13 | — |
| 28 | main | FOR visit i | n=7; a=8; b=13; i=6; nxt=13 | — |
| 29 | main | nxt ← (a + b) | n=7; a=8; b=13; i=6; nxt=21 | — |
| 30 | main | a ← b | n=7; a=13; b=13; i=6; nxt=21 | — |
| 31 | main | b ← nxt | n=7; a=13; b=21; i=6; nxt=21 | — |
| 32 | main | FOR exit | n=7; a=13; b=21; i=6; nxt=21 | — |
| 33 | main | PRINT | n=7; a=13; b=21; i=6; nxt=21 | 13 |

**Why it works:** After k updates, a=F_k and b=F_(k+1). The temporary preserves both old terms.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** F0=0,F1=1,F2=1.

## W018 — Euclidean GCD

```text
Pseudocode
a ← 48
b ← 18
WHILE (b ≠ 0)
    r ← (a MOD b)
    a ← b
    b ← r
END WHILE
PRINT a
```

**Sample output**

```text
6
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 48 | a=48 | — |
| 2 | main | b ← 18 | a=48; b=18 | — |
| 3 | main | WHILE (b ≠ 0) → TRUE | a=48; b=18 | — |
| 4 | main | r ← (a MOD b) | a=48; b=18; r=12 | — |
| 5 | main | a ← b | a=18; b=18; r=12 | — |
| 6 | main | b ← r | a=18; b=12; r=12 | — |
| 7 | main | WHILE (b ≠ 0) → TRUE | a=18; b=12; r=12 | — |
| 8 | main | r ← (a MOD b) | a=18; b=12; r=6 | — |
| 9 | main | a ← b | a=12; b=12; r=6 | — |
| 10 | main | b ← r | a=12; b=6; r=6 | — |
| 11 | main | WHILE (b ≠ 0) → TRUE | a=12; b=6; r=6 | — |
| 12 | main | r ← (a MOD b) | a=12; b=6; r=0 | — |
| 13 | main | a ← b | a=6; b=6; r=0 | — |
| 14 | main | b ← r | a=6; b=0; r=0 | — |
| 15 | main | WHILE (b ≠ 0) → FALSE | a=6; b=0; r=0 | — |
| 16 | main | PRINT | a=6; b=0; r=0 | 6 |

**Why it works:** Common divisors are unchanged by subtracting multiples; remainders strictly shrink until zero.

**Complexity:** O(log(max(a,b)+1)) time, O(1) space

**Boundary checks:** (0,15)→15;(0,0)→0;(7,3)→1.

## W019 — Array sum

```text
Pseudocode
A ← [3, (−2), 7]
s ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    s ← (s + A[i])
END FOR
PRINT s
```

**Sample output**

```text
8
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [3, (−2), 7] | A=[3, -2, 7] | — |
| 2 | main | s ← 0 | A=[3, -2, 7]; s=0 | — |
| 3 | main | FOR visit i | A=[3, -2, 7]; s=0; i=0 | — |
| 4 | main | s ← (s + A[i]) | A=[3, -2, 7]; s=3; i=0 | — |
| 5 | main | FOR visit i | A=[3, -2, 7]; s=3; i=1 | — |
| 6 | main | s ← (s + A[i]) | A=[3, -2, 7]; s=1; i=1 | — |
| 7 | main | FOR visit i | A=[3, -2, 7]; s=1; i=2 | — |
| 8 | main | s ← (s + A[i]) | A=[3, -2, 7]; s=8; i=2 | — |
| 9 | main | FOR exit | A=[3, -2, 7]; s=8; i=2 | — |
| 10 | main | PRINT | A=[3, -2, 7]; s=8; i=2 | 8 |

**Why it works:** All valid indices are visited once, accumulating rather than replacing s.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** []→0;[-5]→-5.

## W020 — Linear search

```text
Pseudocode
A ← [4, 9, 4]
target ← 4
found ← (−1)
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] = target) THEN
        found ← i
        BREAK
    END IF
END FOR
PRINT found
```

**Sample output**

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [4, 9, 4] | A=[4, 9, 4] | — |
| 2 | main | target ← 4 | A=[4, 9, 4]; target=4 | — |
| 3 | main | found ← (−1) | A=[4, 9, 4]; target=4; found=-1 | — |
| 4 | main | FOR visit i | A=[4, 9, 4]; target=4; found=-1; i=0 | — |
| 5 | main | IF (A[i] = target) → TRUE | A=[4, 9, 4]; target=4; found=-1; i=0 | — |
| 6 | main | found ← i | A=[4, 9, 4]; target=4; found=0; i=0 | — |
| 7 | main | BREAK | A=[4, 9, 4]; target=4; found=0; i=0 | — |
| 8 | main | FOR exit | A=[4, 9, 4]; target=4; found=0; i=0 | — |
| 9 | main | PRINT | A=[4, 9, 4]; target=4; found=0; i=0 | 0 |

**Why it works:** BREAK preserves the first match; the initialized sentinel handles absence.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** []→-1;target 8→-1; duplicates must return first index.

## W021 — Maximum array value

```text
Pseudocode
A ← [(−8), (−2), (−5)]
best ← A[0]
FOR i ← 1 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] > best) THEN
        best ← A[i]
    END IF
END FOR
PRINT best
```

**Sample output**

```text
-2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [(−8), (−2), (−5)] | A=[-8, -2, -5] | — |
| 2 | main | best ← A[0] | A=[-8, -2, -5]; best=-8 | — |
| 3 | main | FOR visit i | A=[-8, -2, -5]; best=-8; i=1 | — |
| 4 | main | IF (A[i] > best) → TRUE | A=[-8, -2, -5]; best=-8; i=1 | — |
| 5 | main | best ← A[i] | A=[-8, -2, -5]; best=-2; i=1 | — |
| 6 | main | FOR visit i | A=[-8, -2, -5]; best=-2; i=2 | — |
| 7 | main | IF (A[i] > best) → FALSE | A=[-8, -2, -5]; best=-2; i=2 | — |
| 8 | main | FOR exit | A=[-8, -2, -5]; best=-2; i=2 | — |
| 9 | main | PRINT | A=[-8, -2, -5]; best=-2; i=2 | -2 |

**Why it works:** Initialize from the array so negative-only data cannot invent a zero.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** [-7]→-7; empty array must be rejected.

## W022 — Second distinct largest

```text
Pseudocode
A ← [5, 5, 2, 8, 8]
B ← SORTED(A)
answer ← "NONE"
IF (LENGTH(B) ≥ 2) THEN
    largest ← B[(LENGTH(B) − 1)]
    i ← (LENGTH(B) − 2)
    WHILE (i ≥ 0)
        IF (B[i] ≠ largest) THEN
            answer ← B[i]
            BREAK
        END IF
        i ← (i − 1)
    END WHILE
END IF
PRINT answer
```

**Sample output**

```text
5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [5, 5, 2, 8, 8] | A=[5, 5, 2, 8, 8] | — |
| 2 | main | B ← SORTED(A) | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8] | — |
| 3 | main | answer ← "NONE" | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=NONE | — |
| 4 | main | IF (LENGTH(B) ≥ 2) → TRUE | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=NONE | — |
| 5 | main | largest ← B[(LENGTH(B) − 1)] | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=NONE; largest=8 | — |
| 6 | main | i ← (LENGTH(B) − 2) | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=NONE; largest=8; i=3 | — |
| 7 | main | WHILE (i ≥ 0) → TRUE | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=NONE; largest=8; i=3 | — |
| 8 | main | IF (B[i] ≠ largest) → FALSE | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=NONE; largest=8; i=3 | — |
| 9 | main | i ← (i − 1) | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=NONE; largest=8; i=2 | — |
| 10 | main | WHILE (i ≥ 0) → TRUE | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=NONE; largest=8; i=2 | — |
| 11 | main | IF (B[i] ≠ largest) → TRUE | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=NONE; largest=8; i=2 | — |
| 12 | main | answer ← B[i] | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=5; largest=8; i=2 | — |
| 13 | main | BREAK | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=5; largest=8; i=2 | — |
| 14 | main | PRINT | A=[5, 5, 2, 8, 8]; B=[2, 5, 5, 8, 8]; answer=5; largest=8; i=2 | 5 |

**Why it works:** Skipping all copies of the largest enforces distinctness.

**Complexity:** O(n log n) time, O(n) space for sorted copy

**Boundary checks:** [] and [4,4]→NONE;[-3,-1]→-3.

## W023 — Reverse array in place

```text
Pseudocode
A ← [1, 2, 3, 4, 5]
l ← 0
r ← (LENGTH(A) − 1)
WHILE (l < r)
    temp ← A[l]
    A[l] ← A[r]
    A[r] ← temp
    l ← (l + 1)
    r ← (r − 1)
END WHILE
PRINT A
```

**Sample output**

```text
[5, 4, 3, 2, 1]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [1, 2, 3, 4, 5] | A=[1, 2, 3, 4, 5] | — |
| 2 | main | l ← 0 | A=[1, 2, 3, 4, 5]; l=0 | — |
| 3 | main | r ← (LENGTH(A) − 1) | A=[1, 2, 3, 4, 5]; l=0; r=4 | — |
| 4 | main | WHILE (l < r) → TRUE | A=[1, 2, 3, 4, 5]; l=0; r=4 | — |
| 5 | main | temp ← A[l] | A=[1, 2, 3, 4, 5]; l=0; r=4; temp=1 | — |
| 6 | main | A[l] ← A[r] | A=[5, 2, 3, 4, 5]; l=0; r=4; temp=1 | — |
| 7 | main | A[r] ← temp | A=[5, 2, 3, 4, 1]; l=0; r=4; temp=1 | — |
| 8 | main | l ← (l + 1) | A=[5, 2, 3, 4, 1]; l=1; r=4; temp=1 | — |
| 9 | main | r ← (r − 1) | A=[5, 2, 3, 4, 1]; l=1; r=3; temp=1 | — |
| 10 | main | WHILE (l < r) → TRUE | A=[5, 2, 3, 4, 1]; l=1; r=3; temp=1 | — |
| 11 | main | temp ← A[l] | A=[5, 2, 3, 4, 1]; l=1; r=3; temp=2 | — |
| 12 | main | A[l] ← A[r] | A=[5, 4, 3, 4, 1]; l=1; r=3; temp=2 | — |
| 13 | main | A[r] ← temp | A=[5, 4, 3, 2, 1]; l=1; r=3; temp=2 | — |
| 14 | main | l ← (l + 1) | A=[5, 4, 3, 2, 1]; l=2; r=3; temp=2 | — |
| 15 | main | r ← (r − 1) | A=[5, 4, 3, 2, 1]; l=2; r=2; temp=2 | — |
| 16 | main | WHILE (l < r) → FALSE | A=[5, 4, 3, 2, 1]; l=2; r=2; temp=2 | — |
| 17 | main | PRINT | A=[5, 4, 3, 2, 1]; l=2; r=2; temp=2 | [5, 4, 3, 2, 1] |

**Why it works:** Symmetric swaps move each end to its final position; the center is untouched.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** []→[];[7]→[7]; reverse twice restores original.

## W024 — Count occurrences

```text
Pseudocode
A ← [2, 3, 2, 2]
target ← 2
count ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] = target) THEN
        count ← (count + 1)
    END IF
END FOR
PRINT count
```

**Sample output**

```text
3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [2, 3, 2, 2] | A=[2, 3, 2, 2] | — |
| 2 | main | target ← 2 | A=[2, 3, 2, 2]; target=2 | — |
| 3 | main | count ← 0 | A=[2, 3, 2, 2]; target=2; count=0 | — |
| 4 | main | FOR visit i | A=[2, 3, 2, 2]; target=2; count=0; i=0 | — |
| 5 | main | IF (A[i] = target) → TRUE | A=[2, 3, 2, 2]; target=2; count=0; i=0 | — |
| 6 | main | count ← (count + 1) | A=[2, 3, 2, 2]; target=2; count=1; i=0 | — |
| 7 | main | FOR visit i | A=[2, 3, 2, 2]; target=2; count=1; i=1 | — |
| 8 | main | IF (A[i] = target) → FALSE | A=[2, 3, 2, 2]; target=2; count=1; i=1 | — |
| 9 | main | FOR visit i | A=[2, 3, 2, 2]; target=2; count=1; i=2 | — |
| 10 | main | IF (A[i] = target) → TRUE | A=[2, 3, 2, 2]; target=2; count=1; i=2 | — |
| 11 | main | count ← (count + 1) | A=[2, 3, 2, 2]; target=2; count=2; i=2 | — |
| 12 | main | FOR visit i | A=[2, 3, 2, 2]; target=2; count=2; i=3 | — |
| 13 | main | IF (A[i] = target) → TRUE | A=[2, 3, 2, 2]; target=2; count=2; i=3 | — |
| 14 | main | count ← (count + 1) | A=[2, 3, 2, 2]; target=2; count=3; i=3 | — |
| 15 | main | FOR exit | A=[2, 3, 2, 2]; target=2; count=3; i=3 | — |
| 16 | main | PRINT | A=[2, 3, 2, 2]; target=2; count=3; i=3 | 3 |

**Why it works:** Every matching position contributes one, including duplicates.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** []→0; absent target→0.

## W025 — Vowel count

```text
Pseudocode
s ← "Zeus AI"
s ← LOWER(s)
count ← 0
FOR i ← 0 TO (LENGTH(s) − 1) STEP 1
    IF (s[i] IS_IN "aeiou") THEN
        count ← (count + 1)
    END IF
END FOR
PRINT count
```

**Sample output**

```text
4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "Zeus AI" | s=Zeus AI | — |
| 2 | main | s ← LOWER(s) | s=zeus ai | — |
| 3 | main | count ← 0 | s=zeus ai; count=0 | — |
| 4 | main | FOR visit i | s=zeus ai; count=0; i=0 | — |
| 5 | main | IF (s[i] IS_IN "aeiou") → FALSE | s=zeus ai; count=0; i=0 | — |
| 6 | main | FOR visit i | s=zeus ai; count=0; i=1 | — |
| 7 | main | IF (s[i] IS_IN "aeiou") → TRUE | s=zeus ai; count=0; i=1 | — |
| 8 | main | count ← (count + 1) | s=zeus ai; count=1; i=1 | — |
| 9 | main | FOR visit i | s=zeus ai; count=1; i=2 | — |
| 10 | main | IF (s[i] IS_IN "aeiou") → TRUE | s=zeus ai; count=1; i=2 | — |
| 11 | main | count ← (count + 1) | s=zeus ai; count=2; i=2 | — |
| 12 | main | FOR visit i | s=zeus ai; count=2; i=3 | — |
| 13 | main | IF (s[i] IS_IN "aeiou") → FALSE | s=zeus ai; count=2; i=3 | — |
| 14 | main | FOR visit i | s=zeus ai; count=2; i=4 | — |
| 15 | main | IF (s[i] IS_IN "aeiou") → FALSE | s=zeus ai; count=2; i=4 | — |
| 16 | main | FOR visit i | s=zeus ai; count=2; i=5 | — |
| 17 | main | IF (s[i] IS_IN "aeiou") → TRUE | s=zeus ai; count=2; i=5 | — |
| 18 | main | count ← (count + 1) | s=zeus ai; count=3; i=5 | — |
| 19 | main | FOR visit i | s=zeus ai; count=3; i=6 | — |
| 20 | main | IF (s[i] IS_IN "aeiou") → TRUE | s=zeus ai; count=3; i=6 | — |
| 21 | main | count ← (count + 1) | s=zeus ai; count=4; i=6 | — |
| 22 | main | FOR exit | s=zeus ai; count=4; i=6 | — |
| 23 | main | PRINT | s=zeus ai; count=4; i=6 | 4 |

**Why it works:** Normalize case before membership testing. Spaces are not vowels.

**Complexity:** O(n) time, O(n) space for lowercase copy

**Boundary checks:** empty→0;"rhythm"→0;"AEIOU"→5.

## W026 — String reversal

```text
Pseudocode
s ← "code"
r ← ""
FOR i ← (LENGTH(s) − 1) TO ((−1) + 1) STEP (−1)
    r ← (r + s[i])
END FOR
PRINT r
```

**Sample output**

```text
edoc
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "code" | s=code | — |
| 2 | main | r ← "" | s=code; r= | — |
| 3 | main | FOR visit i | s=code; r=; i=3 | — |
| 4 | main | r ← (r + s[i]) | s=code; r=e; i=3 | — |
| 5 | main | FOR visit i | s=code; r=e; i=2 | — |
| 6 | main | r ← (r + s[i]) | s=code; r=ed; i=2 | — |
| 7 | main | FOR visit i | s=code; r=ed; i=1 | — |
| 8 | main | r ← (r + s[i]) | s=code; r=edo; i=1 | — |
| 9 | main | FOR visit i | s=code; r=edo; i=0 | — |
| 10 | main | r ← (r + s[i]) | s=code; r=edoc; i=0 | — |
| 11 | main | FOR exit | s=code; r=edoc; i=0 | — |
| 12 | main | PRINT | s=code; r=edoc; i=0 | edoc |

**Why it works:** Descending valid indices give reversed order.

**Complexity:** O(n²) copying time for immutable concatenation; O(n) stored result

**Boundary checks:** empty→blank line;"a"→a. An array builder can reduce copying time to O(n).

## W027 — String palindrome

```text
Pseudocode
s ← "abca"
l ← 0
r ← (LENGTH(s) − 1)
ok ← TRUE
WHILE (l < r)
    IF (s[l] ≠ s[r]) THEN
        ok ← FALSE
        BREAK
    END IF
    l ← (l + 1)
    r ← (r − 1)
END WHILE
PRINT ok
```

**Sample output**

```text
FALSE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "abca" | s=abca | — |
| 2 | main | l ← 0 | s=abca; l=0 | — |
| 3 | main | r ← (LENGTH(s) − 1) | s=abca; l=0; r=3 | — |
| 4 | main | ok ← TRUE | s=abca; l=0; r=3; ok=TRUE | — |
| 5 | main | WHILE (l < r) → TRUE | s=abca; l=0; r=3; ok=TRUE | — |
| 6 | main | IF (s[l] ≠ s[r]) → FALSE | s=abca; l=0; r=3; ok=TRUE | — |
| 7 | main | l ← (l + 1) | s=abca; l=1; r=3; ok=TRUE | — |
| 8 | main | r ← (r − 1) | s=abca; l=1; r=2; ok=TRUE | — |
| 9 | main | WHILE (l < r) → TRUE | s=abca; l=1; r=2; ok=TRUE | — |
| 10 | main | IF (s[l] ≠ s[r]) → TRUE | s=abca; l=1; r=2; ok=TRUE | — |
| 11 | main | ok ← FALSE | s=abca; l=1; r=2; ok=FALSE | — |
| 12 | main | BREAK | s=abca; l=1; r=2; ok=FALSE | — |
| 13 | main | PRINT | s=abca; l=1; r=2; ok=FALSE | FALSE |

**Why it works:** One mismatched mirrored pair disproves palindrome; no further comparisons are needed.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** empty and one character TRUE;"Aa" FALSE.

## W028 — Trial-division prime

```text
Pseudocode
n ← 29
prime ← (n ≥ 2)
d ← 2
WHILE (prime AND ((d * d) ≤ n))
    IF ((n MOD d) = 0) THEN
        prime ← FALSE
    END IF
    d ← (d + 1)
END WHILE
PRINT prime
```

**Sample output**

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 29 | n=29 | — |
| 2 | main | prime ← (n ≥ 2) | n=29; prime=TRUE | — |
| 3 | main | d ← 2 | n=29; prime=TRUE; d=2 | — |
| 4 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=29; prime=TRUE; d=2 | — |
| 5 | main | IF ((n MOD d) = 0) → FALSE | n=29; prime=TRUE; d=2 | — |
| 6 | main | d ← (d + 1) | n=29; prime=TRUE; d=3 | — |
| 7 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=29; prime=TRUE; d=3 | — |
| 8 | main | IF ((n MOD d) = 0) → FALSE | n=29; prime=TRUE; d=3 | — |
| 9 | main | d ← (d + 1) | n=29; prime=TRUE; d=4 | — |
| 10 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=29; prime=TRUE; d=4 | — |
| 11 | main | IF ((n MOD d) = 0) → FALSE | n=29; prime=TRUE; d=4 | — |
| 12 | main | d ← (d + 1) | n=29; prime=TRUE; d=5 | — |
| 13 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=29; prime=TRUE; d=5 | — |
| 14 | main | IF ((n MOD d) = 0) → FALSE | n=29; prime=TRUE; d=5 | — |
| 15 | main | d ← (d + 1) | n=29; prime=TRUE; d=6 | — |
| 16 | main | WHILE (prime AND ((d * d) ≤ n)) → FALSE | n=29; prime=TRUE; d=6 | — |
| 17 | main | PRINT | n=29; prime=TRUE; d=6 | TRUE |

**Why it works:** The loop excludes composites with a small factor; no such factor means prime.

**Complexity:** O(sqrt(n)) time, O(1) space

**Boundary checks:** 0,1 FALSE;2 TRUE;49 FALSE.

## W029 — Prime count in a range

```text
Pseudocode
n ← 10
count ← 0
FOR x ← 2 TO ((n + 1) − 1) STEP 1
    prime ← TRUE
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

**Sample output**

```text
4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 10 | n=10 | — |
| 2 | main | count ← 0 | n=10; count=0 | — |
| 3 | main | FOR visit x | n=10; count=0; x=2 | — |
| 4 | main | prime ← TRUE | n=10; count=0; x=2; prime=TRUE | — |
| 5 | main | d ← 2 | n=10; count=0; x=2; prime=TRUE; d=2 | — |
| 6 | main | WHILE (prime AND ((d * d) ≤ x)) → FALSE | n=10; count=0; x=2; prime=TRUE; d=2 | — |
| 7 | main | IF prime → TRUE | n=10; count=0; x=2; prime=TRUE; d=2 | — |
| 8 | main | count ← (count + 1) | n=10; count=1; x=2; prime=TRUE; d=2 | — |
| 9 | main | FOR visit x | n=10; count=1; x=3; prime=TRUE; d=2 | — |
| 10 | main | prime ← TRUE | n=10; count=1; x=3; prime=TRUE; d=2 | — |
| 11 | main | d ← 2 | n=10; count=1; x=3; prime=TRUE; d=2 | — |
| 12 | main | WHILE (prime AND ((d * d) ≤ x)) → FALSE | n=10; count=1; x=3; prime=TRUE; d=2 | — |
| 13 | main | IF prime → TRUE | n=10; count=1; x=3; prime=TRUE; d=2 | — |
| 14 | main | count ← (count + 1) | n=10; count=2; x=3; prime=TRUE; d=2 | — |
| 15 | main | FOR visit x | n=10; count=2; x=4; prime=TRUE; d=2 | — |
| 16 | main | prime ← TRUE | n=10; count=2; x=4; prime=TRUE; d=2 | — |
| 17 | main | d ← 2 | n=10; count=2; x=4; prime=TRUE; d=2 | — |
| 18 | main | WHILE (prime AND ((d * d) ≤ x)) → TRUE | n=10; count=2; x=4; prime=TRUE; d=2 | — |
| 19 | main | IF ((x MOD d) = 0) → TRUE | n=10; count=2; x=4; prime=TRUE; d=2 | — |
| 20 | main | prime ← FALSE | n=10; count=2; x=4; prime=FALSE; d=2 | — |
| 21 | main | d ← (d + 1) | n=10; count=2; x=4; prime=FALSE; d=3 | — |
| 22 | main | WHILE (prime AND ((d * d) ≤ x)) → FALSE | n=10; count=2; x=4; prime=FALSE; d=3 | — |
| 23 | main | IF prime → FALSE | n=10; count=2; x=4; prime=FALSE; d=3 | — |
| 24 | main | FOR visit x | n=10; count=2; x=5; prime=FALSE; d=3 | — |
| 25 | main | prime ← TRUE | n=10; count=2; x=5; prime=TRUE; d=3 | — |
| 26 | main | d ← 2 | n=10; count=2; x=5; prime=TRUE; d=2 | — |
| 27 | main | WHILE (prime AND ((d * d) ≤ x)) → TRUE | n=10; count=2; x=5; prime=TRUE; d=2 | — |
| 28 | main | IF ((x MOD d) = 0) → FALSE | n=10; count=2; x=5; prime=TRUE; d=2 | — |
| 29 | main | d ← (d + 1) | n=10; count=2; x=5; prime=TRUE; d=3 | — |
| 30 | main | WHILE (prime AND ((d * d) ≤ x)) → FALSE | n=10; count=2; x=5; prime=TRUE; d=3 | — |
| 31 | main | IF prime → TRUE | n=10; count=2; x=5; prime=TRUE; d=3 | — |
| 32 | main | count ← (count + 1) | n=10; count=3; x=5; prime=TRUE; d=3 | — |
| 33 | main | FOR visit x | n=10; count=3; x=6; prime=TRUE; d=3 | — |
| 34 | main | prime ← TRUE | n=10; count=3; x=6; prime=TRUE; d=3 | — |
| 35 | main | d ← 2 | n=10; count=3; x=6; prime=TRUE; d=2 | — |
| 36 | main | WHILE (prime AND ((d * d) ≤ x)) → TRUE | n=10; count=3; x=6; prime=TRUE; d=2 | — |
| 37 | main | IF ((x MOD d) = 0) → TRUE | n=10; count=3; x=6; prime=TRUE; d=2 | — |
| 38 | main | prime ← FALSE | n=10; count=3; x=6; prime=FALSE; d=2 | — |
| 39 | main | d ← (d + 1) | n=10; count=3; x=6; prime=FALSE; d=3 | — |
| 40 | main | WHILE (prime AND ((d * d) ≤ x)) → FALSE | n=10; count=3; x=6; prime=FALSE; d=3 | — |
| 41 | main | IF prime → FALSE | n=10; count=3; x=6; prime=FALSE; d=3 | — |
| 42 | main | FOR visit x | n=10; count=3; x=7; prime=FALSE; d=3 | — |
| 43 | main | prime ← TRUE | n=10; count=3; x=7; prime=TRUE; d=3 | — |
| 44 | main | d ← 2 | n=10; count=3; x=7; prime=TRUE; d=2 | — |
| 45 | main | WHILE (prime AND ((d * d) ≤ x)) → TRUE | n=10; count=3; x=7; prime=TRUE; d=2 | — |
| 46 | main | IF ((x MOD d) = 0) → FALSE | n=10; count=3; x=7; prime=TRUE; d=2 | — |
| 47 | main | d ← (d + 1) | n=10; count=3; x=7; prime=TRUE; d=3 | — |
| 48 | main | WHILE (prime AND ((d * d) ≤ x)) → FALSE | n=10; count=3; x=7; prime=TRUE; d=3 | — |
| 49 | main | IF prime → TRUE | n=10; count=3; x=7; prime=TRUE; d=3 | — |
| 50 | main | count ← (count + 1) | n=10; count=4; x=7; prime=TRUE; d=3 | — |
| 51 | main | FOR visit x | n=10; count=4; x=8; prime=TRUE; d=3 | — |
| 52 | main | prime ← TRUE | n=10; count=4; x=8; prime=TRUE; d=3 | — |
| 53 | main | d ← 2 | n=10; count=4; x=8; prime=TRUE; d=2 | — |
| 54 | main | WHILE (prime AND ((d * d) ≤ x)) → TRUE | n=10; count=4; x=8; prime=TRUE; d=2 | — |
| 55 | main | IF ((x MOD d) = 0) → TRUE | n=10; count=4; x=8; prime=TRUE; d=2 | — |
| 56 | main | prime ← FALSE | n=10; count=4; x=8; prime=FALSE; d=2 | — |
| 57 | main | d ← (d + 1) | n=10; count=4; x=8; prime=FALSE; d=3 | — |
| 58 | main | WHILE (prime AND ((d * d) ≤ x)) → FALSE | n=10; count=4; x=8; prime=FALSE; d=3 | — |
| 59 | main | IF prime → FALSE | n=10; count=4; x=8; prime=FALSE; d=3 | — |
| 60 | main | FOR visit x | n=10; count=4; x=9; prime=FALSE; d=3 | — |
| 61 | main | prime ← TRUE | n=10; count=4; x=9; prime=TRUE; d=3 | — |
| 62 | main | d ← 2 | n=10; count=4; x=9; prime=TRUE; d=2 | — |
| 63 | main | WHILE (prime AND ((d * d) ≤ x)) → TRUE | n=10; count=4; x=9; prime=TRUE; d=2 | — |
| 64 | main | IF ((x MOD d) = 0) → FALSE | n=10; count=4; x=9; prime=TRUE; d=2 | — |
| 65 | main | d ← (d + 1) | n=10; count=4; x=9; prime=TRUE; d=3 | — |
| 66 | main | WHILE (prime AND ((d * d) ≤ x)) → TRUE | n=10; count=4; x=9; prime=TRUE; d=3 | — |
| 67 | main | IF ((x MOD d) = 0) → TRUE | n=10; count=4; x=9; prime=TRUE; d=3 | — |
| 68 | main | prime ← FALSE | n=10; count=4; x=9; prime=FALSE; d=3 | — |
| 69 | main | d ← (d + 1) | n=10; count=4; x=9; prime=FALSE; d=4 | — |
| 70 | main | WHILE (prime AND ((d * d) ≤ x)) → FALSE | n=10; count=4; x=9; prime=FALSE; d=4 | — |
| 71 | main | IF prime → FALSE | n=10; count=4; x=9; prime=FALSE; d=4 | — |
| 72 | main | FOR visit x | n=10; count=4; x=10; prime=FALSE; d=4 | — |
| 73 | main | prime ← TRUE | n=10; count=4; x=10; prime=TRUE; d=4 | — |
| 74 | main | d ← 2 | n=10; count=4; x=10; prime=TRUE; d=2 | — |
| 75 | main | WHILE (prime AND ((d * d) ≤ x)) → TRUE | n=10; count=4; x=10; prime=TRUE; d=2 | — |
| 76 | main | IF ((x MOD d) = 0) → TRUE | n=10; count=4; x=10; prime=TRUE; d=2 | — |
| 77 | main | prime ← FALSE | n=10; count=4; x=10; prime=FALSE; d=2 | — |
| 78 | main | d ← (d + 1) | n=10; count=4; x=10; prime=FALSE; d=3 | — |
| 79 | main | WHILE (prime AND ((d * d) ≤ x)) → FALSE | n=10; count=4; x=10; prime=FALSE; d=3 | — |
| 80 | main | IF prime → FALSE | n=10; count=4; x=10; prime=FALSE; d=3 | — |
| 81 | main | FOR exit | n=10; count=4; x=10; prime=FALSE; d=3 | — |
| 82 | main | PRINT | n=10; count=4; x=10; prime=FALSE; d=3 | 4 |

**Why it works:** Each candidate gets fresh prime status; primes here are 2,3,5,7.

**Complexity:** O(n sqrt(n)) upper-bound time, O(1) space

**Boundary checks:** n=0 or1→0;n=2→1.

## W030 — Armstrong test

```text
Pseudocode
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
    s ← (s + POWER(digit, digits))
    n ← (n DIV 10)
END WHILE
PRINT (s = original)
```

**Sample output**

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 153 | n=153 | — |
| 2 | main | original ← n | n=153; original=153 | — |
| 3 | main | digits ← 1 | n=153; original=153; digits=1 | — |
| 4 | main | t ← n | n=153; original=153; digits=1; t=153 | — |
| 5 | main | WHILE (t ≥ 10) → TRUE | n=153; original=153; digits=1; t=153 | — |
| 6 | main | digits ← (digits + 1) | n=153; original=153; digits=2; t=153 | — |
| 7 | main | t ← (t DIV 10) | n=153; original=153; digits=2; t=15 | — |
| 8 | main | WHILE (t ≥ 10) → TRUE | n=153; original=153; digits=2; t=15 | — |
| 9 | main | digits ← (digits + 1) | n=153; original=153; digits=3; t=15 | — |
| 10 | main | t ← (t DIV 10) | n=153; original=153; digits=3; t=1 | — |
| 11 | main | WHILE (t ≥ 10) → FALSE | n=153; original=153; digits=3; t=1 | — |
| 12 | main | s ← 0 | n=153; original=153; digits=3; t=1; s=0 | — |
| 13 | main | WHILE (n > 0) → TRUE | n=153; original=153; digits=3; t=1; s=0 | — |
| 14 | main | digit ← (n MOD 10) | n=153; original=153; digits=3; t=1; s=0; digit=3 | — |
| 15 | main | s ← (s + POWER(digit, digits)) | n=153; original=153; digits=3; t=1; s=27; digit=3 | — |
| 16 | main | n ← (n DIV 10) | n=15; original=153; digits=3; t=1; s=27; digit=3 | — |
| 17 | main | WHILE (n > 0) → TRUE | n=15; original=153; digits=3; t=1; s=27; digit=3 | — |
| 18 | main | digit ← (n MOD 10) | n=15; original=153; digits=3; t=1; s=27; digit=5 | — |
| 19 | main | s ← (s + POWER(digit, digits)) | n=15; original=153; digits=3; t=1; s=152; digit=5 | — |
| 20 | main | n ← (n DIV 10) | n=1; original=153; digits=3; t=1; s=152; digit=5 | — |
| 21 | main | WHILE (n > 0) → TRUE | n=1; original=153; digits=3; t=1; s=152; digit=5 | — |
| 22 | main | digit ← (n MOD 10) | n=1; original=153; digits=3; t=1; s=152; digit=1 | — |
| 23 | main | s ← (s + POWER(digit, digits)) | n=1; original=153; digits=3; t=1; s=153; digit=1 | — |
| 24 | main | n ← (n DIV 10) | n=0; original=153; digits=3; t=1; s=153; digit=1 | — |
| 25 | main | WHILE (n > 0) → FALSE | n=0; original=153; digits=3; t=1; s=153; digit=1 | — |
| 26 | main | PRINT | n=0; original=153; digits=3; t=1; s=153; digit=1 | TRUE |

**Why it works:** 153=1³+5³+3³. Preserve input and determine the actual digit count.

**Complexity:** O(d) power operations and O(1) space; power cost depends on implementation

**Boundary checks:** 0 TRUE;10 FALSE;9474 TRUE.

## W031 — Least common multiple

```text
Pseudocode
a ← 12
b ← 18
x ← a
y ← b
WHILE (y ≠ 0)
    r ← (x MOD y)
    x ← y
    y ← r
END WHILE
IF ((a = 0) OR (b = 0)) THEN
    answer ← 0
ELSE
    answer ← ((a DIV x) * b)
END IF
PRINT answer
```

**Sample output**

```text
36
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 12 | a=12 | — |
| 2 | main | b ← 18 | a=12; b=18 | — |
| 3 | main | x ← a | a=12; b=18; x=12 | — |
| 4 | main | y ← b | a=12; b=18; x=12; y=18 | — |
| 5 | main | WHILE (y ≠ 0) → TRUE | a=12; b=18; x=12; y=18 | — |
| 6 | main | r ← (x MOD y) | a=12; b=18; x=12; y=18; r=12 | — |
| 7 | main | x ← y | a=12; b=18; x=18; y=18; r=12 | — |
| 8 | main | y ← r | a=12; b=18; x=18; y=12; r=12 | — |
| 9 | main | WHILE (y ≠ 0) → TRUE | a=12; b=18; x=18; y=12; r=12 | — |
| 10 | main | r ← (x MOD y) | a=12; b=18; x=18; y=12; r=6 | — |
| 11 | main | x ← y | a=12; b=18; x=12; y=12; r=6 | — |
| 12 | main | y ← r | a=12; b=18; x=12; y=6; r=6 | — |
| 13 | main | WHILE (y ≠ 0) → TRUE | a=12; b=18; x=12; y=6; r=6 | — |
| 14 | main | r ← (x MOD y) | a=12; b=18; x=12; y=6; r=0 | — |
| 15 | main | x ← y | a=12; b=18; x=6; y=6; r=0 | — |
| 16 | main | y ← r | a=12; b=18; x=6; y=0; r=0 | — |
| 17 | main | WHILE (y ≠ 0) → FALSE | a=12; b=18; x=6; y=0; r=0 | — |
| 18 | main | IF ((a = 0) OR (b = 0)) → FALSE | a=12; b=18; x=6; y=0; r=0 | — |
| 19 | main | answer ← ((a DIV x) * b) | a=12; b=18; x=6; y=0; r=0; answer=36 | — |
| 20 | main | PRINT | a=12; b=18; x=6; y=0; r=0; answer=36 | 36 |

**Why it works:** Divide by gcd before multiplying; test zero before dividing by gcd.

**Complexity:** O(log(max(a,b)+1)) time, O(1) space

**Boundary checks:** (0,0)→0;(0,5)→0;(7,3)→21.

## W032 — Count triangular visits

```text
Pseudocode
n ← 4
count ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    FOR j ← 1 TO ((i + 1) − 1) STEP 1
        count ← (count + 1)
    END FOR
END FOR
PRINT count
```

**Sample output**

```text
10
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 4 | n=4 | — |
| 2 | main | count ← 0 | n=4; count=0 | — |
| 3 | main | FOR visit i | n=4; count=0; i=1 | — |
| 4 | main | FOR visit j | n=4; count=0; i=1; j=1 | — |
| 5 | main | count ← (count + 1) | n=4; count=1; i=1; j=1 | — |
| 6 | main | FOR exit | n=4; count=1; i=1; j=1 | — |
| 7 | main | FOR visit i | n=4; count=1; i=2; j=1 | — |
| 8 | main | FOR visit j | n=4; count=1; i=2; j=1 | — |
| 9 | main | count ← (count + 1) | n=4; count=2; i=2; j=1 | — |
| 10 | main | FOR visit j | n=4; count=2; i=2; j=2 | — |
| 11 | main | count ← (count + 1) | n=4; count=3; i=2; j=2 | — |
| 12 | main | FOR exit | n=4; count=3; i=2; j=2 | — |
| 13 | main | FOR visit i | n=4; count=3; i=3; j=2 | — |
| 14 | main | FOR visit j | n=4; count=3; i=3; j=1 | — |
| 15 | main | count ← (count + 1) | n=4; count=4; i=3; j=1 | — |
| 16 | main | FOR visit j | n=4; count=4; i=3; j=2 | — |
| 17 | main | count ← (count + 1) | n=4; count=5; i=3; j=2 | — |
| 18 | main | FOR visit j | n=4; count=5; i=3; j=3 | — |
| 19 | main | count ← (count + 1) | n=4; count=6; i=3; j=3 | — |
| 20 | main | FOR exit | n=4; count=6; i=3; j=3 | — |
| 21 | main | FOR visit i | n=4; count=6; i=4; j=3 | — |
| 22 | main | FOR visit j | n=4; count=6; i=4; j=1 | — |
| 23 | main | count ← (count + 1) | n=4; count=7; i=4; j=1 | — |
| 24 | main | FOR visit j | n=4; count=7; i=4; j=2 | — |
| 25 | main | count ← (count + 1) | n=4; count=8; i=4; j=2 | — |
| 26 | main | FOR visit j | n=4; count=8; i=4; j=3 | — |
| 27 | main | count ← (count + 1) | n=4; count=9; i=4; j=3 | — |
| 28 | main | FOR visit j | n=4; count=9; i=4; j=4 | — |
| 29 | main | count ← (count + 1) | n=4; count=10; i=4; j=4 | — |
| 30 | main | FOR exit | n=4; count=10; i=4; j=4 | — |
| 31 | main | FOR exit | n=4; count=10; i=4; j=4 | — |
| 32 | main | PRINT | n=4; count=10; i=4; j=4 | 10 |

**Why it works:** Row i contributes i; verify with n(n+1)/2.

**Complexity:** O(n²) time, O(1) space

**Boundary checks:** n=0→0;n=1→1.

## W033 — Rows of stars

```text
Pseudocode
n ← 3
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    row ← ""
    FOR j ← 0 TO (i − 1) STEP 1
        row ← (row + "*")
    END FOR
    PRINT row
END FOR
```

**Sample output**

```text
*
**
***
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 3 | n=3 | — |
| 2 | main | FOR visit i | n=3; i=1 | — |
| 3 | main | row ← "" | n=3; i=1; row= | — |
| 4 | main | FOR visit j | n=3; i=1; row=; j=0 | — |
| 5 | main | row ← (row + "*") | n=3; i=1; row=*; j=0 | — |
| 6 | main | FOR exit | n=3; i=1; row=*; j=0 | — |
| 7 | main | PRINT | n=3; i=1; row=*; j=0 | * |
| 8 | main | FOR visit i | n=3; i=2; row=*; j=0 | — |
| 9 | main | row ← "" | n=3; i=2; row=; j=0 | — |
| 10 | main | FOR visit j | n=3; i=2; row=; j=0 | — |
| 11 | main | row ← (row + "*") | n=3; i=2; row=*; j=0 | — |
| 12 | main | FOR visit j | n=3; i=2; row=*; j=1 | — |
| 13 | main | row ← (row + "*") | n=3; i=2; row=**; j=1 | — |
| 14 | main | FOR exit | n=3; i=2; row=**; j=1 | — |
| 15 | main | PRINT | n=3; i=2; row=**; j=1 | ** |
| 16 | main | FOR visit i | n=3; i=3; row=**; j=1 | — |
| 17 | main | row ← "" | n=3; i=3; row=; j=1 | — |
| 18 | main | FOR visit j | n=3; i=3; row=; j=0 | — |
| 19 | main | row ← (row + "*") | n=3; i=3; row=*; j=0 | — |
| 20 | main | FOR visit j | n=3; i=3; row=*; j=1 | — |
| 21 | main | row ← (row + "*") | n=3; i=3; row=**; j=1 | — |
| 22 | main | FOR visit j | n=3; i=3; row=**; j=2 | — |
| 23 | main | row ← (row + "*") | n=3; i=3; row=***; j=2 | — |
| 24 | main | FOR exit | n=3; i=3; row=***; j=2 | — |
| 25 | main | PRINT | n=3; i=3; row=***; j=2 | *** |
| 26 | main | FOR exit | n=3; i=3; row=***; j=2 | — |

**Why it works:** Reset row for every outer iteration; the inner loop controls its length.

**Complexity:** O(n²) characters output; immutable concatenation can cost O(n³) total copying; O(n) row space

**Boundary checks:** n=0 prints no lines; n=1 prints *.

## W034 — Matrix sum

```text
Pseudocode
M ← [[1, 2, 3], [4, 5, 6]]
s ← 0
FOR r ← 0 TO (LENGTH(M) − 1) STEP 1
    FOR c ← 0 TO (LENGTH(M[r]) − 1) STEP 1
        s ← (s + M[r][c])
    END FOR
END FOR
PRINT s
```

**Sample output**

```text
21
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | M ← [[1, 2, 3], [4, 5, 6]] | M=[[1, 2, 3], [4, 5, 6]] | — |
| 2 | main | s ← 0 | M=[[1, 2, 3], [4, 5, 6]]; s=0 | — |
| 3 | main | FOR visit r | M=[[1, 2, 3], [4, 5, 6]]; s=0; r=0 | — |
| 4 | main | FOR visit c | M=[[1, 2, 3], [4, 5, 6]]; s=0; r=0; c=0 | — |
| 5 | main | s ← (s + M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; s=1; r=0; c=0 | — |
| 6 | main | FOR visit c | M=[[1, 2, 3], [4, 5, 6]]; s=1; r=0; c=1 | — |
| 7 | main | s ← (s + M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; s=3; r=0; c=1 | — |
| 8 | main | FOR visit c | M=[[1, 2, 3], [4, 5, 6]]; s=3; r=0; c=2 | — |
| 9 | main | s ← (s + M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; s=6; r=0; c=2 | — |
| 10 | main | FOR exit | M=[[1, 2, 3], [4, 5, 6]]; s=6; r=0; c=2 | — |
| 11 | main | FOR visit r | M=[[1, 2, 3], [4, 5, 6]]; s=6; r=1; c=2 | — |
| 12 | main | FOR visit c | M=[[1, 2, 3], [4, 5, 6]]; s=6; r=1; c=0 | — |
| 13 | main | s ← (s + M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; s=10; r=1; c=0 | — |
| 14 | main | FOR visit c | M=[[1, 2, 3], [4, 5, 6]]; s=10; r=1; c=1 | — |
| 15 | main | s ← (s + M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; s=15; r=1; c=1 | — |
| 16 | main | FOR visit c | M=[[1, 2, 3], [4, 5, 6]]; s=15; r=1; c=2 | — |
| 17 | main | s ← (s + M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; s=21; r=1; c=2 | — |
| 18 | main | FOR exit | M=[[1, 2, 3], [4, 5, 6]]; s=21; r=1; c=2 | — |
| 19 | main | FOR exit | M=[[1, 2, 3], [4, 5, 6]]; s=21; r=1; c=2 | — |
| 20 | main | PRINT | M=[[1, 2, 3], [4, 5, 6]]; s=21; r=1; c=2 | 21 |

**Why it works:** Use each row length for columns; every cell contributes once.

**Complexity:** O(rows*cols) time, O(1) space

**Boundary checks:** [[]]→0;[[7]]→7.

## W035 — Main diagonal sum

```text
Pseudocode
M ← [[1, 2], [3, 4]]
s ← 0
FOR i ← 0 TO (LENGTH(M) − 1) STEP 1
    s ← (s + M[i][i])
END FOR
PRINT s
```

**Sample output**

```text
5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | M ← [[1, 2], [3, 4]] | M=[[1, 2], [3, 4]] | — |
| 2 | main | s ← 0 | M=[[1, 2], [3, 4]]; s=0 | — |
| 3 | main | FOR visit i | M=[[1, 2], [3, 4]]; s=0; i=0 | — |
| 4 | main | s ← (s + M[i][i]) | M=[[1, 2], [3, 4]]; s=1; i=0 | — |
| 5 | main | FOR visit i | M=[[1, 2], [3, 4]]; s=1; i=1 | — |
| 6 | main | s ← (s + M[i][i]) | M=[[1, 2], [3, 4]]; s=5; i=1 | — |
| 7 | main | FOR exit | M=[[1, 2], [3, 4]]; s=5; i=1 | — |
| 8 | main | PRINT | M=[[1, 2], [3, 4]]; s=5; i=1 | 5 |

**Why it works:** Main diagonal coordinates have equal row and column indices.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** []→0;[[9]]→9; reject nonsquare input.

## W036 — Transpose a rectangle

```text
Pseudocode
M ← [[1, 2, 3], [4, 5, 6]]
T ← []
FOR c ← 0 TO (LENGTH(M[0]) − 1) STEP 1
    row ← []
    FOR r ← 0 TO (LENGTH(M) − 1) STEP 1
        APPEND(row, M[r][c])
    END FOR
    APPEND(T, row)
END FOR
PRINT T
```

**Sample output**

```text
[[1, 4], [2, 5], [3, 6]]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | M ← [[1, 2, 3], [4, 5, 6]] | M=[[1, 2, 3], [4, 5, 6]] | — |
| 2 | main | T ← [] | M=[[1, 2, 3], [4, 5, 6]]; T=[] | — |
| 3 | main | FOR visit c | M=[[1, 2, 3], [4, 5, 6]]; T=[]; c=0 | — |
| 4 | main | row ← [] | M=[[1, 2, 3], [4, 5, 6]]; T=[]; c=0; row=[] | — |
| 5 | main | FOR visit r | M=[[1, 2, 3], [4, 5, 6]]; T=[]; c=0; row=[]; r=0 | — |
| 6 | main | APPEND(row, M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; T=[]; c=0; row=[1]; r=0 | — |
| 7 | main | FOR visit r | M=[[1, 2, 3], [4, 5, 6]]; T=[]; c=0; row=[1]; r=1 | — |
| 8 | main | APPEND(row, M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; T=[]; c=0; row=[1, 4]; r=1 | — |
| 9 | main | FOR exit | M=[[1, 2, 3], [4, 5, 6]]; T=[]; c=0; row=[1, 4]; r=1 | — |
| 10 | main | APPEND(T, row) | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4]]; c=0; row=[1, 4]; r=1 | — |
| 11 | main | FOR visit c | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4]]; c=1; row=[1, 4]; r=1 | — |
| 12 | main | row ← [] | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4]]; c=1; row=[]; r=1 | — |
| 13 | main | FOR visit r | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4]]; c=1; row=[]; r=0 | — |
| 14 | main | APPEND(row, M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4]]; c=1; row=[2]; r=0 | — |
| 15 | main | FOR visit r | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4]]; c=1; row=[2]; r=1 | — |
| 16 | main | APPEND(row, M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4]]; c=1; row=[2, 5]; r=1 | — |
| 17 | main | FOR exit | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4]]; c=1; row=[2, 5]; r=1 | — |
| 18 | main | APPEND(T, row) | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5]]; c=1; row=[2, 5]; r=1 | — |
| 19 | main | FOR visit c | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5]]; c=2; row=[2, 5]; r=1 | — |
| 20 | main | row ← [] | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5]]; c=2; row=[]; r=1 | — |
| 21 | main | FOR visit r | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5]]; c=2; row=[]; r=0 | — |
| 22 | main | APPEND(row, M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5]]; c=2; row=[3]; r=0 | — |
| 23 | main | FOR visit r | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5]]; c=2; row=[3]; r=1 | — |
| 24 | main | APPEND(row, M[r][c]) | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5]]; c=2; row=[3, 6]; r=1 | — |
| 25 | main | FOR exit | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5]]; c=2; row=[3, 6]; r=1 | — |
| 26 | main | APPEND(T, row) | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5], [3, 6]]; c=2; row=[3, 6]; r=1 | — |
| 27 | main | FOR exit | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5], [3, 6]]; c=2; row=[3, 6]; r=1 | — |
| 28 | main | PRINT | M=[[1, 2, 3], [4, 5, 6]]; T=[[1, 4], [2, 5], [3, 6]]; c=2; row=[3, 6]; r=1 | [[1, 4], [2, 5], [3, 6]] |

**Why it works:** One output row is one original column; allocate each output row separately.

**Complexity:** O(rc) time, O(rc) output space

**Boundary checks:** [[7]]→[[7]]; [[1,2]]→[[1],[2]].

## W037 — Bubble sort

```text
Pseudocode
A ← [3, 1, 2]
FOR end ← (LENGTH(A) − 1) TO (0 + 1) STEP (−1)
    FOR j ← 0 TO (end − 1) STEP 1
        IF (A[j] > A[(j + 1)]) THEN
            temp ← A[j]
            A[j] ← A[(j + 1)]
            A[(j + 1)] ← temp
        END IF
    END FOR
END FOR
PRINT A
```

**Sample output**

```text
[1, 2, 3]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [3, 1, 2] | A=[3, 1, 2] | — |
| 2 | main | FOR visit end | A=[3, 1, 2]; end=2 | — |
| 3 | main | FOR visit j | A=[3, 1, 2]; end=2; j=0 | — |
| 4 | main | IF (A[j] > A[(j + 1)]) → TRUE | A=[3, 1, 2]; end=2; j=0 | — |
| 5 | main | temp ← A[j] | A=[3, 1, 2]; end=2; j=0; temp=3 | — |
| 6 | main | A[j] ← A[(j + 1)] | A=[1, 1, 2]; end=2; j=0; temp=3 | — |
| 7 | main | A[(j + 1)] ← temp | A=[1, 3, 2]; end=2; j=0; temp=3 | — |
| 8 | main | FOR visit j | A=[1, 3, 2]; end=2; j=1; temp=3 | — |
| 9 | main | IF (A[j] > A[(j + 1)]) → TRUE | A=[1, 3, 2]; end=2; j=1; temp=3 | — |
| 10 | main | temp ← A[j] | A=[1, 3, 2]; end=2; j=1; temp=3 | — |
| 11 | main | A[j] ← A[(j + 1)] | A=[1, 2, 2]; end=2; j=1; temp=3 | — |
| 12 | main | A[(j + 1)] ← temp | A=[1, 2, 3]; end=2; j=1; temp=3 | — |
| 13 | main | FOR exit | A=[1, 2, 3]; end=2; j=1; temp=3 | — |
| 14 | main | FOR visit end | A=[1, 2, 3]; end=1; j=1; temp=3 | — |
| 15 | main | FOR visit j | A=[1, 2, 3]; end=1; j=0; temp=3 | — |
| 16 | main | IF (A[j] > A[(j + 1)]) → FALSE | A=[1, 2, 3]; end=1; j=0; temp=3 | — |
| 17 | main | FOR exit | A=[1, 2, 3]; end=1; j=0; temp=3 | — |
| 18 | main | FOR exit | A=[1, 2, 3]; end=1; j=0; temp=3 | — |
| 19 | main | PRINT | A=[1, 2, 3]; end=1; j=0; temp=3 | [1, 2, 3] |

**Why it works:** Each pass settles the greatest remaining element at end; j+1 is always valid.

**Complexity:** O(n²) time, O(1) space

**Boundary checks:** []→[];[2,2,1]→[1,2,2].

## W038 — Selection sort

```text
Pseudocode
A ← [4, 2, 3, 1]
FOR i ← 0 TO ((LENGTH(A) − 1) − 1) STEP 1
    best ← i
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

**Sample output**

```text
[1, 2, 3, 4]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [4, 2, 3, 1] | A=[4, 2, 3, 1] | — |
| 2 | main | FOR visit i | A=[4, 2, 3, 1]; i=0 | — |
| 3 | main | best ← i | A=[4, 2, 3, 1]; i=0; best=0 | — |
| 4 | main | FOR visit j | A=[4, 2, 3, 1]; i=0; best=0; j=1 | — |
| 5 | main | IF (A[j] < A[best]) → TRUE | A=[4, 2, 3, 1]; i=0; best=0; j=1 | — |
| 6 | main | best ← j | A=[4, 2, 3, 1]; i=0; best=1; j=1 | — |
| 7 | main | FOR visit j | A=[4, 2, 3, 1]; i=0; best=1; j=2 | — |
| 8 | main | IF (A[j] < A[best]) → FALSE | A=[4, 2, 3, 1]; i=0; best=1; j=2 | — |
| 9 | main | FOR visit j | A=[4, 2, 3, 1]; i=0; best=1; j=3 | — |
| 10 | main | IF (A[j] < A[best]) → TRUE | A=[4, 2, 3, 1]; i=0; best=1; j=3 | — |
| 11 | main | best ← j | A=[4, 2, 3, 1]; i=0; best=3; j=3 | — |
| 12 | main | FOR exit | A=[4, 2, 3, 1]; i=0; best=3; j=3 | — |
| 13 | main | temp ← A[i] | A=[4, 2, 3, 1]; i=0; best=3; j=3; temp=4 | — |
| 14 | main | A[i] ← A[best] | A=[1, 2, 3, 1]; i=0; best=3; j=3; temp=4 | — |
| 15 | main | A[best] ← temp | A=[1, 2, 3, 4]; i=0; best=3; j=3; temp=4 | — |
| 16 | main | FOR visit i | A=[1, 2, 3, 4]; i=1; best=3; j=3; temp=4 | — |
| 17 | main | best ← i | A=[1, 2, 3, 4]; i=1; best=1; j=3; temp=4 | — |
| 18 | main | FOR visit j | A=[1, 2, 3, 4]; i=1; best=1; j=2; temp=4 | — |
| 19 | main | IF (A[j] < A[best]) → FALSE | A=[1, 2, 3, 4]; i=1; best=1; j=2; temp=4 | — |
| 20 | main | FOR visit j | A=[1, 2, 3, 4]; i=1; best=1; j=3; temp=4 | — |
| 21 | main | IF (A[j] < A[best]) → FALSE | A=[1, 2, 3, 4]; i=1; best=1; j=3; temp=4 | — |
| 22 | main | FOR exit | A=[1, 2, 3, 4]; i=1; best=1; j=3; temp=4 | — |
| 23 | main | temp ← A[i] | A=[1, 2, 3, 4]; i=1; best=1; j=3; temp=2 | — |
| 24 | main | A[i] ← A[best] | A=[1, 2, 3, 4]; i=1; best=1; j=3; temp=2 | — |
| 25 | main | A[best] ← temp | A=[1, 2, 3, 4]; i=1; best=1; j=3; temp=2 | — |
| 26 | main | FOR visit i | A=[1, 2, 3, 4]; i=2; best=1; j=3; temp=2 | — |
| 27 | main | best ← i | A=[1, 2, 3, 4]; i=2; best=2; j=3; temp=2 | — |
| 28 | main | FOR visit j | A=[1, 2, 3, 4]; i=2; best=2; j=3; temp=2 | — |
| 29 | main | IF (A[j] < A[best]) → FALSE | A=[1, 2, 3, 4]; i=2; best=2; j=3; temp=2 | — |
| 30 | main | FOR exit | A=[1, 2, 3, 4]; i=2; best=2; j=3; temp=2 | — |
| 31 | main | temp ← A[i] | A=[1, 2, 3, 4]; i=2; best=2; j=3; temp=3 | — |
| 32 | main | A[i] ← A[best] | A=[1, 2, 3, 4]; i=2; best=2; j=3; temp=3 | — |
| 33 | main | A[best] ← temp | A=[1, 2, 3, 4]; i=2; best=2; j=3; temp=3 | — |
| 34 | main | FOR exit | A=[1, 2, 3, 4]; i=2; best=2; j=3; temp=3 | — |
| 35 | main | PRINT | A=[1, 2, 3, 4]; i=2; best=2; j=3; temp=3 | [1, 2, 3, 4] |

**Why it works:** The sorted prefix grows by one minimum per pass; reset best to i each pass.

**Complexity:** O(n²) time, O(1) space

**Boundary checks:** empty and singleton skip loops; duplicates remain present.

## W039 — Binary search

```text
Pseudocode
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
        lo ← (mid + 1)
    ELSE
        hi ← (mid − 1)
    END IF
END WHILE
PRINT found
```

**Sample output**

```text
3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [2, 5, 8, 11] | A=[2, 5, 8, 11] | — |
| 2 | main | target ← 11 | A=[2, 5, 8, 11]; target=11 | — |
| 3 | main | lo ← 0 | A=[2, 5, 8, 11]; target=11; lo=0 | — |
| 4 | main | hi ← (LENGTH(A) − 1) | A=[2, 5, 8, 11]; target=11; lo=0; hi=3 | — |
| 5 | main | found ← (−1) | A=[2, 5, 8, 11]; target=11; lo=0; hi=3; found=-1 | — |
| 6 | main | WHILE (lo ≤ hi) → TRUE | A=[2, 5, 8, 11]; target=11; lo=0; hi=3; found=-1 | — |
| 7 | main | mid ← (lo + ((hi − lo) DIV 2)) | A=[2, 5, 8, 11]; target=11; lo=0; hi=3; found=-1; mid=1 | — |
| 8 | main | IF (A[mid] = target) → FALSE | A=[2, 5, 8, 11]; target=11; lo=0; hi=3; found=-1; mid=1 | — |
| 9 | main | IF (A[mid] < target) → TRUE | A=[2, 5, 8, 11]; target=11; lo=0; hi=3; found=-1; mid=1 | — |
| 10 | main | lo ← (mid + 1) | A=[2, 5, 8, 11]; target=11; lo=2; hi=3; found=-1; mid=1 | — |
| 11 | main | WHILE (lo ≤ hi) → TRUE | A=[2, 5, 8, 11]; target=11; lo=2; hi=3; found=-1; mid=1 | — |
| 12 | main | mid ← (lo + ((hi − lo) DIV 2)) | A=[2, 5, 8, 11]; target=11; lo=2; hi=3; found=-1; mid=2 | — |
| 13 | main | IF (A[mid] = target) → FALSE | A=[2, 5, 8, 11]; target=11; lo=2; hi=3; found=-1; mid=2 | — |
| 14 | main | IF (A[mid] < target) → TRUE | A=[2, 5, 8, 11]; target=11; lo=2; hi=3; found=-1; mid=2 | — |
| 15 | main | lo ← (mid + 1) | A=[2, 5, 8, 11]; target=11; lo=3; hi=3; found=-1; mid=2 | — |
| 16 | main | WHILE (lo ≤ hi) → TRUE | A=[2, 5, 8, 11]; target=11; lo=3; hi=3; found=-1; mid=2 | — |
| 17 | main | mid ← (lo + ((hi − lo) DIV 2)) | A=[2, 5, 8, 11]; target=11; lo=3; hi=3; found=-1; mid=3 | — |
| 18 | main | IF (A[mid] = target) → TRUE | A=[2, 5, 8, 11]; target=11; lo=3; hi=3; found=-1; mid=3 | — |
| 19 | main | found ← mid | A=[2, 5, 8, 11]; target=11; lo=3; hi=3; found=3; mid=3 | — |
| 20 | main | BREAK | A=[2, 5, 8, 11]; target=11; lo=3; hi=3; found=3; mid=3 | — |
| 21 | main | PRINT | A=[2, 5, 8, 11]; target=11; lo=3; hi=3; found=3; mid=3 | 3 |

**Why it works:** Every comparison discards mid and one impossible half. Empty intervals terminate.

**Complexity:** O(log(n+1)) time, O(1) space

**Boundary checks:** []→-1; missing 6→-1; duplicates may return any matching index.

## W040 — Recursive factorial

```text
Pseudocode
FUNCTION fact(n)
    IF (n ≤ 1) THEN
        RETURN 1
    END IF
    RETURN (n * fact((n − 1)))
END FUNCTION
PRINT fact(4)
```

**Sample output**

```text
24
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | fact depth 1 | ENTER | n=4 | — |
| 2 | fact depth 1 | IF (n ≤ 1) → FALSE | n=4 | — |
| 3 | fact depth 2 | ENTER | n=3 | — |
| 4 | fact depth 2 | IF (n ≤ 1) → FALSE | n=3 | — |
| 5 | fact depth 3 | ENTER | n=2 | — |
| 6 | fact depth 3 | IF (n ≤ 1) → FALSE | n=2 | — |
| 7 | fact depth 4 | ENTER | n=1 | — |
| 8 | fact depth 4 | IF (n ≤ 1) → TRUE | n=1 | — |
| 9 | fact depth 4 | RETURN 1 | n=1 | — |
| 10 | fact depth 3 | RETURN 2 | n=2 | — |
| 11 | fact depth 2 | RETURN 6 | n=3 | — |
| 12 | fact depth 1 | RETURN 24 | n=4 | — |
| 13 | main | PRINT | — | 24 |

**Why it works:** Calls shrink to base 1, then pending multiplications execute on return.

**Complexity:** O(n) time and O(n) stack

**Boundary checks:** fact(0)=1;fact(1)=1; reject negatives at the input boundary.

## W041 — Recursive digit sum

```text
Pseudocode
FUNCTION digits(n)
    IF (n = 0) THEN
        RETURN 0
    END IF
    RETURN ((n MOD 10) + digits((n DIV 10)))
END FUNCTION
PRINT digits(204)
```

**Sample output**

```text
6
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | digits depth 1 | ENTER | n=204 | — |
| 2 | digits depth 1 | IF (n = 0) → FALSE | n=204 | — |
| 3 | digits depth 2 | ENTER | n=20 | — |
| 4 | digits depth 2 | IF (n = 0) → FALSE | n=20 | — |
| 5 | digits depth 3 | ENTER | n=2 | — |
| 6 | digits depth 3 | IF (n = 0) → FALSE | n=2 | — |
| 7 | digits depth 4 | ENTER | n=0 | — |
| 8 | digits depth 4 | IF (n = 0) → TRUE | n=0 | — |
| 9 | digits depth 4 | RETURN 0 | n=0 | — |
| 10 | digits depth 3 | RETURN 2 | n=2 | — |
| 11 | digits depth 2 | RETURN 2 | n=20 | — |
| 12 | digits depth 1 | RETURN 6 | n=204 | — |
| 13 | main | PRINT | — | 6 |

**Why it works:** The final digit plus digit sum of remaining prefix reconstructs the answer.

**Complexity:** O(d) time and stack

**Boundary checks:** 0→0;10→1.

## W042 — Recursive GCD

```text
Pseudocode
FUNCTION gcd(a, b)
    IF (b = 0) THEN
        RETURN a
    END IF
    RETURN gcd(b, (a MOD b))
END FUNCTION
PRINT gcd(81, 27)
```

**Sample output**

```text
27
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | gcd depth 1 | ENTER | a=81; b=27 | — |
| 2 | gcd depth 1 | IF (b = 0) → FALSE | a=81; b=27 | — |
| 3 | gcd depth 2 | ENTER | a=27; b=0 | — |
| 4 | gcd depth 2 | IF (b = 0) → TRUE | a=27; b=0 | — |
| 5 | gcd depth 2 | RETURN 27 | a=27; b=0 | — |
| 6 | gcd depth 1 | RETURN 27 | a=81; b=27 | — |
| 7 | main | PRINT | — | 27 |

**Why it works:** The second parameter strictly decreases until zero.

**Complexity:** O(log(max(a,b)+1)) time and stack

**Boundary checks:** (0,0)→0;(15,0)→15.

## W043 — Recursive palindrome

```text
Pseudocode
FUNCTION pal(s, l, r)
    IF (l ≥ r) THEN
        RETURN TRUE
    END IF
    IF (s[l] ≠ s[r]) THEN
        RETURN FALSE
    END IF
    RETURN pal(s, (l + 1), (r − 1))
END FUNCTION
s ← "radar"
PRINT pal(s, 0, (LENGTH(s) − 1))
```

**Sample output**

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "radar" | s=radar | — |
| 2 | pal depth 1 | ENTER | s=radar; l=0; r=4 | — |
| 3 | pal depth 1 | IF (l ≥ r) → FALSE | s=radar; l=0; r=4 | — |
| 4 | pal depth 1 | IF (s[l] ≠ s[r]) → FALSE | s=radar; l=0; r=4 | — |
| 5 | pal depth 2 | ENTER | s=radar; l=1; r=3 | — |
| 6 | pal depth 2 | IF (l ≥ r) → FALSE | s=radar; l=1; r=3 | — |
| 7 | pal depth 2 | IF (s[l] ≠ s[r]) → FALSE | s=radar; l=1; r=3 | — |
| 8 | pal depth 3 | ENTER | s=radar; l=2; r=2 | — |
| 9 | pal depth 3 | IF (l ≥ r) → TRUE | s=radar; l=2; r=2 | — |
| 10 | pal depth 3 | RETURN TRUE | s=radar; l=2; r=2 | — |
| 11 | pal depth 2 | RETURN TRUE | s=radar; l=1; r=3 | — |
| 12 | pal depth 1 | RETURN TRUE | s=radar; l=0; r=4 | — |
| 13 | main | PRINT | s=radar | TRUE |

**Why it works:** Base handles empty/center; mismatches return immediately; otherwise reduce interval.

**Complexity:** O(n) time and stack

**Boundary checks:** empty TRUE;"ab" FALSE.

## W044 — Fast exponentiation

```text
Pseudocode
base ← 3
exp ← 5
result ← 1
WHILE (exp > 0)
    IF ((exp MOD 2) = 1) THEN
        result ← (result * base)
    END IF
    base ← (base * base)
    exp ← (exp DIV 2)
END WHILE
PRINT result
```

**Sample output**

```text
243
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | base ← 3 | base=3 | — |
| 2 | main | exp ← 5 | base=3; exp=5 | — |
| 3 | main | result ← 1 | base=3; exp=5; result=1 | — |
| 4 | main | WHILE (exp > 0) → TRUE | base=3; exp=5; result=1 | — |
| 5 | main | IF ((exp MOD 2) = 1) → TRUE | base=3; exp=5; result=1 | — |
| 6 | main | result ← (result * base) | base=3; exp=5; result=3 | — |
| 7 | main | base ← (base * base) | base=9; exp=5; result=3 | — |
| 8 | main | exp ← (exp DIV 2) | base=9; exp=2; result=3 | — |
| 9 | main | WHILE (exp > 0) → TRUE | base=9; exp=2; result=3 | — |
| 10 | main | IF ((exp MOD 2) = 1) → FALSE | base=9; exp=2; result=3 | — |
| 11 | main | base ← (base * base) | base=81; exp=2; result=3 | — |
| 12 | main | exp ← (exp DIV 2) | base=81; exp=1; result=3 | — |
| 13 | main | WHILE (exp > 0) → TRUE | base=81; exp=1; result=3 | — |
| 14 | main | IF ((exp MOD 2) = 1) → TRUE | base=81; exp=1; result=3 | — |
| 15 | main | result ← (result * base) | base=81; exp=1; result=243 | — |
| 16 | main | base ← (base * base) | base=6561; exp=1; result=243 | — |
| 17 | main | exp ← (exp DIV 2) | base=6561; exp=0; result=243 | — |
| 18 | main | WHILE (exp > 0) → FALSE | base=6561; exp=0; result=243 | — |
| 19 | main | PRINT | base=6561; exp=0; result=243 | 243 |

**Why it works:** Consume exponent bits: an odd bit contributes the current power; squaring prepares the next bit.

**Complexity:** O(log(exp+1)) multiplications, O(1) space

**Boundary checks:** exp=0→1;base=0,exp>0→0;negative base works.

## W045 — Set-bit count

```text
Pseudocode
x ← 13
count ← 0
WHILE (x > 0)
    x ← (x BIT_AND (x − 1))
    count ← (count + 1)
END WHILE
PRINT count
```

**Sample output**

```text
3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 13 | x=13 | — |
| 2 | main | count ← 0 | x=13; count=0 | — |
| 3 | main | WHILE (x > 0) → TRUE | x=13; count=0 | — |
| 4 | main | x ← (x BIT_AND (x − 1)) | x=12; count=0 | — |
| 5 | main | count ← (count + 1) | x=12; count=1 | — |
| 6 | main | WHILE (x > 0) → TRUE | x=12; count=1 | — |
| 7 | main | x ← (x BIT_AND (x − 1)) | x=8; count=1 | — |
| 8 | main | count ← (count + 1) | x=8; count=2 | — |
| 9 | main | WHILE (x > 0) → TRUE | x=8; count=2 | — |
| 10 | main | x ← (x BIT_AND (x − 1)) | x=0; count=2 | — |
| 11 | main | count ← (count + 1) | x=0; count=3 | — |
| 12 | main | WHILE (x > 0) → FALSE | x=0; count=3 | — |
| 13 | main | PRINT | x=0; count=3 | 3 |

**Why it works:** Each iteration clears precisely the lowest set bit.

**Complexity:** O(k) time for k set bits, O(1) space

**Boundary checks:** 0→0;8→1;255→8.

## W046 — Power of two

```text
Pseudocode
x ← 16
answer ← ((x > 0) AND ((x BIT_AND (x − 1)) = 0))
PRINT answer
```

**Sample output**

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 16 | x=16 | — |
| 2 | main | answer ← ((x > 0) AND ((x BIT_AND (x − 1)) = 0)) | x=16; answer=TRUE | — |
| 3 | main | PRINT | x=16; answer=TRUE | TRUE |

**Why it works:** Only positive values with exactly one set bit pass both tests.

**Complexity:** O(1) time and space in the unit-cost model

**Boundary checks:** 0 FALSE;1 TRUE;12 FALSE.

## W047 — Unique unpaired element

```text
Pseudocode
A ← [4, 1, 4, 7, 1]
answer ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    answer ← (answer BIT_XOR A[i])
END FOR
PRINT answer
```

**Sample output**

```text
7
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [4, 1, 4, 7, 1] | A=[4, 1, 4, 7, 1] | — |
| 2 | main | answer ← 0 | A=[4, 1, 4, 7, 1]; answer=0 | — |
| 3 | main | FOR visit i | A=[4, 1, 4, 7, 1]; answer=0; i=0 | — |
| 4 | main | answer ← (answer BIT_XOR A[i]) | A=[4, 1, 4, 7, 1]; answer=4; i=0 | — |
| 5 | main | FOR visit i | A=[4, 1, 4, 7, 1]; answer=4; i=1 | — |
| 6 | main | answer ← (answer BIT_XOR A[i]) | A=[4, 1, 4, 7, 1]; answer=5; i=1 | — |
| 7 | main | FOR visit i | A=[4, 1, 4, 7, 1]; answer=5; i=2 | — |
| 8 | main | answer ← (answer BIT_XOR A[i]) | A=[4, 1, 4, 7, 1]; answer=1; i=2 | — |
| 9 | main | FOR visit i | A=[4, 1, 4, 7, 1]; answer=1; i=3 | — |
| 10 | main | answer ← (answer BIT_XOR A[i]) | A=[4, 1, 4, 7, 1]; answer=6; i=3 | — |
| 11 | main | FOR visit i | A=[4, 1, 4, 7, 1]; answer=6; i=4 | — |
| 12 | main | answer ← (answer BIT_XOR A[i]) | A=[4, 1, 4, 7, 1]; answer=7; i=4 | — |
| 13 | main | FOR exit | A=[4, 1, 4, 7, 1]; answer=7; i=4 | — |
| 14 | main | PRINT | A=[4, 1, 4, 7, 1]; answer=7; i=4 | 7 |

**Why it works:** Equal values cancel under XOR; order does not matter. The multiplicity promise is essential.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** [0]→0;[2,2,5]→5; do not use without the promise.

## W048 — Toggle a selected bit

```text
Pseudocode
x ← 10
k ← 1
mask ← (1 SHL k)
answer ← (x BIT_XOR mask)
PRINT answer
```

**Sample output**

```text
8
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 10 | x=10 | — |
| 2 | main | k ← 1 | x=10; k=1 | — |
| 3 | main | mask ← (1 SHL k) | x=10; k=1; mask=2 | — |
| 4 | main | answer ← (x BIT_XOR mask) | x=10; k=1; mask=2; answer=8 | — |
| 5 | main | PRINT | x=10; k=1; mask=2; answer=8 | 8 |

**Why it works:** XOR with a one-bit mask flips just that bit. 1010 XOR 0010=1000.

**Complexity:** O(1) time and space in the unit-cost model

**Boundary checks:** x=0,k=3→8; toggling twice restores x.

## W049 — Prefix sums

```text
Pseudocode
A ← [2, (−1), 4]
P ← [0]
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    APPEND(P, (P[i] + A[i]))
END FOR
PRINT P
```

**Sample output**

```text
[0, 2, 1, 5]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [2, (−1), 4] | A=[2, -1, 4] | — |
| 2 | main | P ← [0] | A=[2, -1, 4]; P=[0] | — |
| 3 | main | FOR visit i | A=[2, -1, 4]; P=[0]; i=0 | — |
| 4 | main | APPEND(P, (P[i] + A[i])) | A=[2, -1, 4]; P=[0, 2]; i=0 | — |
| 5 | main | FOR visit i | A=[2, -1, 4]; P=[0, 2]; i=1 | — |
| 6 | main | APPEND(P, (P[i] + A[i])) | A=[2, -1, 4]; P=[0, 2, 1]; i=1 | — |
| 7 | main | FOR visit i | A=[2, -1, 4]; P=[0, 2, 1]; i=2 | — |
| 8 | main | APPEND(P, (P[i] + A[i])) | A=[2, -1, 4]; P=[0, 2, 1, 5]; i=2 | — |
| 9 | main | FOR exit | A=[2, -1, 4]; P=[0, 2, 1, 5]; i=2 | — |
| 10 | main | PRINT | A=[2, -1, 4]; P=[0, 2, 1, 5]; i=2 | [0, 2, 1, 5] |

**Why it works:** P[i] already sums the first i elements; adding A[i] extends by one.

**Complexity:** O(n) time, O(n) output space

**Boundary checks:** []→[0]; range sum A[l..r]=P[r+1]-P[l].

## W050 — Fixed-window maximum sum

```text
Pseudocode
A ← [2, (−1), 3, 4]
k ← 2
window ← 0
FOR i ← 0 TO (k − 1) STEP 1
    window ← (window + A[i])
END FOR
best ← window
FOR i ← k TO (LENGTH(A) − 1) STEP 1
    window ← ((window − A[(i − k)]) + A[i])
    IF (window > best) THEN
        best ← window
    END IF
END FOR
PRINT best
```

**Sample output**

```text
7
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [2, (−1), 3, 4] | A=[2, -1, 3, 4] | — |
| 2 | main | k ← 2 | A=[2, -1, 3, 4]; k=2 | — |
| 3 | main | window ← 0 | A=[2, -1, 3, 4]; k=2; window=0 | — |
| 4 | main | FOR visit i | A=[2, -1, 3, 4]; k=2; window=0; i=0 | — |
| 5 | main | window ← (window + A[i]) | A=[2, -1, 3, 4]; k=2; window=2; i=0 | — |
| 6 | main | FOR visit i | A=[2, -1, 3, 4]; k=2; window=2; i=1 | — |
| 7 | main | window ← (window + A[i]) | A=[2, -1, 3, 4]; k=2; window=1; i=1 | — |
| 8 | main | FOR exit | A=[2, -1, 3, 4]; k=2; window=1; i=1 | — |
| 9 | main | best ← window | A=[2, -1, 3, 4]; k=2; window=1; i=1; best=1 | — |
| 10 | main | FOR visit i | A=[2, -1, 3, 4]; k=2; window=1; i=2; best=1 | — |
| 11 | main | window ← ((window − A[(i − k)]) + A[i]) | A=[2, -1, 3, 4]; k=2; window=2; i=2; best=1 | — |
| 12 | main | IF (window > best) → TRUE | A=[2, -1, 3, 4]; k=2; window=2; i=2; best=1 | — |
| 13 | main | best ← window | A=[2, -1, 3, 4]; k=2; window=2; i=2; best=2 | — |
| 14 | main | FOR visit i | A=[2, -1, 3, 4]; k=2; window=2; i=3; best=2 | — |
| 15 | main | window ← ((window − A[(i − k)]) + A[i]) | A=[2, -1, 3, 4]; k=2; window=7; i=3; best=2 | — |
| 16 | main | IF (window > best) → TRUE | A=[2, -1, 3, 4]; k=2; window=7; i=3; best=2 | — |
| 17 | main | best ← window | A=[2, -1, 3, 4]; k=2; window=7; i=3; best=7 | — |
| 18 | main | FOR exit | A=[2, -1, 3, 4]; k=2; window=7; i=3; best=7 | — |
| 19 | main | PRINT | A=[2, -1, 3, 4]; k=2; window=7; i=3; best=7 | 7 |

**Why it works:** Slide by removing exactly the leaving element and adding the entering one; initialize best from a real window.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** k=n→total sum;[-5,-2],k=1→-2; reject k=0 or k>n.

## W051 — Remove sorted duplicates

```text
Pseudocode
A ← [1, 1, 2, 2, 3]
B ← []
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF ((i = 0) OR (A[i] ≠ A[(i − 1)])) THEN
        APPEND(B, A[i])
    END IF
END FOR
PRINT B
```

**Sample output**

```text
[1, 2, 3]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [1, 1, 2, 2, 3] | A=[1, 1, 2, 2, 3] | — |
| 2 | main | B ← [] | A=[1, 1, 2, 2, 3]; B=[] | — |
| 3 | main | FOR visit i | A=[1, 1, 2, 2, 3]; B=[]; i=0 | — |
| 4 | main | IF ((i = 0) OR (A[i] ≠ A[(i − 1)])) → TRUE | A=[1, 1, 2, 2, 3]; B=[]; i=0 | — |
| 5 | main | APPEND(B, A[i]) | A=[1, 1, 2, 2, 3]; B=[1]; i=0 | — |
| 6 | main | FOR visit i | A=[1, 1, 2, 2, 3]; B=[1]; i=1 | — |
| 7 | main | IF ((i = 0) OR (A[i] ≠ A[(i − 1)])) → FALSE | A=[1, 1, 2, 2, 3]; B=[1]; i=1 | — |
| 8 | main | FOR visit i | A=[1, 1, 2, 2, 3]; B=[1]; i=2 | — |
| 9 | main | IF ((i = 0) OR (A[i] ≠ A[(i − 1)])) → TRUE | A=[1, 1, 2, 2, 3]; B=[1]; i=2 | — |
| 10 | main | APPEND(B, A[i]) | A=[1, 1, 2, 2, 3]; B=[1, 2]; i=2 | — |
| 11 | main | FOR visit i | A=[1, 1, 2, 2, 3]; B=[1, 2]; i=3 | — |
| 12 | main | IF ((i = 0) OR (A[i] ≠ A[(i − 1)])) → FALSE | A=[1, 1, 2, 2, 3]; B=[1, 2]; i=3 | — |
| 13 | main | FOR visit i | A=[1, 1, 2, 2, 3]; B=[1, 2]; i=4 | — |
| 14 | main | IF ((i = 0) OR (A[i] ≠ A[(i − 1)])) → TRUE | A=[1, 1, 2, 2, 3]; B=[1, 2]; i=4 | — |
| 15 | main | APPEND(B, A[i]) | A=[1, 1, 2, 2, 3]; B=[1, 2, 3]; i=4 | — |
| 16 | main | FOR exit | A=[1, 1, 2, 2, 3]; B=[1, 2, 3]; i=4 | — |
| 17 | main | PRINT | A=[1, 1, 2, 2, 3]; B=[1, 2, 3]; i=4 | [1, 2, 3] |

**Why it works:** Duplicates are adjacent in sorted input; short-circuit protects i-1 when i=0.

**Complexity:** O(n) time, O(n) output space

**Boundary checks:** []→[];[4,4]→[4]; unsorted input needs another method.

## W052 — Merge sorted arrays

```text
Pseudocode
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
WHILE (j < LENGTH(B))
    APPEND(C, B[j])
    j ← (j + 1)
END WHILE
PRINT C
```

**Sample output**

```text
[1, 2, 3, 4, 4]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [1, 4] | A=[1, 4] | — |
| 2 | main | B ← [2, 3, 4] | A=[1, 4]; B=[2, 3, 4] | — |
| 3 | main | i ← 0 | A=[1, 4]; B=[2, 3, 4]; i=0 | — |
| 4 | main | j ← 0 | A=[1, 4]; B=[2, 3, 4]; i=0; j=0 | — |
| 5 | main | C ← [] | A=[1, 4]; B=[2, 3, 4]; i=0; j=0; C=[] | — |
| 6 | main | WHILE ((i < LENGTH(A)) AND (j < LENGTH(B))) → TRUE | A=[1, 4]; B=[2, 3, 4]; i=0; j=0; C=[] | — |
| 7 | main | IF (A[i] ≤ B[j]) → TRUE | A=[1, 4]; B=[2, 3, 4]; i=0; j=0; C=[] | — |
| 8 | main | APPEND(C, A[i]) | A=[1, 4]; B=[2, 3, 4]; i=0; j=0; C=[1] | — |
| 9 | main | i ← (i + 1) | A=[1, 4]; B=[2, 3, 4]; i=1; j=0; C=[1] | — |
| 10 | main | WHILE ((i < LENGTH(A)) AND (j < LENGTH(B))) → TRUE | A=[1, 4]; B=[2, 3, 4]; i=1; j=0; C=[1] | — |
| 11 | main | IF (A[i] ≤ B[j]) → FALSE | A=[1, 4]; B=[2, 3, 4]; i=1; j=0; C=[1] | — |
| 12 | main | APPEND(C, B[j]) | A=[1, 4]; B=[2, 3, 4]; i=1; j=0; C=[1, 2] | — |
| 13 | main | j ← (j + 1) | A=[1, 4]; B=[2, 3, 4]; i=1; j=1; C=[1, 2] | — |
| 14 | main | WHILE ((i < LENGTH(A)) AND (j < LENGTH(B))) → TRUE | A=[1, 4]; B=[2, 3, 4]; i=1; j=1; C=[1, 2] | — |
| 15 | main | IF (A[i] ≤ B[j]) → FALSE | A=[1, 4]; B=[2, 3, 4]; i=1; j=1; C=[1, 2] | — |
| 16 | main | APPEND(C, B[j]) | A=[1, 4]; B=[2, 3, 4]; i=1; j=1; C=[1, 2, 3] | — |
| 17 | main | j ← (j + 1) | A=[1, 4]; B=[2, 3, 4]; i=1; j=2; C=[1, 2, 3] | — |
| 18 | main | WHILE ((i < LENGTH(A)) AND (j < LENGTH(B))) → TRUE | A=[1, 4]; B=[2, 3, 4]; i=1; j=2; C=[1, 2, 3] | — |
| 19 | main | IF (A[i] ≤ B[j]) → TRUE | A=[1, 4]; B=[2, 3, 4]; i=1; j=2; C=[1, 2, 3] | — |
| 20 | main | APPEND(C, A[i]) | A=[1, 4]; B=[2, 3, 4]; i=1; j=2; C=[1, 2, 3, 4] | — |
| 21 | main | i ← (i + 1) | A=[1, 4]; B=[2, 3, 4]; i=2; j=2; C=[1, 2, 3, 4] | — |
| 22 | main | WHILE ((i < LENGTH(A)) AND (j < LENGTH(B))) → FALSE | A=[1, 4]; B=[2, 3, 4]; i=2; j=2; C=[1, 2, 3, 4] | — |
| 23 | main | WHILE (i < LENGTH(A)) → FALSE | A=[1, 4]; B=[2, 3, 4]; i=2; j=2; C=[1, 2, 3, 4] | — |
| 24 | main | WHILE (j < LENGTH(B)) → TRUE | A=[1, 4]; B=[2, 3, 4]; i=2; j=2; C=[1, 2, 3, 4] | — |
| 25 | main | APPEND(C, B[j]) | A=[1, 4]; B=[2, 3, 4]; i=2; j=2; C=[1, 2, 3, 4, 4] | — |
| 26 | main | j ← (j + 1) | A=[1, 4]; B=[2, 3, 4]; i=2; j=3; C=[1, 2, 3, 4, 4] | — |
| 27 | main | WHILE (j < LENGTH(B)) → FALSE | A=[1, 4]; B=[2, 3, 4]; i=2; j=3; C=[1, 2, 3, 4, 4] | — |
| 28 | main | PRINT | A=[1, 4]; B=[2, 3, 4]; i=2; j=3; C=[1, 2, 3, 4, 4] | [1, 2, 3, 4, 4] |

**Why it works:** Choose the smaller front, then copy the unexhausted tail. Every element is consumed once.

**Complexity:** O(n+m) time, O(n+m) output space

**Boundary checks:** One input empty copies the other; both empty→[].

## W053 — Pair sum in sorted array

```text
Pseudocode
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
        l ← (l + 1)
    ELSE
        r ← (r − 1)
    END IF
END WHILE
PRINT found
```

**Sample output**

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [1, 2, 4, 7] | A=[1, 2, 4, 7] | — |
| 2 | main | target ← 9 | A=[1, 2, 4, 7]; target=9 | — |
| 3 | main | l ← 0 | A=[1, 2, 4, 7]; target=9; l=0 | — |
| 4 | main | r ← (LENGTH(A) − 1) | A=[1, 2, 4, 7]; target=9; l=0; r=3 | — |
| 5 | main | found ← FALSE | A=[1, 2, 4, 7]; target=9; l=0; r=3; found=FALSE | — |
| 6 | main | WHILE (l < r) → TRUE | A=[1, 2, 4, 7]; target=9; l=0; r=3; found=FALSE | — |
| 7 | main | s ← (A[l] + A[r]) | A=[1, 2, 4, 7]; target=9; l=0; r=3; found=FALSE; s=8 | — |
| 8 | main | IF (s = target) → FALSE | A=[1, 2, 4, 7]; target=9; l=0; r=3; found=FALSE; s=8 | — |
| 9 | main | IF (s < target) → TRUE | A=[1, 2, 4, 7]; target=9; l=0; r=3; found=FALSE; s=8 | — |
| 10 | main | l ← (l + 1) | A=[1, 2, 4, 7]; target=9; l=1; r=3; found=FALSE; s=8 | — |
| 11 | main | WHILE (l < r) → TRUE | A=[1, 2, 4, 7]; target=9; l=1; r=3; found=FALSE; s=8 | — |
| 12 | main | s ← (A[l] + A[r]) | A=[1, 2, 4, 7]; target=9; l=1; r=3; found=FALSE; s=9 | — |
| 13 | main | IF (s = target) → TRUE | A=[1, 2, 4, 7]; target=9; l=1; r=3; found=FALSE; s=9 | — |
| 14 | main | found ← TRUE | A=[1, 2, 4, 7]; target=9; l=1; r=3; found=TRUE; s=9 | — |
| 15 | main | BREAK | A=[1, 2, 4, 7]; target=9; l=1; r=3; found=TRUE; s=9 | — |
| 16 | main | PRINT | A=[1, 2, 4, 7]; target=9; l=1; r=3; found=TRUE; s=9 | TRUE |

**Why it works:** Too-small sum requires a larger left value; too-large requires a smaller right value. l<r prevents reuse.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** [] or singleton→FALSE;[4,4],target8→TRUE.

## W054 — Insertion sort

```text
Pseudocode
A ← [3, 1, 2]
FOR i ← 1 TO (LENGTH(A) − 1) STEP 1
    key ← A[i]
    j ← (i − 1)
    WHILE ((j ≥ 0) AND (A[j] > key))
        A[(j + 1)] ← A[j]
        j ← (j − 1)
    END WHILE
    A[(j + 1)] ← key
END FOR
PRINT A
```

**Sample output**

```text
[1, 2, 3]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [3, 1, 2] | A=[3, 1, 2] | — |
| 2 | main | FOR visit i | A=[3, 1, 2]; i=1 | — |
| 3 | main | key ← A[i] | A=[3, 1, 2]; i=1; key=1 | — |
| 4 | main | j ← (i − 1) | A=[3, 1, 2]; i=1; key=1; j=0 | — |
| 5 | main | WHILE ((j ≥ 0) AND (A[j] > key)) → TRUE | A=[3, 1, 2]; i=1; key=1; j=0 | — |
| 6 | main | A[(j + 1)] ← A[j] | A=[3, 3, 2]; i=1; key=1; j=0 | — |
| 7 | main | j ← (j − 1) | A=[3, 3, 2]; i=1; key=1; j=-1 | — |
| 8 | main | WHILE ((j ≥ 0) AND (A[j] > key)) → FALSE | A=[3, 3, 2]; i=1; key=1; j=-1 | — |
| 9 | main | A[(j + 1)] ← key | A=[1, 3, 2]; i=1; key=1; j=-1 | — |
| 10 | main | FOR visit i | A=[1, 3, 2]; i=2; key=1; j=-1 | — |
| 11 | main | key ← A[i] | A=[1, 3, 2]; i=2; key=2; j=-1 | — |
| 12 | main | j ← (i − 1) | A=[1, 3, 2]; i=2; key=2; j=1 | — |
| 13 | main | WHILE ((j ≥ 0) AND (A[j] > key)) → TRUE | A=[1, 3, 2]; i=2; key=2; j=1 | — |
| 14 | main | A[(j + 1)] ← A[j] | A=[1, 3, 3]; i=2; key=2; j=1 | — |
| 15 | main | j ← (j − 1) | A=[1, 3, 3]; i=2; key=2; j=0 | — |
| 16 | main | WHILE ((j ≥ 0) AND (A[j] > key)) → FALSE | A=[1, 3, 3]; i=2; key=2; j=0 | — |
| 17 | main | A[(j + 1)] ← key | A=[1, 2, 3]; i=2; key=2; j=0 | — |
| 18 | main | FOR exit | A=[1, 2, 3]; i=2; key=2; j=0 | — |
| 19 | main | PRINT | A=[1, 2, 3]; i=2; key=2; j=0 | [1, 2, 3] |

**Why it works:** Preserve key, shift larger values right, and insert into the gap. The guard avoids negative indexing.

**Complexity:** O(n²) worst time, O(1) space

**Boundary checks:** [] unchanged; sorted input O(n); duplicates preserved.

## W055 — Balanced parentheses

```text
Pseudocode
s ← "(()())"
balance ← 0
ok ← TRUE
FOR i ← 0 TO (LENGTH(s) − 1) STEP 1
    IF (s[i] = "(") THEN
        balance ← (balance + 1)
    ELSE
        balance ← (balance − 1)
    END IF
    IF (balance < 0) THEN
        ok ← FALSE
        BREAK
    END IF
END FOR
PRINT (ok AND (balance = 0))
```

**Sample output**

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "(()())" | s=(()()) | — |
| 2 | main | balance ← 0 | s=(()()); balance=0 | — |
| 3 | main | ok ← TRUE | s=(()()); balance=0; ok=TRUE | — |
| 4 | main | FOR visit i | s=(()()); balance=0; ok=TRUE; i=0 | — |
| 5 | main | IF (s[i] = "(") → TRUE | s=(()()); balance=0; ok=TRUE; i=0 | — |
| 6 | main | balance ← (balance + 1) | s=(()()); balance=1; ok=TRUE; i=0 | — |
| 7 | main | IF (balance < 0) → FALSE | s=(()()); balance=1; ok=TRUE; i=0 | — |
| 8 | main | FOR visit i | s=(()()); balance=1; ok=TRUE; i=1 | — |
| 9 | main | IF (s[i] = "(") → TRUE | s=(()()); balance=1; ok=TRUE; i=1 | — |
| 10 | main | balance ← (balance + 1) | s=(()()); balance=2; ok=TRUE; i=1 | — |
| 11 | main | IF (balance < 0) → FALSE | s=(()()); balance=2; ok=TRUE; i=1 | — |
| 12 | main | FOR visit i | s=(()()); balance=2; ok=TRUE; i=2 | — |
| 13 | main | IF (s[i] = "(") → FALSE | s=(()()); balance=2; ok=TRUE; i=2 | — |
| 14 | main | balance ← (balance − 1) | s=(()()); balance=1; ok=TRUE; i=2 | — |
| 15 | main | IF (balance < 0) → FALSE | s=(()()); balance=1; ok=TRUE; i=2 | — |
| 16 | main | FOR visit i | s=(()()); balance=1; ok=TRUE; i=3 | — |
| 17 | main | IF (s[i] = "(") → TRUE | s=(()()); balance=1; ok=TRUE; i=3 | — |
| 18 | main | balance ← (balance + 1) | s=(()()); balance=2; ok=TRUE; i=3 | — |
| 19 | main | IF (balance < 0) → FALSE | s=(()()); balance=2; ok=TRUE; i=3 | — |
| 20 | main | FOR visit i | s=(()()); balance=2; ok=TRUE; i=4 | — |
| 21 | main | IF (s[i] = "(") → FALSE | s=(()()); balance=2; ok=TRUE; i=4 | — |
| 22 | main | balance ← (balance − 1) | s=(()()); balance=1; ok=TRUE; i=4 | — |
| 23 | main | IF (balance < 0) → FALSE | s=(()()); balance=1; ok=TRUE; i=4 | — |
| 24 | main | FOR visit i | s=(()()); balance=1; ok=TRUE; i=5 | — |
| 25 | main | IF (s[i] = "(") → FALSE | s=(()()); balance=1; ok=TRUE; i=5 | — |
| 26 | main | balance ← (balance − 1) | s=(()()); balance=0; ok=TRUE; i=5 | — |
| 27 | main | IF (balance < 0) → FALSE | s=(()()); balance=0; ok=TRUE; i=5 | — |
| 28 | main | FOR exit | s=(()()); balance=0; ok=TRUE; i=5 | — |
| 29 | main | PRINT | s=(()()); balance=0; ok=TRUE; i=5 | TRUE |

**Why it works:** Every prefix must have nonnegative balance and the complete text must return to zero.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** empty TRUE;")(" FALSE despite final balance zero;"(()" FALSE.

## W056 — Maximum subarray sum

```text
Pseudocode
A ← [(−2), 3, (−1), 4, (−5)]
ending ← A[0]
best ← A[0]
FOR i ← 1 TO (LENGTH(A) − 1) STEP 1
    ending ← MAX(A[i], (ending + A[i]))
    best ← MAX(best, ending)
END FOR
PRINT best
```

**Sample output**

```text
6
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [(−2), 3, (−1), 4, (−5)] | A=[-2, 3, -1, 4, -5] | — |
| 2 | main | ending ← A[0] | A=[-2, 3, -1, 4, -5]; ending=-2 | — |
| 3 | main | best ← A[0] | A=[-2, 3, -1, 4, -5]; ending=-2; best=-2 | — |
| 4 | main | FOR visit i | A=[-2, 3, -1, 4, -5]; ending=-2; best=-2; i=1 | — |
| 5 | main | ending ← MAX(A[i], (ending + A[i])) | A=[-2, 3, -1, 4, -5]; ending=3; best=-2; i=1 | — |
| 6 | main | best ← MAX(best, ending) | A=[-2, 3, -1, 4, -5]; ending=3; best=3; i=1 | — |
| 7 | main | FOR visit i | A=[-2, 3, -1, 4, -5]; ending=3; best=3; i=2 | — |
| 8 | main | ending ← MAX(A[i], (ending + A[i])) | A=[-2, 3, -1, 4, -5]; ending=2; best=3; i=2 | — |
| 9 | main | best ← MAX(best, ending) | A=[-2, 3, -1, 4, -5]; ending=2; best=3; i=2 | — |
| 10 | main | FOR visit i | A=[-2, 3, -1, 4, -5]; ending=2; best=3; i=3 | — |
| 11 | main | ending ← MAX(A[i], (ending + A[i])) | A=[-2, 3, -1, 4, -5]; ending=6; best=3; i=3 | — |
| 12 | main | best ← MAX(best, ending) | A=[-2, 3, -1, 4, -5]; ending=6; best=6; i=3 | — |
| 13 | main | FOR visit i | A=[-2, 3, -1, 4, -5]; ending=6; best=6; i=4 | — |
| 14 | main | ending ← MAX(A[i], (ending + A[i])) | A=[-2, 3, -1, 4, -5]; ending=1; best=6; i=4 | — |
| 15 | main | best ← MAX(best, ending) | A=[-2, 3, -1, 4, -5]; ending=1; best=6; i=4 | — |
| 16 | main | FOR exit | A=[-2, 3, -1, 4, -5]; ending=1; best=6; i=4 | — |
| 17 | main | PRINT | A=[-2, 3, -1, 4, -5]; ending=1; best=6; i=4 | 6 |

**Why it works:** At each position either start fresh or extend the best ending at the previous position. All-negative data stays valid.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** [-7,-2]→-2;[5]→5; reject empty input.

## W057 — Recursive Fibonacci calls

```text
Pseudocode
FUNCTION fib(n)
    IF (n ≤ 1) THEN
        RETURN n
    END IF
    RETURN (fib((n − 1)) + fib((n − 2)))
END FUNCTION
PRINT fib(5)
```

**Sample output**

```text
5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | fib depth 1 | ENTER | n=5 | — |
| 2 | fib depth 1 | IF (n ≤ 1) → FALSE | n=5 | — |
| 3 | fib depth 2 | ENTER | n=4 | — |
| 4 | fib depth 2 | IF (n ≤ 1) → FALSE | n=4 | — |
| 5 | fib depth 3 | ENTER | n=3 | — |
| 6 | fib depth 3 | IF (n ≤ 1) → FALSE | n=3 | — |
| 7 | fib depth 4 | ENTER | n=2 | — |
| 8 | fib depth 4 | IF (n ≤ 1) → FALSE | n=2 | — |
| 9 | fib depth 5 | ENTER | n=1 | — |
| 10 | fib depth 5 | IF (n ≤ 1) → TRUE | n=1 | — |
| 11 | fib depth 5 | RETURN 1 | n=1 | — |
| 12 | fib depth 5 | ENTER | n=0 | — |
| 13 | fib depth 5 | IF (n ≤ 1) → TRUE | n=0 | — |
| 14 | fib depth 5 | RETURN 0 | n=0 | — |
| 15 | fib depth 4 | RETURN 1 | n=2 | — |
| 16 | fib depth 4 | ENTER | n=1 | — |
| 17 | fib depth 4 | IF (n ≤ 1) → TRUE | n=1 | — |
| 18 | fib depth 4 | RETURN 1 | n=1 | — |
| 19 | fib depth 3 | RETURN 2 | n=3 | — |
| 20 | fib depth 3 | ENTER | n=2 | — |
| 21 | fib depth 3 | IF (n ≤ 1) → FALSE | n=2 | — |
| 22 | fib depth 4 | ENTER | n=1 | — |
| 23 | fib depth 4 | IF (n ≤ 1) → TRUE | n=1 | — |
| 24 | fib depth 4 | RETURN 1 | n=1 | — |
| 25 | fib depth 4 | ENTER | n=0 | — |
| 26 | fib depth 4 | IF (n ≤ 1) → TRUE | n=0 | — |
| 27 | fib depth 4 | RETURN 0 | n=0 | — |
| 28 | fib depth 3 | RETURN 1 | n=2 | — |
| 29 | fib depth 2 | RETURN 3 | n=4 | — |
| 30 | fib depth 2 | ENTER | n=3 | — |
| 31 | fib depth 2 | IF (n ≤ 1) → FALSE | n=3 | — |
| 32 | fib depth 3 | ENTER | n=2 | — |
| 33 | fib depth 3 | IF (n ≤ 1) → FALSE | n=2 | — |
| 34 | fib depth 4 | ENTER | n=1 | — |
| 35 | fib depth 4 | IF (n ≤ 1) → TRUE | n=1 | — |
| 36 | fib depth 4 | RETURN 1 | n=1 | — |
| 37 | fib depth 4 | ENTER | n=0 | — |
| 38 | fib depth 4 | IF (n ≤ 1) → TRUE | n=0 | — |
| 39 | fib depth 4 | RETURN 0 | n=0 | — |
| 40 | fib depth 3 | RETURN 1 | n=2 | — |
| 41 | fib depth 3 | ENTER | n=1 | — |
| 42 | fib depth 3 | IF (n ≤ 1) → TRUE | n=1 | — |
| 43 | fib depth 3 | RETURN 1 | n=1 | — |
| 44 | fib depth 2 | RETURN 2 | n=3 | — |
| 45 | fib depth 1 | RETURN 5 | n=5 | — |
| 46 | main | PRINT | — | 5 |

**Why it works:** The recurrence recomputes many overlapping subproblems; trace both branches, not just one descent.

**Complexity:** O(2^n) time upper bound (tight Θ(phi^n)), O(n) maximum stack

**Boundary checks:** fib(0)=0;fib(1)=1; iterative version is O(n) time.

## W058 — Unique diagonal sum

```text
Pseudocode
M ← [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n ← LENGTH(M)
s ← 0
FOR i ← 0 TO (n − 1) STEP 1
    s ← (s + M[i][i])
    IF (i ≠ ((n − 1) − i)) THEN
        s ← (s + M[i][((n − 1) − i)])
    END IF
END FOR
PRINT s
```

**Sample output**

```text
25
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | M ← [[1, 2, 3], [4, 5, 6], [7, 8, 9]] | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]] | — |
| 2 | main | n ← LENGTH(M) | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3 | — |
| 3 | main | s ← 0 | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=0 | — |
| 4 | main | FOR visit i | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=0; i=0 | — |
| 5 | main | s ← (s + M[i][i]) | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=1; i=0 | — |
| 6 | main | IF (i ≠ ((n − 1) − i)) → TRUE | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=1; i=0 | — |
| 7 | main | s ← (s + M[i][((n − 1) − i)]) | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=4; i=0 | — |
| 8 | main | FOR visit i | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=4; i=1 | — |
| 9 | main | s ← (s + M[i][i]) | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=9; i=1 | — |
| 10 | main | IF (i ≠ ((n − 1) − i)) → FALSE | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=9; i=1 | — |
| 11 | main | FOR visit i | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=9; i=2 | — |
| 12 | main | s ← (s + M[i][i]) | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=18; i=2 | — |
| 13 | main | IF (i ≠ ((n − 1) − i)) → TRUE | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=18; i=2 | — |
| 14 | main | s ← (s + M[i][((n − 1) − i)]) | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=25; i=2 | — |
| 15 | main | FOR exit | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=25; i=2 | — |
| 16 | main | PRINT | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; n=3; s=25; i=2 | 25 |

**Why it works:** Both coordinates coincide only at the odd-sized center; skip its second addition.

**Complexity:** O(n) time, O(1) space

**Boundary checks:** []→0;[[7]]→7; even-sized matrices have no overlap.

## W059 — First occurrence by binary search

```text
Pseudocode
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
        hi ← (mid − 1)
    ELSE
        lo ← (mid + 1)
    END IF
END WHILE
PRINT answer
```

**Sample output**

```text
1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [1, 2, 2, 2, 4] | A=[1, 2, 2, 2, 4] | — |
| 2 | main | target ← 2 | A=[1, 2, 2, 2, 4]; target=2 | — |
| 3 | main | lo ← 0 | A=[1, 2, 2, 2, 4]; target=2; lo=0 | — |
| 4 | main | hi ← (LENGTH(A) − 1) | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=4 | — |
| 5 | main | answer ← (−1) | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=4; answer=-1 | — |
| 6 | main | WHILE (lo ≤ hi) → TRUE | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=4; answer=-1 | — |
| 7 | main | mid ← (lo + ((hi − lo) DIV 2)) | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=4; answer=-1; mid=2 | — |
| 8 | main | IF (A[mid] ≥ target) → TRUE | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=4; answer=-1; mid=2 | — |
| 9 | main | IF (A[mid] = target) → TRUE | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=4; answer=-1; mid=2 | — |
| 10 | main | answer ← mid | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=4; answer=2; mid=2 | — |
| 11 | main | hi ← (mid − 1) | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=1; answer=2; mid=2 | — |
| 12 | main | WHILE (lo ≤ hi) → TRUE | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=1; answer=2; mid=2 | — |
| 13 | main | mid ← (lo + ((hi − lo) DIV 2)) | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=1; answer=2; mid=0 | — |
| 14 | main | IF (A[mid] ≥ target) → FALSE | A=[1, 2, 2, 2, 4]; target=2; lo=0; hi=1; answer=2; mid=0 | — |
| 15 | main | lo ← (mid + 1) | A=[1, 2, 2, 2, 4]; target=2; lo=1; hi=1; answer=2; mid=0 | — |
| 16 | main | WHILE (lo ≤ hi) → TRUE | A=[1, 2, 2, 2, 4]; target=2; lo=1; hi=1; answer=2; mid=0 | — |
| 17 | main | mid ← (lo + ((hi − lo) DIV 2)) | A=[1, 2, 2, 2, 4]; target=2; lo=1; hi=1; answer=2; mid=1 | — |
| 18 | main | IF (A[mid] ≥ target) → TRUE | A=[1, 2, 2, 2, 4]; target=2; lo=1; hi=1; answer=2; mid=1 | — |
| 19 | main | IF (A[mid] = target) → TRUE | A=[1, 2, 2, 2, 4]; target=2; lo=1; hi=1; answer=2; mid=1 | — |
| 20 | main | answer ← mid | A=[1, 2, 2, 2, 4]; target=2; lo=1; hi=1; answer=1; mid=1 | — |
| 21 | main | hi ← (mid − 1) | A=[1, 2, 2, 2, 4]; target=2; lo=1; hi=0; answer=1; mid=1 | — |
| 22 | main | WHILE (lo ≤ hi) → FALSE | A=[1, 2, 2, 2, 4]; target=2; lo=1; hi=0; answer=1; mid=1 | — |
| 23 | main | PRINT | A=[1, 2, 2, 2, 4]; target=2; lo=1; hi=0; answer=1; mid=1 | 1 |

**Why it works:** Save a match and keep searching left; every discarded right portion cannot contain an earlier match.

**Complexity:** O(log(n+1)) time, O(1) space

**Boundary checks:** []→-1;[2,2]→0;missing target→-1.

## W060 — Recursive subset-sum decision

```text
Pseudocode
FUNCTION possible(A, i, target)
    IF (target = 0) THEN
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

**Sample output**

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [3, 5, 7] | A=[3, 5, 7] | — |
| 2 | possible depth 1 | ENTER | A=[3, 5, 7]; i=0; target=10 | — |
| 3 | possible depth 1 | IF (target = 0) → FALSE | A=[3, 5, 7]; i=0; target=10 | — |
| 4 | possible depth 1 | IF (i = LENGTH(A)) → FALSE | A=[3, 5, 7]; i=0; target=10 | — |
| 5 | possible depth 2 | ENTER | A=[3, 5, 7]; i=1; target=7 | — |
| 6 | possible depth 2 | IF (target = 0) → FALSE | A=[3, 5, 7]; i=1; target=7 | — |
| 7 | possible depth 2 | IF (i = LENGTH(A)) → FALSE | A=[3, 5, 7]; i=1; target=7 | — |
| 8 | possible depth 3 | ENTER | A=[3, 5, 7]; i=2; target=2 | — |
| 9 | possible depth 3 | IF (target = 0) → FALSE | A=[3, 5, 7]; i=2; target=2 | — |
| 10 | possible depth 3 | IF (i = LENGTH(A)) → FALSE | A=[3, 5, 7]; i=2; target=2 | — |
| 11 | possible depth 3 | IF ((A[i] ≤ target) AND possible(A, (i + 1), (target − A[i]))) → FALSE | A=[3, 5, 7]; i=2; target=2 | — |
| 12 | possible depth 4 | ENTER | A=[3, 5, 7]; i=3; target=2 | — |
| 13 | possible depth 4 | IF (target = 0) → FALSE | A=[3, 5, 7]; i=3; target=2 | — |
| 14 | possible depth 4 | IF (i = LENGTH(A)) → TRUE | A=[3, 5, 7]; i=3; target=2 | — |
| 15 | possible depth 4 | RETURN FALSE | A=[3, 5, 7]; i=3; target=2 | — |
| 16 | possible depth 3 | RETURN FALSE | A=[3, 5, 7]; i=2; target=2 | — |
| 17 | possible depth 2 | IF ((A[i] ≤ target) AND possible(A, (i + 1), (target − A[i]))) → FALSE | A=[3, 5, 7]; i=1; target=7 | — |
| 18 | possible depth 3 | ENTER | A=[3, 5, 7]; i=2; target=7 | — |
| 19 | possible depth 3 | IF (target = 0) → FALSE | A=[3, 5, 7]; i=2; target=7 | — |
| 20 | possible depth 3 | IF (i = LENGTH(A)) → FALSE | A=[3, 5, 7]; i=2; target=7 | — |
| 21 | possible depth 4 | ENTER | A=[3, 5, 7]; i=3; target=0 | — |
| 22 | possible depth 4 | IF (target = 0) → TRUE | A=[3, 5, 7]; i=3; target=0 | — |
| 23 | possible depth 4 | RETURN TRUE | A=[3, 5, 7]; i=3; target=0 | — |
| 24 | possible depth 3 | IF ((A[i] ≤ target) AND possible(A, (i + 1), (target − A[i]))) → TRUE | A=[3, 5, 7]; i=2; target=7 | — |
| 25 | possible depth 3 | RETURN TRUE | A=[3, 5, 7]; i=2; target=7 | — |
| 26 | possible depth 2 | RETURN TRUE | A=[3, 5, 7]; i=1; target=7 | — |
| 27 | possible depth 1 | IF ((A[i] ≤ target) AND possible(A, (i + 1), (target − A[i]))) → TRUE | A=[3, 5, 7]; i=0; target=10 | — |
| 28 | possible depth 1 | RETURN TRUE | A=[3, 5, 7]; i=0; target=10 | — |
| 29 | main | PRINT | A=[3, 5, 7] | TRUE |

**Why it works:** Each element is included or excluded; i always advances. Successful include branch short-circuits unnecessary work.

**Complexity:** O(2^n) worst time, O(n) stack; no sliced copies

**Boundary checks:** [] target0 TRUE;[] target1 FALSE;[4,6] target5 FALSE.
