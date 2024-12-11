from sympy.logic.boolalg import And, Or, Not
from sympy.abc import A, B, C  # Example propositions

# Define the knowledge base
knowledge_base = And(
    Or(Not(A), B),  # ¬A ∨ B
    Or(Not(B), C),  # ¬B ∨ C
    Not(C)          # ¬C
)

# Statement to prove: A
statement = A

# Negate the statement for refutation
negated_statement = Not(statement)

# Combine the knowledge base with the negated statement
refutation_base = And(knowledge_base, negated_statement)

# Check satisfiability of the refutation base
from sympy.logic.inference import satisfiable

result = satisfiable(refutation_base)
if result:
    print("No contradiction found. Statement is not proven. Counterexample:", result)
else:
    print("Contradiction found. The statement is proven to be true.")
