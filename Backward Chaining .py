import re
from collections import defaultdict

# Knowledge base
rules = defaultdict(list)
facts = set()

# Add rules and facts
def add_clause(clause):
    if '==>' in clause:
        premises, conclusion = clause.split('==>')
        premises = [p.strip() for p in premises.strip().split(',')]
        conclusion = conclusion.strip()
        rules[conclusion].append(premises)
    else:
        facts.add(clause.strip())

# Knowledge base definition
kb = [
    "mammal(A) ==> vertebrate(A)",
    "vertebrate(A) ==> animal(A)",
    "vertebrate(A),flying(A) ==> bird(A)",
    "vertebrate(\"duck\")",
    "flying(\"duck\")",
    "mammal(\"cat\")"
]

for clause in kb:
    add_clause(clause)

# Match predicate and argument
def parse(expr):
    match = re.match(r"(\w+)\((.+)\)", expr)
    return match.group(1), match.group(2)

# Backward chaining
def bc(goal, seen=set()):
    if goal in facts:
        return True
    if goal in seen:
        return False
    seen.add(goal)

    pred, arg = parse(goal)

    # Try matching rules
    for conclusion, premises_list in rules.items():
        c_pred, c_arg = parse(conclusion)
        if c_pred == pred:
            for premises in premises_list:
                subst = {}
                if c_arg[0].isupper():  # Variable
                    subst[c_arg] = arg
                elif c_arg != arg:
                    continue  # Can't unify

                # Apply substitution and prove all premises
                new_goals = []
                for prem in premises:
                    p_pred, p_arg = parse(prem)
                    if p_arg in subst:
                        new_goals.append(f"{p_pred}({subst[p_arg]})")
                    else:
                        new_goals.append(prem)

                if all(bc(g, seen.copy()) for g in new_goals):
                    return True
    return False

# Query
query = input("Enter goal (e.g., animal(\"cat\")): ").strip()

if bc(query):
    print(f"{query} can be derived from the knowledge base.")
else:
    print(f"{query} CANNOT be derived from the knowledge base.")
