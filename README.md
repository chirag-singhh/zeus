# Zeus technical assessment: tomorrow-ready preparation

Prepared for **10 October 2026**. Start studying on **9 October 2026**. This is an original learning repository, not a collection of actual or previous-year Zeus questions. The mock timings, topic balance and scoring are training choices, not claims about the employer's assessment.

## Repository and progress

Read a topic, solve without the answer key, trace on paper, then check. Record the mistake and retry it after an hour. You do not need to finish every question today: accuracy on representative problems comes before volume.

| File | Purpose |
|---|---|
| [README.md](README.md) | Full theory, conventions, worked examples and topic drills |
| [pseudocode-writing-questions.md](pseudocode-writing-questions.md) | W001–W060: build algorithms, easy to hard |
| [pseudocode-writing-answers.md](pseudocode-writing-answers.md) | Complete algorithms, execution tables and complexity |
| [output-prediction-questions.md](output-prediction-questions.md) | O001–O100: predict exact output |
| [output-prediction-answers.md](output-prediction-answers.md) | Outputs, variable tables and explanations |
| [error-detection-questions.md](error-detection-questions.md) | E001–E075: locate and repair faults |
| [error-detection-answers.md](error-detection-answers.md) | Root causes, corrections and verification |
| [mock-tests.md](mock-tests.md) | M1-Q01–M3-Q30: three timed mixed tests |
| [mock-test-answers.md](mock-test-answers.md) | Full solutions and partial-credit rubric |
| [last-minute-revision.md](last-minute-revision.md) | One-day schedule, 30-minute checklist, exam strategy |
| [PROGRESS.md](PROGRESS.md) | Generation and verification checklist |
| tools/build_repository.py | Reproducible generation and independent execution checks |
| verification/report.json | Counts, ID matching and output-check results |

## Our pseudocode contract — read before solving

Pseudocode has no universal standard. These rules apply to every **Pseudocode** block here. A explicitly labelled Python, C or Java block follows that language instead.

- Variables must be initialized before use. Integers have unlimited precision here; REAL supports fractional values; BOOLEAN is TRUE or FALSE; STRING is a sequence of characters. No implicit Boolean-to-integer conversion or truthiness.
- `x ← expression` assigns; `=` compares equality; `≠`, `<`, `≤`, `>` and `≥` compare values. Conditions must be Boolean. Quotes denote strings; `+` joins two strings or adds two numbers, never silently joins a number to a string.
- Arrays and strings use **zero-based indexing**. For length n, valid indices are 0 through n−1. Empty arrays have no valid index. Negative indexing is an error here. Matrices use `M[row][column]`. `LENGTH`, `APPEND`, `ABS`, `MIN`, `MAX`, `SORTED`, `SUM`, `COUNT`, `REVERSE`, `SLICE` and `JOIN` have their ordinary meanings. SLICE uses start-inclusive/end-exclusive bounds; REVERSE returns a reversed copy. COUNT counts exact matches; JOIN inserts the given separator. SORTED returns an ascending copy. An array literal creates a new array; `B ← A` aliases the same array.
- `FOR i ← a TO b STEP s` includes b if reached, evaluates a/b/s once when entered, uses positive or negative nonzero s, and skips its body when the initial bound fails. Default STEP is 1. Positive steps require i ≤ b; negative steps require i ≥ b. i retains its last visited value after a nonempty loop; do not infer a post-loop i after an empty loop. `CONTINUE` advances to the next FOR iteration; `BREAK` exits only the innermost loop. Do not modify a FOR control variable in its body; use WHILE for such questions.
- `WHILE condition ... END WHILE` tests first. `DO ... WHILE condition` tests last and runs at least once. Indentation and END markers establish blocks. `IF ... THEN`, `ELSE IF`, `ELSE`, `END IF` use only the first true branch.
- `DIV` truncates toward zero: −7 DIV 3 = −2. `a MOD b = a − (a DIV b) × b`; −7 MOD 3 = −1. Division by zero is a runtime error. `/` is real division. Nonnegative digit problems use DIV 10 and MOD 10.
- Precedence, highest first: parentheses/indexing/function calls; unary numeric `−`, `BIT_NOT8`, Boolean `NOT`; `* / DIV MOD`; `+ −`; `SHL SHR`; `BIT_AND`; `BIT_XOR`; `BIT_OR`; one comparison; `AND`; `OR`; conditional `x IF c ELSE y`; assignment as a statement. Binary operators at the same level associate left to right. There is no exponent operator in the contract; use `POWER(a,b)`. Always parenthesize mixtures of comparison, bits and logic. Do not chain comparisons in pseudocode.
- AND/OR evaluate left to right and **short-circuit**. `FALSE AND dangerous()` does not call dangerous; `TRUE OR dangerous()` does not call dangerous. NOT negates a Boolean. Bit operators operate on nonnegative integers unless stated otherwise. `BIT_NOT8(x)` flips exactly 8 bits and requires 0 ≤ x ≤ 255. `x SHL k` means x × 2^k; `x SHR k` means x DIV 2^k for x ≥ 0 and integer k ≥ 0. No overflow in neutral pseudocode.
- Functions receive scalar values by value. Arrays are shared references: element changes are visible to callers; reassignment of a parameter does not replace the caller's variable. RETURN exits immediately. Recursion uses a fresh frame with its own parameters/locals. Arguments and expression operands evaluate left to right.
- `PRINT v1, v2` produces one line, values separated by one space. Booleans print TRUE/FALSE; arrays print `[a, b]`; printing a string prints its characters without quotation marks. Each separate PRINT starts a new line. An empty string produces a blank line. This exact convention is used by the answer keys.
- Increment/decrement are **not** neutral-pseudocode operators. Write `i ← i + 1` or `i ← i − 1`. Prefix/postfix questions below carry a real-language label.

