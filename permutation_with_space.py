def permutate_with_space(ip, op):
    if len(ip) == 0:
        print(op)
        return
    op1 = op + " " + ip[0]
    op2 = op + ip[0]
    ip = ip[1:]
    permutate_with_space(ip, op1)
    permutate_with_space(ip, op2)
    return

if __name__ == "__main__":
     s= "ABC"
     permutate_with_space("BC", "A")