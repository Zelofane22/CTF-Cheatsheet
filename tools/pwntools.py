from pwn import *

exe = ELF("./binary")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
    else:
        r = remote("10.0.2.15", 9999)

    return r


def main():
    r = conn()
    # tech 1 : reçois une ligne
    #r.recvline()

    # tech 2 : reçois tout
    #r.recvall()

    # tech 3 : reçois jusqua b'<caractère>'
    r.recvuntil(b'\n')
    payload = cyclic(90)

    # tech 4 : send line after a recev line
    """
    r.recvlineafter('<char>', payload)
    """
    log.info("Loading..."
            f"{hexdump(payload)}")
    r.sendline(payload)
    r.interactive()


if __name__ == "__main__":
    main()