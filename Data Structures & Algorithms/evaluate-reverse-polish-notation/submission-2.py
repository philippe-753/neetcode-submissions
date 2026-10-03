class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = "+-*/"

        for token in tokens:
            if token not in operations:
                stack.append(float(token))
            else:
                num_1 = stack.pop()
                num_2 = stack.pop()
                if token == "+":
                    ans = self._add(num_1, num_2)
                elif token == "-":
                    ans = self._substrack(num_1, num_2)
                elif token == "*":
                    ans = self._multiply(num_1, num_2)
                else:
                    ans =self._divide(num_1, num_2)

                stack.append(ans)
        
        return int(stack[-1])

    @staticmethod
    def _add(a:float, b:float)-> int:
        return int(a + b)
    
    @staticmethod
    def _substrack(a:float, b:float) -> int:
        return int(b - a)
    
    @staticmethod
    def _multiply(a:float, b:float) -> int:
        return int(a * b)

    @staticmethod
    def _divide(a:float, b:float) -> int:
        return int(b / a)