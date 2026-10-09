# Output-prediction answers

Exact output appears in a code block, followed by a full execution table. An output containing multiple lines must retain their order. For real-language examples, the explanatory table expands language side effects into steps.

## O001 — Multiplication before addition

**Answer: A**

```text
10
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← (4 + (3 * 2)) | x=10 | — |
| 2 | main | PRINT | x=10 | 10 |

**Explanation:** Multiplication is evaluated first, so 4+6=10.

## O002 — Left-associative subtraction

**Answer: B**

```text
11
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← ((20 − 6) − 3) | x=11 | — |
| 2 | main | PRINT | x=11 | 11 |

**Explanation:** Group (20-6)-3, not 20-(6-3).

## O003 — Integer quotient and remainder

**Answer: C**

```text
5 3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 23 | a=23 | — |
| 2 | main | PRINT | a=23 | 5 3 |

**Explanation:** 23=5*4+3.

## O004 — Signed truncation

**Answer: D**

```text
-5 -3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← (−23) | a=-23 | — |
| 2 | main | q ← DIVIDE_TRUNC(a, 4) | a=-23; q=-5 | — |
| 3 | main | r ← (a − (q * 4)) | a=-23; q=-5; r=-3 | — |
| 4 | main | PRINT | a=-23; q=-5; r=-3 | -5 -3 |

**Explanation:** Truncation goes toward zero; remainder reconstructs the dividend.

## O005 — Assignment uses old values

**Answer: A**

```text
10 5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 3 | x=3 | — |
| 2 | main | y ← (x + 2) | x=3; y=5 | — |
| 3 | main | x ← (y * 2) | x=10; y=5 | — |
| 4 | main | PRINT | x=10; y=5 | 10 5 |

**Explanation:** Changing x later does not recompute y.

## O006 — Temporary swap

**Answer: B**

```text
8 2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 2 | a=2 | — |
| 2 | main | b ← 8 | a=2; b=8 | — |
| 3 | main | t ← a | a=2; b=8; t=2 | — |
| 4 | main | a ← b | a=8; b=8; t=2 | — |
| 5 | main | b ← t | a=8; b=2; t=2 | — |
| 6 | main | PRINT | a=8; b=2; t=2 | 8 2 |

**Explanation:** Temporary preserves the old a.

## O007 — Nested boundary condition

**Answer: C**

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

## O008 — Independent IF blocks

**Answer: D**

```text
3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 6 | x=6 | — |
| 2 | main | s ← 0 | x=6; s=0 | — |
| 3 | main | IF (x > 3) → TRUE | x=6; s=0 | — |
| 4 | main | s ← (s + 1) | x=6; s=1 | — |
| 5 | main | IF ((x MOD 2) = 0) → TRUE | x=6; s=1 | — |
| 6 | main | s ← (s + 2) | x=6; s=3 | — |
| 7 | main | PRINT | x=6; s=3 | 3 |

**Explanation:** Both IFs execute independently.

## O009 — Only one alternative

**Answer: A**

```text
A
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 7 | x=7 | — |
| 2 | main | IF (x > 4) → TRUE | x=7 | — |
| 3 | main | PRINT | x=7 | A |

**Explanation:** The outer true branch bypasses its entire ELSE.

## O010 — Conditional expression

**Answer: B**

```text
9
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 4 | x=4 | — |
| 2 | main | y ← 9 | x=4; y=9 | — |
| 3 | main | z ← (x IF (x > y) ELSE y) | x=4; y=9; z=9 | — |
| 4 | main | PRINT | x=4; y=9; z=9 | 9 |

**Explanation:** The test is false, selecting y.

## O011 — Inclusive step-two loop

**Answer: C**

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

## O012 — Descending loop

**Answer: D**

```text
12
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← 0 | s=0 | — |
| 2 | main | FOR visit i | s=0; i=6 | — |
| 3 | main | s ← (s + i) | s=6; i=6 | — |
| 4 | main | FOR visit i | s=6; i=4 | — |
| 5 | main | s ← (s + i) | s=10; i=4 | — |
| 6 | main | FOR visit i | s=10; i=2 | — |
| 7 | main | s ← (s + i) | s=12; i=2 | — |
| 8 | main | FOR exit | s=12; i=2 | — |
| 9 | main | PRINT | s=12; i=2 | 12 |

**Explanation:** Visits 6,4,2; lower bound in the displayed contract is 1.

## O013 — Skipped FOR body

**Answer: A**

```text
9
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← 9 | s=9 | — |
| 2 | main | FOR exit | s=9 | — |
| 3 | main | PRINT | s=9 | 9 |

**Explanation:** Positive step cannot start above the inclusive end 2.

## O014 — Doubling loop

**Answer: B**

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

## O015 — Halving loop

**Answer: C**

```text
5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 19 | n=19 | — |
| 2 | main | count ← 0 | n=19; count=0 | — |
| 3 | main | WHILE (n > 0) → TRUE | n=19; count=0 | — |
| 4 | main | n ← (n DIV 2) | n=9; count=0 | — |
| 5 | main | count ← (count + 1) | n=9; count=1 | — |
| 6 | main | WHILE (n > 0) → TRUE | n=9; count=1 | — |
| 7 | main | n ← (n DIV 2) | n=4; count=1 | — |
| 8 | main | count ← (count + 1) | n=4; count=2 | — |
| 9 | main | WHILE (n > 0) → TRUE | n=4; count=2 | — |
| 10 | main | n ← (n DIV 2) | n=2; count=2 | — |
| 11 | main | count ← (count + 1) | n=2; count=3 | — |
| 12 | main | WHILE (n > 0) → TRUE | n=2; count=3 | — |
| 13 | main | n ← (n DIV 2) | n=1; count=3 | — |
| 14 | main | count ← (count + 1) | n=1; count=4 | — |
| 15 | main | WHILE (n > 0) → TRUE | n=1; count=4 | — |
| 16 | main | n ← (n DIV 2) | n=0; count=4 | — |
| 17 | main | count ← (count + 1) | n=0; count=5 | — |
| 18 | main | WHILE (n > 0) → FALSE | n=0; count=5 | — |
| 19 | main | PRINT | n=0; count=5 | 5 |

**Explanation:** 19→9→4→2→1→0 has five updates.

## O016 — Decrement before accumulation

**Answer: D**

