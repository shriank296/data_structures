def substring(ip,op):
    if len(ip) == 0:
        print(op)
        return
    op1 = op
    op2 = op + ip[0]
    ip = ip[1:]
    substring(ip,op1)
    substring(ip, op2)
    return

substring('abc',"")        