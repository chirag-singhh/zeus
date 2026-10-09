# Last-minute revision — assessment on 10 October 2026

You are studying on 9 October. Aim to recognize the operation pattern and trace accurately before trying to memorize a large bank. All times below are **Asia/Kolkata (UTC+05:30)**. If you start later, shift the blocks and prioritize the core sequence below; preserve sleep. The examination's start time has not been supplied, so exam-day activities are relative to your reporting time.

## One-day plan: 9 October 2026

| Local time | Work | Deliverable |
|---|---|---|
| 08:00–08:30 | README contract, assignment, precedence, DIV/MOD | One page of conventions; redo the signed division example |
| 08:30–09:30 | Conditions, FOR/WHILE/DO-WHILE, bounds and steps | O001–O023; paper traces before checking |
| 09:30–09:40 | Break | Leave the screen |
| 09:40–10:40 | Arrays, strings, searching, sorting | O024–O038; W019,W020,W021,W023 |
| 10:40–11:25 | Debugging initialization, limits, update order | E001,E006,E008,E012,E016,E019,E021,E028,E039 |
| 11:25–11:40 | Break and error-log review | Three personal trap rules |
| 11:40–12:30 | Functions, recursion and bits | O039–O053; W040,W041,W045,W046 |
| 12:30–13:15 | Lunch and rest | Pause studying |
| 13:15–14:15 | Mock 1, closed keys, 60-minute timer | Scored attempt after stopping timer |
| 14:15–14:45 | Check Mock 1 | Rule behind each mistake; retry two without key |
| 14:45–15:00 | Break | Reset concentration |
| 15:00–15:45 | Digits, prime, Fibonacci, GCD and logic | W012–W018,W028; README truth/constraint tables |
| 15:45–16:45 | Mock 2, closed keys | Second timed attempt |
| 16:45–17:15 | Check Mock 2 | Compare repeated mistakes, not just score |
| 17:15–17:45 | Walk/snack | Rest |
| 17:45–18:30 | Language traps, matrices, harder boundaries | O085–O100; E031,E043,E044,E046,E050,E054 |
| 18:30–19:15 | Dinner | Rest |
| 19:15–20:15 | Mock 3 if alert; otherwise retry mistakes | Final timed attempt or focused consolidation |
| 20:15–20:45 | Grade and repair | Last error-log entries; stop adding new topics |
| 20:45–21:15 | 30-minute checklist below | One clean reference sheet |
| After 21:15 | Prepare assessment logistics, wind down | Reporting details checked from your actual invitation |

**If only four hours remain:** 40 minutes contract/loops → 40 arrays/search → 30 recursion/bits → 30 debugging → 60 Mock 1 → 30 review → 10 personal error sheet. The question banks are a reusable resource; finishing all 235 bank questions today is not required. If a mock exposes a basic gap, use the optional third-mock block for that gap.

## 30-minute rapid revision checklist

| Minute | Action | Self-check |
|---|---|---|
| 0–3 | Assignment, precedence, associativity | 2+3*4=14;20−6−3=11 |
| 3–6 | DIV/MOD and language distinction | Neutral/C/Java −7 DIV 3=−2, rem −1; Python −7//3=−3, rem 2 |
| 6–10 | Loop bounds, steps and zero iterations | 1..7 STEP2 visits 1,3,5,7; descending 5..1 STEP−2 visits 5,3,1 |
| 10–13 | BREAK/CONTINUE and nested loops | BREAK only innermost; triangle through n has n(n+1)/2 visits |
| 13–16 | Arrays, strings, search | Last index n−1; binary search sorted input and mid±1; preserve first-match semantics |
| 16–19 | Recursion and functions | Base case, progress, frame locals; print-before versus print-after |
| 19–22 | Bitwise and Boolean | 5 AND 3=1; OR=7; XOR=6; NOT8(5)=250; short-circuit may skip faults |
| 22–25 | Number patterns | digit←n MOD10; n←n DIV10; product starts1; prime excludes0,1; square-root equality |
| 25–28 | Debug boundaries and logic | Try empty/singleton,0,1,duplicates,all-negative; seek counterexamples for “must” |
| 28–30 | Personal error sheet and logistics | Name your top three traps; confirm actual reporting time and allowed tools |