## 1. Variables, types, assignment and comparison

A variable is a named box holding a value. Assignment replaces its contents. A comparison asks a yes/no question; it does not change the variable. INTEGER suits counters; REAL suits averages; BOOLEAN suits decisions; STRING suits text. A temporary box prevents data loss during a swap.

```text
Pseudocode
a ← 4
b ← 9
temp ← a
a ← b
b ← temp
PRINT a, b, (a = b)
```

| Statement | a | b | temp | Explanation |
|---|---:|---:|---:|---|
| initialize | 4 | 9 | — | separate values |
| temp ← a | 4 | 9 | 4 | preserve original a |
| a ← b | 9 | 9 | 4 | a is overwritten |
| b ← temp | 9 | 4 | 4 | swap complete |

Output: `9 4 FALSE`. Mistakes: reading an uninitialized variable; writing `a ← b; b ← a` as a swap; confusing `=` with assignment in another language. Shortcut: draw one column per variable and update only the target column. Check the multiset of values after swapping.

Topic drills: **T01-E** swap 2 and 7 using a temporary; **T01-M** rotate (1,2,3) to (3,1,2); **T01-H** explain why two independent scalar function parameters cannot swap the caller's boxes. Checks: E → (7,2); M → save c, then c←b, b←a, a←saved; H → return the new pair or use reference parameters explicitly.

## 2. Operators, precedence, associativity, DIV and MOD

Arithmetic builds values. Parentheses override precedence. Associativity decides grouping when precedence ties; subtraction and DIV group left to right. A quotient counts whole groups; a remainder records what is left.

```text
Pseudocode
x ← 17 DIV 5
y ← 17 MOD 5
z ← 2 + 3 * 4
w ← (2 + 3) * 4
PRINT x, y, z, w
```

| Expression | Evaluation | Value |
|---|---|---:|
| 17 DIV 5 | truncate 3.4 | 3 |
| 17 MOD 5 | 17−3×5 | 2 |
| 2+3×4 | multiply, then add | 14 |
| (2+3)×4 | add, then multiply | 20 |

Mistakes: assuming `/` is always integer division; applying Python negative // semantics to C/Java; treating `a-b-c` as `a-(b-c)`. Shortcut: rewrite the expression with explicit parentheses and substitute one operator at a time. Check `a = q*b+r`.

Drills: **T02-E** 23 DIV 4 and MOD 4; **T02-M** 20−6−3×2; **T02-H** −23 DIV 4 and MOD 4 under our rules. Checks: 5,3; 8; −5,−3. For signed inputs, |r|<|b| and nonzero r has the dividend's sign.

## 3. Conditions and nested if/else

A condition selects a route. Nested conditions make a second decision within the selected route. ELSE attaches to its matching IF; indentation matters. Evaluate branches in order.

```text
Pseudocode
x ← 0
IF x ≥ 0 THEN
    IF x = 0 THEN
        PRINT "zero"
    ELSE
        PRINT "positive"
    END IF
ELSE
    PRINT "negative"
END IF
```

| Decision | Result | Next action |
|---|---|---|
| x≥0 | TRUE | enter outer IF |
| x=0 | TRUE | print zero |
| remaining branches | skipped | stop |

