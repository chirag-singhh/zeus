# Mock-test answers

Grade only after stopping the timer. Every selected question has a full solution here; no answer is delegated to another file. Original bank IDs are omitted from the test body to keep the attempt self-contained.

# Mock 1 — solutions

## M1-Q01 — Output prediction: Multiplication before addition

**Answer: A**

```text
10
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← (4 + (3 * 2)) | x=10 | — |
| 2 | main | PRINT | x=10 | 10 |

**Explanation:** Multiplication is evaluated first, so 4+6=10.

## M1-Q02 — Output prediction: Integer quotient and remainder

**Answer: B**

```text
5 3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 23 | a=23 | — |
| 2 | main | PRINT | a=23 | 5 3 |

**Explanation:** 23=5*4+3.

## M1-Q03 — Output prediction: Nested boundary condition

**Answer: D**

```text
Z
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 0 | x=0 | — |
| 2 | main | IF (x ≥ 0) → TRUE | x=0 | — |
| 3 | main | IF (x > 0) → FALSE | x=0 | — |
| 4 | main | PRINT | x=0 | Z |

**Explanation:** Zero enters the nonnegative branch, then fails the positive test.

## M1-Q04 — Output prediction: Inclusive step-two loop

**Answer: D**

```text
16
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← 0 | s=0 | — |
| 2 | main | FOR visit i | s=0; i=1 | — |
| 3 | main | s ← (s + i) | s=1; i=1 | — |
| 4 | main | FOR visit i | s=1; i=3 | — |
| 5 | main | s ← (s + i) | s=4; i=3 | — |
| 6 | main | FOR visit i | s=4; i=5 | — |
| 7 | main | s ← (s + i) | s=9; i=5 | — |
| 8 | main | FOR visit i | s=9; i=7 | — |
| 9 | main | s ← (s + i) | s=16; i=7 | — |
| 10 | main | FOR exit | s=16; i=7 | — |
| 11 | main | PRINT | s=16; i=7 | 16 |

**Explanation:** Visits 1,3,5,7, then stops.

## M1-Q05 — Output prediction: Doubling loop

**Answer: C**

```text
15 16
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | i ← 1 | i=1 | — |
| 2 | main | s ← 0 | i=1; s=0 | — |
| 3 | main | WHILE (i ≤ 8) → TRUE | i=1; s=0 | — |
| 4 | main | s ← (s + i) | i=1; s=1 | — |
| 5 | main | i ← (i * 2) | i=2; s=1 | — |
| 6 | main | WHILE (i ≤ 8) → TRUE | i=2; s=1 | — |
| 7 | main | s ← (s + i) | i=2; s=3 | — |
| 8 | main | i ← (i * 2) | i=4; s=3 | — |
| 9 | main | WHILE (i ≤ 8) → TRUE | i=4; s=3 | — |
| 10 | main | s ← (s + i) | i=4; s=7 | — |
| 11 | main | i ← (i * 2) | i=8; s=7 | — |
| 12 | main | WHILE (i ≤ 8) → TRUE | i=8; s=7 | — |
| 13 | main | s ← (s + i) | i=8; s=15 | — |
| 14 | main | i ← (i * 2) | i=16; s=15 | — |
| 15 | main | WHILE (i ≤ 8) → FALSE | i=16; s=15 | — |
| 16 | main | PRINT | i=16; s=15 | 15 16 |

**Explanation:** The rejected i=16 is retained but not added.

## M1-Q06 — Output prediction: BREAK before addition

**Answer: C**

```text
6
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← 0 | s=0 | — |
| 2 | main | FOR visit i | s=0; i=1 | — |
| 3 | main | IF (i = 4) → FALSE | s=0; i=1 | — |
| 4 | main | s ← (s + i) | s=1; i=1 | — |
| 5 | main | FOR visit i | s=1; i=2 | — |
| 6 | main | IF (i = 4) → FALSE | s=1; i=2 | — |
| 7 | main | s ← (s + i) | s=3; i=2 | — |
| 8 | main | FOR visit i | s=3; i=3 | — |
| 9 | main | IF (i = 4) → FALSE | s=3; i=3 | — |
| 10 | main | s ← (s + i) | s=6; i=3 | — |
| 11 | main | FOR visit i | s=6; i=4 | — |
| 12 | main | IF (i = 4) → TRUE | s=6; i=4 | — |
| 13 | main | BREAK | s=6; i=4 | — |
| 14 | main | FOR exit | s=6; i=4 | — |
| 15 | main | PRINT | s=6; i=4 | 6 |

**Explanation:** The value 4 never reaches the addition.

## M1-Q07 — Output prediction: Rectangular nested loop

**Answer: C**

```text
6
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | count ← 0 | count=0 | — |
| 2 | main | FOR visit i | count=0; i=0 | — |
| 3 | main | FOR visit j | count=0; i=0; j=0 | — |
| 4 | main | count ← (count + 1) | count=1; i=0; j=0 | — |
| 5 | main | FOR visit j | count=1; i=0; j=1 | — |
| 6 | main | count ← (count + 1) | count=2; i=0; j=1 | — |
| 7 | main | FOR exit | count=2; i=0; j=1 | — |
| 8 | main | FOR visit i | count=2; i=1; j=1 | — |
| 9 | main | FOR visit j | count=2; i=1; j=0 | — |
| 10 | main | count ← (count + 1) | count=3; i=1; j=0 | — |
| 11 | main | FOR visit j | count=3; i=1; j=1 | — |
| 12 | main | count ← (count + 1) | count=4; i=1; j=1 | — |
| 13 | main | FOR exit | count=4; i=1; j=1 | — |
| 14 | main | FOR visit i | count=4; i=2; j=1 | — |
| 15 | main | FOR visit j | count=4; i=2; j=0 | — |
| 16 | main | count ← (count + 1) | count=5; i=2; j=0 | — |
| 17 | main | FOR visit j | count=5; i=2; j=1 | — |
| 18 | main | count ← (count + 1) | count=6; i=2; j=1 | — |
| 19 | main | FOR exit | count=6; i=2; j=1 | — |
| 20 | main | FOR exit | count=6; i=2; j=1 | — |
| 21 | main | PRINT | count=6; i=2; j=1 | 6 |

**Explanation:** Three complete inner loops of two visits.

## M1-Q08 — Output prediction: Array accumulation

**Answer: B**

```text
8
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [2, 5, 1] | A=[2, 5, 1] | — |
| 2 | main | s ← 0 | A=[2, 5, 1]; s=0 | — |
| 3 | main | FOR visit i | A=[2, 5, 1]; s=0; i=0 | — |
| 4 | main | s ← (s + A[i]) | A=[2, 5, 1]; s=2; i=0 | — |
| 5 | main | FOR visit i | A=[2, 5, 1]; s=2; i=1 | — |
| 6 | main | s ← (s + A[i]) | A=[2, 5, 1]; s=7; i=1 | — |
| 7 | main | FOR visit i | A=[2, 5, 1]; s=7; i=2 | — |
| 8 | main | s ← (s + A[i]) | A=[2, 5, 1]; s=8; i=2 | — |
| 9 | main | FOR exit | A=[2, 5, 1]; s=8; i=2 | — |
| 10 | main | PRINT | A=[2, 5, 1]; s=8; i=2 | 8 |

**Explanation:** Each element is added exactly once.

## M1-Q09 — Output prediction: First matching index

**Answer: A**

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [5, 2, 5] | A=[5, 2, 5] | — |
| 2 | main | answer ← (−1) | A=[5, 2, 5]; answer=-1 | — |
| 3 | main | FOR visit i | A=[5, 2, 5]; answer=-1; i=0 | — |
| 4 | main | IF (A[i] = 5) → TRUE | A=[5, 2, 5]; answer=-1; i=0 | — |
| 5 | main | answer ← i | A=[5, 2, 5]; answer=0; i=0 | — |
| 6 | main | BREAK | A=[5, 2, 5]; answer=0; i=0 | — |
| 7 | main | FOR exit | A=[5, 2, 5]; answer=0; i=0 | — |
| 8 | main | PRINT | A=[5, 2, 5]; answer=0; i=0 | 0 |

**Explanation:** BREAK preserves the first match.

## M1-Q10 — Output prediction: String reverse loop

**Answer: A**

```text
cba
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "abc" | s=abc | — |
| 2 | main | r ← "" | s=abc; r= | — |
| 3 | main | FOR visit i | s=abc; r=; i=2 | — |
| 4 | main | r ← (r + s[i]) | s=abc; r=c; i=2 | — |
| 5 | main | FOR visit i | s=abc; r=c; i=1 | — |
| 6 | main | r ← (r + s[i]) | s=abc; r=cb; i=1 | — |
| 7 | main | FOR visit i | s=abc; r=cb; i=0 | — |
| 8 | main | r ← (r + s[i]) | s=abc; r=cba; i=0 | — |
| 9 | main | FOR exit | s=abc; r=cba; i=0 | — |
| 10 | main | PRINT | s=abc; r=cba; i=0 | cba |

**Explanation:** Indices 2,1,0 supply c,b,a.

## M1-Q11 — Output prediction: Bitwise AND

**Answer: D**

```text
8
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 13 | a=13 | — |
| 2 | main | b ← 10 | a=13; b=10 | — |
| 3 | main | PRINT | a=13; b=10 | 8 |

**Explanation:** 1101 AND 1010 = 1000.

## M1-Q12 — Output prediction: Guard division with AND

**Answer: A**

```text
FALSE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | d ← 0 | d=0 | — |
| 2 | main | PRINT | d=0 | FALSE |

**Explanation:** False left operand skips division entirely.

## M1-Q13 — Error detection: Swap two values — program review

**Category:** logic

**Fault and root cause:** The temporary stores b instead of the original a, so the original a is lost.

**Faulty execution / counterexample:** output: '9 9'

**Complete corrected program**

```text
Pseudocode
a ← 4
b ← 9
temp ← a
a ← b
b ← temp
PRINT a, b
```

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
a ← 5
b ← 5
temp ← a
a ← b
b ← temp
PRINT a, b
```

