"""Generate original assessment practice and verify neutral code two ways.

Run with Python 3.10+ from any directory. No network or third-party packages.
The AST interpreter implements only the explicitly documented training subset.
"""
import ast
import copy
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = []


def fmt(v):
    if v is True: return 'TRUE'
    if v is False: return 'FALSE'
    if v is None: return 'NONE'
    if isinstance(v, (list, tuple)): return '[' + ', '.join(fmt(x) for x in v) + ']'
    return str(v)


def div(a, b):
    if b == 0: raise ZeroDivisionError('DIV by zero')
    return (abs(a) // abs(b)) * (-1 if (a < 0) != (b < 0) else 1)


def mod(a, b): return a - div(a, b) * b


def ex(n):
    if isinstance(n, ast.Constant):
        return json.dumps(n.value) if isinstance(n.value, str) else fmt(n.value)
    if isinstance(n, ast.Name): return n.id
    if isinstance(n, (ast.List, ast.Tuple)): return '[' + ', '.join(ex(x) for x in n.elts) + ']'
    if isinstance(n, ast.BinOp):
        op = {ast.Add:'+', ast.Sub:'−', ast.Mult:'*', ast.Div:'/', ast.FloorDiv:'DIV', ast.Mod:'MOD', ast.BitAnd:'BIT_AND', ast.BitOr:'BIT_OR', ast.BitXor:'BIT_XOR', ast.LShift:'SHL', ast.RShift:'SHR'}[type(n.op)]
        return f'({ex(n.left)} {op} {ex(n.right)})'
    if isinstance(n, ast.UnaryOp):
        op = {ast.Not:'NOT ', ast.USub:'−', ast.UAdd:'+'}[type(n.op)]
        return f'({op}{ex(n.operand)})'
    if isinstance(n, ast.BoolOp): return '(' + (' AND ' if isinstance(n.op, ast.And) else ' OR ').join(ex(x) for x in n.values) + ')'
    if isinstance(n, ast.Compare):
        assert len(n.ops) == 1, 'No chained neutral comparisons'
        op = {ast.Eq:'=', ast.NotEq:'≠', ast.Lt:'<', ast.LtE:'≤', ast.Gt:'>', ast.GtE:'≥', ast.In:'IS_IN', ast.NotIn:'IS_NOT_IN'}[type(n.ops[0])]
        return f'({ex(n.left)} {op} {ex(n.comparators[0])})'
    if isinstance(n, ast.IfExp): return f'({ex(n.body)} IF {ex(n.test)} ELSE {ex(n.orelse)})'
    if isinstance(n, ast.Subscript):
        if isinstance(n.slice, ast.Slice):
            lo = ex(n.slice.lower) if n.slice.lower else '0'
            hi = ex(n.slice.upper) if n.slice.upper else f'LENGTH({ex(n.value)})'
            return f'SLICE({ex(n.value)}, {lo}, {hi})'
        return f'{ex(n.value)}[{ex(n.slice)}]'
    if isinstance(n, ast.Call):
        if isinstance(n.func, ast.Attribute):
            if n.func.attr == 'append': return f'APPEND({ex(n.func.value)}, {ex(n.args[0])})'
            if n.func.attr == 'lower': return f'LOWER({ex(n.func.value)})'
            if n.func.attr == 'count': return f'COUNT({ex(n.func.value)}, {ex(n.args[0])})'
            if n.func.attr == 'join': return f'JOIN({ex(n.args[0])}, {ex(n.func.value)})'
        name = ex(n.func)
        name = {'len':'LENGTH', 'abs':'ABS', 'min':'MIN', 'max':'MAX', 'sorted':'SORTED', 'sum':'SUM', 'str':'STRING', 'list':'COPY', 'div':'DIVIDE_TRUNC', 'mod':'REMAINDER_TRUNC', 'not8':'BIT_NOT8', 'pow':'POWER'}.get(name, name)
        return name + '(' + ', '.join(ex(x) for x in n.args) + ')'
    raise ValueError(ast.dump(n))


def pseudo(code):
    tree = ast.parse(code)
    def block(nodes, depth=0):
        lines = []
        pad = '    ' * depth
        for n in nodes:
            if isinstance(n, ast.Assign): lines.append(pad + ex(n.targets[0]) + ' ← ' + ex(n.value))
            elif isinstance(n, ast.Expr):
                if isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name) and n.value.func.id == 'print':
                    lines.append(pad + 'PRINT ' + ', '.join(ex(x) for x in n.value.args))
                else: lines.append(pad + ex(n.value))
            elif isinstance(n, ast.If):
                lines.append(pad + 'IF ' + ex(n.test) + ' THEN')
                lines += block(n.body, depth+1)
                if n.orelse:
                    lines.append(pad + 'ELSE')
                    lines += block(n.orelse, depth+1)
                lines.append(pad + 'END IF')
            elif isinstance(n, ast.While):
                lines.append(pad + 'WHILE ' + ex(n.test))
                lines += block(n.body, depth+1)
                lines.append(pad + 'END WHILE')
            elif isinstance(n, ast.For):
                args = n.iter.args
                if len(args) == 1: start, stop, step = '0', args[0], '1'
                else: start, stop, step = ex(args[0]), args[1], ex(args[2]) if len(args)>2 else '1'
                step_value = ast.literal_eval(args[2]) if len(args)>2 else 1
                end = f'({ex(stop)} {"+ 1" if step_value < 0 else "− 1"})'
                lines.append(pad + f'FOR {ex(n.target)} ← {start} TO {end} STEP {step}')
                lines += block(n.body, depth+1)
                lines.append(pad + 'END FOR')
            elif isinstance(n, ast.FunctionDef):
                lines.append(pad + f'FUNCTION {n.name}(' + ', '.join(a.arg for a in n.args.args) + ')')
                lines += block(n.body, depth+1)
                lines.append(pad + 'END FUNCTION')
            elif isinstance(n, ast.Return): lines.append(pad + 'RETURN ' + ex(n.value))
            elif isinstance(n, ast.Break): lines.append(pad + 'BREAK')
            elif isinstance(n, ast.Continue): lines.append(pad + 'CONTINUE')
            elif isinstance(n, ast.Pass): lines.append(pad + '// no action')
            else: raise ValueError(ast.dump(n))
        return lines
    return '\n'.join(block(tree.body))


class Signal(Exception):
    def __init__(self, kind, value=None): self.kind, self.value = kind, value