```text
10
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | i ← 5 | i=5 | — |
| 2 | main | s ← 0 | i=5; s=0 | — |
| 3 | main | WHILE (i > 0) → TRUE | i=5; s=0 | — |
| 4 | main | i ← (i − 1) | i=4; s=0 | — |
| 5 | main | s ← (s + i) | i=4; s=4 | — |
| 6 | main | WHILE (i > 0) → TRUE | i=4; s=4 | — |
| 7 | main | i ← (i − 1) | i=3; s=4 | — |
| 8 | main | s ← (s + i) | i=3; s=7 | — |
| 9 | main | WHILE (i > 0) → TRUE | i=3; s=7 | — |
| 10 | main | i ← (i − 1) | i=2; s=7 | — |
| 11 | main | s ← (s + i) | i=2; s=9 | — |
| 12 | main | WHILE (i > 0) → TRUE | i=2; s=9 | — |
| 13 | main | i ← (i − 1) | i=1; s=9 | — |
| 14 | main | s ← (s + i) | i=1; s=10 | — |
| 15 | main | WHILE (i > 0) → TRUE | i=1; s=10 | — |
| 16 | main | i ← (i − 1) | i=0; s=10 | — |
| 17 | main | s ← (s + i) | i=0; s=10 | — |
| 18 | main | WHILE (i > 0) → FALSE | i=0; s=10 | — |
| 19 | main | PRINT | i=0; s=10 | 10 |

**Explanation:** Added values are 4,3,2,1,0.

## O017 — BREAK before addition

**Answer: A**

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

## O018 — CONTINUE skips evens

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

## O019 — WHILE update before CONTINUE

**Answer: C**

```text
12
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | i ← 0 | i=0 | — |
| 2 | main | s ← 0 | i=0; s=0 | — |
| 3 | main | WHILE (i < 5) → TRUE | i=0; s=0 | — |
| 4 | main | i ← (i + 1) | i=1; s=0 | — |
| 5 | main | IF (i = 3) → FALSE | i=1; s=0 | — |
| 6 | main | s ← (s + i) | i=1; s=1 | — |
| 7 | main | WHILE (i < 5) → TRUE | i=1; s=1 | — |
| 8 | main | i ← (i + 1) | i=2; s=1 | — |
| 9 | main | IF (i = 3) → FALSE | i=2; s=1 | — |
| 10 | main | s ← (s + i) | i=2; s=3 | — |
| 11 | main | WHILE (i < 5) → TRUE | i=2; s=3 | — |
| 12 | main | i ← (i + 1) | i=3; s=3 | — |
| 13 | main | IF (i = 3) → TRUE | i=3; s=3 | — |
| 14 | main | CONTINUE | i=3; s=3 | — |
| 15 | main | WHILE (i < 5) → TRUE | i=3; s=3 | — |
| 16 | main | i ← (i + 1) | i=4; s=3 | — |
| 17 | main | IF (i = 3) → FALSE | i=4; s=3 | — |
| 18 | main | s ← (s + i) | i=4; s=7 | — |
| 19 | main | WHILE (i < 5) → TRUE | i=4; s=7 | — |
| 20 | main | i ← (i + 1) | i=5; s=7 | — |
| 21 | main | IF (i = 3) → FALSE | i=5; s=7 | — |
| 22 | main | s ← (s + i) | i=5; s=12 | — |
| 23 | main | WHILE (i < 5) → FALSE | i=5; s=12 | — |
| 24 | main | PRINT | i=5; s=12 | 12 |

**Explanation:** Progress occurs before the skip; all values except 3 contribute.

## O020 — Rectangular nested loop

**Answer: D**

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

## O021 — Triangular loop

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

## O022 — Inner BREAK only

**Answer: B**

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

## O023 — Dependent step increments

**Answer: C**

```text
8
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | count ← 0 | count=0 | — |
| 2 | main | FOR visit i | count=0; i=1 | — |
| 3 | main | j ← i | count=0; i=1; j=1 | — |
| 4 | main | WHILE (j ≤ 4) → TRUE | count=0; i=1; j=1 | — |
| 5 | main | count ← (count + 1) | count=1; i=1; j=1 | — |
| 6 | main | j ← (j + i) | count=1; i=1; j=2 | — |
| 7 | main | WHILE (j ≤ 4) → TRUE | count=1; i=1; j=2 | — |
| 8 | main | count ← (count + 1) | count=2; i=1; j=2 | — |
| 9 | main | j ← (j + i) | count=2; i=1; j=3 | — |
| 10 | main | WHILE (j ≤ 4) → TRUE | count=2; i=1; j=3 | — |
| 11 | main | count ← (count + 1) | count=3; i=1; j=3 | — |
| 12 | main | j ← (j + i) | count=3; i=1; j=4 | — |
| 13 | main | WHILE (j ≤ 4) → TRUE | count=3; i=1; j=4 | — |
| 14 | main | count ← (count + 1) | count=4; i=1; j=4 | — |
| 15 | main | j ← (j + i) | count=4; i=1; j=5 | — |
| 16 | main | WHILE (j ≤ 4) → FALSE | count=4; i=1; j=5 | — |
| 17 | main | FOR visit i | count=4; i=2; j=5 | — |
| 18 | main | j ← i | count=4; i=2; j=2 | — |
| 19 | main | WHILE (j ≤ 4) → TRUE | count=4; i=2; j=2 | — |
| 20 | main | count ← (count + 1) | count=5; i=2; j=2 | — |
| 21 | main | j ← (j + i) | count=5; i=2; j=4 | — |
| 22 | main | WHILE (j ≤ 4) → TRUE | count=5; i=2; j=4 | — |
| 23 | main | count ← (count + 1) | count=6; i=2; j=4 | — |
| 24 | main | j ← (j + i) | count=6; i=2; j=6 | — |
| 25 | main | WHILE (j ≤ 4) → FALSE | count=6; i=2; j=6 | — |
| 26 | main | FOR visit i | count=6; i=3; j=6 | — |
| 27 | main | j ← i | count=6; i=3; j=3 | — |
| 28 | main | WHILE (j ≤ 4) → TRUE | count=6; i=3; j=3 | — |
| 29 | main | count ← (count + 1) | count=7; i=3; j=3 | — |
| 30 | main | j ← (j + i) | count=7; i=3; j=6 | — |
| 31 | main | WHILE (j ≤ 4) → FALSE | count=7; i=3; j=6 | — |
| 32 | main | FOR visit i | count=7; i=4; j=6 | — |
| 33 | main | j ← i | count=7; i=4; j=4 | — |
| 34 | main | WHILE (j ≤ 4) → TRUE | count=7; i=4; j=4 | — |
| 35 | main | count ← (count + 1) | count=8; i=4; j=4 | — |
| 36 | main | j ← (j + i) | count=8; i=4; j=8 | — |
| 37 | main | WHILE (j ≤ 4) → FALSE | count=8; i=4; j=8 | — |
| 38 | main | FOR exit | count=8; i=4; j=8 | — |
| 39 | main | PRINT | count=8; i=4; j=8 | 8 |

**Explanation:** Counts by row are 4,2,1,1, not 4*4.

## O024 — Array accumulation

**Answer: D**

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

## O025 — Array mutation feeds next step

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

## O026 — Array alias

**Answer: B**

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

## O027 — Array copy

**Answer: C**

```text
[3, 4] [3, 9]
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [3, 4] | A=[3, 4] | — |
| 2 | main | B ← COPY(A) | A=[3, 4]; B=[3, 4] | — |
| 3 | main | B[1] ← 9 | A=[3, 4]; B=[3, 9] | — |
| 4 | main | PRINT | A=[3, 4]; B=[3, 9] | [3, 4] [3, 9] |

**Explanation:** COPY makes a separate outer array; these elements are scalars.

## O028 — First matching index

**Answer: D**

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

## O029 — Last matching index

**Answer: A**