```text
5 5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 5 | a=5 | — |
| 2 | main | b ← 5 | a=5; b=5 | — |
| 3 | main | temp ← a | a=5; b=5; temp=5 | — |
| 4 | main | a ← b | a=5; b=5; temp=5 | — |
| 5 | main | b ← temp | a=5; b=5; temp=5 | — |
| 6 | main | PRINT | a=5; b=5; temp=5 | 5 5 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M1-Q14 — Error detection: Grade bands — program review

**Category:** boundary

**Fault and root cause:** Mark 60 falls into the next band because equality is excluded.

**Faulty execution / counterexample:** output: 'C'

**Complete corrected program**

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

**Corrected sample output**

```text
B
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | mark ← 60 | mark=60 | — |
| 2 | main | IF (mark ≥ 80) → FALSE | mark=60 | — |
| 3 | main | IF (mark ≥ 60) → TRUE | mark=60 | — |
| 4 | main | PRINT | mark=60 | B |

**Additional verification input and complete trace**

```text
Pseudocode
mark ← 40
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

```text
C
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | mark ← 40 | mark=40 | — |
| 2 | main | IF (mark ≥ 80) → FALSE | mark=40 | — |
| 3 | main | IF (mark ≥ 60) → FALSE | mark=40 | — |
| 4 | main | IF (mark ≥ 40) → TRUE | mark=40 | — |
| 5 | main | PRINT | mark=40 | C |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M1-Q15 — Error detection: Sum from one to n — program review

**Category:** boundary/loop

**Fault and root cause:** The inclusive n term is omitted by using end n-1 in the displayed FOR.

**Faulty execution / counterexample:** output: '10'

**Complete corrected program**

```text
Pseudocode
n ← 5
s ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    s ← (s + i)
END FOR
PRINT s
```

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
n ← 0
s ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    s ← (s + i)
END FOR
PRINT s
```

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 0 | n=0 | — |
| 2 | main | s ← 0 | n=0; s=0 | — |
| 3 | main | FOR exit | n=0; s=0 | — |
| 4 | main | PRINT | n=0; s=0 | 0 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M1-Q16 — Error detection: Count decimal digits — program review

**Category:** boundary

**Fault and root cause:** Starting at zero fails to count the remaining one-digit number and makes zero have zero digits.

**Faulty execution / counterexample:** output: '3'

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
n ← 0
count ← 1
WHILE (n ≥ 10)
    count ← (count + 1)
    n ← (n DIV 10)
END WHILE
PRINT count
```

```text
1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 0 | n=0 | — |
| 2 | main | count ← 1 | n=0; count=1 | — |
| 3 | main | WHILE (n ≥ 10) → FALSE | n=0; count=1 | — |
| 4 | main | PRINT | n=0; count=1 | 1 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M1-Q17 — Error detection: Array sum — program review

**Category:** boundary/runtime

**Fault and root cause:** One extra index equals LENGTH(A), beyond the last valid position.

**Faulty execution / counterexample:** IndexError: neutral index out of bounds

**Complete corrected program**

```text
Pseudocode
A ← [3, (−2), 7]
s ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    s ← (s + A[i])
END FOR
PRINT s
```

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
A ← []
s ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    s ← (s + A[i])
END FOR
PRINT s
```

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [] | A=[] | — |
| 2 | main | s ← 0 | A=[]; s=0 | — |
| 3 | main | FOR exit | A=[]; s=0 | — |
| 4 | main | PRINT | A=[]; s=0 | 0 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M1-Q18 — Error detection: Maximum array value — program review

**Category:** boundary/logic

**Fault and root cause:** Invented zero exceeds every all-negative input and may not occur in the array.

**Faulty execution / counterexample:** output: '0'

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
A ← [(−7)]
best ← A[0]
FOR i ← 1 TO (LENGTH(A) − 1) STEP 1
    IF (A[i] > best) THEN
        best ← A[i]
    END IF
END FOR
PRINT best
```

```text
-7
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [(−7)] | A=[-7] | — |
| 2 | main | best ← A[0] | A=[-7]; best=-7 | — |
| 3 | main | FOR exit | A=[-7]; best=-7 | — |
| 4 | main | PRINT | A=[-7]; best=-7 | -7 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M1-Q19 — Error detection: Trial-division prime — program review

**Category:** boundary/logic

**Fault and root cause:** Excluding the square-root divisor classifies prime squares such as 49 incorrectly.

**Faulty execution / counterexample:** output: 'TRUE' (sample masks the fault); boundary program: output: 'TRUE'

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
n ← 49
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

```text
FALSE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 49 | n=49 | — |
| 2 | main | prime ← (n ≥ 2) | n=49; prime=TRUE | — |
| 3 | main | d ← 2 | n=49; prime=TRUE; d=2 | — |
| 4 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=49; prime=TRUE; d=2 | — |
| 5 | main | IF ((n MOD d) = 0) → FALSE | n=49; prime=TRUE; d=2 | — |
| 6 | main | d ← (d + 1) | n=49; prime=TRUE; d=3 | — |
| 7 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=49; prime=TRUE; d=3 | — |
| 8 | main | IF ((n MOD d) = 0) → FALSE | n=49; prime=TRUE; d=3 | — |
| 9 | main | d ← (d + 1) | n=49; prime=TRUE; d=4 | — |
| 10 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=49; prime=TRUE; d=4 | — |
| 11 | main | IF ((n MOD d) = 0) → FALSE | n=49; prime=TRUE; d=4 | — |
| 12 | main | d ← (d + 1) | n=49; prime=TRUE; d=5 | — |
| 13 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=49; prime=TRUE; d=5 | — |
| 14 | main | IF ((n MOD d) = 0) → FALSE | n=49; prime=TRUE; d=5 | — |
| 15 | main | d ← (d + 1) | n=49; prime=TRUE; d=6 | — |
| 16 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=49; prime=TRUE; d=6 | — |
| 17 | main | IF ((n MOD d) = 0) → FALSE | n=49; prime=TRUE; d=6 | — |
| 18 | main | d ← (d + 1) | n=49; prime=TRUE; d=7 | — |
| 19 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=49; prime=TRUE; d=7 | — |
| 20 | main | IF ((n MOD d) = 0) → TRUE | n=49; prime=TRUE; d=7 | — |
| 21 | main | prime ← FALSE | n=49; prime=FALSE; d=7 | — |
| 22 | main | d ← (d + 1) | n=49; prime=FALSE; d=8 | — |
| 23 | main | WHILE (prime AND ((d * d) ≤ n)) → FALSE | n=49; prime=FALSE; d=8 | — |
| 24 | main | PRINT | n=49; prime=FALSE; d=8 | FALSE |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M1-Q20 — Error detection: Binary search — program review

**Category:** loop/termination

**Fault and root cause:** When mid=lo and its value is too small, lo does not advance and the interval repeats.

**Faulty execution / counterexample:** Sample target 11: (lo,hi,mid) is (0,3,1), then (1,3,2), then (2,3,2) forever. A[2]=8 is below 11, but lo stays 2.

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
A ← [2, 5, 8, 11]
target ← 6
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

```text
-1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [2, 5, 8, 11] | A=[2, 5, 8, 11] | — |
| 2 | main | target ← 6 | A=[2, 5, 8, 11]; target=6 | — |
| 3 | main | lo ← 0 | A=[2, 5, 8, 11]; target=6; lo=0 | — |
| 4 | main | hi ← (LENGTH(A) − 1) | A=[2, 5, 8, 11]; target=6; lo=0; hi=3 | — |
| 5 | main | found ← (−1) | A=[2, 5, 8, 11]; target=6; lo=0; hi=3; found=-1 | — |
| 6 | main | WHILE (lo ≤ hi) → TRUE | A=[2, 5, 8, 11]; target=6; lo=0; hi=3; found=-1 | — |
| 7 | main | mid ← (lo + ((hi − lo) DIV 2)) | A=[2, 5, 8, 11]; target=6; lo=0; hi=3; found=-1; mid=1 | — |
| 8 | main | IF (A[mid] = target) → FALSE | A=[2, 5, 8, 11]; target=6; lo=0; hi=3; found=-1; mid=1 | — |
| 9 | main | IF (A[mid] < target) → TRUE | A=[2, 5, 8, 11]; target=6; lo=0; hi=3; found=-1; mid=1 | — |
| 10 | main | lo ← (mid + 1) | A=[2, 5, 8, 11]; target=6; lo=2; hi=3; found=-1; mid=1 | — |
| 11 | main | WHILE (lo ≤ hi) → TRUE | A=[2, 5, 8, 11]; target=6; lo=2; hi=3; found=-1; mid=1 | — |
| 12 | main | mid ← (lo + ((hi − lo) DIV 2)) | A=[2, 5, 8, 11]; target=6; lo=2; hi=3; found=-1; mid=2 | — |
| 13 | main | IF (A[mid] = target) → FALSE | A=[2, 5, 8, 11]; target=6; lo=2; hi=3; found=-1; mid=2 | — |
| 14 | main | IF (A[mid] < target) → FALSE | A=[2, 5, 8, 11]; target=6; lo=2; hi=3; found=-1; mid=2 | — |
| 15 | main | hi ← (mid − 1) | A=[2, 5, 8, 11]; target=6; lo=2; hi=1; found=-1; mid=2 | — |
| 16 | main | WHILE (lo ≤ hi) → FALSE | A=[2, 5, 8, 11]; target=6; lo=2; hi=1; found=-1; mid=2 | — |
| 17 | main | PRINT | A=[2, 5, 8, 11]; target=6; lo=2; hi=1; found=-1; mid=2 | -1 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M1-Q21 — Pseudocode writing: Even or odd

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