Mistakes: two separate IFs can both run; ELSE IF allows one branch; boundary equality is easily lost. Shortcut: test just below, at and just above each threshold.

Drills: **T03-E** classify −2; **T03-M** grades A for ≥80, B for ≥60, C otherwise; classify 60; **T03-H** choose largest of three including ties. Checks: negative; B; initialize best to first and replace only when a later value is greater, so ties remain valid.

## 4. Switch and ternary expressions

SWITCH chooses an exact matching case. Our teaching SWITCH has **no fall-through**; real C/Java statement switches can fall through when BREAK is omitted. A ternary chooses one of two values; only the selected value expression runs.

```text
Pseudocode
day ← 2
SWITCH day
    CASE 1: label ← "Mon"
    CASE 2: label ← "Tue"
    DEFAULT: label ← "Other"
END SWITCH
best ← 7 IF 7 > 3 ELSE 3
PRINT label, best
```

| Step | State | Reason |
|---|---|---|
| match day=2 | label=Tue | exact match |
| test 7>3 | TRUE | choose first value |
| result | Tue 7 | other expressions skipped |

Mistakes: importing fall-through into neutral code; mixing statements with value expressions; reversing ternary positions. C/Java spelling: `c ? x : y`; Python spelling: `x if c else y`. Shortcut: first decide the condition, then inspect only the selected value.

Drills: **T04-E** select default for day 9; **T04-M** minimum via ternary for 8 and −1; **T04-H** in a C switch, case 1 prints A then falls into case 2 printing B before BREAK: input 1? Checks: Other; −1; AB when no spaces/newlines are printed.

## 5. FOR, WHILE and DO-WHILE

FOR is useful when visits are planned. WHILE repeats while a condition remains true. DO-WHILE performs the body before checking, so even a initially false condition allows one execution.

```text
Pseudocode
s ← 0
FOR i ← 1 TO 5 STEP 2
    s ← s + i
END FOR
j ← 3
WHILE j > 0
    j ← j − 1
END WHILE
k ← 0
DO
    k ← k + 1
WHILE k < 0
PRINT s, j, k
```

| Loop | Visited/body values | Final state |
|---|---|---|
| FOR | i=1,3,5; s=1,4,9 | s=9 |
| WHILE | j:3→2→1→0 | j=0 |
| DO-WHILE | k:0→1, test FALSE | k=1 |

Mistakes: forgetting update; treating inclusive TO like Python range; assuming every loop executes. Shortcut for increasing arithmetic visits: if a≤b and s>0, count=floor((b−a)/s)+1. For decreasing visits a≥b and s<0, count=floor((a−b)/|s|)+1. Check first, last and next rejected value.

Drills: **T05-E** visits 0 TO 3; **T05-M** visits 7 TO 1 STEP −2; **T05-H** contrast WHILE FALSE with DO body WHILE FALSE. Checks: 0,1,2,3; 7,5,3,1; zero bodies versus one.

## 6. Nested loops, break, continue and boundaries

Each outer iteration starts a fresh inner loop. BREAK exits the innermost loop only. CONTINUE skips the remaining body, then proceeds with that loop's usual next step. In a WHILE, any required update must still occur before CONTINUE.

```text
Pseudocode
count ← 0
FOR i ← 1 TO 3
    FOR j ← 1 TO i
        IF j = 2 THEN
            CONTINUE
        END IF
        count ← count + 1
    END FOR
END FOR
PRINT count
```

| i | j visits | Counted j | count after row |
|---:|---|---|---:|
| 1 | 1 | 1 | 1 |
| 2 | 1,2 | 1 | 2 |
| 3 | 1,2,3 | 1,3 | 4 |

Mistakes: multiplying bounds when the inner limit depends on i; assuming BREAK exits all loops; putting the WHILE update after a CONTINUE; using ≤LENGTH for indexing. Shortcut: rectangular loops count n×m; triangular loops 1+…+n=n(n+1)/2. Check the innermost operation, not just the header.

Drills: **T06-E** 2 rows ×3 columns; **T06-M** triangular loop through 4; **T06-H** same triangle but break inner loop at j=2 before counting. Checks: 6; 10; one count per outer row, total 4.

## 7. Prefix/postfix increment and decrement: real languages

Prefix changes the variable and produces the new value. Postfix produces the old value and changes the variable. Side effects and evaluation order are language rules, not universal arithmetic shortcuts.

```java
// Java: separate statements, well-defined
int x = 4;
int a = x++; // a=4, x=5
int b = ++x; // x=6, b=6
int c = x--; // c=6, x=5
int d = --x; // x=4, d=4
System.out.println(a + " " + b + " " + c + " " + d + " " + x);
```