class Machine:
    """Independent small AST interpreter, with all executed conditions and changes."""
    def __init__(self):
        self.rows, self.output, self.functions, self.depth = [], [], {}, 0
    def record(self, scope, action, env, emitted=''):
        if len(self.rows)>12000: raise RuntimeError('execution guard')
        state = '; '.join(f'{k}={fmt(v)}' for k,v in env.items()) or '—'
        self.rows.append([str(len(self.rows)+1), scope, action, state, emitted or '—'])
    def value(self, n, env):
        if isinstance(n, ast.Constant): return n.value
        if isinstance(n, ast.Name): return env[n.id]
        if isinstance(n, (ast.List, ast.Tuple)): return [self.value(x,env) for x in n.elts]
        if isinstance(n, ast.BinOp):
            a,b = self.value(n.left,env), self.value(n.right,env)
            ops = {ast.Add:lambda:a+b, ast.Sub:lambda:a-b, ast.Mult:lambda:a*b, ast.Div:lambda:a/b, ast.FloorDiv:lambda:div(a,b), ast.Mod:lambda:mod(a,b), ast.BitAnd:lambda:a&b, ast.BitOr:lambda:a|b, ast.BitXor:lambda:a^b, ast.LShift:lambda:a<<b, ast.RShift:lambda:a>>b}
            return ops[type(n.op)]()
        if isinstance(n, ast.UnaryOp):
            v = self.value(n.operand,env)
            return {ast.Not:lambda:not v, ast.USub:lambda:-v, ast.UAdd:lambda:+v}[type(n.op)]()
        if isinstance(n, ast.BoolOp):
            for child in n.values:
                v = self.value(child,env)
                if isinstance(n.op,ast.And) and not v: return False
                if isinstance(n.op,ast.Or) and v: return True
            return bool(v)
        if isinstance(n, ast.Compare):
            a,b = self.value(n.left,env), self.value(n.comparators[0],env)
            return {ast.Eq:lambda:a==b, ast.NotEq:lambda:a!=b, ast.Lt:lambda:a<b, ast.LtE:lambda:a<=b, ast.Gt:lambda:a>b, ast.GtE:lambda:a>=b, ast.In:lambda:a in b, ast.NotIn:lambda:a not in b}[type(n.ops[0])]()
        if isinstance(n, ast.IfExp): return self.value(n.body if self.value(n.test,env) else n.orelse,env)
        if isinstance(n, ast.Subscript):
            v = self.value(n.value,env)
            if isinstance(n.slice, ast.Slice):
                lo = self.value(n.slice.lower,env) if n.slice.lower else 0
                hi = self.value(n.slice.upper,env) if n.slice.upper else len(v)
                return v[lo:hi]
            i = self.value(n.slice,env)
            if i < 0 or i >= len(v): raise IndexError('neutral index out of bounds')
            return v[i]
        if isinstance(n, ast.Call):
            if isinstance(n.func, ast.Attribute):
                v = self.value(n.func.value,env)
                args = [self.value(x,env) for x in n.args]
                if n.func.attr == 'append': v.append(args[0]); return None
                if n.func.attr == 'lower': return v.lower()
                if n.func.attr == 'count': return v.count(args[0])
                if n.func.attr == 'join': return v.join(args[0])
            name = n.func.id
            args = [self.value(x,env) for x in n.args]
            if name == 'print':
                text = ' '.join(fmt(v) for v in args)
                self.output.append(text)
                return None
            builtins = {'len':len, 'abs':abs, 'min':min, 'max':max, 'sorted':sorted, 'sum':sum, 'str':str, 'list':list, 'div':div, 'mod':mod, 'not8':lambda x:255^x, 'pow':pow}
            if name in builtins: return builtins[name](*args)
            f = self.functions[name]
            local = dict(zip((a.arg for a in f.args.args),args))
            self.depth += 1
            scope = f'{name} depth {self.depth}'
            self.record(scope,'ENTER',local)
            try:
                self.block(f.body,local,scope)
                result = None
            except Signal as s:
                if s.kind!='return': raise
                result = s.value
            self.depth -= 1
            return result
        raise ValueError(ast.dump(n))
    def block(self, nodes, env, scope='main'):
        for n in nodes:
            if isinstance(n,ast.FunctionDef): self.functions[n.name]=n; continue
            if isinstance(n,ast.Assign):
                v = self.value(n.value,env)
                t = n.targets[0]
                if isinstance(t,ast.Name): env[t.id]=v
                else:
                    arr = self.value(t.value,env); i = self.value(t.slice,env)
                    if i<0 or i>=len(arr): raise IndexError('neutral index out of bounds')
                    arr[i]=v
                self.record(scope,ex(t)+' ← '+ex(n.value),env)
            elif isinstance(n,ast.Expr):
                before = len(self.output)
                self.value(n.value,env)
                self.record(scope, 'PRINT' if isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Name) and n.value.func.id=='print' else ex(n.value),env, '\\n'.join(self.output[before:]))
            elif isinstance(n,ast.If):
                ok = self.value(n.test,env)
                self.record(scope,'IF '+ex(n.test)+' → '+fmt(ok),env)
                self.block(n.body if ok else n.orelse,env,scope)
            elif isinstance(n,ast.While):
                while True:
                    ok = self.value(n.test,env)
                    self.record(scope,'WHILE '+ex(n.test)+' → '+fmt(ok),env)
                    if not ok: break
                    try: self.block(n.body,env,scope)
                    except Signal as s:
                        if s.kind=='break': break
                        if s.kind=='continue': continue
                        raise
            elif isinstance(n,ast.For):
                args = [self.value(x,env) for x in n.iter.args]
                for v in range(*args):
                    env[n.target.id]=v
                    self.record(scope,'FOR visit '+n.target.id,env)
                    try: self.block(n.body,env,scope)
                    except Signal as s:
                        if s.kind=='break': break
                        if s.kind=='continue': continue
                        raise
                self.record(scope,'FOR exit',env)
            elif isinstance(n,ast.Return):
                v=self.value(n.value,env)
                self.record(scope,'RETURN '+fmt(v),env)
                raise Signal('return',v)
            elif isinstance(n,(ast.Break,ast.Continue)):
                k='break' if isinstance(n,ast.Break) else 'continue'
                self.record(scope,k.upper(),env); raise Signal(k)
            elif isinstance(n,ast.Pass): self.record(scope,'no action',env)
            else: raise ValueError(ast.dump(n))
    def run(self,code): self.block(ast.parse(code).body,{}); return '\n'.join(self.output)


def execute(code):
    machine=Machine()
    out=machine.run(code)
    independent=[]
    ns={'print':lambda *a:independent.append(' '.join(fmt(v) for v in a)), 'div':div,'mod':mod,'not8':lambda x:255^x}
    exec(compile(code,'reference','exec'),ns)
    assert out=='\n'.join(independent), (code,out,independent)
    return out,machine.rows


def table(rows, headers=None):
    headers=headers or ['Step','Frame','Executed operation / decision','Variables after step','Printed line']
    esc=lambda v:str(v).replace('|','\\|').replace('\n','<br>')
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+'\n'.join('| '+' | '.join(esc(v) for v in row)+' |' for row in rows)


def fenced(code,lang='text'): return f'```{lang}\n{code}\n```'
def write(name,text): (ROOT/name).write_text(text.rstrip()+'\n',encoding='utf-8')


W=[]
def w(title,task,code,expected,why,complexity,edges):
    W.append(dict(title=title,task=task,code=code,expected=expected,why=why,complexity=complexity,edges=edges))

# W001–W020: foundations. Every input contract and sample is explicit.
w('Swap two values','Write pseudocode to swap two integers using a temporary variable. Demonstrate a=4,b=9.',
  'a=4\nb=9\ntemp=a\na=b\nb=temp\nprint(a,b)','9 4','Preserve a before overwriting it; both original values survive.','O(1) time, O(1) space','Equal values (5,5) remain (5,5); negatives work unchanged.')
w('Rotate three values','Rotate (a,b,c) to (c,a,b). Demonstrate (1,2,3).',
  'a=1\nb=2\nc=3\ntemp=c\nc=b\nb=a\na=temp\nprint(a,b,c)','3 1 2','Saving c allows rightward movement without losing the old values.','O(1) time and space','(0,0,0) stays unchanged.')
w('Quotient and remainder','For integer a and nonzero integer b, print truncation-toward-zero quotient and remainder. Demonstrate a=-17,b=5.',
  'a=-17\nb=5\nq=div(a,b)\nr=a-q*b\nprint(q,r)','-3 -2','q truncates toward zero; reconstructing r enforces a=q*b+r. DIVIDE_TRUNC is the contract DIV helper.','O(1) time and space','a=0,b=5 gives 0 0; a=17,b=-5 gives -3 2; reject b=0.')
w('Even or odd','Classify any integer n as even or odd. Demonstrate n=-7.',
  'n=-7\nif mod(n,2)==0:\n    print("even")\nelse:\n    print("odd")','odd','Only zero remainder matters, so signed remainder policy does not change parity.','O(1) time and space','0 is even; -8 is even.')
w('Largest of three','Find the largest of three integers including ties. Demonstrate (7,7,2).',
  'a=7\nb=7\nc=2\nbest=a\nif b>best:\n    best=b\nif c>best:\n    best=c\nprint(best)','7','Start from a real input value rather than zero; independent comparisons preserve ties.','O(1) time and space','(-9,-2,-5) gives -2; all equal returns that value.')
w('Grade bands','Given a valid integer mark 0..100, print A for >=80, B for >=60, C for >=40, F otherwise. Demonstrate 60.',
  'mark=60\nif mark>=80:\n    print("A")\nelse:\n    if mark>=60:\n        print("B")\n    else:\n        if mark>=40:\n            print("C")\n        else:\n            print("F")','B','Descending thresholds mean the first matching band is correct.','O(1) time and space','39→F,40→C,79→B,80→A; outside 0..100 is invalid input.')
w('Leap year','Implement Gregorian leap-year rules for a positive integer year: divisible by 400, or by 4 but not 100. Demonstrate 1900.',
  'year=1900\nleap=(year%400==0) or ((year%4==0) and (year%100!=0))\nprint(leap)','FALSE','The century exception is overridden only by divisibility by 400.','O(1) time and space','2000 TRUE,2024 TRUE,2023 FALSE.')
w('Sum from one to n','Using a loop, sum 1 through nonnegative n. Demonstrate n=5.',
  'n=5\ns=0\nfor i in range(1,n+1):\n    s=s+i\nprint(s)','15','The inclusive upper bound includes n. An empty loop handles zero.','O(n) time, O(1) space','n=0→0; n=1→1.')
w('Odd-number sum','Sum the positive odd numbers at most nonnegative n with a step of two. Demonstrate n=8.',
  'n=8\ns=0\nfor i in range(1,n+1,2):\n    s=s+i\nprint(s)','16','Visits are 1,3,5,7; n need not itself be visited.','O(n) time, O(1) space','n=0→0; n=1→1; n=9→25.')