## Quick pattern reference

| Pattern | Remember | Independent check |
|---|---|---|
| Increasing loop | count=floor((end−start)/step)+1 if initial test passes | list first, last and rejected value |
| Decreasing loop | count=floor((start−end)/abs(step))+1 if initial test passes | sign of step must match direction |
| Sum/product | start 0 / start 1 | empty input yields identity |
| Digit loop | extract before removing; save original | digit count equals iteration count except special zero rule |
| Fibonacci | t=a+b; a=b; b=t | after k steps a=F_k,b=F_(k+1) |
| GCD | r=a MOD b; a=b; b=r | result divides both original values |
| Prime | n≥2; try d*d≤n | squares 4,9,49 must fail |
| Binary search | lo≤hi, discard mid via ±1 | interval strictly shrinks |
| Reverse array/text | left/right meet or cross | mirrored indices total n−1 |
| Prefix sum | P0=0, P[i+1]=P[i]+A[i] | full sum=P[n] |
| XOR pairs | x XOR x=0, x XOR 0=x | requires the stated occurrence promise |
| Power of two | x>0 AND (x AND (x−1))=0 | test x=0 and x=1 |
| Two-pointer sum | sorted input; move left for small sum | pointers distinct, interval shrinks |
| Recursion | base + decreasing problem + return | draw descent and unwind separately |
| Complexity | add sequential work; count dependent nested visits | logarithmic updates multiply/divide, not add/subtract |
| Implication | P→Q ≡ NOT P OR Q | only true→false violates it; converse is not guaranteed |

## Real-language reminder

- Java/C prefix ++ gives the new value; postfix ++ gives the old value. Use a side-effect table.
- Java operands are evaluated left to right. C does not guarantee that general order; never assign an output to unsequenced multiple modifications of the same scalar.
- Python ++x is unary plus twice, not increment; x++ is syntax-invalid. Python negative indexing is valid; our pseudocode negative indexing is invalid.
- Neutral BIT_NOT8 flips eight bits. Python ~x is −x−1; Java int bitwise NOT acts on signed 32-bit ints. Read width and signedness before tracing shifts.
- Neutral SWITCH here has no fall-through; classic C/Java statement switch can fall through without BREAK.

## Exam-day strategy: 10 October

Before your actual reporting time, spend 10–15 minutes looking at your own error sheet, eat normally, and check the invitation's login/reporting requirements. Avoid a new hard-topic sprint. Do not assume the practice scoring or timings apply to Zeus.

During the assessment:

1. Read the assessment's language, pseudocode conventions and marking rules. Identify inclusive/exclusive bounds and division semantics before solving.
2. First pass: take short arithmetic, straight-line assignments, simple loops and familiar patterns. Mark long recursion/nested-loop items for return.
3. Make a tiny table for every changing variable; for array problems write indices above values. Record every PRINT separately.
4. Before choosing an option, check one competing option against the exact step where it would go wrong. Common distractors differ by the last iteration, a prefix/postfix value or a missed return.
5. For debugging, inspect initialization → condition → update → access → return. Repair the cause and test a boundary rather than patch one example.
6. For reasoning, distinguish “must” from “could.” One valid counterexample disproves “must”; one valid witness proves “could.” Data sufficiency can determine NO without determining an exact number.
7. Reserve the final 5–10% of the available time for marked items and transcription checks. Guessing strategy depends on the actual negative-marking policy.

## Mini dry-run sheet to copy

| Step / call depth | Condition | Variables before | Operation | Variables after | Output |
|---|---|---|---|---|---|
| initialization | — | — | copy given values | initial state | — |
| iteration 1 | write TRUE/FALSE | record relevant values | execute in order | update immediately | exact line |
| exit | write rejected test | retained state | body skipped | final state | — |

For a recursive call, create a new row/frame rather than overwrite the caller's pending work. For infinite-loop suspicion, show a stationary state or a variable moving away from its required stopping value.

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