| Statement | Expression result | x afterward |
|---|---:|---:|
| a=x++ | 4 | 5 |
| b=++x | 6 | 6 |
| c=x-- | 6 | 5 |
| d=--x | 4 | 4 |

Java evaluates operands left to right; e.g. starting x=2, `x++ + ++x` yields 2+4=6 and leaves x=4. This is **Java only**. C expressions such as `x++ + ++x` modify x without sequencing and have undefined behavior; there is no valid output to predict. C `&&`, `||`, the comma operator and the condition of `?:` establish relevant sequencing, but function argument order is not a left-to-right guarantee. Prefer separate statements. Python has no ++ or -- operators: `++x` parses as two unary plus operations and leaves x unchanged; `--x` is two unary minuses, also unchanged. `x++` is invalid Python syntax. C signed overflow is undefined; Java int wraps; Python integers grow. Our neutral integers do not overflow.

Mistakes: assuming prefix means “first in the whole expression”; transferring Java order to C; treating Python ++ as an increment. Shortcut: mark OLD/NEW next to each occurrence and update a table only in a language with defined evaluation.

Drills: **T07-E** Java x=3, a=x--; **T07-M** Java x=2, y=++x+x++; **T07-H** explain C x++ + ++x and Python ++x. Checks: a=3,x=2; y=6,x=4; C undefined, Python unchanged.

## 8. Arrays: indexing, traversal, mutation and aliasing

An array stores ordered elements. Index zero names the first one. A traversal visits valid indices, often to accumulate or modify. Mutation changes an element; an alias refers to the same array.

```text
Pseudocode
A ← [3, 1, 4]
s ← 0
FOR i ← 0 TO LENGTH(A) − 1
    s ← s + A[i]
END FOR
B ← A
B[0] ← 9
PRINT s, A
```

| i/action | A[i] | s | A |
|---|---:|---:|---|
| i=0 | 3 | 3 | [3,1,4] |
| i=1 | 1 | 4 | [3,1,4] |
| i=2 | 4 | 8 | [3,1,4] |
| B[0]←9 | — | 8 | [9,1,4] |

Mistakes: last index n rather than n−1; initializing maximum to zero when all values are negative; confusing a copy and alias. Shortcut: write array indices above values. For nonempty maximum initialize from A[0]; handle empty input separately.

Drills: **T08-E** last index of length 5; **T08-M** maximum of [−7,−2,−9]; **T08-H** A=[1,2], B←A, B[1]←8: A? Checks: 4; −2; [1,8].

## 9. Searching and sorting

Linear search tests elements in order. Binary search repeatedly halves a **sorted** interval. Bubble sort swaps neighboring inversions, moving a large element toward the right. Selection sort chooses the smallest remaining element.

```text
Pseudocode
A ← [2, 5, 8, 11, 14]
lo ← 0
hi ← LENGTH(A) − 1
found ← −1
WHILE lo ≤ hi
    mid ← lo + (hi − lo) DIV 2
    IF A[mid] = 11 THEN
        found ← mid
        BREAK
    ELSE IF A[mid] < 11 THEN
        lo ← mid + 1
    ELSE
        hi ← mid − 1
    END IF
END WHILE
PRINT found
```

| lo | hi | mid | A[mid] | Action |
|---:|---:|---:|---:|---|
| 0 | 4 | 2 | 8 | lo=3 |
| 3 | 4 | 3 | 11 | found=3, break |

Bubble example: [3,1,2] → compare (3,1), swap → [1,3,2] → compare (3,2), swap → [1,2,3]. Mistakes: binary search on unsorted data; setting lo=mid instead of mid+1; accessing j+1 at the last index. Shortcut: trace bounds, not the entire array, for binary search. Verify sorted output is nondecreasing and has the same counts of each original value.

Drills: **T09-E** first index of 5 in [5,2,5]; **T09-M** one bubble pass on [4,2,3]; **T09-H** binary search absent target 6 in [2,5,8]. Checks: 0; [2,3,4]; mid1=5→lo2, mid2=8→hi1, empty interval→−1.

## 10. Strings

A string is indexed text. LENGTH counts characters in our ASCII exercises. Compare characters exactly unless case normalization is requested. Build reversed text by visiting from the last character. Real Python/Java strings are immutable; construct a new string rather than assign to a character.

