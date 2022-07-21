decrypt_function_address = 0x48DB90

def get_delphi_string(addr):
    return get_strlit_contents(addr, get_wide_dword(addr - 4))

def create_subs_table():
    table = {}
    
    h = next_head(decrypt_function_address)
    while print_insn_mnem(h) != "mov" or print_operand(h, 0) != "ebx":
        h = next_head(h)
    h = next_head(h)
    
    for _ in range(0x5E):
    
        while print_insn_mnem(h) != "mov" or print_operand(h, 0) != "edx" or get_operand_type(h, 1) != o_imm:
            h = next_head(h)
        c = get_delphi_string(get_operand_value(h, 1)) # current character tested
        
        while print_insn_mnem(h) != "mov" or print_operand(h, 0) != "eax" or get_operand_type(h, 1) != o_imm:
            h = next_head(h)
        s = get_delphi_string(get_operand_value(h, 1)) # character to replace with
        
        table[c.decode()] = s.decode()
        
        while print_insn_mnem(h) != "lea" or print_operand(h, 0) != "eax":
            h = next_head(h)
    
    return table
    
table = create_subs_table()

for x in XrefsTo(decrypt_function_address):
    for h in Heads(x.frm - 10, x.frm):
        if "mov" == print_insn_mnem(h) and print_operand(h, 0) == "edx":
            to_decode = get_delphi_string(get_operand_value(h, 1)).decode()
            decoded = "".join(table[c] for c in to_decode)
            set_cmt(x.frm, f"{decoded}", False)