w('Countdown','Print integers from nonnegative n down to zero, one per line. Demonstrate n=3.',
  'n=3\nfor i in range(n,-1,-1):\n    print(i)','3\n2\n1\n0','Negative step must pair with a decreasing bound. Zero is included.','O(n) time, O(1) auxiliary space','n=0 prints a single 0.')
w('Multiplication table','Print k*n for k=1..5, one per line. Demonstrate n=3.',
  'n=3\nfor k in range(1,6):\n    print(k*n)','3\n6\n9\n12\n15','k controls the row while n remains constant.','O(1) time and space for five rows; O(m) if m rows','n=0 prints five zeros; negative n is allowed.')
w('Count decimal digits','Count digits of a nonnegative integer, treating zero as one digit. Demonstrate n=1002.',
  'n=1002\ncount=1\nwhile n>=10:\n    count=count+1\n    n=n//10\nprint(count)','4','Starting at one counts the final single-digit value including zero.','O(d) time, O(1) space, d=digits','0→1;9→1;10→2.')
w('Digit sum','Find sum of decimal digits of nonnegative n. Demonstrate n=405.',
  'n=405\ns=0\nwhile n>0:\n    s=s+n%10\n    n=n//10\nprint(s)','9','MOD extracts before DIV removes the last digit.','O(d) time, O(1) space','0→0;999→27.')
w('Reverse an integer','Reverse decimal digits numerically for nonnegative n. Demonstrate n=120.',
  'n=120\nr=0\nwhile n>0:\n    r=r*10+n%10\n    n=n//10\nprint(r)','21','Multiply accumulated reversal by ten before adding the next digit. Leading zeros are not stored in an integer.','O(d) time, O(1) space','0→0;1000→1.')
w('Numeric palindrome','Determine whether nonnegative n reads the same forwards and backwards. Demonstrate n=1221.',
  'n=1221\noriginal=n\nr=0\nwhile n>0:\n    r=r*10+n%10\n    n=n//10\nprint(r==original)','TRUE','Compare reversal with saved original, not consumed n.','O(d) time, O(1) space','0 TRUE,10 FALSE,7 TRUE.')
w('Iterative factorial','Compute n! for integer n>=0 without recursion. Demonstrate n=5.',
  'n=5\np=1\nfor i in range(1,n+1):\n    p=p*i\nprint(p)','120','The multiplicative identity is 1. The empty product gives 0!=1.','O(n) time, O(1) space in the unit-cost model','n=0→1; n=1→1; reject negatives.')
w('Fibonacci term','Compute F_n for n>=0, F0=0,F1=1, using constant auxiliary space. Demonstrate n=7.',
  'n=7\na=0\nb=1\nfor i in range(n):\n    nxt=a+b\n    a=b\n    b=nxt\nprint(a)','13','After k updates, a=F_k and b=F_(k+1). The temporary preserves both old terms.','O(n) time, O(1) space','F0=0,F1=1,F2=1.')
w('Euclidean GCD','Compute GCD of two nonnegative integers, defining GCD(0,0)=0. Demonstrate (48,18).',
  'a=48\nb=18\nwhile b!=0:\n    r=a%b\n    a=b\n    b=r\nprint(a)','6','Common divisors are unchanged by subtracting multiples; remainders strictly shrink until zero.','O(log(max(a,b)+1)) time, O(1) space','(0,15)→15;(0,0)→0;(7,3)→1.')
w('Array sum','Sum a possibly empty integer array. Demonstrate [3,-2,7].',
  'A=[3,-2,7]\ns=0\nfor i in range(len(A)):\n    s=s+A[i]\nprint(s)','8','All valid indices are visited once, accumulating rather than replacing s.','O(n) time, O(1) space','[]→0;[-5]→-5.')
w('Linear search','Return the first index of target or -1 if absent in any integer array. Demonstrate A=[4,9,4],target=4.',
  'A=[4,9,4]\ntarget=4\nfound=-1\nfor i in range(len(A)):\n    if A[i]==target:\n        found=i\n        break\nprint(found)','0','BREAK preserves the first match; the initialized sentinel handles absence.','O(n) time, O(1) space','[]→-1;target 8→-1; duplicates must return first index.')
# W021–W040: intermediate algorithms and invariants.
w('Maximum array value','Return the largest value of a nonempty integer array. Demonstrate [-8,-2,-5].',
  'A=[-8,-2,-5]\nbest=A[0]\nfor i in range(1,len(A)):\n    if A[i]>best:\n        best=A[i]\nprint(best)','-2','Initialize from the array so negative-only data cannot invent a zero.','O(n) time, O(1) space','[-7]→-7; empty array must be rejected.')
w('Second distinct largest','Find the second distinct largest value, or print NONE if fewer than two distinct values exist. Use sorting for clarity; demonstrate [5,5,2,8,8].',
  'A=[5,5,2,8,8]\nB=sorted(A)\nanswer="NONE"\nif len(B)>=2:\n    largest=B[len(B)-1]\n    i=len(B)-2\n    while i>=0:\n        if B[i]!=largest:\n            answer=B[i]\n            break\n        i=i-1\nprint(answer)','5','Skipping all copies of the largest enforces distinctness.','O(n log n) time, O(n) space for sorted copy','[] and [4,4]→NONE;[-3,-1]→-3.')
w('Reverse array in place','Reverse any array using two indices and O(1) extra space. Demonstrate [1,2,3,4,5].',
  'A=[1,2,3,4,5]\nl=0\nr=len(A)-1\nwhile l<r:\n    temp=A[l]\n    A[l]=A[r]\n    A[r]=temp\n    l=l+1\n    r=r-1\nprint(A)','[5, 4, 3, 2, 1]','Symmetric swaps move each end to its final position; the center is untouched.','O(n) time, O(1) space','[]→[];[7]→[7]; reverse twice restores original.')
w('Count occurrences','Count exact occurrences of target in a possibly empty array. Demonstrate [2,3,2,2],target=2.',
  'A=[2,3,2,2]\ntarget=2\ncount=0\nfor i in range(len(A)):\n    if A[i]==target:\n        count=count+1\nprint(count)','3','Every matching position contributes one, including duplicates.','O(n) time, O(1) space','[]→0; absent target→0.')
w('Vowel count','Count ASCII vowels in a string ignoring case. Demonstrate "Zeus AI". LOWER returns a lowercase copy; IS_IN tests membership.',
  's="Zeus AI"\ns=s.lower()\ncount=0\nfor i in range(len(s)):\n    if s[i] in "aeiou":\n        count=count+1\nprint(count)','4','Normalize case before membership testing. Spaces are not vowels.','O(n) time, O(n) space for lowercase copy','empty→0;"rhythm"→0;"AEIOU"→5.')
w('String reversal','Build reversed ASCII text without a reverse builtin. Demonstrate "code".',
  's="code"\nr=""\nfor i in range(len(s)-1,-1,-1):\n    r=r+s[i]\nprint(r)','edoc','Descending valid indices give reversed order.','O(n²) copying time for immutable concatenation; O(n) stored result','empty→blank line;"a"→a. An array builder can reduce copying time to O(n).')
w('String palindrome','Check exact, case-sensitive palindrome with two pointers. Demonstrate "abca".',
  's="abca"\nl=0\nr=len(s)-1\nok=True\nwhile l<r:\n    if s[l]!=s[r]:\n        ok=False\n        break\n    l=l+1\n    r=r-1\nprint(ok)','FALSE','One mismatched mirrored pair disproves palindrome; no further comparisons are needed.','O(n) time, O(1) space','empty and one character TRUE;"Aa" FALSE.')
w('Trial-division prime','Test primality for integer n>=0 using divisors up to sqrt(n). Demonstrate n=29.',
  'n=29\nprime=n>=2\nd=2\nwhile prime and d*d<=n:\n    if n%d==0:\n        prime=False\n    d=d+1\nprint(prime)','TRUE','The loop excludes composites with a small factor; no such factor means prime.','O(sqrt(n)) time, O(1) space','0,1 FALSE;2 TRUE;49 FALSE.')
w('Prime count in a range','Count primes in inclusive [2,n], n>=0. Demonstrate n=10.',
  'n=10\ncount=0\nfor x in range(2,n+1):\n    prime=True\n    d=2\n    while prime and d*d<=x:\n        if x%d==0:\n            prime=False\n        d=d+1\n    if prime:\n        count=count+1\nprint(count)','4','Each candidate gets fresh prime status; primes here are 2,3,5,7.','O(n sqrt(n)) upper-bound time, O(1) space','n=0 or1→0;n=2→1.')