## M1-Q22 — Pseudocode writing: Sum from one to n

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

## M1-Q23 — Pseudocode writing: Digit sum

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

## M1-Q24 — Pseudocode writing: Array sum

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

## M1-Q25 — Pseudocode writing: Linear search

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

## M1-Q26 — Logical reasoning: Chain of implications

**Answer: A — P is FALSE**

| Allowed P | Allowed Q | Given R |
| --- | --- | --- |
| FALSE | FALSE | FALSE |

If Q were true, R would be true, contradicting the given fact. Thus Q is false; P must then also be false by contrapositive. Reversing an implication is unnecessary.

## M1-Q27 — Logical reasoning: Sets and existence

**Answer: B — Some blue things are devices**

| Step | Reason | Result |
| --- | --- | --- |
| Some widgets are blue | Choose one witness w | w is a widget and blue |
| All widgets are devices | Apply to w | w is also a device |
| Conclusion | Same witness | Some blue things are devices |

The existential statement supplies an actual witness. The universal statement classifies that witness but says nothing about every device or every blue thing.

## M1-Q28 — Logical reasoning: Three-person ordering

**Answer: A — A**

| Order | A before B | C not first | Valid |
| --- | --- | --- | --- |
| ABC | TRUE | TRUE | TRUE |
| ACB | TRUE | TRUE | TRUE |
| BAC | FALSE | TRUE | FALSE |
| BCA | FALSE | TRUE | FALSE |
| CAB | TRUE | FALSE | FALSE |
| CBA | FALSE | FALSE | FALSE |

Both surviving orders place A first. B and C can exchange later positions.

## M1-Q29 — Logical reasoning: Data sufficiency: exact integer

**Answer: D — Not even together**

| Information | Possible values | Determination |
| --- | --- | --- |
| I alone | …,0,2,4,6,… | Multiple values |
| II alone | 2,3,4 | Multiple values |
| Both | 2,4 | Still multiple |

Two surviving values are enough to disprove unique determination. No hidden positivity or extra constraint may be assumed.

## M1-Q30 — Logical reasoning: Specified sequence rule

**Answer: C — 37**

| n | n² | a_n |
| --- | --- | --- |
| 1 | 1 | 2 |
| 2 | 4 | 5 |
| 3 | 9 | 10 |
| 4 | 16 | 17 |
| 5 | 25 | 26 |
| 6 | 36 | 37 |

Use the supplied rule rather than infer a unique law from a finite sequence. n=6 gives 36+1=37; consecutive differences are 3,5,7,9,11.

# Mock 2 — solutions

## M2-Q01 — Output prediction: CONTINUE skips evens

**Answer: B**

```text
9
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← 0 | s=0 | — |
| 2 | main | FOR visit i | s=0; i=1 | — |
| 3 | main | IF ((i MOD 2) = 0) → FALSE | s=0; i=1 | — |
| 4 | main | s ← (s + i) | s=1; i=1 | — |
| 5 | main | FOR visit i | s=1; i=2 | — |
| 6 | main | IF ((i MOD 2) = 0) → TRUE | s=1; i=2 | — |
| 7 | main | CONTINUE | s=1; i=2 | — |
| 8 | main | FOR visit i | s=1; i=3 | — |
| 9 | main | IF ((i MOD 2) = 0) → FALSE | s=1; i=3 | — |
| 10 | main | s ← (s + i) | s=4; i=3 | — |
| 11 | main | FOR visit i | s=4; i=4 | — |
| 12 | main | IF ((i MOD 2) = 0) → TRUE | s=4; i=4 | — |
| 13 | main | CONTINUE | s=4; i=4 | — |
| 14 | main | FOR visit i | s=4; i=5 | — |
| 15 | main | IF ((i MOD 2) = 0) → FALSE | s=4; i=5 | — |
| 16 | main | s ← (s + i) | s=9; i=5 | — |
| 17 | main | FOR visit i | s=9; i=6 | — |
| 18 | main | IF ((i MOD 2) = 0) → TRUE | s=9; i=6 | — |
| 19 | main | CONTINUE | s=9; i=6 | — |
| 20 | main | FOR exit | s=9; i=6 | — |
| 21 | main | PRINT | s=9; i=6 | 9 |

**Explanation:** Only 1,3,5 are added.

## M2-Q02 — Output prediction: Triangular loop

**Answer: A**

```text
10
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | count ← 0 | count=0 | — |
| 2 | main | FOR visit i | count=0; i=1 | — |
| 3 | main | FOR visit j | count=0; i=1; j=0 | — |
| 4 | main | count ← (count + 1) | count=1; i=1; j=0 | — |
| 5 | main | FOR exit | count=1; i=1; j=0 | — |
| 6 | main | FOR visit i | count=1; i=2; j=0 | — |
| 7 | main | FOR visit j | count=1; i=2; j=0 | — |
| 8 | main | count ← (count + 1) | count=2; i=2; j=0 | — |
| 9 | main | FOR visit j | count=2; i=2; j=1 | — |
| 10 | main | count ← (count + 1) | count=3; i=2; j=1 | — |
| 11 | main | FOR exit | count=3; i=2; j=1 | — |
| 12 | main | FOR visit i | count=3; i=3; j=1 | — |
| 13 | main | FOR visit j | count=3; i=3; j=0 | — |
| 14 | main | count ← (count + 1) | count=4; i=3; j=0 | — |
| 15 | main | FOR visit j | count=4; i=3; j=1 | — |
| 16 | main | count ← (count + 1) | count=5; i=3; j=1 | — |
| 17 | main | FOR visit j | count=5; i=3; j=2 | — |
| 18 | main | count ← (count + 1) | count=6; i=3; j=2 | — |
| 19 | main | FOR exit | count=6; i=3; j=2 | — |
| 20 | main | FOR visit i | count=6; i=4; j=2 | — |
| 21 | main | FOR visit j | count=6; i=4; j=0 | — |
| 22 | main | count ← (count + 1) | count=7; i=4; j=0 | — |
| 23 | main | FOR visit j | count=7; i=4; j=1 | — |
| 24 | main | count ← (count + 1) | count=8; i=4; j=1 | — |
| 25 | main | FOR visit j | count=8; i=4; j=2 | — |
| 26 | main | count ← (count + 1) | count=9; i=4; j=2 | — |
| 27 | main | FOR visit j | count=9; i=4; j=3 | — |
| 28 | main | count ← (count + 1) | count=10; i=4; j=3 | — |
| 29 | main | FOR exit | count=10; i=4; j=3 | — |
| 30 | main | FOR exit | count=10; i=4; j=3 | — |
| 31 | main | PRINT | count=10; i=4; j=3 | 10 |

**Explanation:** Rows contribute 1+2+3+4.

## M2-Q03 — Output prediction: Inner BREAK only

**Answer: C**

```text
6
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | count ← 0 | count=0 | — |
| 2 | main | FOR visit i | count=0; i=0 | — |
| 3 | main | FOR visit j | count=0; i=0; j=0 | — |
| 4 | main | IF (j = 2) → FALSE | count=0; i=0; j=0 | — |
| 5 | main | count ← (count + 1) | count=1; i=0; j=0 | — |
| 6 | main | FOR visit j | count=1; i=0; j=1 | — |
| 7 | main | IF (j = 2) → FALSE | count=1; i=0; j=1 | — |
| 8 | main | count ← (count + 1) | count=2; i=0; j=1 | — |
| 9 | main | FOR visit j | count=2; i=0; j=2 | — |
| 10 | main | IF (j = 2) → TRUE | count=2; i=0; j=2 | — |
| 11 | main | BREAK | count=2; i=0; j=2 | — |
| 12 | main | FOR exit | count=2; i=0; j=2 | — |
| 13 | main | FOR visit i | count=2; i=1; j=2 | — |
| 14 | main | FOR visit j | count=2; i=1; j=0 | — |
| 15 | main | IF (j = 2) → FALSE | count=2; i=1; j=0 | — |
| 16 | main | count ← (count + 1) | count=3; i=1; j=0 | — |
| 17 | main | FOR visit j | count=3; i=1; j=1 | — |
| 18 | main | IF (j = 2) → FALSE | count=3; i=1; j=1 | — |
| 19 | main | count ← (count + 1) | count=4; i=1; j=1 | — |
| 20 | main | FOR visit j | count=4; i=1; j=2 | — |
| 21 | main | IF (j = 2) → TRUE | count=4; i=1; j=2 | — |
| 22 | main | BREAK | count=4; i=1; j=2 | — |
| 23 | main | FOR exit | count=4; i=1; j=2 | — |
| 24 | main | FOR visit i | count=4; i=2; j=2 | — |
| 25 | main | FOR visit j | count=4; i=2; j=0 | — |
| 26 | main | IF (j = 2) → FALSE | count=4; i=2; j=0 | — |
| 27 | main | count ← (count + 1) | count=5; i=2; j=0 | — |
| 28 | main | FOR visit j | count=5; i=2; j=1 | — |
| 29 | main | IF (j = 2) → FALSE | count=5; i=2; j=1 | — |
| 30 | main | count ← (count + 1) | count=6; i=2; j=1 | — |
| 31 | main | FOR visit j | count=6; i=2; j=2 | — |
| 32 | main | IF (j = 2) → TRUE | count=6; i=2; j=2 | — |
| 33 | main | BREAK | count=6; i=2; j=2 | — |
| 34 | main | FOR exit | count=6; i=2; j=2 | — |
| 35 | main | FOR exit | count=6; i=2; j=2 | — |
| 36 | main | PRINT | count=6; i=2; j=2 | 6 |

**Explanation:** Each row counts j=0,1; outer loop continues.

## M2-Q04 — Output prediction: Array mutation feeds next step

**Answer: A**

```text
[1, 3, 6, 10]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [1, 2, 3, 4] | A=[1, 2, 3, 4] | — |
| 2 | main | FOR visit i | A=[1, 2, 3, 4]; i=1 | — |
| 3 | main | A[i] ← (A[i] + A[(i − 1)]) | A=[1, 3, 3, 4]; i=1 | — |
| 4 | main | FOR visit i | A=[1, 3, 3, 4]; i=2 | — |
| 5 | main | A[i] ← (A[i] + A[(i − 1)]) | A=[1, 3, 6, 4]; i=2 | — |
| 6 | main | FOR visit i | A=[1, 3, 6, 4]; i=3 | — |
| 7 | main | A[i] ← (A[i] + A[(i − 1)]) | A=[1, 3, 6, 10]; i=3 | — |
| 8 | main | FOR exit | A=[1, 3, 6, 10]; i=3 | — |
| 9 | main | PRINT | A=[1, 3, 6, 10]; i=3 | [1, 3, 6, 10] |

