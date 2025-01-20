class Solution:
    def isValid(self, s: str) -> bool:
        unique = []
        for i, letter in enumerate(s):
            unique.append(letter)
            if letter == '(':
                unique.append(')')
            elif letter == '[':
                unique.append(']')
            elif letter == '{':
                unique.append('}')
            else:
                if len(unique) == 0 or letter != unique.pop():
                    return False
            
        