```text
2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [5, 2, 5] | A=[5, 2, 5] | — |
| 2 | main | answer ← (−1) | A=[5, 2, 5]; answer=-1 | — |
| 3 | main | FOR visit i | A=[5, 2, 5]; answer=-1; i=0 | — |
| 4 | main | IF (A[i] = 5) → TRUE | A=[5, 2, 5]; answer=-1; i=0 | — |
| 5 | main | answer ← i | A=[5, 2, 5]; answer=0; i=0 | — |
| 6 | main | FOR visit i | A=[5, 2, 5]; answer=0; i=1 | — |
| 7 | main | IF (A[i] = 5) → FALSE | A=[5, 2, 5]; answer=0; i=1 | — |
| 8 | main | FOR visit i | A=[5, 2, 5]; answer=0; i=2 | — |
| 9 | main | IF (A[i] = 5) → TRUE | A=[5, 2, 5]; answer=0; i=2 | — |
| 10 | main | answer ← i | A=[5, 2, 5]; answer=2; i=2 | — |
| 11 | main | FOR exit | A=[5, 2, 5]; answer=2; i=2 | — |
| 12 | main | PRINT | A=[5, 2, 5]; answer=2; i=2 | 2 |

**Explanation:** Without BREAK the later match overwrites the earlier one.

## O030 — One bubble pass

**Answer: B**

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

## O031 — Selection minimum index

**Answer: C**

```text
3 2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [8, 3, 7, 2] | A=[8, 3, 7, 2] | — |
| 2 | main | best ← 0 | A=[8, 3, 7, 2]; best=0 | — |
| 3 | main | FOR visit i | A=[8, 3, 7, 2]; best=0; i=1 | — |
| 4 | main | IF (A[i] < A[best]) → TRUE | A=[8, 3, 7, 2]; best=0; i=1 | — |
| 5 | main | best ← i | A=[8, 3, 7, 2]; best=1; i=1 | — |
| 6 | main | FOR visit i | A=[8, 3, 7, 2]; best=1; i=2 | — |
| 7 | main | IF (A[i] < A[best]) → FALSE | A=[8, 3, 7, 2]; best=1; i=2 | — |
| 8 | main | FOR visit i | A=[8, 3, 7, 2]; best=1; i=3 | — |
| 9 | main | IF (A[i] < A[best]) → TRUE | A=[8, 3, 7, 2]; best=1; i=3 | — |
| 10 | main | best ← i | A=[8, 3, 7, 2]; best=3; i=3 | — |
| 11 | main | FOR exit | A=[8, 3, 7, 2]; best=3; i=3 | — |
| 12 | main | PRINT | A=[8, 3, 7, 2]; best=3; i=3 | 3 2 |

**Explanation:** best stores an index, not the minimum itself.

## O032 — Binary search successful

**Answer: D**

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

## O033 — String reverse loop

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

## O034 — Character filtering

**Answer: B**

```text
3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "banana" | s=banana | — |
| 2 | main | count ← 0 | s=banana; count=0 | — |
| 3 | main | FOR visit i | s=banana; count=0; i=0 | — |
| 4 | main | IF (s[i] = "a") → FALSE | s=banana; count=0; i=0 | — |
| 5 | main | FOR visit i | s=banana; count=0; i=1 | — |
| 6 | main | IF (s[i] = "a") → TRUE | s=banana; count=0; i=1 | — |
| 7 | main | count ← (count + 1) | s=banana; count=1; i=1 | — |
| 8 | main | FOR visit i | s=banana; count=1; i=2 | — |
| 9 | main | IF (s[i] = "a") → FALSE | s=banana; count=1; i=2 | — |
| 10 | main | FOR visit i | s=banana; count=1; i=3 | — |
| 11 | main | IF (s[i] = "a") → TRUE | s=banana; count=1; i=3 | — |
| 12 | main | count ← (count + 1) | s=banana; count=2; i=3 | — |
| 13 | main | FOR visit i | s=banana; count=2; i=4 | — |
| 14 | main | IF (s[i] = "a") → FALSE | s=banana; count=2; i=4 | — |
| 15 | main | FOR visit i | s=banana; count=2; i=5 | — |
| 16 | main | IF (s[i] = "a") → TRUE | s=banana; count=2; i=5 | — |
| 17 | main | count ← (count + 1) | s=banana; count=3; i=5 | — |
| 18 | main | FOR exit | s=banana; count=3; i=5 | — |
| 19 | main | PRINT | s=banana; count=3; i=5 | 3 |

**Explanation:** Matches at positions 1,3,5.

## O035 — End-exclusive slice

**Answer: C**

```text
eu
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "zeus" | s=zeus | — |
| 2 | main | PRINT | s=zeus | eu |

**Explanation:** Indices 1 and 2 are included, index 3 excluded.

## O036 — String concatenation

**Answer: D**

```text
123
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "" | s= | — |
| 2 | main | FOR visit i | s=; i=1 | — |
| 3 | main | s ← (s + STRING(i)) | s=1; i=1 | — |
| 4 | main | FOR visit i | s=1; i=2 | — |
| 5 | main | s ← (s + STRING(i)) | s=12; i=2 | — |
| 6 | main | FOR visit i | s=12; i=3 | — |
| 7 | main | s ← (s + STRING(i)) | s=123; i=3 | — |
| 8 | main | FOR exit | s=123; i=3 | — |
| 9 | main | PRINT | s=123; i=3 | 123 |

**Explanation:** STRING converts each integer before joining text.

## O037 — Matrix row total

**Answer: A**

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

## O038 — Secondary diagonal

**Answer: B**

```text
15
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | M ← [[1, 2, 3], [4, 5, 6], [7, 8, 9]] | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]] | — |
| 2 | main | s ← 0 | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; s=0 | — |
| 3 | main | FOR visit i | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; s=0; i=0 | — |
| 4 | main | s ← (s + M[i][(2 − i)]) | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; s=3; i=0 | — |
| 5 | main | FOR visit i | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; s=3; i=1 | — |
| 6 | main | s ← (s + M[i][(2 − i)]) | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; s=8; i=1 | — |
| 7 | main | FOR visit i | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; s=8; i=2 | — |
| 8 | main | s ← (s + M[i][(2 − i)]) | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; s=15; i=2 | — |
| 9 | main | FOR exit | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; s=15; i=2 | — |
| 10 | main | PRINT | M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]; s=15; i=2 | 15 |

**Explanation:** Coordinates (0,2),(1,1),(2,0) give 3,5,7.

## O039 — Scalar parameter value

**Answer: C**

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

## O040 — Array parameter mutation

**Answer: D**

```text
[7, 3] 7
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← [2, 3] | a=[2, 3] | — |
| 2 | change depth 1 | ENTER | A=[2, 3] | — |
| 3 | change depth 1 | A[0] ← (A[0] + 5) | A=[7, 3] | — |
| 4 | change depth 1 | RETURN 7 | A=[7, 3] | — |
| 5 | main | b ← change(a) | a=[7, 3]; b=7 | — |
| 6 | main | PRINT | a=[7, 3]; b=7 | [7, 3] 7 |

**Explanation:** The parameter aliases the caller array, so element mutation is shared.

## O041 — Nested function calls

**Answer: A**

```text
13
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | twice depth 1 | ENTER | x=3 | — |
| 2 | twice depth 1 | RETURN 6 | x=3 | — |
| 3 | twice depth 1 | ENTER | x=6 | — |
| 4 | twice depth 1 | RETURN 12 | x=6 | — |
| 5 | main | PRINT | — | 13 |

**Explanation:** Inner call returns 6; outer returns 12; add 1.

## O042 — Early RETURN

**Answer: B**

