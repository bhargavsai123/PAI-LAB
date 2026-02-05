class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        return all(constraint(variable, value, assignment)
                   for constraint in self.constraints)

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        var = next(v for v in self.variables if v not in assignment)

        for value in self.domains[var]:
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                assignment.pop(var)

        return None


def crypt(words, result):
    variables = list(set(''.join(words) + result))

    if len(variables) > 10:
        print("Too many unique letters")
        return

    domains = {v: list(range(10)) for v in variables}
    leading_letters = {w[0] for w in words + [result]}

    def constraint(var, value, assignment):
        # No two letters can have same digit
        if value in assignment.values():
            return False

        # Leading letter cannot be zero
        if var in leading_letters and value == 0:
            return False

        temp = assignment.copy()
        temp[var] = value

        # Check equation only when all assigned
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
        print("Solution Found:")
        for k in sorted(solution):
            print(f"{k} : {solution[k]}")
    else:
        print("No solution found.")


words = input("Enter words (space separated): ").upper().split()
result = input("Enter result word: ").upper()
crypt(words, result)
