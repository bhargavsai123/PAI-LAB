class CSP:
    def __init__(self,variables,domains,constraints):
        self.variables=variables
        self.domains=domains
        self.constraints=constraints

    def is_consistent(self,variable,value,assignment):
        return all(constraint(variable,value,assignment)
                   for constraint in self.constraints)

    def backtrack(self,assignment):
        if len(assignment) == len(self.variables):
            return assignment
        var = next(variable for variable in self.variables if variable not in assignment)
        for value in self.domains[var]:
            if self.is_consistent(var,value,assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                assignment.pop(var)
        return None
    
def crypt(words,result):
    variables=list(set(''.join(words)+result))
    if len(variables) > 10:
        print("Too Many Unique Letters")
        return
    domains = {v:list(range(10)) for v in variables}
    leading_letters={w[0] for w in words + [result]}

    def constraint(var,value,assignment):
        if value in assignment.values():
            return False

        temp = assignment.copy()
        temp[var] = value

        if len(temp) == len(variables):
            def word_to_number(word):
                return int(''.join(str(temp[c]) for c in word))

            left = sum(word_to_number(w) for w in words)
            right = word_to_number(result)
            return left == right

        return True
        
    csp = CSP(variables, domains, [constraint])
    solution = csp.backtrack({})
    if solution:
        print("Solution Found : ")
        for variable, value in solution.items():
            print(f"{variable}:{value}")
    else:
        print("No Solution.")

words = input("Enter words (space separated): ").upper().split()
result = input("Enter result word: ").upper()

crypt(words, result)
    