```text
Pseudocode
s ← "level"
left ← 0
right ← LENGTH(s) − 1
ok ← TRUE
WHILE left < right
    IF s[left] ≠ s[right] THEN
        ok ← FALSE
        BREAK
    END IF
    left ← left + 1
    right ← right − 1
END WHILE
PRINT ok
```

| left | right | Pair | Match |
|---:|---:|---|---|
| 0 | 4 | l/l | TRUE |
| 1 | 3 | e/e | TRUE |
| 2 | 2 | loop stops | TRUE retained |

Mistakes: counting spaces as vowels; using case-sensitive equality for a case-insensitive specification; right=LENGTH; unnecessarily comparing middle character to itself. Shortcut: mirrored positions sum to n−1. Empty and one-character strings are palindromes under the usual definition.

Drills: **T10-E** index 1 in "code"; **T10-M** vowels in "Zeus" ignoring case; **T10-H** palindrome "abca"? Checks: o; 2; a/a matches then b/c fails.

## 11. Matrices

A matrix is an array of rows. Row and column bounds may differ. A transpose exchanges coordinates: result[j][i]=original[i][j]. A square matrix's main diagonal has row=column; secondary diagonal has row+column=n−1.

```text
Pseudocode
M ← [[1, 2, 3], [4, 5, 6]]
s ← 0
FOR r ← 0 TO 1
    FOR c ← 0 TO 2
        s ← s + M[r][c]
    END FOR
END FOR
PRINT s
```

| Row | Values added | s after row |
|---:|---|---:|
| 0 | 1,2,3 | 6 |
| 1 | 4,5,6 | 21 |

Mistakes: using number of rows for a column bound; transposing in place as if every matrix is square; counting the center twice in combined diagonals. Shortcut: write dimensions r×c; transpose has c×r. Check a 2×3 matrix to expose swapped bounds.

Drills: **T11-E** M[1][2] above; **T11-M** transpose shape; **T11-H** both-diagonal sum of [[1,2,3],[4,5,6],[7,8,9]] counting center once. Checks: 6; 3×2; (1+5+9)+(3+5+7)−5=25.

## 12. Functions, parameters and returns

A function packages a task. Arguments provide input; parameters are local names; RETURN supplies a result and ends the call. Merely computing a value does not return it. Distinguish printing from returning.

```text
Pseudocode
FUNCTION addOne(x)
    x ← x + 1
    RETURN x
END FUNCTION
a ← 5
b ← addOne(a)
PRINT a, b
```

| Stage | caller a | local x | caller b |
|---|---:|---:|---:|
| before call | 5 | — | — |
| entry | 5 | 5 | — |
| update | 5 | 6 | — |
| return | 5 | frame gone | 6 |

Mistakes: expecting scalar parameter mutation to change caller; forgetting RETURN in one branch; treating output text as a returned number. Shortcut: draw a box around local variables. Verify every promised return path.

Drills: **T12-E** addOne(0); **T12-M** call twice as addOne(addOne(3)); **T12-H** array parameter A has A[0]←8 versus A←[8]. Checks: 1; 5; first mutates caller's array, second only rebinds local parameter.

## 13. Recursion and call stacks

Recursion means a function calls itself on a smaller problem. A base case stops it. Every active call occupies a stack frame. On return, frames unwind in reverse order. Print-before-call and print-after-call produce different sequences.

```text
Pseudocode
FUNCTION fact(n)
    IF n ≤ 1 THEN
        RETURN 1
    END IF
    RETURN n * fact(n − 1)
END FUNCTION
PRINT fact(4)
```

| Frame | Waiting expression | Returned value |
|---|---|---:|
| fact(4) | 4×fact(3) | 24 |
| fact(3) | 3×fact(2) | 6 |
| fact(2) | 2×fact(1) | 2 |
| fact(1) | base | 1 |

Execution descends 4→3→2→1, then returns 1→2→6→24. Mistakes: no base case; argument moves away from base; assuming all locals are one shared variable; forgetting work after recursive call. Shortcut: write the descent and return phases separately. Factorial is O(n) time and O(n) stack; naive Fibonacci is exponential time and O(n) maximum stack.

Drills: **T13-E** fact(0); **T13-M** print n then recurse n−1 until 0 from 3; **T13-H** recurse first then print n from 3. Checks: 1; 3,2,1 on separate lines; 1,2,3 on separate lines.

## 14. Binary and bitwise operators

Binary places have weights 1,2,4,8,… from right to left. AND keeps a bit only when both have 1; OR keeps it if either has 1; XOR keeps it when they differ. NOT needs a width to avoid ambiguous leading bits. Shifts move bits left/right.

