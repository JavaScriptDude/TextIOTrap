## TextIOTrap

Simple class for trapping / capturing Python Text IO streams like from `subprocess.popen`, `pexpect`, `sys.stderr` and others; enabling the capture output of or dropping streams with cross platform `DEVNULL` helper. 

### Installation

```
python3 -m pip install tiotrap
```


### Usage

This tool contains one class `TextIOTrap` and a helper `DEVNULL`.


### Examples

#### (Ex1) Use `TextIOTrap` to capture stdout of a chatty process using `store` option:
```python3
_stdout_bk = sys.stdout # Store original stdout
ttrap = tiotrap.TextIOTrap(store=True)

try:
    sys.stdout = ttrap # Map stdout to tiotrap
    print("TEST1")
    # call some chatty functions()
    print("TEST2")

finally:
    sys.stdout = _stdout_bk # Restore stdout
```
Output of print:
```
captured logs:
TEST1
<chatty outputs here>
TEST2
```


#### (Ex2) Use `TextIOTrap` to capture stdout using `write_handler` option:
```python3
aTrap = []
_stdout_bk = sys.stdout
try:
    sys.stdout = tiotrap.TextIOTrap(write_handler=lambda s: aTrap.append(s))
    print("TEST1")
    print("TEST2")

finally:
    sys.stdout = _stdout_bk
# print adds extra \n end so remove with rstrip()
print(f"aTrap:\n{''.join(aTrap).rstrip()}\n~end~\n")
```

Output of print:
```
aTrappedStdout = ['TEST1', 'TEST2']
```
You can substitute lambda with a function or method call to handle `writes` with your own code.



#### (Ex3) Use `TextIOTrap` grab output `pexpect` call :
```python3
ttrap = tiotrap.TextIOTrap(store=True)

p = pexpect.spawn('ls -la')
p.logfile = ttrap
p.expect(pexpect.EOF)

print(f"`ls -la` cmd output:\n{ttrap.entries()}\n~")
```

Output of print:
```
ls output:
<full directory listing here of cwd>
```

Other uses of `TextIOTrap`:
* Output the stdout of a `subprocess.popen` call in real time to a secondary log file
* ...


#### (Ex4) Use `TextIOTrap` grab output `pexpect` call :
```python3
ttrap = tiotrap.TextIOTrap(store=True)

p = pexpect.spawn('ls -la')
p.logfile = ttrap
p.expect(pexpect.EOF)

print("ls -la` cmd output (as was written):")
for write in ttrap:
    print(write)
```
Output: Similar to Ex4


#### (Ex5) Use `DEVNULL` to drop all output of a TextIO Stream
```python3
_stdout_bk = sys.stdout

try:
    sys.stdout = tiotrap.DEVNULL
    print("THIS WILL NOT PRINT")

finally:
    sys.stdout = _stdout_bk

print("THIS WILL PRINT")
```
This DEVNULL is very simple implementation and is fully cross platform unlike someother DEVNULL implementations.


Note:` TextIOTrap` has been set up to be compatible with the standard methods for a Text IO streams. I'll be glad to update if any edge cases are discovered.
