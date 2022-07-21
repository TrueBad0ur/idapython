%include "io.inc"

section .text
global CMAIN
CMAIN:
    mov ebp, esp; for correct debugging
    nop
    nop
    nop
    mov eax, str1
    PRINT_STRING str1
    
    nop
    nop
    nop
    mov eax, str2
    PRINT_STRING str1
    
    nop
    nop
    nop
    mov eax, str3
    PRINT_STRING str1
    
    xor eax, eax
    ret

    
.bss
    str1 db "Hell", 0
    str2 db "o wo", 0
    str3 db "rld!", 0
