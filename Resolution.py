from sympy.logic.boolalg import Or, And, Not
from sympy.abc import A, B, C  # Example propositions

# Define clauses
clause1 = Or(A, Not(B))  # A ∨ ¬B
clause2 = Or(B, Not(C))  # B ∨ ¬C
clause3 = Not(A)         # ¬A

# Combine clauses
knowledge_base = And(clause1, clause2, clause3)

# Query: Is C true given the knowledge base?
query = C

# Check satisfiability
from sympy.logic.inference import satisfiable

result = satisfiable(And(knowledge_base, Not(query)))
if result:
    print("Query cannot be resolved as true. Counterexample:", result)
else:
    print("Query resolved as true.")