```text
4 3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | f depth 1 | ENTER | x=-4 | — |
| 2 | f depth 1 | IF (x > 0) → FALSE | x=-4 | — |
| 3 | f depth 1 | RETURN 4 | x=-4 | — |
| 4 | f depth 1 | ENTER | x=3 | — |
| 5 | f depth 1 | IF (x > 0) → TRUE | x=3 | — |
| 6 | f depth 1 | RETURN 3 | x=3 | — |
| 7 | main | PRINT | — | 4 3 |

**Explanation:** Each call follows its own branch and exits at RETURN.

## O043 — Recursive factorial trace

**Answer: C**

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

## O044 — Print on descent

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
| 16 | main | f(3) | — | 3\n2\n1 |

**Explanation:** Printing happens before the recursive call.

## O045 — Print on return

**Answer: A**

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
| 13 | f depth 2 | f((n − 1)) | n=2 | 1 |
| 14 | f depth 2 | PRINT | n=2 | 2 |
| 15 | f depth 2 | RETURN 2 | n=2 | — |
| 16 | f depth 1 | f((n − 1)) | n=3 | 1\n2 |
| 17 | f depth 1 | PRINT | n=3 | 3 |
| 18 | f depth 1 | RETURN 3 | n=3 | — |
| 19 | main | f(3) | — | 1\n2\n3 |

**Explanation:** Pending prints execute while the stack unwinds.

## O046 — Two recursive branches

**Answer: B**

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

## O047 — Recursive halving

**Answer: C**

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

## O048 — Bitwise AND

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

## O049 — Bitwise OR and XOR

**Answer: A**

```text
7 6
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 5 | a=5 | — |
| 2 | main | b ← 3 | a=5; b=3 | — |
| 3 | main | PRINT | a=5; b=3 | 7 6 |

**Explanation:** 0101 OR 0011=0111; XOR=0110.

## O050 — Eight-bit complement

**Answer: B**

```text
250
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | PRINT | — | 250 |

**Explanation:** 00000101 becomes 11111010; width is explicitly eight bits.

## O051 — Shift then addition

**Answer: C**

```text
13 6
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 3 | x=3 | — |
| 2 | main | PRINT | x=3 | 13 6 |

**Explanation:** 3 shifted two bits is 12; nonnegative right shift truncates 13/2.

## O052 — XOR cancellation

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

## O053 — Clear set bits

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

## O054 — Guard division with AND

**Answer: B**

```text
FALSE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | d ← 0 | d=0 | — |
| 2 | main | PRINT | d=0 | FALSE |

**Explanation:** False left operand skips division entirely.

## O055 — OR skips call side effect

**Answer: C**

```text
TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | PRINT | — | TRUE |

**Explanation:** True left operand skips mark, so it prints nothing.

## O056 — De Morgan evaluation

**Answer: D**

```text
TRUE TRUE
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | p ← TRUE | p=TRUE | — |
| 2 | main | q ← FALSE | p=TRUE; q=FALSE | — |
| 3 | main | PRINT | p=TRUE; q=FALSE | TRUE TRUE |

**Explanation:** Both equivalent expressions are true.

## O057 — Digit extraction order

**Answer: A**

```text
11
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 407 | n=407 | — |
| 2 | main | s ← 0 | n=407; s=0 | — |
| 3 | main | WHILE (n > 0) → TRUE | n=407; s=0 | — |
| 4 | main | s ← (s + (n MOD 10)) | n=407; s=7 | — |
| 5 | main | n ← (n DIV 10) | n=40; s=7 | — |
| 6 | main | WHILE (n > 0) → TRUE | n=40; s=7 | — |
| 7 | main | s ← (s + (n MOD 10)) | n=40; s=7 | — |
| 8 | main | n ← (n DIV 10) | n=4; s=7 | — |
| 9 | main | WHILE (n > 0) → TRUE | n=4; s=7 | — |
| 10 | main | s ← (s + (n MOD 10)) | n=4; s=11 | — |
| 11 | main | n ← (n DIV 10) | n=0; s=11 | — |
| 12 | main | WHILE (n > 0) → FALSE | n=0; s=11 | — |
| 13 | main | PRINT | n=0; s=11 | 11 |

**Explanation:** Digits arrive as 7,0,4.

## O058 — Numeric reversal drops zeros

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

## O059 — Euclid state

**Answer: C**

```text
5 0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 35 | a=35 | — |
| 2 | main | b ← 15 | a=35; b=15 | — |
| 3 | main | WHILE (b ≠ 0) → TRUE | a=35; b=15 | — |
| 4 | main | r ← (a MOD b) | a=35; b=15; r=5 | — |
| 5 | main | a ← b | a=15; b=15; r=5 | — |
| 6 | main | b ← r | a=15; b=5; r=5 | — |
| 7 | main | WHILE (b ≠ 0) → TRUE | a=15; b=5; r=5 | — |
| 8 | main | r ← (a MOD b) | a=15; b=5; r=0 | — |
| 9 | main | a ← b | a=5; b=5; r=0 | — |
| 10 | main | b ← r | a=5; b=0; r=0 | — |
| 11 | main | WHILE (b ≠ 0) → FALSE | a=5; b=0; r=0 | — |
| 12 | main | PRINT | a=5; b=0; r=0 | 5 0 |

**Explanation:** Pairs are (35,15),(15,5),(5,0).

## O060 — Negative-only maximum

**Answer: D**

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

## O061 — Boundary sequence 0/5/2

**Answer: A**

```text
0 2 4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "" | s= | — |
| 2 | main | FOR visit i | s=; i=0 | — |
| 3 | main | IF (s ≠ "") → FALSE | s=; i=0 | — |
| 4 | main | s ← (s + STRING(i)) | s=0; i=0 | — |
| 5 | main | FOR visit i | s=0; i=2 | — |
| 6 | main | IF (s ≠ "") → TRUE | s=0; i=2 | — |
| 7 | main | s ← (s + " ") | s=0 ; i=2 | — |
| 8 | main | s ← (s + STRING(i)) | s=0 2; i=2 | — |
| 9 | main | FOR visit i | s=0 2; i=4 | — |
| 10 | main | IF (s ≠ "") → TRUE | s=0 2; i=4 | — |
| 11 | main | s ← (s + " ") | s=0 2 ; i=4 | — |
| 12 | main | s ← (s + STRING(i)) | s=0 2 4; i=4 | — |
| 13 | main | FOR exit | s=0 2 4; i=4 | — |
| 14 | main | IF (s = "") → FALSE | s=0 2 4; i=4 | — |
| 15 | main | PRINT | s=0 2 4; i=4 | 0 2 4 |

**Explanation:** Check the first value, signed step and inclusive end shown in the pseudocode; EMPTY is a deliberate sentinel.

## O062 — Boundary sequence 5/-1/-2

**Answer: B**

```text
5 3 1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "" | s= | — |
| 2 | main | FOR visit i | s=; i=5 | — |
| 3 | main | IF (s ≠ "") → FALSE | s=; i=5 | — |
| 4 | main | s ← (s + STRING(i)) | s=5; i=5 | — |
| 5 | main | FOR visit i | s=5; i=3 | — |
| 6 | main | IF (s ≠ "") → TRUE | s=5; i=3 | — |
| 7 | main | s ← (s + " ") | s=5 ; i=3 | — |
| 8 | main | s ← (s + STRING(i)) | s=5 3; i=3 | — |
| 9 | main | FOR visit i | s=5 3; i=1 | — |
| 10 | main | IF (s ≠ "") → TRUE | s=5 3; i=1 | — |
| 11 | main | s ← (s + " ") | s=5 3 ; i=1 | — |
| 12 | main | s ← (s + STRING(i)) | s=5 3 1; i=1 | — |
| 13 | main | FOR exit | s=5 3 1; i=1 | — |
| 14 | main | IF (s = "") → FALSE | s=5 3 1; i=1 | — |
| 15 | main | PRINT | s=5 3 1; i=1 | 5 3 1 |

**Explanation:** Check the first value, signed step and inclusive end shown in the pseudocode; EMPTY is a deliberate sentinel.

## O063 — Boundary sequence 3/3/1

**Answer: C**

```text
EMPTY
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "" | s= | — |
| 2 | main | FOR exit | s= | — |
| 3 | main | IF (s = "") → TRUE | s= | — |
| 4 | main | s ← "EMPTY" | s=EMPTY | — |
| 5 | main | PRINT | s=EMPTY | EMPTY |

