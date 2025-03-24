from stack import stack

def delete_middle_element(stack, k):
    if k == 1:
        return stack.pop()
    stack.pop()
    return delete_middle_element(stack, k-1)


k = len(stack) // 2 + 1

print(delete_middle_element(stack, k))