**Explanation:** Previous elements have already changed, creating prefix sums.

## M2-Q05 — Output prediction: Array alias

**Answer: A**

```text
[3, 9] [3, 9]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [3, 4] | A=[3, 4] | — |
| 2 | main | B ← A | A=[3, 4]; B=[3, 4] | — |
| 3 | main | B[1] ← 9 | A=[3, 9]; B=[3, 9] | — |
| 4 | main | PRINT | A=[3, 9]; B=[3, 9] | [3, 9] [3, 9] |

**Explanation:** Both variables refer to the same array.

## M2-Q06 — Output prediction: One bubble pass

**Answer: D**

```text
[1, 3, 2, 4]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [4, 1, 3, 2] | A=[4, 1, 3, 2] | — |
| 2 | main | FOR visit j | A=[4, 1, 3, 2]; j=0 | — |
| 3 | main | IF (A[j] > A[(j + 1)]) → TRUE | A=[4, 1, 3, 2]; j=0 | — |
| 4 | main | t ← A[j] | A=[4, 1, 3, 2]; j=0; t=4 | — |
| 5 | main | A[j] ← A[(j + 1)] | A=[1, 1, 3, 2]; j=0; t=4 | — |
| 6 | main | A[(j + 1)] ← t | A=[1, 4, 3, 2]; j=0; t=4 | — |
| 7 | main | FOR visit j | A=[1, 4, 3, 2]; j=1; t=4 | — |
| 8 | main | IF (A[j] > A[(j + 1)]) → TRUE | A=[1, 4, 3, 2]; j=1; t=4 | — |
| 9 | main | t ← A[j] | A=[1, 4, 3, 2]; j=1; t=4 | — |
| 10 | main | A[j] ← A[(j + 1)] | A=[1, 3, 3, 2]; j=1; t=4 | — |
| 11 | main | A[(j + 1)] ← t | A=[1, 3, 4, 2]; j=1; t=4 | — |
| 12 | main | FOR visit j | A=[1, 3, 4, 2]; j=2; t=4 | — |
| 13 | main | IF (A[j] > A[(j + 1)]) → TRUE | A=[1, 3, 4, 2]; j=2; t=4 | — |
| 14 | main | t ← A[j] | A=[1, 3, 4, 2]; j=2; t=4 | — |
| 15 | main | A[j] ← A[(j + 1)] | A=[1, 3, 2, 2]; j=2; t=4 | — |
| 16 | main | A[(j + 1)] ← t | A=[1, 3, 2, 4]; j=2; t=4 | — |
| 17 | main | FOR exit | A=[1, 3, 2, 4]; j=2; t=4 | — |
| 18 | main | PRINT | A=[1, 3, 2, 4]; j=2; t=4 | [1, 3, 2, 4] |

**Explanation:** One pass settles the largest, not necessarily all elements.

## M2-Q07 — Output prediction: Binary search successful

**Answer: C**

```text
3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [1, 4, 6, 9, 12] | A=[1, 4, 6, 9, 12] | — |
| 2 | main | lo ← 0 | A=[1, 4, 6, 9, 12]; lo=0 | — |
| 3 | main | hi ← 4 | A=[1, 4, 6, 9, 12]; lo=0; hi=4 | — |
| 4 | main | answer ← (−1) | A=[1, 4, 6, 9, 12]; lo=0; hi=4; answer=-1 | — |
| 5 | main | WHILE (lo ≤ hi) → TRUE | A=[1, 4, 6, 9, 12]; lo=0; hi=4; answer=-1 | — |
| 6 | main | mid ← (lo + ((hi − lo) DIV 2)) | A=[1, 4, 6, 9, 12]; lo=0; hi=4; answer=-1; mid=2 | — |
| 7 | main | IF (A[mid] = 9) → FALSE | A=[1, 4, 6, 9, 12]; lo=0; hi=4; answer=-1; mid=2 | — |
| 8 | main | IF (A[mid] < 9) → TRUE | A=[1, 4, 6, 9, 12]; lo=0; hi=4; answer=-1; mid=2 | — |
| 9 | main | lo ← (mid + 1) | A=[1, 4, 6, 9, 12]; lo=3; hi=4; answer=-1; mid=2 | — |
| 10 | main | WHILE (lo ≤ hi) → TRUE | A=[1, 4, 6, 9, 12]; lo=3; hi=4; answer=-1; mid=2 | — |
| 11 | main | mid ← (lo + ((hi − lo) DIV 2)) | A=[1, 4, 6, 9, 12]; lo=3; hi=4; answer=-1; mid=3 | — |
| 12 | main | IF (A[mid] = 9) → TRUE | A=[1, 4, 6, 9, 12]; lo=3; hi=4; answer=-1; mid=3 | — |
| 13 | main | answer ← mid | A=[1, 4, 6, 9, 12]; lo=3; hi=4; answer=3; mid=3 | — |
| 14 | main | BREAK | A=[1, 4, 6, 9, 12]; lo=3; hi=4; answer=3; mid=3 | — |
| 15 | main | PRINT | A=[1, 4, 6, 9, 12]; lo=3; hi=4; answer=3; mid=3 | 3 |

**Explanation:** Inspect index 2 then index 3.

## M2-Q08 — Output prediction: Matrix row total

**Answer: B**

```text
7
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | M ← [[2, 1], [3, 4]] | M=[[2, 1], [3, 4]] | — |
| 2 | main | s ← 0 | M=[[2, 1], [3, 4]]; s=0 | — |
| 3 | main | FOR visit c | M=[[2, 1], [3, 4]]; s=0; c=0 | — |
| 4 | main | s ← (s + M[1][c]) | M=[[2, 1], [3, 4]]; s=3; c=0 | — |
| 5 | main | FOR visit c | M=[[2, 1], [3, 4]]; s=3; c=1 | — |
| 6 | main | s ← (s + M[1][c]) | M=[[2, 1], [3, 4]]; s=7; c=1 | — |
| 7 | main | FOR exit | M=[[2, 1], [3, 4]]; s=7; c=1 | — |
| 8 | main | PRINT | M=[[2, 1], [3, 4]]; s=7; c=1 | 7 |

**Explanation:** Row index 1 is the second row.

## M2-Q09 — Output prediction: Scalar parameter value

**Answer: D**

```text
2 7
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 2 | a=2 | — |
| 2 | change depth 1 | ENTER | x=2 | — |
| 3 | change depth 1 | x ← (x + 5) | x=7 | — |
| 4 | change depth 1 | RETURN 7 | x=7 | — |
| 5 | main | b ← change(a) | a=2; b=7 | — |
| 6 | main | PRINT | a=2; b=7 | 2 7 |

**Explanation:** Local scalar reassignment does not change caller a.

## M2-Q10 — Output prediction: Recursive factorial trace

**Answer: D**

```text
24
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | f depth 1 | ENTER | n=4 | — |
| 2 | f depth 1 | IF (n ≤ 1) → FALSE | n=4 | — |
| 3 | f depth 2 | ENTER | n=3 | — |
| 4 | f depth 2 | IF (n ≤ 1) → FALSE | n=3 | — |
| 5 | f depth 3 | ENTER | n=2 | — |
| 6 | f depth 3 | IF (n ≤ 1) → FALSE | n=2 | — |
| 7 | f depth 4 | ENTER | n=1 | — |
| 8 | f depth 4 | IF (n ≤ 1) → TRUE | n=1 | — |
| 9 | f depth 4 | RETURN 1 | n=1 | — |
| 10 | f depth 3 | RETURN 2 | n=2 | — |
| 11 | f depth 2 | RETURN 6 | n=3 | — |
| 12 | f depth 1 | RETURN 24 | n=4 | — |
| 13 | main | PRINT | — | 24 |

**Explanation:** Return values unwind 1,2,6,24.

## M2-Q11 — Output prediction: Eight-bit complement

**Answer: D**

```text
250
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | PRINT | — | 250 |

**Explanation:** 00000101 becomes 11111010; width is explicitly eight bits.

## M2-Q12 — Output prediction: Negative-only maximum

**Answer: C**

```text
-2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [(−4), (−9), (−2)] | A=[-4, -9, -2] | — |
| 2 | main | best ← A[0] | A=[-4, -9, -2]; best=-4 | — |
| 3 | main | FOR visit i | A=[-4, -9, -2]; best=-4; i=1 | — |
| 4 | main | IF (A[i] > best) → FALSE | A=[-4, -9, -2]; best=-4; i=1 | — |
| 5 | main | FOR visit i | A=[-4, -9, -2]; best=-4; i=2 | — |
| 6 | main | IF (A[i] > best) → TRUE | A=[-4, -9, -2]; best=-4; i=2 | — |
| 7 | main | best ← A[i] | A=[-4, -9, -2]; best=-2; i=2 | — |
| 8 | main | FOR exit | A=[-4, -9, -2]; best=-2; i=2 | — |
| 9 | main | PRINT | A=[-4, -9, -2]; best=-2; i=2 | -2 |

