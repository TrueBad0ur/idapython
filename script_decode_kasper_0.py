def decode_str(s, key="dc67f@#$%hlsdfg"):
	key = [ord(key[i]) & 0x1F for i in range(len(key))]
	result = [ord(s[i]) ^ key[i % len(key)] for i in range(len(s)) if s[i] != 0xE0]
	return ''.join([chr(i) for i in result])

for x in XrefsTo(0x00475610):
	for h in Heads(x.frm - 10, x.frm):
		if print_insn_mnem(h) == "mov" and print_operand(h, 0) == "eax":
			s = get_strlit_contents(get_operand_value(h, 1), get_wide_dword(get_operand_value(h, 1) - 4))
			set_cmt(x.frm, decode_str(s), False)