w('Armstrong test','For nonnegative n, test whether n equals the sum of each digit raised to the number of digits. Demonstrate 153; POWER is integer exponentiation.',
  'n=153\noriginal=n\ndigits=1\nt=n\nwhile t>=10:\n    digits=digits+1\n    t=t//10\ns=0\nwhile n>0:\n    digit=n%10\n    s=s+pow(digit,digits)\n    n=n//10\nprint(s==original)','TRUE','153=1³+5³+3³. Preserve input and determine the actual digit count.','O(d) power operations and O(1) space; power cost depends on implementation','0 TRUE;10 FALSE;9474 TRUE.')
w('Least common multiple','Compute LCM of nonnegative a,b using GCD, with LCM=0 if either input is 0. Demonstrate (12,18).',
  'a=12\nb=18\nx=a\ny=b\nwhile y!=0:\n    r=x%y\n    x=y\n    y=r\nif a==0 or b==0:\n    answer=0\nelse:\n    answer=(a//x)*b\nprint(answer)','36','Divide by gcd before multiplying; test zero before dividing by gcd.','O(log(max(a,b)+1)) time, O(1) space','(0,0)→0;(0,5)→0;(7,3)→21.')
w('Count triangular visits','Count pairs (i,j) with 1<=j<=i<=n using nested loops. Demonstrate n=4.',
  'n=4\ncount=0\nfor i in range(1,n+1):\n    for j in range(1,i+1):\n        count=count+1\nprint(count)','10','Row i contributes i; verify with n(n+1)/2.','O(n²) time, O(1) space','n=0→0;n=1→1.')
w('Rows of stars','Print a left-aligned triangle of n rows, row i containing i stars. Demonstrate n=3.',
  'n=3\nfor i in range(1,n+1):\n    row=""\n    for j in range(i):\n        row=row+"*"\n    print(row)','*\n**\n***','Reset row for every outer iteration; the inner loop controls its length.','O(n²) characters output; immutable concatenation can cost O(n³) total copying; O(n) row space','n=0 prints no lines; n=1 prints *.')
w('Matrix sum','Sum a rectangular integer matrix with at least one row; rows may have zero columns. Demonstrate [[1,2,3],[4,5,6]].',
  'M=[[1,2,3],[4,5,6]]\ns=0\nfor r in range(len(M)):\n    for c in range(len(M[r])):\n        s=s+M[r][c]\nprint(s)','21','Use each row length for columns; every cell contributes once.','O(rows*cols) time, O(1) space','[[]]→0;[[7]]→7.')
w('Main diagonal sum','Sum the main diagonal of a square matrix. Demonstrate [[1,2],[3,4]].',
  'M=[[1,2],[3,4]]\ns=0\nfor i in range(len(M)):\n    s=s+M[i][i]\nprint(s)','5','Main diagonal coordinates have equal row and column indices.','O(n) time, O(1) space','[]→0;[[9]]→9; reject nonsquare input.')
w('Transpose a rectangle','Build a new transpose of a rectangular matrix with >=1 row and >=1 column. Demonstrate [[1,2,3],[4,5,6]].',
  'M=[[1,2,3],[4,5,6]]\nT=[]\nfor c in range(len(M[0])):\n    row=[]\n    for r in range(len(M)):\n        row.append(M[r][c])\n    T.append(row)\nprint(T)','[[1, 4], [2, 5], [3, 6]]','One output row is one original column; allocate each output row separately.','O(rc) time, O(rc) output space','[[7]]→[[7]]; [[1,2]]→[[1],[2]].')
w('Bubble sort','Sort an integer array ascending in place using adjacent swaps. Demonstrate [3,1,2].',
  'A=[3,1,2]\nfor end in range(len(A)-1,0,-1):\n    for j in range(end):\n        if A[j]>A[j+1]:\n            temp=A[j]\n            A[j]=A[j+1]\n            A[j+1]=temp\nprint(A)','[1, 2, 3]','Each pass settles the greatest remaining element at end; j+1 is always valid.','O(n²) time, O(1) space','[]→[];[2,2,1]→[1,2,2].')
w('Selection sort','Sort ascending in place by selecting the smallest remaining value. Demonstrate [4,2,3,1].',
  'A=[4,2,3,1]\nfor i in range(len(A)-1):\n    best=i\n    for j in range(i+1,len(A)):\n        if A[j]<A[best]:\n            best=j\n    temp=A[i]\n    A[i]=A[best]\n    A[best]=temp\nprint(A)','[1, 2, 3, 4]','The sorted prefix grows by one minimum per pass; reset best to i each pass.','O(n²) time, O(1) space','empty and singleton skip loops; duplicates remain present.')
w('Binary search','Search an ascending integer array for target; return any matching index or -1. Demonstrate [2,5,8,11],target=11.',
  'A=[2,5,8,11]\ntarget=11\nlo=0\nhi=len(A)-1\nfound=-1\nwhile lo<=hi:\n    mid=lo+(hi-lo)//2\n    if A[mid]==target:\n        found=mid\n        break\n    if A[mid]<target:\n        lo=mid+1\n    else:\n        hi=mid-1\nprint(found)','3','Every comparison discards mid and one impossible half. Empty intervals terminate.','O(log(n+1)) time, O(1) space','[]→-1; missing 6→-1; duplicates may return any matching index.')
w('Recursive factorial','Write a recursive factorial for n>=0 with a correct base case. Demonstrate n=4.',
  'def fact(n):\n    if n<=1:\n        return 1\n    return n*fact(n-1)\nprint(fact(4))','24','Calls shrink to base 1, then pending multiplications execute on return.','O(n) time and O(n) stack','fact(0)=1;fact(1)=1; reject negatives at the input boundary.')
# W041–W060: harder combinations, recursion and bit patterns.
w('Recursive digit sum','Compute digit sum recursively for nonnegative n. Demonstrate 204.',
  'def digits(n):\n    if n==0:\n        return 0\n    return n%10+digits(n//10)\nprint(digits(204))','6','The final digit plus digit sum of remaining prefix reconstructs the answer.','O(d) time and stack','0→0;10→1.')
w('Recursive GCD','Write recursive Euclid for nonnegative a,b. Demonstrate (81,27).',
  'def gcd(a,b):\n    if b==0:\n        return a\n    return gcd(b,a%b)\nprint(gcd(81,27))','27','The second parameter strictly decreases until zero.','O(log(max(a,b)+1)) time and stack','(0,0)→0;(15,0)→15.')
w('Recursive palindrome','Check an ASCII string using recursive inward-moving indices. Demonstrate "radar".',
  'def pal(s,l,r):\n    if l>=r:\n        return True\n    if s[l]!=s[r]:\n        return False\n    return pal(s,l+1,r-1)\ns="radar"\nprint(pal(s,0,len(s)-1))','TRUE','Base handles empty/center; mismatches return immediately; otherwise reduce interval.','O(n) time and stack','empty TRUE;"ab" FALSE.')
w('Fast exponentiation','Compute base^exp for integer base and exp>=0 using repeated squaring. Define 0^0=1 in this exercise. Demonstrate 3^5.',
  'base=3\nexp=5\nresult=1\nwhile exp>0:\n    if exp%2==1:\n        result=result*base\n    base=base*base\n    exp=exp//2\nprint(result)','243','Consume exponent bits: an odd bit contributes the current power; squaring prepares the next bit.','O(log(exp+1)) multiplications, O(1) space','exp=0→1;base=0,exp>0→0;negative base works.')
w('Set-bit count','Count 1 bits of a nonnegative integer using x AND (x-1). Demonstrate x=13.',
  'x=13\ncount=0\nwhile x>0:\n    x=x&(x-1)\n    count=count+1\nprint(count)','3','Each iteration clears precisely the lowest set bit.','O(k) time for k set bits, O(1) space','0→0;8→1;255→8.')
w('Power of two','Test whether nonnegative x is a positive power of two using a bitwise condition. Demonstrate x=16.',
  'x=16\nanswer=(x>0) and ((x&(x-1))==0)\nprint(answer)','TRUE','Only positive values with exactly one set bit pass both tests.','O(1) time and space in the unit-cost model','0 FALSE;1 TRUE;12 FALSE.')
w('Unique unpaired element','Every integer in the array occurs twice except one that occurs once. Find the unique value using XOR. Inputs are nonnegative; demonstrate [4,1,4,7,1].',
  'A=[4,1,4,7,1]\nanswer=0\nfor i in range(len(A)):\n    answer=answer^A[i]\nprint(answer)','7','Equal values cancel under XOR; order does not matter. The multiplicity promise is essential.','O(n) time, O(1) space','[0]→0;[2,2,5]→5; do not use without the promise.')
