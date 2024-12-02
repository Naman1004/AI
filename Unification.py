def unify(var1, var2, substitution=None):
    """
    Perform unification between two terms.
    :param var1: First term
    :param var2: Second term
    :param substitution: Current substitution map
    :return: A dictionary representing the substitution, or None if unification fails
    """
    if substitution is None:
        substitution = {}

    if var1 == var2:
        return substitution

    if isinstance(var1, str) and var1.islower():  # var1 is a variable
        return unify_variable(var1, var2, substitution)

    if isinstance(var2, str) and var2.islower():  # var2 is a variable
        return unify_variable(var2, var1, substitution)

    if isinstance(var1, list) and isinstance(var2, list) and len(var1) == len(var2):
        for t1, t2 in zip(var1, var2):
            substitution = unify(t1, t2, substitution)
            if substitution is None:
                return None
        return substitution

    return None  # Unification fails


def unify_variable(var, term, substitution):
    """
    Handle unification of a variable with another term.
    :param var: Variable (e.g., "x")
    :param term: Another term
    :param substitution: Current substitution map
    :return: Updated substitution map, or None if unification fails
    """
    if var in substitution:
        return unify(substitution[var], term, substitution)
    elif occurs_check(var, term, substitution):
        return None
    else:
        substitution[var] = term
        return substitution


def occurs_check(var, term, substitution):
    """
    Perform the occurs check to ensure no infinite recursion.
    :param var: Variable (e.g., "x")
    :param term: Term to check against
    :param substitution: Current substitution map
    :return: True if occurs check fails, False otherwise
    """
    if var == term:
        return True
    elif isinstance(term, list):
        return any(occurs_check(var, t, substitution) for t in term)
    elif term in substitution:
        return occurs_check(var, substitution[term], substitution)
    return False


# Example Usage
if __name__ == "__main__":
    term1 = ["f", "x", "y"]
    term2 = ["f", "a", "b"]
    result = unify(term1, term2)
    if result:
        print("Unification succeeded:", result)
    else:
        print("Unification failed")
