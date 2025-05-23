def permutate_with_case(ip, op):
    if len(ip) == 0:
        print(op)
        return
    op1 = op + ip[0]
    op2 = op + ip[0].upper()
    ip = ip[1:]
    permutate_with_case(ip, op1)
    permutate_with_case(ip, op2)
    return

permutate_with_case("abc","")