w('Toggle a selected bit','Toggle bit k (zero=least significant) of nonnegative x using XOR; k>=0. Demonstrate x=10,k=1.',
  'x=10\nk=1\nmask=1<<k\nanswer=x^mask\nprint(answer)','8','XOR with a one-bit mask flips just that bit. 1010 XOR 0010=1000.','O(1) time and space in the unit-cost model','x=0,k=3→8; toggling twice restores x.')
w('Prefix sums','Build prefix array P of length n+1 with P[0]=0 and P[i+1]=sum A[0..i]. Demonstrate [2,-1,4].',
  'A=[2,-1,4]\nP=[0]\nfor i in range(len(A)):\n    P.append(P[i]+A[i])\nprint(P)','[0, 2, 1, 5]','P[i] already sums the first i elements; adding A[i] extends by one.','O(n) time, O(n) output space','[]→[0]; range sum A[l..r]=P[r+1]-P[l].')
w('Fixed-window maximum sum','For array A and valid 1<=k<=LENGTH(A), find maximum sum of any contiguous k-element window. Demonstrate [2,-1,3,4],k=2.',
  'A=[2,-1,3,4]\nk=2\nwindow=0\nfor i in range(k):\n    window=window+A[i]\nbest=window\nfor i in range(k,len(A)):\n    window=window-A[i-k]+A[i]\n    if window>best:\n        best=window\nprint(best)','7','Slide by removing exactly the leaving element and adding the entering one; initialize best from a real window.','O(n) time, O(1) space','k=n→total sum;[-5,-2],k=1→-2; reject k=0 or k>n.')
w('Remove sorted duplicates','Return a new array containing one copy of each value of sorted input. Demonstrate [1,1,2,2,3].',
  'A=[1,1,2,2,3]\nB=[]\nfor i in range(len(A)):\n    if i==0 or A[i]!=A[i-1]:\n        B.append(A[i])\nprint(B)','[1, 2, 3]','Duplicates are adjacent in sorted input; short-circuit protects i-1 when i=0.','O(n) time, O(n) output space','[]→[];[4,4]→[4]; unsorted input needs another method.')
w('Merge sorted arrays','Merge two ascending arrays into one ascending array, retaining duplicates. Demonstrate [1,4] and [2,3,4].',
  'A=[1,4]\nB=[2,3,4]\ni=0\nj=0\nC=[]\nwhile i<len(A) and j<len(B):\n    if A[i]<=B[j]:\n        C.append(A[i])\n        i=i+1\n    else:\n        C.append(B[j])\n        j=j+1\nwhile i<len(A):\n    C.append(A[i])\n    i=i+1\nwhile j<len(B):\n    C.append(B[j])\n    j=j+1\nprint(C)','[1, 2, 3, 4, 4]','Choose the smaller front, then copy the unexhausted tail. Every element is consumed once.','O(n+m) time, O(n+m) output space','One input empty copies the other; both empty→[].')
w('Pair sum in sorted array','Given ascending array and target, determine if two distinct positions sum to target using two pointers. Demonstrate [1,2,4,7],target=9.',
  'A=[1,2,4,7]\ntarget=9\nl=0\nr=len(A)-1\nfound=False\nwhile l<r:\n    s=A[l]+A[r]\n    if s==target:\n        found=True\n        break\n    if s<target:\n        l=l+1\n    else:\n        r=r-1\nprint(found)','TRUE','Too-small sum requires a larger left value; too-large requires a smaller right value. l<r prevents reuse.','O(n) time, O(1) space','[] or singleton→FALSE;[4,4],target8→TRUE.')
w('Insertion sort','Sort ascending in place with a shifting insertion sort. Demonstrate [3,1,2].',
  'A=[3,1,2]\nfor i in range(1,len(A)):\n    key=A[i]\n    j=i-1\n    while j>=0 and A[j]>key:\n        A[j+1]=A[j]\n        j=j-1\n    A[j+1]=key\nprint(A)','[1, 2, 3]','Preserve key, shift larger values right, and insert into the gap. The guard avoids negative indexing.','O(n²) worst time, O(1) space','[] unchanged; sorted input O(n); duplicates preserved.')
w('Balanced parentheses','For text containing only ( and ), determine if parentheses are balanced using a counter. Demonstrate "(()())".',
  's="(()())"\nbalance=0\nok=True\nfor i in range(len(s)):\n    if s[i]=="(":\n        balance=balance+1\n    else:\n        balance=balance-1\n    if balance<0:\n        ok=False\n        break\nprint(ok and balance==0)','TRUE','Every prefix must have nonnegative balance and the complete text must return to zero.','O(n) time, O(1) space','empty TRUE;")(" FALSE despite final balance zero;"(()" FALSE.')
w('Maximum subarray sum','For nonempty integer array, find maximum sum of a nonempty contiguous subarray. Demonstrate [-2,3,-1,4,-5].',
  'A=[-2,3,-1,4,-5]\nending=A[0]\nbest=A[0]\nfor i in range(1,len(A)):\n    ending=max(A[i],ending+A[i])\n    best=max(best,ending)\nprint(best)','6','At each position either start fresh or extend the best ending at the previous position. All-negative data stays valid.','O(n) time, O(1) space','[-7,-2]→-2;[5]→5; reject empty input.')
w('Recursive Fibonacci calls','Return F_n recursively for n>=0; then explain why this version is slower than iteration. Demonstrate n=5.',
  'def fib(n):\n    if n<=1:\n        return n\n    return fib(n-1)+fib(n-2)\nprint(fib(5))','5','The recurrence recomputes many overlapping subproblems; trace both branches, not just one descent.','O(2^n) time upper bound (tight Θ(phi^n)), O(n) maximum stack','fib(0)=0;fib(1)=1; iterative version is O(n) time.')
w('Unique diagonal sum','For a square matrix sum both diagonals counting any shared center once. Demonstrate [[1,2,3],[4,5,6],[7,8,9]].',
  'M=[[1,2,3],[4,5,6],[7,8,9]]\nn=len(M)\ns=0\nfor i in range(n):\n    s=s+M[i][i]\n    if i!=n-1-i:\n        s=s+M[i][n-1-i]\nprint(s)','25','Both coordinates coincide only at the odd-sized center; skip its second addition.','O(n) time, O(1) space','[]→0;[[7]]→7; even-sized matrices have no overlap.')
w('First occurrence by binary search','Return the leftmost index of target in a sorted array, or -1. Demonstrate [1,2,2,2,4],target=2.',
  'A=[1,2,2,2,4]\ntarget=2\nlo=0\nhi=len(A)-1\nanswer=-1\nwhile lo<=hi:\n    mid=lo+(hi-lo)//2\n    if A[mid]>=target:\n        if A[mid]==target:\n            answer=mid\n        hi=mid-1\n    else:\n        lo=mid+1\nprint(answer)','1','Save a match and keep searching left; every discarded right portion cannot contain an earlier match.','O(log(n+1)) time, O(1) space','[]→-1;[2,2]→0;missing target→-1.')
w('Recursive subset-sum decision','Given nonnegative array A and nonnegative target, decide if some subset sums to target. Empty subset allowed. Demonstrate [3,5,7],target=10.',
  'def possible(A,i,target):\n    if target==0:\n        return True\n    if i==len(A):\n        return False\n    if A[i]<=target and possible(A,i+1,target-A[i]):\n        return True\n    return possible(A,i+1,target)\nA=[3,5,7]\nprint(possible(A,0,10))','TRUE','Each element is included or excluded; i always advances. Successful include branch short-circuits unnecessary work.','O(2^n) worst time, O(n) stack; no sliced copies','[] target0 TRUE;[] target1 FALSE;[4,6] target5 FALSE.')


def build_writing():
    assert len(W)==60
    q=['# Pseudocode-writing questions','Solve on paper first. IDs W001–W020 are easy, W021–W040 medium, W041–W060 hard. Use the README contract. For each: specify the input domain, write an algorithm, dry-run the supplied sample, state time/space complexity and test one boundary. These are original exercises.']
    a=['# Pseudocode-writing answers','Each solution includes complete pseudocode and a statement-by-statement variable trace. Tables show the state after each listed operation; IF/WHILE rows show the evaluated decision. Function frames have separate local state.']
    for i,item in enumerate(W,1):
        ident=f'W{i:03}'
        item['id']=ident
        out,rows=execute(item['code'])
        assert out==item['expected'],(ident,out,item['expected'])
        q += [f'## {ident} — {item["title"]}',item['task']]
        a += [f'## {ident} — {item["title"]}',fenced('Pseudocode\n'+pseudo(item['code'])), '**Sample output**',fenced(out),table(rows),'**Why it works:** '+item['why'],'**Complexity:** '+item['complexity'],'**Boundary checks:** '+item['edges']]
        item['answer']='\n\n'.join(a[-8:])
        CHECKS.append({'id':ident,'check':'AST interpreter = Python reference = expected sample','trace_rows':len(rows)})
    write('pseudocode-writing-questions.md','\n\n'.join(q))
    write('pseudocode-writing-answers.md','\n\n'.join(a))