```text
Pseudocode
a ← 12
b ← 10
PRINT (a BIT_AND b), (a BIT_OR b), (a BIT_XOR b)
PRINT BIT_NOT8(12), (3 SHL 2), (13 SHR 1)
```

| Operator | Binary calculation | Decimal |
|---|---|---:|
| AND | 1100 AND 1010 = 1000 | 8 |
| OR | 1100 OR 1010 = 1110 | 14 |
| XOR | 1100 XOR 1010 = 0110 | 6 |
| NOT8 | 00001100 → 11110011 | 243 |
| shifts | 3×4; 13 DIV 2 | 12;6 |

Mistakes: XOR is not power; bitwise AND is not short-circuit Boolean AND; applying width-free NOT to an assumed 8-bit value; shifting a negative signed value without identifying the language. Python `~12` = −13, unlike BIT_NOT8. Java shifts on int use only the low 5 shift-count bits; `>>` sign-extends, `>>>` zero-fills. C invalid shift counts and some signed shifts cause undefined or implementation-dependent behavior. Neutral examples avoid these cases.

Shortcut: align bits; XOR with the same value twice cancels it; x BIT_AND 1 tests oddness; positive power of two satisfies x BIT_AND (x−1)=0. Check x>0 first.

Drills: **T14-E** 5 XOR 3; **T14-M** BIT_NOT8(255); **T14-H** repeatedly x←x BIT_AND (x−1) from 13. Checks: 6; 0; 13→12→8→0, three set bits.

## 15. Boolean logic and short-circuit evaluation

Booleans combine facts. AND requires both; OR requires at least one; NOT reverses. Logical implication P→Q is FALSE only when P is TRUE and Q is FALSE; represent it as `(NOT P) OR Q`.

| P | Q | P AND Q | P OR Q | P XOR Q (logical exclusive-or) | P→Q |
|---|---|---|---|---|---|
| FALSE | FALSE | FALSE | FALSE | FALSE | TRUE |
| FALSE | TRUE | FALSE | TRUE | TRUE | TRUE |
| TRUE | FALSE | FALSE | TRUE | TRUE | FALSE |
| TRUE | TRUE | TRUE | TRUE | FALSE | TRUE |

```text
Pseudocode
d ← 0
safe ← (d ≠ 0) AND (12 DIV d > 2)
PRINT safe
```

| Step | Value | Effect |
|---|---|---|
| d≠0 | FALSE | AND is decided |
| 12 DIV d >2 | not evaluated | division avoided |
| safe | FALSE | printed |

Mistakes: evaluating skipped terms; confusing NOT(P AND Q) with (NOT P) AND (NOT Q); replacing “only if” with its converse. De Morgan: NOT(P AND Q)=(NOT P) OR (NOT Q). NOT(P OR Q)=(NOT P) AND (NOT Q). Shortcut: evaluate left to right; cross out skipped calls. To disprove a conclusion, find one allowed truth-table row where it fails.

Drills: **T15-E** TRUE AND FALSE; **T15-M** NOT(FALSE OR TRUE); **T15-H** P→Q and Q=FALSE: what follows? Checks: FALSE; FALSE; P=FALSE by contrapositive.

## 16. Digits, reversal and numerical palindromes

For a nonnegative decimal integer, MOD 10 removes the last digit's value and DIV 10 removes that position. A sum accumulator starts at 0; a reverse accumulator uses reverse×10+digit. Zero has one decimal digit. Negative inputs require an explicitly stated policy.

```text
Pseudocode
n ← 1203
rev ← 0
sum ← 0
WHILE n > 0
    digit ← n MOD 10
    sum ← sum + digit
    rev ← rev * 10 + digit
    n ← n DIV 10
END WHILE
PRINT sum, rev
```

| n before | digit | sum | rev | n after |
|---:|---:|---:|---:|---:|
| 1203 | 3 | 3 | 3 | 120 |
| 120 | 0 | 3 | 30 | 12 |
| 12 | 2 | 5 | 302 | 1 |
| 1 | 1 | 6 | 3021 | 0 |

Mistakes: overwriting n before saving original for palindrome; sum×10 instead of sum+digit; expecting numerical reversal to preserve leading zeros. Shortcut: exactly one iteration per nonzero input digit. Check reverse(120)=21, not a three-digit integer.

Drills: **T16-E** last digit of 47; **T16-M** digit sum of 909; **T16-H** is 120 a numeric palindrome? Checks: 7; 18; FALSE, reverse=21.

## 17. Prime numbers