**Explanation:** Maximum starts from an actual element, not invented zero.

## M2-Q13 — Error detection: Leap year — program review

**Category:** logic

**Fault and root cause:** The two qualifying leap-year routes are alternatives, not simultaneous requirements.

**Faulty execution / counterexample:** output: 'FALSE' (sample masks the fault); boundary program: output: 'FALSE'

**Complete corrected program**

```text
Pseudocode
year ← 1900
leap ← (((year MOD 400) = 0) OR (((year MOD 4) = 0) AND ((year MOD 100) ≠ 0)))
PRINT leap
```

**Corrected sample output**

```text
FALSE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | year ← 1900 | year=1900 | — |
| 2 | main | leap ← (((year MOD 400) = 0) OR (((year MOD 4) = 0) AND ((year MOD 100) ≠ 0))) | year=1900; leap=FALSE | — |
| 3 | main | PRINT | year=1900; leap=FALSE | FALSE |

**Additional verification input and complete trace**

```text
Pseudocode
year ← 2024
leap ← (((year MOD 400) = 0) OR (((year MOD 4) = 0) AND ((year MOD 100) ≠ 0)))
PRINT leap
```

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | year ← 2024 | year=2024 | — |
| 2 | main | leap ← (((year MOD 400) = 0) OR (((year MOD 4) = 0) AND ((year MOD 100) ≠ 0))) | year=2024; leap=TRUE | — |
| 3 | main | PRINT | year=2024; leap=TRUE | TRUE |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M2-Q14 — Error detection: Fibonacci term — program review

**Category:** logic

**Fault and root cause:** a has already become old b; using a+b now adds old b twice.

**Faulty execution / counterexample:** output: '64'

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
n ← 0
a ← 0
b ← 1
FOR i ← 0 TO (n − 1) STEP 1
    nxt ← (a + b)
    a ← b
    b ← nxt
END FOR
PRINT a
```

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 0 | n=0 | — |
| 2 | main | a ← 0 | n=0; a=0 | — |
| 3 | main | b ← 1 | n=0; a=0; b=1 | — |
| 4 | main | FOR exit | n=0; a=0; b=1 | — |
| 5 | main | PRINT | n=0; a=0; b=1 | 0 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M2-Q15 — Error detection: Second distinct largest — program review

**Category:** logic

**Fault and root cause:** This selects another copy of the maximum instead of the second distinct value.

**Faulty execution / counterexample:** output: '8'

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
A ← [4, 4]
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

```text
NONE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [4, 4] | A=[4, 4] | — |
| 2 | main | B ← SORTED(A) | A=[4, 4]; B=[4, 4] | — |
| 3 | main | answer ← "NONE" | A=[4, 4]; B=[4, 4]; answer=NONE | — |
| 4 | main | IF (LENGTH(B) ≥ 2) → TRUE | A=[4, 4]; B=[4, 4]; answer=NONE | — |
| 5 | main | largest ← B[(LENGTH(B) − 1)] | A=[4, 4]; B=[4, 4]; answer=NONE; largest=4 | — |
| 6 | main | i ← (LENGTH(B) − 2) | A=[4, 4]; B=[4, 4]; answer=NONE; largest=4; i=0 | — |
| 7 | main | WHILE (i ≥ 0) → TRUE | A=[4, 4]; B=[4, 4]; answer=NONE; largest=4; i=0 | — |
| 8 | main | IF (B[i] ≠ largest) → FALSE | A=[4, 4]; B=[4, 4]; answer=NONE; largest=4; i=0 | — |
| 9 | main | i ← (i − 1) | A=[4, 4]; B=[4, 4]; answer=NONE; largest=4; i=-1 | — |
| 10 | main | WHILE (i ≥ 0) → FALSE | A=[4, 4]; B=[4, 4]; answer=NONE; largest=4; i=-1 | — |
| 11 | main | PRINT | A=[4, 4]; B=[4, 4]; answer=NONE; largest=4; i=-1 | NONE |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M2-Q16 — Error detection: Vowel count — program review

**Category:** logic

**Fault and root cause:** Uppercase vowels are never normalized, so an explicitly case-insensitive count undercounts.

**Faulty execution / counterexample:** output: '2'

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
s ← "AEIOU"
s ← LOWER(s)
count ← 0
FOR i ← 0 TO (LENGTH(s) − 1) STEP 1
    IF (s[i] IS_IN "aeiou") THEN
        count ← (count + 1)
    END IF
END FOR
PRINT count
```

```text
5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "AEIOU" | s=AEIOU | — |
| 2 | main | s ← LOWER(s) | s=aeiou | — |
| 3 | main | count ← 0 | s=aeiou; count=0 | — |
| 4 | main | FOR visit i | s=aeiou; count=0; i=0 | — |
| 5 | main | IF (s[i] IS_IN "aeiou") → TRUE | s=aeiou; count=0; i=0 | — |
| 6 | main | count ← (count + 1) | s=aeiou; count=1; i=0 | — |
| 7 | main | FOR visit i | s=aeiou; count=1; i=1 | — |
| 8 | main | IF (s[i] IS_IN "aeiou") → TRUE | s=aeiou; count=1; i=1 | — |
| 9 | main | count ← (count + 1) | s=aeiou; count=2; i=1 | — |
| 10 | main | FOR visit i | s=aeiou; count=2; i=2 | — |
| 11 | main | IF (s[i] IS_IN "aeiou") → TRUE | s=aeiou; count=2; i=2 | — |
| 12 | main | count ← (count + 1) | s=aeiou; count=3; i=2 | — |
| 13 | main | FOR visit i | s=aeiou; count=3; i=3 | — |
| 14 | main | IF (s[i] IS_IN "aeiou") → TRUE | s=aeiou; count=3; i=3 | — |
| 15 | main | count ← (count + 1) | s=aeiou; count=4; i=3 | — |
| 16 | main | FOR visit i | s=aeiou; count=4; i=4 | — |
| 17 | main | IF (s[i] IS_IN "aeiou") → TRUE | s=aeiou; count=4; i=4 | — |
| 18 | main | count ← (count + 1) | s=aeiou; count=5; i=4 | — |
| 19 | main | FOR exit | s=aeiou; count=5; i=4 | — |
| 20 | main | PRINT | s=aeiou; count=5; i=4 | 5 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M2-Q17 — Error detection: Matrix sum — program review

**Category:** boundary/logic

**Fault and root cause:** The column limit is taken from row count; rectangular matrices lose cells or go out of bounds.

**Faulty execution / counterexample:** output: '12'

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
M ← [[]]
s ← 0
FOR r ← 0 TO (LENGTH(M) − 1) STEP 1
    FOR c ← 0 TO (LENGTH(M[r]) − 1) STEP 1
        s ← (s + M[r][c])
    END FOR
END FOR
PRINT s
```

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | M ← [[]] | M=[[]] | — |
| 2 | main | s ← 0 | M=[[]]; s=0 | — |
| 3 | main | FOR visit r | M=[[]]; s=0; r=0 | — |
| 4 | main | FOR exit | M=[[]]; s=0; r=0 | — |
| 5 | main | FOR exit | M=[[]]; s=0; r=0 | — |
| 6 | main | PRINT | M=[[]]; s=0; r=0 | 0 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M2-Q18 — Error detection: Transpose a rectangle — program review

**Category:** boundary/runtime

**Fault and root cause:** Coordinates are read backwards; a rectangle exposes an invalid row index.

**Faulty execution / counterexample:** IndexError: neutral index out of bounds

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
M ← [[7]]
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

```text
[[7]]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | M ← [[7]] | M=[[7]] | — |
| 2 | main | T ← [] | M=[[7]]; T=[] | — |
| 3 | main | FOR visit c | M=[[7]]; T=[]; c=0 | — |
| 4 | main | row ← [] | M=[[7]]; T=[]; c=0; row=[] | — |
| 5 | main | FOR visit r | M=[[7]]; T=[]; c=0; row=[]; r=0 | — |
| 6 | main | APPEND(row, M[r][c]) | M=[[7]]; T=[]; c=0; row=[7]; r=0 | — |
| 7 | main | FOR exit | M=[[7]]; T=[]; c=0; row=[7]; r=0 | — |
| 8 | main | APPEND(T, row) | M=[[7]]; T=[[7]]; c=0; row=[7]; r=0 | — |
| 9 | main | FOR exit | M=[[7]]; T=[[7]]; c=0; row=[7]; r=0 | — |
| 10 | main | PRINT | M=[[7]]; T=[[7]]; c=0; row=[7]; r=0 | [[7]] |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M2-Q19 — Error detection: Power of two — program review

**Category:** boundary

**Fault and root cause:** One equals 2^0 and is a positive power of two. The guard must include one while excluding zero.

**Faulty execution / counterexample:** output: 'TRUE' (sample masks the fault); boundary program: output: 'FALSE'

**Complete corrected program**

```text
Pseudocode
x ← 16
answer ← ((x > 0) AND ((x BIT_AND (x − 1)) = 0))
PRINT answer
```

**Corrected sample output**

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 16 | x=16 | — |
| 2 | main | answer ← ((x > 0) AND ((x BIT_AND (x − 1)) = 0)) | x=16; answer=TRUE | — |
| 3 | main | PRINT | x=16; answer=TRUE | TRUE |

**Additional verification input and complete trace**

```text
Pseudocode
x ← 1
answer ← ((x > 0) AND ((x BIT_AND (x − 1)) = 0))
PRINT answer
```

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 1 | x=1 | — |
| 2 | main | answer ← ((x > 0) AND ((x BIT_AND (x − 1)) = 0)) | x=1; answer=TRUE | — |
| 3 | main | PRINT | x=1; answer=TRUE | TRUE |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M2-Q20 — Error detection: Remove sorted duplicates — program review

**Category:** logic

**Fault and root cause:** The condition must accept the first value unconditionally; AND can evaluate an invalid previous index and rejects later changes.

**Faulty execution / counterexample:** IndexError: neutral index out of bounds

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
A ← []
B ← []
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    IF ((i = 0) OR (A[i] ≠ A[(i − 1)])) THEN
        APPEND(B, A[i])
    END IF
END FOR
PRINT B
```