**Explanation:** Check the first value, signed step and inclusive end shown in the pseudocode; EMPTY is a deliberate sentinel.

## O064 — Boundary sequence 8/1/-3

**Answer: D**

```text
8 5 2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← "" | s= | — |
| 2 | main | FOR visit i | s=; i=8 | — |
| 3 | main | IF (s ≠ "") → FALSE | s=; i=8 | — |
| 4 | main | s ← (s + STRING(i)) | s=8; i=8 | — |
| 5 | main | FOR visit i | s=8; i=5 | — |
| 6 | main | IF (s ≠ "") → TRUE | s=8; i=5 | — |
| 7 | main | s ← (s + " ") | s=8 ; i=5 | — |
| 8 | main | s ← (s + STRING(i)) | s=8 5; i=5 | — |
| 9 | main | FOR visit i | s=8 5; i=2 | — |
| 10 | main | IF (s ≠ "") → TRUE | s=8 5; i=2 | — |
| 11 | main | s ← (s + " ") | s=8 5 ; i=2 | — |
| 12 | main | s ← (s + STRING(i)) | s=8 5 2; i=2 | — |
| 13 | main | FOR exit | s=8 5 2; i=2 | — |
| 14 | main | IF (s = "") → FALSE | s=8 5 2; i=2 | — |
| 15 | main | PRINT | s=8 5 2; i=2 | 8 5 2 |

**Explanation:** Check the first value, signed step and inclusive end shown in the pseudocode; EMPTY is a deliberate sentinel.

## O065 — Digit count boundary n=0

**Answer: A**

```text
1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 0 | n=0 | — |
| 2 | main | count ← 1 | n=0; count=1 | — |
| 3 | main | WHILE (n ≥ 10) → FALSE | n=0; count=1 | — |
| 4 | main | PRINT | n=0; count=1 | 1 |

**Explanation:** One initial digit plus one count for every removable decimal position.

## O066 — Digit count boundary n=1

**Answer: B**

```text
1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 1 | n=1 | — |
| 2 | main | count ← 1 | n=1; count=1 | — |
| 3 | main | WHILE (n ≥ 10) → FALSE | n=1; count=1 | — |
| 4 | main | PRINT | n=1; count=1 | 1 |

**Explanation:** One initial digit plus one count for every removable decimal position.

## O067 — Digit count boundary n=10

**Answer: C**

```text
2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 10 | n=10 | — |
| 2 | main | count ← 1 | n=10; count=1 | — |
| 3 | main | WHILE (n ≥ 10) → TRUE | n=10; count=1 | — |
| 4 | main | count ← (count + 1) | n=10; count=2 | — |
| 5 | main | n ← (n DIV 10) | n=1; count=2 | — |
| 6 | main | WHILE (n ≥ 10) → FALSE | n=1; count=2 | — |
| 7 | main | PRINT | n=1; count=2 | 2 |

**Explanation:** One initial digit plus one count for every removable decimal position.

## O068 — Digit count boundary n=1001

**Answer: D**

```text
4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 1001 | n=1001 | — |
| 2 | main | count ← 1 | n=1001; count=1 | — |
| 3 | main | WHILE (n ≥ 10) → TRUE | n=1001; count=1 | — |
| 4 | main | count ← (count + 1) | n=1001; count=2 | — |
| 5 | main | n ← (n DIV 10) | n=100; count=2 | — |
| 6 | main | WHILE (n ≥ 10) → TRUE | n=100; count=2 | — |
| 7 | main | count ← (count + 1) | n=100; count=3 | — |
| 8 | main | n ← (n DIV 10) | n=10; count=3 | — |
| 9 | main | WHILE (n ≥ 10) → TRUE | n=10; count=3 | — |
| 10 | main | count ← (count + 1) | n=10; count=4 | — |
| 11 | main | n ← (n DIV 10) | n=1; count=4 | — |
| 12 | main | WHILE (n ≥ 10) → FALSE | n=1; count=4 | — |
| 13 | main | PRINT | n=1; count=4 | 4 |

**Explanation:** One initial digit plus one count for every removable decimal position.

## O069 — Prime boundary n=1

**Answer: A**

```text
FALSE 2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 1 | n=1 | — |
| 2 | main | prime ← (n ≥ 2) | n=1; prime=FALSE | — |
| 3 | main | d ← 2 | n=1; prime=FALSE; d=2 | — |
| 4 | main | WHILE (prime AND ((d * d) ≤ n)) → FALSE | n=1; prime=FALSE; d=2 | — |
| 5 | main | PRINT | n=1; prime=FALSE; d=2 | FALSE 2 |

**Explanation:** d advances after every tested divisor, including the divisor that disproves primality.

## O070 — Prime boundary n=2

**Answer: B**

```text
TRUE 2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 2 | n=2 | — |
| 2 | main | prime ← (n ≥ 2) | n=2; prime=TRUE | — |
| 3 | main | d ← 2 | n=2; prime=TRUE; d=2 | — |
| 4 | main | WHILE (prime AND ((d * d) ≤ n)) → FALSE | n=2; prime=TRUE; d=2 | — |
| 5 | main | PRINT | n=2; prime=TRUE; d=2 | TRUE 2 |

**Explanation:** d advances after every tested divisor, including the divisor that disproves primality.

## O071 — Prime boundary n=9

**Answer: C**

```text
FALSE 4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 9 | n=9 | — |
| 2 | main | prime ← (n ≥ 2) | n=9; prime=TRUE | — |
| 3 | main | d ← 2 | n=9; prime=TRUE; d=2 | — |
| 4 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=9; prime=TRUE; d=2 | — |
| 5 | main | IF ((n MOD d) = 0) → FALSE | n=9; prime=TRUE; d=2 | — |
| 6 | main | d ← (d + 1) | n=9; prime=TRUE; d=3 | — |
| 7 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=9; prime=TRUE; d=3 | — |
| 8 | main | IF ((n MOD d) = 0) → TRUE | n=9; prime=TRUE; d=3 | — |
| 9 | main | prime ← FALSE | n=9; prime=FALSE; d=3 | — |
| 10 | main | d ← (d + 1) | n=9; prime=FALSE; d=4 | — |
| 11 | main | WHILE (prime AND ((d * d) ≤ n)) → FALSE | n=9; prime=FALSE; d=4 | — |
| 12 | main | PRINT | n=9; prime=FALSE; d=4 | FALSE 4 |

**Explanation:** d advances after every tested divisor, including the divisor that disproves primality.

## O072 — Prime boundary n=17

**Answer: D**