O=[]
def o(title,code,expected,why,distractors=None,language='Pseudocode',display=None):
    O.append(dict(title=title,code=code,expected=expected,why=why,distractors=distractors,language=language,display=display))

o('Multiplication before addition','x=4+3*2\nprint(x)','10','Multiplication is evaluated first, so 4+6=10.',['14','11','8'])
o('Left-associative subtraction','x=20-6-3\nprint(x)','11','Group (20-6)-3, not 20-(6-3).',['17','14','9'])
o('Integer quotient and remainder','a=23\nprint(a//4,a%4)','5 3','23=5*4+3.',['5 2','6 3','5.75 0'])
o('Signed truncation','a=-23\nq=div(a,4)\nr=a-q*4\nprint(q,r)','-5 -3','Truncation goes toward zero; remainder reconstructs the dividend.',['-6 1','-5 3','-6 -3'])
o('Assignment uses old values','x=3\ny=x+2\nx=y*2\nprint(x,y)','10 5','Changing x later does not recompute y.',['10 10','6 5','5 10'])
o('Temporary swap','a=2\nb=8\nt=a\na=b\nb=t\nprint(a,b)','8 2','Temporary preserves the old a.',['8 8','2 8','2 2'])
o('Nested boundary condition','x=0\nif x>=0:\n    if x>0:\n        print("P")\n    else:\n        print("Z")\nelse:\n    print("N")','Z','Zero enters the nonnegative branch, then fails the positive test.',['P','N','P\nZ'])
o('Independent IF blocks','x=6\ns=0\nif x>3:\n    s=s+1\nif x%2==0:\n    s=s+2\nprint(s)','3','Both IFs execute independently.',['1','2','0'])
o('Only one alternative','x=7\nif x>4:\n    print("A")\nelse:\n    if x>2:\n        print("B")\n    else:\n        print("C")','A','The outer true branch bypasses its entire ELSE.',['B','A\nB','C'])
o('Conditional expression','x=4\ny=9\nz=x if x>y else y\nprint(z)','9','The test is false, selecting y.',['4','13','FALSE'])
o('Inclusive step-two loop','s=0\nfor i in range(1,8,2):\n    s=s+i\nprint(s)','16','Visits 1,3,5,7, then stops.',['9','25','12'])
o('Descending loop','s=0\nfor i in range(6,0,-2):\n    s=s+i\nprint(s)','12','Visits 6,4,2; lower bound in the displayed contract is 1.',['10','6','14'])
o('Skipped FOR body','s=9\nfor i in range(5,3):\n    s=0\nprint(s)','9','Positive step cannot start above the inclusive end 2.',['0','5','3'])
o('Doubling loop','i=1\ns=0\nwhile i<=8:\n    s=s+i\n    i=i*2\nprint(s,i)','15 16','The rejected i=16 is retained but not added.',['7 8','15 8','31 32'])
o('Halving loop','n=19\ncount=0\nwhile n>0:\n    n=n//2\n    count=count+1\nprint(count)','5','19→9→4→2→1→0 has five updates.',['4','6','19'])
o('Decrement before accumulation','i=5\ns=0\nwhile i>0:\n    i=i-1\n    s=s+i\nprint(s)','10','Added values are 4,3,2,1,0.',['15','5','14'])
o('BREAK before addition','s=0\nfor i in range(1,7):\n    if i==4:\n        break\n    s=s+i\nprint(s)','6','The value 4 never reaches the addition.',['10','21','3'])
o('CONTINUE skips evens','s=0\nfor i in range(1,7):\n    if i%2==0:\n        continue\n    s=s+i\nprint(s)','9','Only 1,3,5 are added.',['12','21','6'])
o('WHILE update before CONTINUE','i=0\ns=0\nwhile i<5:\n    i=i+1\n    if i==3:\n        continue\n    s=s+i\nprint(s)','12','Progress occurs before the skip; all values except 3 contribute.',['15','9','Does not terminate'])
o('Rectangular nested loop','count=0\nfor i in range(3):\n    for j in range(2):\n        count=count+1\nprint(count)','6','Three complete inner loops of two visits.',['5','3','9'])
o('Triangular loop','count=0\nfor i in range(1,5):\n    for j in range(i):\n        count=count+1\nprint(count)','10','Rows contribute 1+2+3+4.',['16','6','8'])
o('Inner BREAK only','count=0\nfor i in range(3):\n    for j in range(4):\n        if j==2:\n            break\n        count=count+1\nprint(count)','6','Each row counts j=0,1; outer loop continues.',['2','12','9'])
o('Dependent step increments','count=0\nfor i in range(1,5):\n    j=i\n    while j<=4:\n        count=count+1\n        j=j+i\nprint(count)','8','Counts by row are 4,2,1,1, not 4*4.',['10','16','7'])
o('Array accumulation','A=[2,5,1]\ns=0\nfor i in range(len(A)):\n    s=s+A[i]\nprint(s)','8','Each element is added exactly once.',['7','3','5'])
o('Array mutation feeds next step','A=[1,2,3,4]\nfor i in range(1,len(A)):\n    A[i]=A[i]+A[i-1]\nprint(A)','[1, 3, 6, 10]','Previous elements have already changed, creating prefix sums.',['[1, 3, 5, 7]','[1, 2, 3, 4]','[10, 6, 3, 1]'])
o('Array alias','A=[3,4]\nB=A\nB[1]=9\nprint(A,B)','[3, 9] [3, 9]','Both variables refer to the same array.',['[3, 4] [3, 9]','[3, 9] [3, 4]','[9, 4] [9, 4]'])
o('Array copy','A=[3,4]\nB=list(A)\nB[1]=9\nprint(A,B)','[3, 4] [3, 9]','COPY makes a separate outer array; these elements are scalars.',['[3, 9] [3, 9]','[3, 4] [3, 4]','[3, 9] [3, 4]'])
o('First matching index','A=[5,2,5]\nanswer=-1\nfor i in range(len(A)):\n    if A[i]==5:\n        answer=i\n        break\nprint(answer)','0','BREAK preserves the first match.',['2','1','-1'])
o('Last matching index','A=[5,2,5]\nanswer=-1\nfor i in range(len(A)):\n    if A[i]==5:\n        answer=i\nprint(answer)','2','Without BREAK the later match overwrites the earlier one.',['0','1','3'])
o('One bubble pass','A=[4,1,3,2]\nfor j in range(len(A)-1):\n    if A[j]>A[j+1]:\n        t=A[j]\n        A[j]=A[j+1]\n        A[j+1]=t\nprint(A)','[1, 3, 2, 4]','One pass settles the largest, not necessarily all elements.',['[1, 2, 3, 4]','[4, 3, 2, 1]','[1, 4, 2, 3]'])
o('Selection minimum index','A=[8,3,7,2]\nbest=0\nfor i in range(1,len(A)):\n    if A[i]<A[best]:\n        best=i\nprint(best,A[best])','3 2','best stores an index, not the minimum itself.',['2 3','1 3','2 2'])
o('Binary search successful','A=[1,4,6,9,12]\nlo=0\nhi=4\nanswer=-1\nwhile lo<=hi:\n    mid=lo+(hi-lo)//2\n    if A[mid]==9:\n        answer=mid\n        break\n    if A[mid]<9:\n        lo=mid+1\n    else:\n        hi=mid-1\nprint(answer)','3','Inspect index 2 then index 3.',['2','4','-1'])
o('String reverse loop','s="abc"\nr=""\nfor i in range(len(s)-1,-1,-1):\n    r=r+s[i]\nprint(r)','cba','Indices 2,1,0 supply c,b,a.',['abc','bc','cab'])
o('Character filtering','s="banana"\ncount=0\nfor i in range(len(s)):\n    if s[i]=="a":\n        count=count+1\nprint(count)','3','Matches at positions 1,3,5.',['2','4','6'])
o('End-exclusive slice','s="zeus"\nprint(s[1:3])','eu','Indices 1 and 2 are included, index 3 excluded.',['eus','ze','us'])
o('String concatenation','s=""\nfor i in range(1,4):\n    s=s+str(i)\nprint(s)','123','STRING converts each integer before joining text.',['6','321','1 2 3'])
o('Matrix row total','M=[[2,1],[3,4]]\ns=0\nfor c in range(2):\n    s=s+M[1][c]\nprint(s)','7','Row index 1 is the second row.',['3','10','5'])
o('Secondary diagonal','M=[[1,2,3],[4,5,6],[7,8,9]]\ns=0\nfor i in range(3):\n    s=s+M[i][2-i]\nprint(s)','15','Coordinates (0,2),(1,1),(2,0) give 3,5,7.',['25','45','12'])
o('Scalar parameter value','def change(x):\n    x=x+5\n    return x\na=2\nb=change(a)\nprint(a,b)','2 7','Local scalar reassignment does not change caller a.',['7 7','2 2','7 2'])
o('Array parameter mutation','def change(A):\n    A[0]=A[0]+5\n    return A[0]\na=[2,3]\nb=change(a)\nprint(a,b)','[7, 3] 7','The parameter aliases the caller array, so element mutation is shared.',['[2, 3] 7','[7, 3] 2','[2, 3] 2'])
o('Nested function calls','def twice(x):\n    return x*2\nprint(twice(twice(3))+1)','13','Inner call returns 6; outer returns 12; add 1.',['7','12','14'])
o('Early RETURN','def f(x):\n    if x>0:\n        return x\n    return -x\nprint(f(-4),f(3))','4 3','Each call follows its own branch and exits at RETURN.',['-4 3','4 -3','-4 -3'])
o('Recursive factorial trace','def f(n):\n    if n<=1:\n        return 1\n    return n*f(n-1)\nprint(f(4))','24','Return values unwind 1,2,6,24.',['10','16','4'])
o('Print on descent','def f(n):\n    if n==0:\n        return 0\n    print(n)\n    return f(n-1)\nf(3)','3\n2\n1','Printing happens before the recursive call.',['1\n2\n3','3\n2\n1\n0','0\n1\n2\n3'])
o('Print on return','def f(n):\n    if n==0:\n        return 0\n    f(n-1)\n    print(n)\n    return n\nf(3)','1\n2\n3','Pending prints execute while the stack unwinds.',['3\n2\n1','0\n1\n2\n3','3'])
o('Two recursive branches','def f(n):\n    if n<=1:\n        return n\n    return f(n-1)+f(n-2)\nprint(f(5))','5','Both branches contribute; base values are 0 and 1.',['8','3','15'])
o('Recursive halving','def f(n):\n    if n==0:\n        return 0\n    return 1+f(n//2)\nprint(f(10))','4','Calls 10,5,2,1 contribute 1 each; 0 contributes 0.',['3','5','10'])
o('Bitwise AND','a=13\nb=10\nprint(a&b)','8','1101 AND 1010 = 1000.',['7','15','23'])
o('Bitwise OR and XOR','a=5\nb=3\nprint(a|b,a^b)','7 6','0101 OR 0011=0111; XOR=0110.',['6 7','1 6','7 1'])
o('Eight-bit complement','print(not8(5))','250','00000101 becomes 11111010; width is explicitly eight bits.',['-6','251','5'])
o('Shift then addition','x=3\nprint((x<<2)+1,13>>1)','13 6','3 shifted two bits is 12; nonnegative right shift truncates 13/2.',['16 6','7 6','13 7'])
o('XOR cancellation','A=[6,2,6,9,2]\nx=0\nfor i in range(len(A)):\n    x=x^A[i]\nprint(x)','9','Each paired value cancels, leaving 9.',['0','25','6'])
o('Clear set bits','x=14\ncount=0\nwhile x>0:\n    x=x&(x-1)\n    count=count+1\nprint(count)','3','1110→1100→1000→0000.',['4','2','14'])
o('Guard division with AND','d=0\nprint((d!=0) and (12//d>1))','FALSE','False left operand skips division entirely.',['TRUE','Runtime error','0'])
o('OR skips call side effect','def mark():\n    print("called")\n    return False\nprint(True or mark())','TRUE','True left operand skips mark, so it prints nothing.',['called\nTRUE','called\nFALSE','FALSE'])
o('De Morgan evaluation','p=True\nq=False\nprint(not(p and q),(not p) or (not q))','TRUE TRUE','Both equivalent expressions are true.',['FALSE FALSE','TRUE FALSE','FALSE TRUE'])
o('Digit extraction order','n=407\ns=0\nwhile n>0:\n    s=s+n%10\n    n=n//10\nprint(s)','11','Digits arrive as 7,0,4.',['407','7','4'])
o('Numeric reversal drops zeros','n=1200\nr=0\nwhile n>0:\n    r=r*10+n%10\n    n=n//10\nprint(r)','21','Initial extracted zeros do not add leading positions to an integer.',['0021','1200','12'])
o('Euclid state','a=35\nb=15\nwhile b!=0:\n    r=a%b\n    a=b\n    b=r\nprint(a,b)','5 0','Pairs are (35,15),(15,5),(5,0).',['15 5','0 5','5 5'])
o('Negative-only maximum','A=[-4,-9,-2]\nbest=A[0]\nfor i in range(1,len(A)):\n    if A[i]>best:\n        best=A[i]\nprint(best)','-2','Maximum starts from an actual element, not invented zero.',['0','-9','-4'])

