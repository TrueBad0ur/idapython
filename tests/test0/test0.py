start_function_address = 0x401390

h = next_head(start_function_address)

for _ in range(3):
    while print_insn_mnem(h) != "nop" or print_insn_mnem(h+1) != "nop" or print_insn_mnem(h+2) != "nop":
        h = next_head(h)
    h = next_head(h)
    h = next_head(h)
    h = next_head(h)
    
    print(print_insn_mnem(h), end=" ")
    print(print_operand(h, 0), end=", ")
    print(get_strlit_contents(get_operand_value(h, 1)).decode())
    
    
    #print(hex(h))