```text
TRUE 5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | n ← 17 | n=17 | — |
| 2 | main | prime ← (n ≥ 2) | n=17; prime=TRUE | — |
| 3 | main | d ← 2 | n=17; prime=TRUE; d=2 | — |
| 4 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=17; prime=TRUE; d=2 | — |
| 5 | main | IF ((n MOD d) = 0) → FALSE | n=17; prime=TRUE; d=2 | — |
| 6 | main | d ← (d + 1) | n=17; prime=TRUE; d=3 | — |
| 7 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=17; prime=TRUE; d=3 | — |
| 8 | main | IF ((n MOD d) = 0) → FALSE | n=17; prime=TRUE; d=3 | — |
| 9 | main | d ← (d + 1) | n=17; prime=TRUE; d=4 | — |
| 10 | main | WHILE (prime AND ((d * d) ≤ n)) → TRUE | n=17; prime=TRUE; d=4 | — |
| 11 | main | IF ((n MOD d) = 0) → FALSE | n=17; prime=TRUE; d=4 | — |
| 12 | main | d ← (d + 1) | n=17; prime=TRUE; d=5 | — |
| 13 | main | WHILE (prime AND ((d * d) ≤ n)) → FALSE | n=17; prime=TRUE; d=5 | — |
| 14 | main | PRINT | n=17; prime=TRUE; d=5 | TRUE 5 |

**Explanation:** d advances after every tested divisor, including the divisor that disproves primality.

## O073 — Fibonacci state after 0 updates

**Answer: A**

```text
0 1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 0 | a=0 | — |
| 2 | main | b ← 1 | a=0; b=1 | — |
| 3 | main | FOR exit | a=0; b=1 | — |
| 4 | main | PRINT | a=0; b=1 | 0 1 |

**Explanation:** After k updates the pair is (F_k,F_(k+1)); the temporary prevents reuse of an overwritten a.

## O074 — Fibonacci state after 1 updates

**Answer: B**

```text
1 1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 0 | a=0 | — |
| 2 | main | b ← 1 | a=0; b=1 | — |
| 3 | main | FOR visit i | a=0; b=1; i=0 | — |
| 4 | main | t ← (a + b) | a=0; b=1; i=0; t=1 | — |
| 5 | main | a ← b | a=1; b=1; i=0; t=1 | — |
| 6 | main | b ← t | a=1; b=1; i=0; t=1 | — |
| 7 | main | FOR exit | a=1; b=1; i=0; t=1 | — |
| 8 | main | PRINT | a=1; b=1; i=0; t=1 | 1 1 |

**Explanation:** After k updates the pair is (F_k,F_(k+1)); the temporary prevents reuse of an overwritten a.

## O075 — Fibonacci state after 4 updates

**Answer: C**

```text
3 5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 0 | a=0 | — |
| 2 | main | b ← 1 | a=0; b=1 | — |
| 3 | main | FOR visit i | a=0; b=1; i=0 | — |
| 4 | main | t ← (a + b) | a=0; b=1; i=0; t=1 | — |
| 5 | main | a ← b | a=1; b=1; i=0; t=1 | — |
| 6 | main | b ← t | a=1; b=1; i=0; t=1 | — |
| 7 | main | FOR visit i | a=1; b=1; i=1; t=1 | — |
| 8 | main | t ← (a + b) | a=1; b=1; i=1; t=2 | — |
| 9 | main | a ← b | a=1; b=1; i=1; t=2 | — |
| 10 | main | b ← t | a=1; b=2; i=1; t=2 | — |
| 11 | main | FOR visit i | a=1; b=2; i=2; t=2 | — |
| 12 | main | t ← (a + b) | a=1; b=2; i=2; t=3 | — |
| 13 | main | a ← b | a=2; b=2; i=2; t=3 | — |
| 14 | main | b ← t | a=2; b=3; i=2; t=3 | — |
| 15 | main | FOR visit i | a=2; b=3; i=3; t=3 | — |
| 16 | main | t ← (a + b) | a=2; b=3; i=3; t=5 | — |
| 17 | main | a ← b | a=3; b=3; i=3; t=5 | — |
| 18 | main | b ← t | a=3; b=5; i=3; t=5 | — |
| 19 | main | FOR exit | a=3; b=5; i=3; t=5 | — |
| 20 | main | PRINT | a=3; b=5; i=3; t=5 | 3 5 |

**Explanation:** After k updates the pair is (F_k,F_(k+1)); the temporary prevents reuse of an overwritten a.

## O076 — Fibonacci state after 6 updates

**Answer: D**

```text
8 13
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | a ← 0 | a=0 | — |
| 2 | main | b ← 1 | a=0; b=1 | — |
| 3 | main | FOR visit i | a=0; b=1; i=0 | — |
| 4 | main | t ← (a + b) | a=0; b=1; i=0; t=1 | — |
| 5 | main | a ← b | a=1; b=1; i=0; t=1 | — |
| 6 | main | b ← t | a=1; b=1; i=0; t=1 | — |
| 7 | main | FOR visit i | a=1; b=1; i=1; t=1 | — |
| 8 | main | t ← (a + b) | a=1; b=1; i=1; t=2 | — |
| 9 | main | a ← b | a=1; b=1; i=1; t=2 | — |
| 10 | main | b ← t | a=1; b=2; i=1; t=2 | — |
| 11 | main | FOR visit i | a=1; b=2; i=2; t=2 | — |
| 12 | main | t ← (a + b) | a=1; b=2; i=2; t=3 | — |
| 13 | main | a ← b | a=2; b=2; i=2; t=3 | — |
| 14 | main | b ← t | a=2; b=3; i=2; t=3 | — |
| 15 | main | FOR visit i | a=2; b=3; i=3; t=3 | — |
| 16 | main | t ← (a + b) | a=2; b=3; i=3; t=5 | — |
| 17 | main | a ← b | a=3; b=3; i=3; t=5 | — |
| 18 | main | b ← t | a=3; b=5; i=3; t=5 | — |
| 19 | main | FOR visit i | a=3; b=5; i=4; t=5 | — |
| 20 | main | t ← (a + b) | a=3; b=5; i=4; t=8 | — |
| 21 | main | a ← b | a=5; b=5; i=4; t=8 | — |
| 22 | main | b ← t | a=5; b=8; i=4; t=8 | — |
| 23 | main | FOR visit i | a=5; b=8; i=5; t=8 | — |
| 24 | main | t ← (a + b) | a=5; b=8; i=5; t=13 | — |
| 25 | main | a ← b | a=8; b=8; i=5; t=13 | — |
| 26 | main | b ← t | a=8; b=13; i=5; t=13 | — |
| 27 | main | FOR exit | a=8; b=13; i=5; t=13 | — |
| 28 | main | PRINT | a=8; b=13; i=5; t=13 | 8 13 |

**Explanation:** After k updates the pair is (F_k,F_(k+1)); the temporary prevents reuse of an overwritten a.

## O077 — Search edge [], target 1

**Answer: A**

```text
-1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [] | A=[] | — |
| 2 | main | target ← 1 | A=[]; target=1 | — |
| 3 | main | found ← (−1) | A=[]; target=1; found=-1 | — |
| 4 | main | FOR exit | A=[]; target=1; found=-1 | — |
| 5 | main | PRINT | A=[]; target=1; found=-1 | -1 |

**Explanation:** A first-match search breaks only after a match; empty and absent cases preserve -1.

## O078 — Search edge [3], target 3

**Answer: B**

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [3] | A=[3] | — |
| 2 | main | target ← 3 | A=[3]; target=3 | — |
| 3 | main | found ← (−1) | A=[3]; target=3; found=-1 | — |
| 4 | main | FOR visit i | A=[3]; target=3; found=-1; i=0 | — |
| 5 | main | IF (A[i] = target) → TRUE | A=[3]; target=3; found=-1; i=0 | — |
| 6 | main | found ← i | A=[3]; target=3; found=0; i=0 | — |
| 7 | main | BREAK | A=[3]; target=3; found=0; i=0 | — |
| 8 | main | FOR exit | A=[3]; target=3; found=0; i=0 | — |
| 9 | main | PRINT | A=[3]; target=3; found=0; i=0 | 0 |

**Explanation:** A first-match search breaks only after a match; empty and absent cases preserve -1.

