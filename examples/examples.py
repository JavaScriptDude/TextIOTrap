import sys
import pexpect
import tiotrap

# Examples provided from README.md
def main():
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()


def example_1():
    print("\n(Ex1) Use `TextIOTrap` to capture stdout of a chatty process using `store` option")

    _stdout_bk = sys.stdout # Store original stdout
    ttrap = tiotrap.TextIOTrap(store=True)

    try:
        sys.stdout = ttrap # Map stdout to tiotrap
        print("TEST1")
        # call some chatty functions()
        print("TEST2")
    
    finally:
        sys.stdout = _stdout_bk # Restore stdout
    
    print(f"Captured logs:\n{ttrap.entries()}\n~end~\n")

    print("END (Ex1)")


def example_2():
    print("\n(Ex2) Use `TextIOTrap` to capture stdout using `write_handler` option")

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

    print("END (Ex2)")


def example_3():
    print("\n(Ex3) Using `TextIOTrap` grab output `pexpect` call")

    ttrap = tiotrap.TextIOTrap(store=True)

    p = pexpect.spawn('ls -la')
    p.logfile = ttrap
    p.expect(pexpect.EOF)

    print(f"`ls -la` cmd output:\n{ttrap.entries()}\n~")

    print("END (Ex3)")


def example_4():
    print("\n(Ex4) Using `TextIOTrap` grab output `pexpect` call (__iter__)")
    
    ttrap = tiotrap.TextIOTrap(store=True)

    p = pexpect.spawn('ls -la')
    p.logfile = ttrap
    p.expect(pexpect.EOF)

    print("ls -la` cmd output (as was written):")
    for write in ttrap:
        print(write)

    print("END (Ex4)")


def example_5():
    print("\n(Ex5) `DEVNULL` can be used to drop all output of a TextIO Stream")

    _stdout_bk = sys.stdout

    try:
        sys.stdout = tiotrap.DEVNULL
        print("THIS WILL NOT PRINT")
    
    finally:
        sys.stdout = _stdout_bk
    
    print("THIS WILL PRINT")
    
    print("end (ex5)")




if __name__ == '__main__':
    main()