```text
[]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [] | A=[] | — |
| 2 | main | B ← [] | A=[]; B=[] | — |
| 3 | main | FOR exit | A=[]; B=[] | — |
| 4 | main | PRINT | A=[]; B=[] | [] |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M2-Q21 — Pseudocode writing: Reverse array in place

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

## M2-Q22 — Pseudocode writing: String palindrome

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

## M2-Q23 — Pseudocode writing: Trial-division prime

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

## M2-Q24 — Pseudocode writing: Bubble sort

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

## M2-Q25 — Pseudocode writing: Binary search

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

## M2-Q26 — Logical reasoning: Count satisfying assignments

**Answer: B — 2**

| P | Q | P OR Q | P AND Q | Expression |
| --- | --- | --- | --- | --- |
| FALSE | FALSE | FALSE | FALSE | FALSE |
| FALSE | TRUE | TRUE | FALSE | TRUE |
| TRUE | FALSE | TRUE | FALSE | TRUE |
| TRUE | TRUE | TRUE | TRUE | FALSE |

Exactly one input must be true. The two rows are (FALSE,TRUE) and (TRUE,FALSE).

## M2-Q27 — Logical reasoning: Four-person ordering count

**Answer: B — 1**

| D-last candidate | A before B | B before C | Valid |
| --- | --- | --- | --- |
| ABCD | TRUE | TRUE | TRUE |
| ACBD | TRUE | FALSE | FALSE |
| BACD | FALSE | TRUE | FALSE |
| BCAD | FALSE | TRUE | FALSE |
| CABD | TRUE | FALSE | FALSE |
| CBAD | FALSE | FALSE | FALSE |

D consumes the last position. The remaining three have a fixed relative order A,B,C, giving exactly one arrangement.

## M2-Q28 — Logical reasoning: Grid-path counting

**Answer: B — 6**

| Candidate | Move string |
| --- | --- |
| 1 | DDRR |
| 2 | DRDR |
| 3 | DRRD |
| 4 | RDDR |
| 5 | RDRD |
| 6 | RRDD |

Choose the two of four positions occupied by R: 4 choose 2=6. Equal letters are indistinguishable, so 4! alone would overcount.

## M2-Q29 — Logical reasoning: Digit constraints

**Answer: C — 63**

| Equation/result | Reason |
| --- | --- |
| a+b=9 | sum rule |
| a-b=3 | difference rule |
| 2a=12 | add equations |
| a=6,b=3 | substitute |
| 10a+b=63 | reconstruct |

The tens digit is a, not b. Reversed 36 meets the sum but violates the direction of the difference.

## M2-Q30 — Logical reasoning: Sufficiency of a yes/no answer

**Answer: A — I alone; II not**

| Information | Check | Conclusion |
| --- | --- | --- |
| I alone | Odd n has no factor 2 | Always NO |
| II alone | n=3→NO; n=6→YES | Not determined |
| Both | Odd multiple of 3 | NO already follows from I |

Determining a yes/no question includes guaranteeing NO. I alone rules out divisibility by 6, even without an exact value of n.

# Mock 3 — solutions

## M3-Q01 — Output prediction: Print on descent

**Answer: D**

```text
3
2
1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | f depth 1 | ENTER | n=3 | — |
| 2 | f depth 1 | IF (n = 0) → FALSE | n=3 | — |
| 3 | f depth 1 | PRINT | n=3 | 3 |
| 4 | f depth 2 | ENTER | n=2 | — |
| 5 | f depth 2 | IF (n = 0) → FALSE | n=2 | — |
| 6 | f depth 2 | PRINT | n=2 | 2 |
| 7 | f depth 3 | ENTER | n=1 | — |
| 8 | f depth 3 | IF (n = 0) → FALSE | n=1 | — |
| 9 | f depth 3 | PRINT | n=1 | 1 |
| 10 | f depth 4 | ENTER | n=0 | — |
| 11 | f depth 4 | IF (n = 0) → TRUE | n=0 | — |
| 12 | f depth 4 | RETURN 0 | n=0 | — |
| 13 | f depth 3 | RETURN 0 | n=1 | — |
| 14 | f depth 2 | RETURN 0 | n=2 | — |
| 15 | f depth 1 | RETURN 0 | n=3 | — |
| 16 | main | f(3) | — | — |

**Explanation:** Printing happens before the recursive call.

## M3-Q02 — Output prediction: Print on return

**Answer: B**

```text
1
2
3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | f depth 1 | ENTER | n=3 | — |
| 2 | f depth 1 | IF (n = 0) → FALSE | n=3 | — |
| 3 | f depth 2 | ENTER | n=2 | — |
| 4 | f depth 2 | IF (n = 0) → FALSE | n=2 | — |
| 5 | f depth 3 | ENTER | n=1 | — |
| 6 | f depth 3 | IF (n = 0) → FALSE | n=1 | — |
| 7 | f depth 4 | ENTER | n=0 | — |
| 8 | f depth 4 | IF (n = 0) → TRUE | n=0 | — |
| 9 | f depth 4 | RETURN 0 | n=0 | — |
| 10 | f depth 3 | f((n − 1)) | n=1 | — |
| 11 | f depth 3 | PRINT | n=1 | 1 |
| 12 | f depth 3 | RETURN 1 | n=1 | — |
| 13 | f depth 2 | f((n − 1)) | n=2 | — |
| 14 | f depth 2 | PRINT | n=2 | 2 |
| 15 | f depth 2 | RETURN 2 | n=2 | — |
| 16 | f depth 1 | f((n − 1)) | n=3 | — |
| 17 | f depth 1 | PRINT | n=3 | 3 |
| 18 | f depth 1 | RETURN 3 | n=3 | — |
| 19 | main | f(3) | — | — |

**Explanation:** Pending prints execute while the stack unwinds.

## M3-Q03 — Output prediction: Two recursive branches

**Answer: A**

```text
5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | f depth 1 | ENTER | n=5 | — |
| 2 | f depth 1 | IF (n ≤ 1) → FALSE | n=5 | — |
| 3 | f depth 2 | ENTER | n=4 | — |
| 4 | f depth 2 | IF (n ≤ 1) → FALSE | n=4 | — |
| 5 | f depth 3 | ENTER | n=3 | — |
| 6 | f depth 3 | IF (n ≤ 1) → FALSE | n=3 | — |
| 7 | f depth 4 | ENTER | n=2 | — |
| 8 | f depth 4 | IF (n ≤ 1) → FALSE | n=2 | — |
| 9 | f depth 5 | ENTER | n=1 | — |
| 10 | f depth 5 | IF (n ≤ 1) → TRUE | n=1 | — |
| 11 | f depth 5 | RETURN 1 | n=1 | — |
| 12 | f depth 5 | ENTER | n=0 | — |
| 13 | f depth 5 | IF (n ≤ 1) → TRUE | n=0 | — |
| 14 | f depth 5 | RETURN 0 | n=0 | — |
| 15 | f depth 4 | RETURN 1 | n=2 | — |
| 16 | f depth 4 | ENTER | n=1 | — |
| 17 | f depth 4 | IF (n ≤ 1) → TRUE | n=1 | — |
| 18 | f depth 4 | RETURN 1 | n=1 | — |
| 19 | f depth 3 | RETURN 2 | n=3 | — |
| 20 | f depth 3 | ENTER | n=2 | — |
| 21 | f depth 3 | IF (n ≤ 1) → FALSE | n=2 | — |
| 22 | f depth 4 | ENTER | n=1 | — |
| 23 | f depth 4 | IF (n ≤ 1) → TRUE | n=1 | — |
| 24 | f depth 4 | RETURN 1 | n=1 | — |
| 25 | f depth 4 | ENTER | n=0 | — |
| 26 | f depth 4 | IF (n ≤ 1) → TRUE | n=0 | — |
| 27 | f depth 4 | RETURN 0 | n=0 | — |
| 28 | f depth 3 | RETURN 1 | n=2 | — |
| 29 | f depth 2 | RETURN 3 | n=4 | — |
| 30 | f depth 2 | ENTER | n=3 | — |
| 31 | f depth 2 | IF (n ≤ 1) → FALSE | n=3 | — |
| 32 | f depth 3 | ENTER | n=2 | — |
| 33 | f depth 3 | IF (n ≤ 1) → FALSE | n=2 | — |
| 34 | f depth 4 | ENTER | n=1 | — |
| 35 | f depth 4 | IF (n ≤ 1) → TRUE | n=1 | — |
| 36 | f depth 4 | RETURN 1 | n=1 | — |
| 37 | f depth 4 | ENTER | n=0 | — |
| 38 | f depth 4 | IF (n ≤ 1) → TRUE | n=0 | — |
| 39 | f depth 4 | RETURN 0 | n=0 | — |
| 40 | f depth 3 | RETURN 1 | n=2 | — |
| 41 | f depth 3 | ENTER | n=1 | — |
| 42 | f depth 3 | IF (n ≤ 1) → TRUE | n=1 | — |
| 43 | f depth 3 | RETURN 1 | n=1 | — |
| 44 | f depth 2 | RETURN 2 | n=3 | — |
| 45 | f depth 1 | RETURN 5 | n=5 | — |
| 46 | main | PRINT | — | 5 |