## O079 — Search edge [2, 2, 2], target 2

**Answer: C**

```text
0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [2, 2, 2] | A=[2, 2, 2] | — |
| 2 | main | target ← 2 | A=[2, 2, 2]; target=2 | — |
| 3 | main | found ← (−1) | A=[2, 2, 2]; target=2; found=-1 | — |
| 4 | main | FOR visit i | A=[2, 2, 2]; target=2; found=-1; i=0 | — |
| 5 | main | IF (A[i] = target) → TRUE | A=[2, 2, 2]; target=2; found=-1; i=0 | — |
| 6 | main | found ← i | A=[2, 2, 2]; target=2; found=0; i=0 | — |
| 7 | main | BREAK | A=[2, 2, 2]; target=2; found=0; i=0 | — |
| 8 | main | FOR exit | A=[2, 2, 2]; target=2; found=0; i=0 | — |
| 9 | main | PRINT | A=[2, 2, 2]; target=2; found=0; i=0 | 0 |

**Explanation:** A first-match search breaks only after a match; empty and absent cases preserve -1.

## O080 — Search edge [1, 4, 7], target 5

**Answer: D**

```text
-1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [1, 4, 7] | A=[1, 4, 7] | — |
| 2 | main | target ← 5 | A=[1, 4, 7]; target=5 | — |
| 3 | main | found ← (−1) | A=[1, 4, 7]; target=5; found=-1 | — |
| 4 | main | FOR visit i | A=[1, 4, 7]; target=5; found=-1; i=0 | — |
| 5 | main | IF (A[i] = target) → FALSE | A=[1, 4, 7]; target=5; found=-1; i=0 | — |
| 6 | main | FOR visit i | A=[1, 4, 7]; target=5; found=-1; i=1 | — |
| 7 | main | IF (A[i] = target) → FALSE | A=[1, 4, 7]; target=5; found=-1; i=1 | — |
| 8 | main | FOR visit i | A=[1, 4, 7]; target=5; found=-1; i=2 | — |
| 9 | main | IF (A[i] = target) → FALSE | A=[1, 4, 7]; target=5; found=-1; i=2 | — |
| 10 | main | FOR exit | A=[1, 4, 7]; target=5; found=-1; i=2 | — |
| 11 | main | PRINT | A=[1, 4, 7]; target=5; found=-1; i=2 | -1 |

**Explanation:** A first-match search breaks only after a match; empty and absent cases preserve -1.

## O081 — Parity-filtered triangle n=1

**Answer: A**

```text
1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | count ← 0 | count=0 | — |
| 2 | main | FOR visit i | count=0; i=1 | — |
| 3 | main | FOR visit j | count=0; i=1; j=1 | — |
| 4 | main | IF (((i + j) MOD 2) = 0) → TRUE | count=0; i=1; j=1 | — |
| 5 | main | count ← (count + 1) | count=1; i=1; j=1 | — |
| 6 | main | FOR exit | count=1; i=1; j=1 | — |
| 7 | main | FOR exit | count=1; i=1; j=1 | — |
| 8 | main | PRINT | count=1; i=1; j=1 | 1 |

**Explanation:** Only pairs of equal parity contribute; the inner bound depends on the row.

## O082 — Parity-filtered triangle n=2

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

## O083 — Parity-filtered triangle n=3

**Answer: C**

```text
4
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
| 14 | main | FOR visit i | count=2; i=3; j=2 | — |
| 15 | main | FOR visit j | count=2; i=3; j=1 | — |
| 16 | main | IF (((i + j) MOD 2) = 0) → TRUE | count=2; i=3; j=1 | — |
| 17 | main | count ← (count + 1) | count=3; i=3; j=1 | — |
| 18 | main | FOR visit j | count=3; i=3; j=2 | — |
| 19 | main | IF (((i + j) MOD 2) = 0) → FALSE | count=3; i=3; j=2 | — |
| 20 | main | FOR visit j | count=3; i=3; j=3 | — |
| 21 | main | IF (((i + j) MOD 2) = 0) → TRUE | count=3; i=3; j=3 | — |
| 22 | main | count ← (count + 1) | count=4; i=3; j=3 | — |
| 23 | main | FOR exit | count=4; i=3; j=3 | — |
| 24 | main | FOR exit | count=4; i=3; j=3 | — |
| 25 | main | PRINT | count=4; i=3; j=3 | 4 |

**Explanation:** Only pairs of equal parity contribute; the inner bound depends on the row.

## O084 — Parity-filtered triangle n=4

**Answer: D**

```text
6
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
| 14 | main | FOR visit i | count=2; i=3; j=2 | — |
| 15 | main | FOR visit j | count=2; i=3; j=1 | — |
| 16 | main | IF (((i + j) MOD 2) = 0) → TRUE | count=2; i=3; j=1 | — |
| 17 | main | count ← (count + 1) | count=3; i=3; j=1 | — |
| 18 | main | FOR visit j | count=3; i=3; j=2 | — |
| 19 | main | IF (((i + j) MOD 2) = 0) → FALSE | count=3; i=3; j=2 | — |
| 20 | main | FOR visit j | count=3; i=3; j=3 | — |
| 21 | main | IF (((i + j) MOD 2) = 0) → TRUE | count=3; i=3; j=3 | — |
| 22 | main | count ← (count + 1) | count=4; i=3; j=3 | — |
| 23 | main | FOR exit | count=4; i=3; j=3 | — |
| 24 | main | FOR visit i | count=4; i=4; j=3 | — |
| 25 | main | FOR visit j | count=4; i=4; j=1 | — |
| 26 | main | IF (((i + j) MOD 2) = 0) → FALSE | count=4; i=4; j=1 | — |
| 27 | main | FOR visit j | count=4; i=4; j=2 | — |
| 28 | main | IF (((i + j) MOD 2) = 0) → TRUE | count=4; i=4; j=2 | — |
| 29 | main | count ← (count + 1) | count=5; i=4; j=2 | — |
| 30 | main | FOR visit j | count=5; i=4; j=3 | — |
| 31 | main | IF (((i + j) MOD 2) = 0) → FALSE | count=5; i=4; j=3 | — |
| 32 | main | FOR visit j | count=5; i=4; j=4 | — |
| 33 | main | IF (((i + j) MOD 2) = 0) → TRUE | count=5; i=4; j=4 | — |
| 34 | main | count ← (count + 1) | count=6; i=4; j=4 | — |
| 35 | main | FOR exit | count=6; i=4; j=4 | — |
| 36 | main | FOR exit | count=6; i=4; j=4 | — |
| 37 | main | PRINT | count=6; i=4; j=4 | 6 |

**Explanation:** Only pairs of equal parity contribute; the inner bound depends on the row.

## O085 — Java postfix then prefix

**Answer: A**

```text
4 6 6
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 4 | x=4 | — |
| 2 | main | a ← x | x=4; a=4 | — |
| 3 | main | x ← (x + 1) | x=5; a=4 | — |
| 4 | main | x ← (x + 1) | x=6; a=4 | — |
| 5 | main | b ← x | x=6; a=4; b=6 | — |
| 6 | main | PRINT | x=6; a=4; b=6 | 4 6 6 |

**Explanation:** Java postfix yields the old value; prefix yields the new value.

The table separates side effects into their evaluation order. The displayed program above follows Java rules; the reference model is used only for verification.

## O086 — Java left-to-right increments

**Answer: B**

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

## O087 — Java decrements

**Answer: C**

