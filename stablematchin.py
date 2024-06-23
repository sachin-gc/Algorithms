def stable_marriage(men_preferences, women_preferences):
    # Number of men and women
    n = len(men_preferences)

    # All men and women are initially free
    free_men = list(range(n))
    women_partner = [-1] * n #[-1,-1,-1,-1]
    men_next_proposal = [0] * n#[0,0,0,0]   `

    # While there are free men
    while free_men:
        # Take the first free man
        man = free_men[0]
        # Find the next woman on his preference list
        woman = men_preferences[man][men_next_proposal[man]]

        if women_partner[woman] == -1:
            # If the woman is free, engage them
            women_partner[woman] = man
            free_men.pop(0)
        else:
            # If the woman is already engaged, find her current partner
            current_partner = women_partner[woman]

            # Find the preferences of the woman
            woman_prefers = women_preferences[woman]

            # Check if she prefers the new man over her current partner
            if woman_prefers.index(man) < woman_prefers.index(current_partner):
                # She prefers the new man, engage them
                women_partner[woman] = man
                free_men.pop(0)
                # The previous partner is now free
                free_men.append(current_partner)

        # Move to the next woman on the man's preference list
        men_next_proposal[man] += 1

    # Create the result as pairs of men and women
    result = [(women_partner[w], w) for w in range(n)]
    return result


# Example usage
men_preferences = [
    [1,0,3,2],
    [3,1,0,2],
    [1,3,0,2],
    [0,1,3,2]
]

women_preferences = [
    [2,3,1,0],
    [1,0,2,3],
    [3,0,1,2],
    [2,1,3,0]
]

matches = stable_marriage(men_preferences, women_preferences)
print("Stable matches (man, woman):",matches)