A prime is an integer ≥2 with exactly two positive divisors. If n is composite, at least one factor is ≤sqrt(n). Trial division only needs d*d≤n, with equality included for perfect squares.

```text
Pseudocode
n ← 25
prime ← (n ≥ 2)
d ← 2
WHILE prime AND d * d ≤ n
    IF n MOD d = 0 THEN
        prime ← FALSE
    END IF
    d ← d + 1
END WHILE
PRINT prime
```

| d tested | n MOD d | prime afterward |
|---:|---:|---|
| 2 | 1 | TRUE |
| 3 | 1 | TRUE |
| 4 | 1 | TRUE |
| 5 | 0 | FALSE |

Mistakes: treating 1 as prime; excluding sqrt(n); stopping after a single non-divisor. Shortcut: test 0,1,2,4,9 and a prime. For fixed-width integers avoid d*d overflow by d≤n DIV d; our integers do not overflow.

Drills: **T17-E** is 1 prime? **T17-M** why test divisor 7 for 49? **T17-H** complexity in numeric n and in its bit length? Checks: FALSE; equality at sqrt matters; O(sqrt(n)) trials, exponential in input bit length rather than polynomial in it.

## 18. Factorial, Fibonacci and GCD

Factorial multiplies 1 through n and has 0!=1. Fibonacci here starts F0=0,F1=1; each later term sums the previous two. Euclid's GCD replaces (a,b) with (b,a MOD b) until b=0. GCD(0,0)=0 by our convention.

```text
Pseudocode
a ← 48
b ← 18
WHILE b ≠ 0
    r ← a MOD b
    a ← b
    b ← r
END WHILE
PRINT a
```

| a before | b before | r | next (a,b) |
|---:|---:|---:|---|
| 48 | 18 | 12 | (18,12) |
| 18 | 12 | 6 | (12,6) |
| 12 | 6 | 0 | (6,0) |

Fibonacci update must preserve old values: next←a+b; a←b; b←next. Trace pairs for four updates from (0,1): (1,1),(1,2),(2,3),(3,5), so F4=3. Factorial trace n=4: product 1→1→2→6→24.

Mistakes: product starts at 0; Fibonacci updates overwrite an old value too early; taking MOD after replacing a; division by zero at b=0. Shortcut: factorial identity is 1, sum identity is 0. Euclid preserves common divisors; final answer must divide both original numbers.

Drills: **T18-E** 0!; **T18-M** F6; **T18-H** GCD(0,15). Checks: 1; 8; first step (15,0), answer 15.

## 19. Time and space complexity

Time counts how work grows with input size, not seconds. Space counts extra storage, including live recursion frames. O describes an upper bound; Θ a tight bound. State whether stored output counts. Here complexity notes use worst-case time and auxiliary space unless specified.

```text
Pseudocode
i ← 1
count ← 0
WHILE i < n
    count ← count + 1
    i ← i * 2
END WHILE
PRINT count
```

| n | i values entering body | count |
|---:|---|---:|
| 8 | 1,2,4 | 3 |
| 9 | 1,2,4,8 | 4 |
| 16 | 1,2,4,8 | 4 |

One fixed calculation is O(1); full traversal O(n); nested independent n loops O(n²); halving/doubling O(log n); linear recursion O(n) stack; naive Fibonacci O(2^n) upper bound. A returned n-element array uses O(n) output space. We use the usual unit-cost arithmetic model; large integer bit costs are outside basic assessment analysis.

Mistakes: any nesting means n² (bounds matter); binary search O(n); recursive code always O(n); ignoring slice allocations. Shortcut: count operation executions. Independent loops add, nested loop visits multiply or sum, recursion requires counting calls.

Drills: **T19-E** two sequential n traversals; **T19-M** triangle of n rows; **T19-H** outer n loop with inner doubling from 1 to n. Checks: Θ(n); Θ(n²); Θ(n log n), assuming n≥2.

## 20. Logical reasoning and data sufficiency

Translate sentences into constraints. “All A are B” means A is a subset of B, not B a subset of A. “Some” asserts at least one member; “all” alone does not assert that any members exist. A necessary condition must hold in every permitted arrangement. A sufficient condition guarantees a conclusion. Do not import unstated facts.

Example: three people A,B,C take distinct positions 1,2,3; A is before B; C is not first.

| Order | A before B? | C not first? | Allowed? |
|---|---|---|---|
| ABC | TRUE | TRUE | TRUE |
| ACB | TRUE | TRUE | TRUE |
| BAC | FALSE | TRUE | FALSE |
| BCA | FALSE | TRUE | FALSE |
| CAB | TRUE | FALSE | FALSE |
| CBA | FALSE | FALSE | FALSE |

