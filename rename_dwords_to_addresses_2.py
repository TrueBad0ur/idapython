# rename dwords code
# buhtrap
# 004166E4 dword_4166E4 dd 419498h
# 004166E8 dword_4166E8 dd 4194A8h

# .data:00419498 somefunc1 db 'somefunc1',0
# .data:004194A8 somefunc2 db 'somefunc2',0

ea = get_screen_ea()

for i in range(1):

    var_to_rename = ea
    string_addr = ida_bytes.get_dword(ea)
    name = get_name(string_addr)
    set_name(var_to_rename, "_" + name)
    
    ea += 4
