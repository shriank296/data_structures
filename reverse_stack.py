from stack import stack

def reverse_recursive(stack):
    if len(stack) == 0:
        return stack
    val = stack.pop()
    reverse_recursive(stack)
    insert_at_bottom(stack, val)
    return stack


def insert_at_bottom(stack, val):
    if len(stack) == 0:
        return stack.push(val)
    item = stack.pop()
    insert_at_bottom(stack, val)
    stack.push(item)


# stack.display()
reverse_recursive(stack)
stack.display()    

