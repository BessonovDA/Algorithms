class StackBracket:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return 'error'
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def is_correct_bracket_seq(bracket_seq):
    open_brackets = ['{', '(', '[']
    closed_brackets = ['}', ')', ']']
    bracket_stack = StackBracket()
    for bracket in bracket_seq:
        if bracket in open_brackets:
            bracket_stack.push(bracket)
        else:
            prev_bracket = bracket_stack.pop()
            if prev_bracket != open_brackets[closed_brackets.index(bracket)]:
                return False
    if bracket_stack.size() > 0:
        return False
    return True


if __name__ == '__main__':
  #  print(is_correct_bracket_seq(input()))

    print(is_correct_bracket_seq('{((}))'))
