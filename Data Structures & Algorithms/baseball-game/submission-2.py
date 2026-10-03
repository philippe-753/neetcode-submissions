class Solution:
    def calPoints(self, operations: List[str]) -> int:
        N = len(operations)
        stack = []

        for op in operations:
            print("-----")
            print(op)
            if op.isnumeric() or op.startswith("-"):
                stack.append(int(op))
            else:
                if not stack:
                    continue
                prev = stack.pop()
                if op == "+":
                    prev2 = stack.pop()
                    stack.append(prev2)
                    stack.append(prev)
                    stack.append(prev + prev2)

                if op == "D":
                    stack.append(prev)
                    stack.append(2*prev)
        return sum(stack)