Conclusion: A must be first; B's exact position cannot be determined. For sufficiency, test statement I alone, II alone, then both. “Cannot determine” is a valid result if two valid cases produce different answers.

Syntax example: `valid ← (posA < posB) AND (posC ≠ 1)`. Mistakes: assuming a converse; assuming existence from a universal statement; selecting a statement true in only one arrangement. Shortcut: enumerate tiny spaces and seek a counterexample before accepting “must.”

Drills: **T20-E** all cats are animals, M is a cat: M? **T20-M** A→B, B true: A? **T20-H** x integer, I:x>0, II:x<3; is exact x known? Checks: animal; unknown; possible 1 or 2, not sufficient even together.

## 21. Error detection and repairs

First decide what the program is supposed to do. Then separate syntax (cannot parse), runtime (fails on a executed operation), logic (runs but wrong result), boundary (fails at limits) and termination (never makes required progress). A single fault can fit several categories.

```text
Pseudocode — faulty
A ← [2, 4, 6]
s ← 0
FOR i ← 0 TO LENGTH(A)
    s ← s + A[i]
END FOR
```

| i | action | s |
|---:|---|---:|
| 0 | add 2 | 2 |
| 1 | add 4 | 6 |
| 2 | add 6 | 12 |
| 3 | A[3] out of bounds | runtime error |

Repair: end at LENGTH(A)−1. Verify empty array (0), one element [7] (7), and sample (12). Mistakes: changing code without understanding specification; patching only the example; adding an arbitrary BREAK instead of repairing loop progress. Shortcut: inspect initialization, test, update, access and return in that order. Test min input, exact boundary, duplicates and all-negative values.

Drills: **T21-E** factorial accumulator starts 0; **T21-M** binary search updates lo=mid; **T21-H** recursion n−2 with base n=0 for positive odd n. Checks: initialize to 1; use mid+1 after discarding mid; base n≤0 or domain/parity validation plus a compatible recurrence.

## 22. Dry-run method and independent checking

Use this repeatable procedure: (1) name the language and rules, (2) parenthesize expressions, (3) record initial values, (4) test the condition, (5) execute statements in order, (6) update loop state, (7) record each PRINT separately, (8) test the exit condition. With recursion, add a call-depth column. With arrays, note mutations immediately.

```text
Pseudocode
x ← 1
s ← 0
WHILE x ≤ 4
    s ← s + x
    x ← x * 2
END WHILE
PRINT s
```

| x before test | x≤4 | s after body | x after update |
|---:|---|---:|---:|
| 1 | TRUE | 1 | 2 |
| 2 | TRUE | 3 | 4 |
| 4 | TRUE | 7 | 8 |
| 8 | FALSE | 7 unchanged | 8 |

Output 7. Mistakes: writing only final values, counting the rejected iteration, erasing old values before evaluating the RHS. Shortcut: use invariants — sum equals values already visited; search has discarded only impossible positions; sort preserves elements. Independent checking means a second method, such as enumeration versus formula, not repeating the same guess.

Drills: **T22-E** replace bound 4 with 0; **T22-M** replace ≤ with <; **T22-H** replace x←x*2 with x←x−1. Checks: 0; 3; never terminates from x=1 because x remains ≤4 and decreases without bound in our unlimited-integer model.

## Priorities for tomorrow

Start with the contract, arithmetic/Boolean rules, loop bounds and variable tables. Next study arrays, digit problems, recursion and bitwise patterns. Debug the same categories immediately after tracing them. Use timed mocks to diagnose weak areas; the last-minute guide gives the complete schedule and 30-minute checklist. Learn why a distractor is wrong rather than memorize an option letter.

## References and scope

The original exercises use the broad style of tracing, short algorithms and MCQs found in the [official Infosys recruitment sample paper](https://infytq.onwingspan.com/public-assets/InfosysCampusRecruitmentSampleTest-SystemsEngineer.pdf) and the third-party [Capgemini-labelled pseudocode practice quiz](https://www.geeksforgeeks.org/quizzes/capgemini-pseudocode-quiz-questions/). The latter is a practice reference, not an official employer specification. No question is copied and no Zeus pattern is inferred from either source.

For real-language details, consult [Python expression rules](https://docs.python.org/3/reference/expressions.html), [Java expression rules](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html), and the [public C11 committee draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), especially C 6.5 on sequencing. If the assessment gives its own pseudocode conventions, those override this repository's training contract.
