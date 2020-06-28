
 # 20. 有效的括号
 # 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
 # <p>
 # 有效字符串需满足：
 # <p>
 # 左括号必须用相同类型的右括号闭合。
 # 左括号必须以正确的顺序闭合。
 # 注意空字符串可被认为是有效字符串。
 
def solution(s: str) -> bool:
    stack =[]
    for char in s:
        if char == '(':
            stack.append(')')
        elif char == '[':
            stack.append(']')
        elif char == '{':
            stack.append('}')
        elif len(stack)==0 or stack.pop() != char:
            return False
    if len(stack) != 0:
        return False
    return True

def main():
    print(solution("["))

main()
