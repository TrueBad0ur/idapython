# used in UxIoctlTable
# get_screen_ea()

TABLE_START = 0x1C005CB20
TABLE_END = 0x1C005CF30

while TABLE_START <= TABLE_END:
    create_data(TABLE_START, ida_bytes.qword_flag(), 8, ida_netnode.BADNODE)
    TABLE_START+=8
