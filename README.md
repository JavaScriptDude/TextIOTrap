## tiotrap

Simple class for trapping / capturing Text IO streams like `subprocess.popen`, capturing output of library calls to stdout or stderr and a DEVNULL helper to drop Text IO streams. 

### Installation

```
python3 -m pip install tiotrap
```


### Usage

This tool contains one class `TextIOTrap` and a helper `DEVNULL`.


#### Use `TextIOTrap` to capture stdout of a chatty process using `store` option:
```python3
_stdout_bk = sys.stdout # Store original stdout
tio_trap = tiotrap.TextIOTrap(store=True)

try:
  sys.stdout = tio_trap # Map stdout to tiotrap
  print("TEST1")
  # call some chatty functions()
  print("TEST2")
  
finally:
  sys.stdout = _stdout_bk # Restore stdout
  
print(f"captured logs:\n{str(tio_trap)}\n~end~\n")
```
Output of print:
```
captured logs:
TEST1
<chatty outputs here>
TEST2
```


#### Use `TextIOTrap` to capture stdout using `write_handler` option:
```python3
aTrappedStdout = []
_stdout_bk = sys.stdout

try:
  sys.stdout = tiotrap.TextIOTrap(write_handler=lambda s: aTrappedStdout.append(s))
  print("TEST1")
  print("TEST2")
  
finally:
  sys.stdout = _stdout_bk
  
print(f"aTrappedStdout = {aTrappedStdout}")
```

Output of print:
```
aTrappedStdout = ['TEST1', 'TEST2']
```
You can substitute lambda with a function or method call to handle `writes` with your own code.



#### Using `TextIOTrap` grab output `pexpect` call :
```python3
tio_trap = tiotrap.TextIOTrap(store=True)

p = pexpect.spawn('ls -la')
p.logfile = tio_trap
p.expect(pexpect.EOF)

print(f"ls output:\n{str(tio_trap)}\n~")
```

Output of print:
```
ls output:
<full directory listing here of cwd>
```

Other uses of `TextIOTrap`:
* Output the stdout of a `subprocess.popen` call in real time to a secondary log file
* ...



#### `DEVNULL` can be used to drop all output of a TextIO Stream
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