# Twenty-four additional questions: six boundary-focused families, each changes
# execution shape (bounds, sign, divisibility, parity or early exit), not only output.
for start,stop,step in [(0,5,2),(5,-1,-2),(3,3,1),(8,1,-3)]:
    vals=list(range(start,stop,step)); expected=' '.join(map(str,vals)) or 'EMPTY'
    code=f's=""\nfor i in range({start},{stop},{step}):\n    if s!="":\n        s=s+" "\n    s=s+str(i)\nif s=="":\n    s="EMPTY"\nprint(s)'
    o(f'Boundary sequence {start}/{stop}/{step}',code,expected,'Check the first value, signed step and inclusive end shown in the pseudocode; EMPTY is a deliberate sentinel.',[str(start), ' '.join(map(str,vals+[stop])), 'Does not terminate'])
for n in [0,1,10,1001]:
    count=len(str(n))
    o(f'Digit count boundary n={n}',f'n={n}\ncount=1\nwhile n>=10:\n    count=count+1\n    n=n//10\nprint(count)',str(count),'One initial digit plus one count for every removable decimal position.',[str(count-1),str(count+1),str(count+2)])
for n in [1,2,9,17]:
    prime=n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
    o(f'Prime boundary n={n}',f'n={n}\nprime=n>=2\nd=2\nwhile prime and d*d<=n:\n    if n%d==0:\n        prime=False\n    d=d+1\nprint(prime,d)',fmt(prime)+' '+str((next((d+1 for d in range(2,math.isqrt(n)+1) if n%d==0),math.isqrt(n)+1)) if n>=2 else 2),'d advances after every tested divisor, including the divisor that disproves primality.',['TRUE 2','FALSE 2','FALSE 5'] if n==17 else None)
for n in [0,1,4,6]:
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    o(f'Fibonacci state after {n} updates',f'a=0\nb=1\nfor i in range({n}):\n    t=a+b\n    a=b\n    b=t\nprint(a,b)',f'{a} {b}','After k updates the pair is (F_k,F_(k+1)); the temporary prevents reuse of an overwritten a.')
for A,target in [([],1),([3],3),([2,2,2],2),([1,4,7],5)]:
    found=A.index(target) if target in A else -1
    o(f'Search edge {A}, target {target}',f'A={A!r}\ntarget={target}\nfound=-1\nfor i in range(len(A)):\n    if A[i]==target:\n        found=i\n        break\nprint(found)',str(found),'A first-match search breaks only after a match; empty and absent cases preserve -1.')
for n in [1,2,3,4]:
    count=sum(1 for i in range(1,n+1) for j in range(1,i+1) if (i+j)%2==0)
    o(f'Parity-filtered triangle n={n}',f'count=0\nfor i in range(1,{n+1}):\n    for j in range(1,i+1):\n        if (i+j)%2==0:\n            count=count+1\nprint(count)',str(count),'Only pairs of equal parity contribute; the inner bound depends on the row.')

