# def letter_case_permutate(ip, op):
#     if ip[0].isdigit():
#         op = op + ip[0]
#         ip = ip[1:]
#     if len(ip) == 0:
#         print(op)
#         return 
#     op1 = op + ip[0].swapcase()
#     op2 = op + ip[0]
#     ip = ip[1:]
#     letter_case_permutate(ip, op1)
#     letter_case_permutate(ip, op2)
#     return

def letter_case_permutate(ip, op):
    if len(ip) == 0:
        print(op)
        return 
    if ip[0].isalpha():
        op1 = op + ip[0].swapcase()
        op2 = op + ip[0]
        ip = ip[1:]
        letter_case_permutate(ip, op1)
        letter_case_permutate(ip, op2)
    else:
        op = op + ip[0]
        ip = ip[1:]
        letter_case_permutate(ip, op)    
    return

letter_case_permutate('a1b2', '')    
