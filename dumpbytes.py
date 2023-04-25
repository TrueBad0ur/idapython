filename = "C:\\path\\to\\new\\file"
address = 0x400000
size = 0x31337
dbgr = False
with open(filename, "wb") as out:
    data = get_bytes(address, size, use_dbg=dbgr)
    out.write(data)