# Real-language snippets. Equivalent separated-statement reference programs are
# checked by both evaluators; language syntax/semantics are explicitly documented.
o('Java postfix then prefix','x=4\na=x\nx=x+1\nx=x+1\nb=x\nprint(a,b,x)','4 6 6','Java postfix yields the old value; prefix yields the new value.', ['5 6 6','4 5 6','4 6 5'],'Java','int x=4;\nint a=x++;\nint b=++x;\nSystem.out.println(a+" "+b+" "+x);')
o('Java left-to-right increments','x=2\na=x\nx=x+1\nx=x+1\nb=x\ny=a+b\nprint(y,x)','6 4','Java evaluates the left operand x++ first, then ++x. This expression must not be transplanted to C.',['5 4','7 4','Undefined behavior'],'Java','int x=2;\nint y=x++ + ++x;\nSystem.out.println(y+" "+x);')
o('Java decrements','x=5\na=x\nx=x-1\nx=x-1\nb=x\nprint(a,b,x)','5 3 3','Postfix uses 5; then prefix decreases 4 to 3.', ['4 3 3','5 4 3','5 3 4'],'Java','int x=5;\nint a=x--;\nint b=--x;\nSystem.out.println(a+" "+b+" "+x);')
o('Java division sign','q=div(-7,3)\nr=mod(-7,3)\nprint(q,r)','-2 -1','Java integer / truncates toward zero; remainder has dividend sign.',['-3 2','-2 1','-3 -1'],'Java','System.out.println((-7/3)+" "+(-7%3));')
o('Java AND short-circuit','x=0\nflag=False\nprint(flag,x)','FALSE 0','The false first operand skips ++x entirely; Java prints lowercase false.', ['TRUE 1','FALSE 1','Runtime error'],'Java','int x=0;\nboolean flag=(x!=0) && (++x>0);\nSystem.out.println(flag+" "+x);')
o('Java switch fall-through','x=2\ns=0\ns=s+2\ns=s+3\nprint(s)','5','case 2 has no break, so case 3 also runs before its break.',['2','3','0'],'Java','int x=2, s=0;\nswitch(x) {\n  case 1: s+=1; break;\n  case 2: s+=2;\n  case 3: s+=3; break;\n  default: s=0;\n}\nSystem.out.println(s);')
o('Java ternary skips other arm','x=3\ny=x\nx=x+1\nprint(y,x)','3 4','Only the selected x++ arm executes.',['4 4','3 5','4 5'],'Java','int x=3;\nint y=(x>0) ? x++ : ++x;\nSystem.out.println(y+" "+x);')
o('Java logical OR skip','x=1\nflag=True\nprint(flag,x)','TRUE 1','True first operand skips x++ in the right operand. Java prints lowercase true.',['TRUE 2','FALSE 1','FALSE 2'],'Java','int x=1;\nboolean flag=(x==1) || (x++>0);\nSystem.out.println(flag+" "+x);')
o('Python floor division','q=-7//3\nr=-7%3\nprint(q,r)','-3 2','Python // floors toward minus infinity; positive divisor makes the remainder nonnegative.',['-2 -1','-2 1','-3 -1'],'Python','print(-7 // 3, -7 % 3)')
o('Python double unary plus','x=4\ny=++x\nprint(x,y)','4 4','++x is two unary plus signs, not increment.',['5 5','4 5','Syntax error'],'Python','x = 4\ny = ++x\nprint(x, y)')
o('Python range end excluded','s=0\nfor i in range(1,5):\n    s=s+i\nprint(s)','10','Python range visits 1,2,3,4; end 5 is excluded.',['15','6','5'],'Python','s = 0\nfor i in range(1, 5):\n    s += i\nprint(s)')
o('Python negative indexing','A=[2,4,6]\nprint(A[2])','6','In real Python A[-1] denotes the last element; our neutral pseudocode forbids negative indices.',['Runtime error','2','4'],'Python','A = [2, 4, 6]\nprint(A[-1])')
o('C increments separated','x=3\na=x\nx=x+1\nx=x+1\nb=x\nprint(a,b,x)','3 5 5','Each modification is in a separate full expression, so no unsequenced side effects.',['4 5 5','3 4 5','Undefined behavior'],'C','#include <stdio.h>\nint main(void) {\n    int x=3;\n    int a=x++;\n    int b=++x;\n    printf("%d %d %d\\n",a,b,x);\n    return 0;\n}')
o('C decrement loop','s=0\ni=4\nwhile i>0:\n    s=s+i\n    i=i-1\nprint(s,i)','10 0','Post-decrement loop update happens after the body each time.',['6 0','10 1','15 0'],'C','#include <stdio.h>\nint main(void) {\n    int s=0,i;\n    for(i=4;i>0;i--) s+=i;\n    printf("%d %d\\n",s,i);\n    return 0;\n}')
o('C do-while runs once','x=0\nx=x+1\nprint(x)','1','do-while enters the body once before testing x<0.',['0','2','Does not terminate'],'C','#include <stdio.h>\nint main(void) {\n    int x=0;\n    do { x++; } while(x<0);\n    printf("%d\\n",x);\n    return 0;\n}')
o('C integer division','q=div(17,5)\nr=mod(17,5)\nprint(q,r)','3 2','Both operands are int, so division truncates.',['3.4 0','4 2','3 3'],'C','#include <stdio.h>\nint main(void) {\n    printf("%d %d\\n",17/5,17%5);\n    return 0;\n}')


def candidates(out):
    """Distinct plausible alternatives, preserving type/shape when possible."""
    if out in ('TRUE','FALSE'): return ['FALSE' if out=='TRUE' else 'TRUE','Runtime error','No output']
    if out.lstrip('-').isdigit():
        v=int(out); return [str(v+1),str(v-1),str(v+2)]
    if '\n' in out:
        lines=out.split('\n'); return ['\n'.join(reversed(lines)), '\n'.join(lines[:-1]),out+'\n0','No output']
    pieces=out.split()
    if all(p.lstrip('-').isdigit() for p in pieces):
        return [' '.join(reversed(pieces)), ' '.join(str(int(p)+1) for p in pieces), ' '.join(str(int(p)-1) for p in pieces),'0']
    return ['No output','Runtime error','Does not terminate']


def prepare_output(item,index):
    # Python negative floor // is intentionally checked under Python rules only.
    if item['language']=='Python' and item['title']=='Python floor division':
        reference=[]
        exec(item['display'],{'print':lambda *a:reference.append(' '.join(map(str,a)))})
        out='\n'.join(reference)
        rows=[['1','Python','-7 // 3 → -3','q=-3','—'],['2','Python','-7 % 3 → 2','r=2','—'],['3','Python','print','q=-3; r=2',out]]
    else: out,rows=execute(item['code'])
    assert out==item['expected'],(index,item['title'],out,item['expected'])
    if item['language']=='Java':
        out=out.replace('TRUE','true').replace('FALSE','false')
    item['out']=out; item['rows']=rows
    choices=[out]
    extras=item['distractors'] or candidates(out)
    for c in extras+candidates(out)+['Runtime error','No output','Does not terminate','Syntax error']:
        if item['language']=='Java': c=c.replace('TRUE','true').replace('FALSE','false')
        if c not in choices: choices.append(c)
        if len(choices)==4: break
    assert len(choices)==4
    correct_slot=(index-1)%4
    choices.insert(correct_slot,choices.pop(0))
    item['choices']=choices;item['letter']='ABCD'[correct_slot]
    display=item['display'] or pseudo(item['code'])
    lang={'Pseudocode':'text','Python':'python','Java':'java','C':'c'}[item['language']]
    item['prompt']='Predict the exact output. **Language: '+item['language']+'**.\n\n'+fenced(display,lang)+'\n\n'+'\n\n'.join(f'**{letter}.** '+fenced(c) for letter,c in zip('ABCD',choices))
    item['solution']='**Answer: '+item['letter']+'**\n\n'+fenced(out)+'\n\n'+table(rows)+'\n\n**Explanation:** '+item['why']
    if item['language']!='Pseudocode':
        item['solution']+='\n\nThe table separates side effects into their evaluation order. The displayed program above follows '+item['language']+' rules; the reference model is used only for verification.'
    CHECKS.append({'id':item.get('id',f'O{index:03}'),'check':'two executions + expected output; real-language rows use explicit semantic models','trace_rows':len(rows)})


def build_outputs():
    assert len(O)==100,len(O)
    q=['# Output-prediction questions','Original practice: O001–O020 easy, O021–O060 medium, O061–O100 mixed boundary and language traps. Use the README contract for neutral code. Java snippets belong inside main; C snippets are complete programs. Choose one option and write your own variable table before checking.']
    a=['# Output-prediction answers','Exact output appears in a code block, followed by a full execution table. An output containing multiple lines must retain their order. For real-language examples, the explanatory table expands language side effects into steps.']
    for i,item in enumerate(O,1):
        item['id']=f'O{i:03}'
        prepare_output(item,i)
        q += [f'## {item["id"]} — {item["title"]}',item['prompt']]
        a += [f'## {item["id"]} — {item["title"]}',item['solution']]
    write('output-prediction-questions.md','\n\n'.join(q))
    write('output-prediction-answers.md','\n\n'.join(a))