**Explanation:** Both branches contribute; base values are 0 and 1.

## M3-Q04 — Output prediction: Recursive halving

**Answer: A**

```text
4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | f depth 1 | ENTER | n=10 | — |
| 2 | f depth 1 | IF (n = 0) → FALSE | n=10 | — |
| 3 | f depth 2 | ENTER | n=5 | — |
| 4 | f depth 2 | IF (n = 0) → FALSE | n=5 | — |
| 5 | f depth 3 | ENTER | n=2 | — |
| 6 | f depth 3 | IF (n = 0) → FALSE | n=2 | — |
| 7 | f depth 4 | ENTER | n=1 | — |
| 8 | f depth 4 | IF (n = 0) → FALSE | n=1 | — |
| 9 | f depth 5 | ENTER | n=0 | — |
| 10 | f depth 5 | IF (n = 0) → TRUE | n=0 | — |
| 11 | f depth 5 | RETURN 0 | n=0 | — |
| 12 | f depth 4 | RETURN 1 | n=1 | — |
| 13 | f depth 3 | RETURN 2 | n=2 | — |
| 14 | f depth 2 | RETURN 3 | n=5 | — |
| 15 | f depth 1 | RETURN 4 | n=10 | — |
| 16 | main | PRINT | — | 4 |

**Explanation:** Calls 10,5,2,1 contribute 1 each; 0 contributes 0.

## M3-Q05 — Output prediction: XOR cancellation

**Answer: D**

```text
9
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [6, 2, 6, 9, 2] | A=[6, 2, 6, 9, 2] | — |
| 2 | main | x ← 0 | A=[6, 2, 6, 9, 2]; x=0 | — |
| 3 | main | FOR visit i | A=[6, 2, 6, 9, 2]; x=0; i=0 | — |
| 4 | main | x ← (x BIT_XOR A[i]) | A=[6, 2, 6, 9, 2]; x=6; i=0 | — |
| 5 | main | FOR visit i | A=[6, 2, 6, 9, 2]; x=6; i=1 | — |
| 6 | main | x ← (x BIT_XOR A[i]) | A=[6, 2, 6, 9, 2]; x=4; i=1 | — |
| 7 | main | FOR visit i | A=[6, 2, 6, 9, 2]; x=4; i=2 | — |
| 8 | main | x ← (x BIT_XOR A[i]) | A=[6, 2, 6, 9, 2]; x=2; i=2 | — |
| 9 | main | FOR visit i | A=[6, 2, 6, 9, 2]; x=2; i=3 | — |
| 10 | main | x ← (x BIT_XOR A[i]) | A=[6, 2, 6, 9, 2]; x=11; i=3 | — |
| 11 | main | FOR visit i | A=[6, 2, 6, 9, 2]; x=11; i=4 | — |
| 12 | main | x ← (x BIT_XOR A[i]) | A=[6, 2, 6, 9, 2]; x=9; i=4 | — |
| 13 | main | FOR exit | A=[6, 2, 6, 9, 2]; x=9; i=4 | — |
| 14 | main | PRINT | A=[6, 2, 6, 9, 2]; x=9; i=4 | 9 |

**Explanation:** Each paired value cancels, leaving 9.

## M3-Q06 — Output prediction: Clear set bits

**Answer: A**

```text
3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 14 | x=14 | — |
| 2 | main | count ← 0 | x=14; count=0 | — |
| 3 | main | WHILE (x > 0) → TRUE | x=14; count=0 | — |
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

**Explanation:** 1110→1100→1000→0000.

## M3-Q07 — Output prediction: Numeric reversal drops zeros

**Answer: B**

```text
21
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 1200 | n=1200 | — |
| 2 | main | r ← 0 | n=1200; r=0 | — |
| 3 | main | WHILE (n > 0) → TRUE | n=1200; r=0 | — |
| 4 | main | r ← ((r * 10) + (n MOD 10)) | n=1200; r=0 | — |
| 5 | main | n ← (n DIV 10) | n=120; r=0 | — |
| 6 | main | WHILE (n > 0) → TRUE | n=120; r=0 | — |
| 7 | main | r ← ((r * 10) + (n MOD 10)) | n=120; r=0 | — |
| 8 | main | n ← (n DIV 10) | n=12; r=0 | — |
| 9 | main | WHILE (n > 0) → TRUE | n=12; r=0 | — |
| 10 | main | r ← ((r * 10) + (n MOD 10)) | n=12; r=2 | — |
| 11 | main | n ← (n DIV 10) | n=1; r=2 | — |
| 12 | main | WHILE (n > 0) → TRUE | n=1; r=2 | — |
| 13 | main | r ← ((r * 10) + (n MOD 10)) | n=1; r=21 | — |
| 14 | main | n ← (n DIV 10) | n=0; r=21 | — |
| 15 | main | WHILE (n > 0) → FALSE | n=0; r=21 | — |
| 16 | main | PRINT | n=0; r=21 | 21 |

**Explanation:** Initial extracted zeros do not add leading positions to an integer.

## M3-Q08 — Output prediction: Parity-filtered triangle n=2

**Answer: B**

```text
2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | count ← 0 | count=0 | — |
| 2 | main | FOR visit i | count=0; i=1 | — |
| 3 | main | FOR visit j | count=0; i=1; j=1 | — |
| 4 | main | IF (((i + j) MOD 2) = 0) → TRUE | count=0; i=1; j=1 | — |
| 5 | main | count ← (count + 1) | count=1; i=1; j=1 | — |
| 6 | main | FOR exit | count=1; i=1; j=1 | — |
| 7 | main | FOR visit i | count=1; i=2; j=1 | — |
| 8 | main | FOR visit j | count=1; i=2; j=1 | — |
| 9 | main | IF (((i + j) MOD 2) = 0) → FALSE | count=1; i=2; j=1 | — |
| 10 | main | FOR visit j | count=1; i=2; j=2 | — |
| 11 | main | IF (((i + j) MOD 2) = 0) → TRUE | count=1; i=2; j=2 | — |
| 12 | main | count ← (count + 1) | count=2; i=2; j=2 | — |
| 13 | main | FOR exit | count=2; i=2; j=2 | — |
| 14 | main | FOR exit | count=2; i=2; j=2 | — |
| 15 | main | PRINT | count=2; i=2; j=2 | 2 |

**Explanation:** Only pairs of equal parity contribute; the inner bound depends on the row.

## M3-Q09 — Output prediction: Java left-to-right increments

**Answer: D**

```text
6 4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 2 | x=2 | — |
| 2 | main | a ← x | x=2; a=2 | — |
| 3 | main | x ← (x + 1) | x=3; a=2 | — |
| 4 | main | x ← (x + 1) | x=4; a=2 | — |
| 5 | main | b ← x | x=4; a=2; b=4 | — |
| 6 | main | y ← (a + b) | x=4; a=2; b=4; y=6 | — |
| 7 | main | PRINT | x=4; a=2; b=4; y=6 | 6 4 |

**Explanation:** Java evaluates the left operand x++ first, then ++x. This expression must not be transplanted to C.

The table separates side effects into their evaluation order. The displayed program above follows Java rules; the reference model is used only for verification.

## M3-Q10 — Output prediction: Java AND short-circuit

**Answer: B**

```text
false 0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 0 | x=0 | — |
| 2 | main | flag ← FALSE | x=0; flag=FALSE | — |
| 3 | main | PRINT | x=0; flag=FALSE | false 0 |

**Explanation:** The false first operand skips ++x entirely; Java prints lowercase false.

The table separates side effects into their evaluation order. The displayed program above follows Java rules; the reference model is used only for verification.

## M3-Q11 — Output prediction: Python double unary plus

**Answer: C**

```text
4 4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 4 | x=4 | — |
| 2 | main | y ← (+(+x)) | x=4; y=4 | — |
| 3 | main | PRINT | x=4; y=4 | 4 4 |

**Explanation:** ++x is two unary plus signs, not increment.

The table separates side effects into their evaluation order. The displayed program above follows Python rules; the reference model is used only for verification.

## M3-Q12 — Output prediction: C do-while runs once

**Answer: A**

```text
1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 0 | x=0 | — |
| 2 | main | x ← (x + 1) | x=1 | — |
| 3 | main | PRINT | x=1 | 1 |

**Explanation:** do-while enters the body once before testing x<0.

The table separates side effects into their evaluation order. The displayed program above follows C rules; the reference model is used only for verification.

## M3-Q13 — Error detection: Least common multiple — program review

**Category:** boundary/runtime

**Fault and root cause:** The zero-input guard misses (0,0) and then divides by GCD=0.

**Faulty execution / counterexample:** output: '36' (sample masks the fault); boundary program: ZeroDivisionError: DIV by zero

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
a ← 0
b ← 0
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

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 0 | a=0 | — |
| 2 | main | b ← 0 | a=0; b=0 | — |
| 3 | main | x ← a | a=0; b=0; x=0 | — |
| 4 | main | y ← b | a=0; b=0; x=0; y=0 | — |
| 5 | main | WHILE (y ≠ 0) → FALSE | a=0; b=0; x=0; y=0 | — |
| 6 | main | IF ((a = 0) OR (b = 0)) → TRUE | a=0; b=0; x=0; y=0 | — |
| 7 | main | answer ← 0 | a=0; b=0; x=0; y=0; answer=0 | — |
| 8 | main | PRINT | a=0; b=0; x=0; y=0; answer=0 | 0 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M3-Q14 — Error detection: Recursive palindrome — program review

**Category:** loop/runtime

**Fault and root cause:** The right index expands beyond the string instead of moving inward.

**Faulty execution / counterexample:** IndexError: neutral index out of bounds

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

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
s ← "ab"
PRINT pal(s, 0, (LENGTH(s) − 1))
```