```text
5 3 3
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 5 | x=5 | — |
| 2 | main | a ← x | x=5; a=5 | — |
| 3 | main | x ← (x − 1) | x=4; a=5 | — |
| 4 | main | x ← (x − 1) | x=3; a=5 | — |
| 5 | main | b ← x | x=3; a=5; b=3 | — |
| 6 | main | PRINT | x=3; a=5; b=3 | 5 3 3 |

**Explanation:** Postfix uses 5; then prefix decreases 4 to 3.

The table separates side effects into their evaluation order. The displayed program above follows Java rules; the reference model is used only for verification.

## O088 — Java division sign

**Answer: D**

```text
-2 -1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | q ← DIVIDE_TRUNC((−7), 3) | q=-2 | — |
| 2 | main | r ← REMAINDER_TRUNC((−7), 3) | q=-2; r=-1 | — |
| 3 | main | PRINT | q=-2; r=-1 | -2 -1 |

**Explanation:** Java integer / truncates toward zero; remainder has dividend sign.

The table separates side effects into their evaluation order. The displayed program above follows Java rules; the reference model is used only for verification.

## O089 — Java AND short-circuit

**Answer: A**

```text
false 0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 0 | x=0 | — |
| 2 | main | flag ← FALSE | x=0; flag=FALSE | — |
| 3 | main | PRINT | x=0; flag=FALSE | FALSE 0 |

**Explanation:** The false first operand skips ++x entirely; Java prints lowercase false.

The table separates side effects into their evaluation order. The displayed program above follows Java rules; the reference model is used only for verification.

## O090 — Java switch fall-through

**Answer: B**

```text
5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 2 | x=2 | — |
| 2 | main | s ← 0 | x=2; s=0 | — |
| 3 | main | s ← (s + 2) | x=2; s=2 | — |
| 4 | main | s ← (s + 3) | x=2; s=5 | — |
| 5 | main | PRINT | x=2; s=5 | 5 |

**Explanation:** case 2 has no break, so case 3 also runs before its break.

The table separates side effects into their evaluation order. The displayed program above follows Java rules; the reference model is used only for verification.

## O091 — Java ternary skips other arm

**Answer: C**

```text
3 4
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 3 | x=3 | — |
| 2 | main | y ← x | x=3; y=3 | — |
| 3 | main | x ← (x + 1) | x=4; y=3 | — |
| 4 | main | PRINT | x=4; y=3 | 3 4 |

**Explanation:** Only the selected x++ arm executes.

The table separates side effects into their evaluation order. The displayed program above follows Java rules; the reference model is used only for verification.

## O092 — Java logical OR skip

**Answer: D**

```text
true 1
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 1 | x=1 | — |
| 2 | main | flag ← TRUE | x=1; flag=TRUE | — |
| 3 | main | PRINT | x=1; flag=TRUE | TRUE 1 |

**Explanation:** True first operand skips x++ in the right operand. Java prints lowercase true.

The table separates side effects into their evaluation order. The displayed program above follows Java rules; the reference model is used only for verification.

## O093 — Python floor division

**Answer: A**

```text
-3 2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | Python | -7 // 3 → -3 | q=-3 | — |
| 2 | Python | -7 % 3 → 2 | r=2 | — |
| 3 | Python | print | q=-3; r=2 | -3 2 |

**Explanation:** Python // floors toward minus infinity; positive divisor makes the remainder nonnegative.

The table separates side effects into their evaluation order. The displayed program above follows Python rules; the reference model is used only for verification.

## O094 — Python double unary plus

**Answer: B**

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

## O095 — Python range end excluded

**Answer: C**

```text
10
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← 0 | s=0 | — |
| 2 | main | FOR visit i | s=0; i=1 | — |
| 3 | main | s ← (s + i) | s=1; i=1 | — |
| 4 | main | FOR visit i | s=1; i=2 | — |
| 5 | main | s ← (s + i) | s=3; i=2 | — |
| 6 | main | FOR visit i | s=3; i=3 | — |
| 7 | main | s ← (s + i) | s=6; i=3 | — |
| 8 | main | FOR visit i | s=6; i=4 | — |
| 9 | main | s ← (s + i) | s=10; i=4 | — |
| 10 | main | FOR exit | s=10; i=4 | — |
| 11 | main | PRINT | s=10; i=4 | 10 |

**Explanation:** Python range visits 1,2,3,4; end 5 is excluded.

The table separates side effects into their evaluation order. The displayed program above follows Python rules; the reference model is used only for verification.

## O096 — Python negative indexing

**Answer: D**

```text
6
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | A ← [2, 4, 6] | A=[2, 4, 6] | — |
| 2 | main | PRINT | A=[2, 4, 6] | 6 |

**Explanation:** In real Python A[-1] denotes the last element; our neutral pseudocode forbids negative indices.

The table separates side effects into their evaluation order. The displayed program above follows Python rules; the reference model is used only for verification.

## O097 — C increments separated

**Answer: A**

```text
3 5 5
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | x ← 3 | x=3 | — |
| 2 | main | a ← x | x=3; a=3 | — |
| 3 | main | x ← (x + 1) | x=4; a=3 | — |
| 4 | main | x ← (x + 1) | x=5; a=3 | — |
| 5 | main | b ← x | x=5; a=3; b=5 | — |
| 6 | main | PRINT | x=5; a=3; b=5 | 3 5 5 |

**Explanation:** Each modification is in a separate full expression, so no unsequenced side effects.

The table separates side effects into their evaluation order. The displayed program above follows C rules; the reference model is used only for verification.

## O098 — C decrement loop

**Answer: B**

```text
10 0
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | s ← 0 | s=0 | — |
| 2 | main | i ← 4 | s=0; i=4 | — |
| 3 | main | WHILE (i > 0) → TRUE | s=0; i=4 | — |
| 4 | main | s ← (s + i) | s=4; i=4 | — |
| 5 | main | i ← (i − 1) | s=4; i=3 | — |
| 6 | main | WHILE (i > 0) → TRUE | s=4; i=3 | — |
| 7 | main | s ← (s + i) | s=7; i=3 | — |
| 8 | main | i ← (i − 1) | s=7; i=2 | — |
| 9 | main | WHILE (i > 0) → TRUE | s=7; i=2 | — |
| 10 | main | s ← (s + i) | s=9; i=2 | — |
| 11 | main | i ← (i − 1) | s=9; i=1 | — |
| 12 | main | WHILE (i > 0) → TRUE | s=9; i=1 | — |
| 13 | main | s ← (s + i) | s=10; i=1 | — |
| 14 | main | i ← (i − 1) | s=10; i=0 | — |
| 15 | main | WHILE (i > 0) → FALSE | s=10; i=0 | — |
| 16 | main | PRINT | s=10; i=0 | 10 0 |

**Explanation:** Post-decrement loop update happens after the body each time.

The table separates side effects into their evaluation order. The displayed program above follows C rules; the reference model is used only for verification.

## O099 — C do-while runs once

**Answer: C**

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

## O100 — C integer division

**Answer: D**

```text
3 2
```

| Step | Frame | Executed operation / decision | Variables after step | Printed line |
| --- | --- | --- | --- | --- |
| 1 | main | q ← DIVIDE_TRUNC(17, 5) | q=3 | — |
| 2 | main | r ← REMAINDER_TRUNC(17, 5) | q=3; r=2 | — |
| 3 | main | PRINT | q=3; r=2 | 3 2 |

**Explanation:** Both operands are int, so division truncates.

The table separates side effects into their evaluation order. The displayed program above follows C rules; the reference model is used only for verification.
