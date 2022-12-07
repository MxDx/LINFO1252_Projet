
lock:
    .long 0

enter:
    movl $1, %eax
    xchgl %eax, (lock)

    testl %eax, %eax
    jnz enter
    ret

leave:
    movl $0, %eax
    xchgl %eax, (lock)
    ret