```text
FALSE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "ab" | s=ab | — |
| 2 | pal depth 1 | ENTER | s=ab; l=0; r=1 | — |
| 3 | pal depth 1 | IF (l ≥ r) → FALSE | s=ab; l=0; r=1 | — |
| 4 | pal depth 1 | IF (s[l] ≠ s[r]) → TRUE | s=ab; l=0; r=1 | — |
| 5 | pal depth 1 | RETURN FALSE | s=ab; l=0; r=1 | — |
| 6 | main | PRINT | s=ab | FALSE |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M3-Q15 — Error detection: Fast exponentiation — program review

**Category:** loop/termination

**Fault and root cause:** A positive exponent grows rather than shrinking to zero; the algorithm cannot finish.

**Faulty execution / counterexample:** exp: 5→10→20→40→…; exp>0 stays TRUE in unlimited integers.

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
base ← 3
exp ← 0
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

```text
1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | base ← 3 | base=3 | — |
| 2 | main | exp ← 0 | base=3; exp=0 | — |
| 3 | main | result ← 1 | base=3; exp=0; result=1 | — |
| 4 | main | WHILE (exp > 0) → FALSE | base=3; exp=0; result=1 | — |
| 5 | main | PRINT | base=3; exp=0; result=1 | 1 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M3-Q16 — Error detection: Fixed-window maximum sum — program review

**Category:** boundary/logic

**Fault and root cause:** Zero may exceed every actual window sum for all-negative inputs.

**Faulty execution / counterexample:** output: '7' (sample masks the fault); boundary program: output: '0'

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
A ← [(−5), (−2)]
k ← 1
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

```text
-2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [(−5), (−2)] | A=[-5, -2] | — |
| 2 | main | k ← 1 | A=[-5, -2]; k=1 | — |
| 3 | main | window ← 0 | A=[-5, -2]; k=1; window=0 | — |
| 4 | main | FOR visit i | A=[-5, -2]; k=1; window=0; i=0 | — |
| 5 | main | window ← (window + A[i]) | A=[-5, -2]; k=1; window=-5; i=0 | — |
| 6 | main | FOR exit | A=[-5, -2]; k=1; window=-5; i=0 | — |
| 7 | main | best ← window | A=[-5, -2]; k=1; window=-5; i=0; best=-5 | — |
| 8 | main | FOR visit i | A=[-5, -2]; k=1; window=-5; i=1; best=-5 | — |
| 9 | main | window ← ((window − A[(i − k)]) + A[i]) | A=[-5, -2]; k=1; window=-2; i=1; best=-5 | — |
| 10 | main | IF (window > best) → TRUE | A=[-5, -2]; k=1; window=-2; i=1; best=-5 | — |
| 11 | main | best ← window | A=[-5, -2]; k=1; window=-2; i=1; best=-2 | — |
| 12 | main | FOR exit | A=[-5, -2]; k=1; window=-2; i=1; best=-2 | — |
| 13 | main | PRINT | A=[-5, -2]; k=1; window=-2; i=1; best=-2 | -2 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M3-Q17 — Error detection: Insertion sort — program review

**Category:** boundary/logic

**Fault and root cause:** After shifts, j names the element before the gap, possibly -1. Insert at j+1.

**Faulty execution / counterexample:** IndexError: neutral index out of bounds

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
A ← []
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

```text
[]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [] | A=[] | — |
| 2 | main | FOR exit | A=[] | — |
| 3 | main | PRINT | A=[] | [] |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M3-Q18 — Error detection: Balanced parentheses — program review

**Category:** logic

**Fault and root cause:** The invalid-prefix test is wrong: balance must never become negative. Checking an impossible upper bound accepts )( after its balance returns to zero.

**Faulty execution / counterexample:** output: 'TRUE' (sample masks the fault); boundary program: output: 'TRUE'

**Complete corrected program**

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

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
s ← ")("
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

```text
FALSE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← ")(" | s=)( | — |
| 2 | main | balance ← 0 | s=)(; balance=0 | — |
| 3 | main | ok ← TRUE | s=)(; balance=0; ok=TRUE | — |
| 4 | main | FOR visit i | s=)(; balance=0; ok=TRUE; i=0 | — |
| 5 | main | IF (s[i] = "(") → FALSE | s=)(; balance=0; ok=TRUE; i=0 | — |
| 6 | main | balance ← (balance − 1) | s=)(; balance=-1; ok=TRUE; i=0 | — |
| 7 | main | IF (balance < 0) → TRUE | s=)(; balance=-1; ok=TRUE; i=0 | — |
| 8 | main | ok ← FALSE | s=)(; balance=-1; ok=FALSE; i=0 | — |
| 9 | main | BREAK | s=)(; balance=-1; ok=FALSE; i=0 | — |
| 10 | main | FOR exit | s=)(; balance=-1; ok=FALSE; i=0 | — |
| 11 | main | PRINT | s=)(; balance=-1; ok=FALSE; i=0 | FALSE |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M3-Q19 — Error detection: Sum from one to n — grammar/type review

**Category:** syntax

**Fault and root cause:** A FOR requires END FOR; END IF does not close it.

**Faulty execution / counterexample:** Under the strict contract this program fails the stated grammar/type requirement before it can produce the required result.

**Complete corrected program**

```text
Pseudocode
n ← 5
s ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    s ← (s + i)
END FOR
PRINT s
```

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
n ← 0
s ← 0
FOR i ← 1 TO ((n + 1) − 1) STEP 1
    s ← (s + i)
END FOR
PRINT s
```

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 0 | n=0 | — |
| 2 | main | s ← 0 | n=0; s=0 | — |
| 3 | main | FOR exit | n=0; s=0 | — |
| 4 | main | PRINT | n=0; s=0 | 0 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M3-Q20 — Error detection: Array sum — grammar/type review

**Category:** type/runtime

**Fault and root cause:** Adding an integer to a string is not permitted; the numeric accumulator must be an integer.

**Faulty execution / counterexample:** Under the strict contract this program fails the stated grammar/type requirement before it can produce the required result.

**Complete corrected program**

```text
Pseudocode
A ← [3, (−2), 7]
s ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    s ← (s + A[i])
END FOR
PRINT s
```

**Corrected sample output**

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

**Additional verification input and complete trace**

```text
Pseudocode
A ← []
s ← 0
FOR i ← 0 TO (LENGTH(A) − 1) STEP 1
    s ← (s + A[i])
END FOR
PRINT s
```

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [] | A=[] | — |
| 2 | main | s ← 0 | A=[]; s=0 | — |
| 3 | main | FOR exit | A=[]; s=0 | — |
| 4 | main | PRINT | A=[]; s=0 | 0 |

**Check:** The repair follows the required behavior on the demonstrated sample and boundary; these checks support the stated root-cause argument and are not exhaustive proof.

## M3-Q21 — Pseudocode writing: Fast exponentiation

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

## M3-Q22 — Pseudocode writing: Prefix sums

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

## M3-Q23 — Pseudocode writing: Fixed-window maximum sum

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

## M3-Q24 — Pseudocode writing: First occurrence by binary search

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

## M3-Q25 — Pseudocode writing: Recursive subset-sum decision

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

## M3-Q26 — Logical reasoning: Converse trap

**Answer: C — It may be successful or unsuccessful**

| Success | Validation | Implication check |
| --- | --- | --- |
| successful=TRUE | validation=TRUE | Allowed |
| successful=FALSE | validation=TRUE | Also allowed |
| successful=TRUE | validation=FALSE | Forbidden |

Passing validation is necessary for success but has not been stated sufficient. Two permitted cases disagree about success.

## M3-Q27 — Logical reasoning: Three-Boolean count

**Answer: C — 5**

| P | Q | R | Expression |
| --- | --- | --- | --- |
| FALSE | FALSE | FALSE | FALSE |
| FALSE | FALSE | TRUE | TRUE |
| FALSE | TRUE | FALSE | FALSE |
| FALSE | TRUE | TRUE | TRUE |
| TRUE | FALSE | FALSE | FALSE |
| TRUE | FALSE | TRUE | TRUE |
| TRUE | TRUE | FALSE | TRUE |
| TRUE | TRUE | TRUE | TRUE |

R true contributes four assignments. R false contributes only P=Q=TRUE, one more. Total five without double counting.

## M3-Q28 — Logical reasoning: Repair an invariant

**Answer: B — s ← s + A[i]**

| Stage | Calculation | Result |
| --- | --- | --- |
| before | A=[2,3], visited first value | s=2 |
| add A[1] | 2+3 | s=5, invariant holds |
| overwrite | s=3 | loses previous 2 |
| multiply | s=6 | not the visited sum |

An invariant is a statement that remains true after every iteration. Zero initialization establishes the empty-prefix sum; addition extends it.

## M3-Q29 — Logical reasoning: Growth reasoning

**Answer: C — O(n log(n+1))**

| Input | Inner visits | Total |
| --- | --- | --- |
| n=4 | j=1,2,4 | 4*3=12 |
| n=8 | j=1,2,4,8 | 8*4=32 |
| general | floor(log2(n))+1 visits | n*(floor(log2(n))+1) |

The inner loop is logarithmic, not linear. Multiplying by n outer repetitions gives Θ(n log(n+1)); writing log(n+1) also handles n=1.

## M3-Q30 — Logical reasoning: Boolean constraint puzzle

**Answer: B — A does not attend; C attends**

| A | Given B | C |
| --- | --- | --- |
| FALSE | TRUE | TRUE |

B implies C directly. A together with B would violate A implies NOT B, so A must be absent. Enumerating all truth assignments confirms the unique surviving row.

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
