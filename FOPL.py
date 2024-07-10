class Clause:
    def __init__(self, literals):
        self.literals = set(literals)

    def __str__(self):
        return str(self.literals)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.literals == other.literals

    def __hash__(self):
        return hash(frozenset(self.literals))

    def resolution(self, other):
        resolvents = set()
        for literal1 in self.literals:
            for literal2 in other.literals:
                if literal1.negation() == literal2:
                    new_literals = (self.literals - {literal1}).union(other.literals - {literal2})
                    if new_literals:
                        resolvents.add(Clause(new_literals))
        return resolvents


class Literal:
    def __init__(self, name, negated=False):
        self.name = name
        self.negated = negated

    def __str__(self):
        return '~' + self.name if self.negated else self.name

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name and self.negated == other.negated

    def __hash__(self):
        return hash((self.name, self.negated))

    def negation(self):
        return Literal(self.name, not self.negated)


def resolution(clauses):
    new_clauses = set()
    for c1 in clauses:
        for c2 in clauses:
            if c1 == c2:
                continue
            resolvents = c1.resolution(c2)
            for resolvent in resolvents:
                if resolvent not in clauses:
                    new_clauses.add(resolvent)
    return new_clauses


# Example usage

c1 = Clause({Literal("P"), Literal("Q", True)})
c2 = Clause({Literal("R"), Literal("Q")})
c3 = Clause({Literal("S", True), Literal("T")})

clauses = {c1, c2, c3}

print(resolution(clauses))
