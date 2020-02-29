men = {
    'Xavier': ['Amy', 'Bertha', 'Clare'],
    'Yancey': ['Amy', 'Bertha', 'Clare'],
    'Zeus': ['Amy', 'Bertha', 'Clare']
}
women = {
    'Amy': ['Xavier', 'Yancey', 'Zeus'],
    'Bertha': ['Xavier', 'Yancey', 'Zeus'],
    'Clare': ['Xavier', 'Yancey', 'Zeus']
}
women_matches = {
    'Amy': None,
    'Bertha': None,
    'Clare': None
}

def create_stable_pair(men):
    """
    Given a dictionary of men and women with their preferences of each other,
    match each male with a female such that it would produce a stable pair - 
    considering their preferences
    """

    # Iterate through the dictionary of men
    for proposing_man in sorted(men.keys(), reverse=True):
        assign_woman(proposing_man, men, women_matches, women)
        print(women_matches)


def assign_woman(proposing_man, preferrence_list, pairs, women):
    # Then check the man's list of preferrences of women
    for preferred_woman in preferrence_list[proposing_man]:
        # Check if the women has any partner
        if women_matches[preferred_woman] == None:
            women_matches[preferred_woman] = proposing_man
            break

        # If the woman does have a partner, check the woman's preferrences
        current_partner_ranking = None
        proposing_man_ranking = None
        for key, man in enumerate(women[preferred_woman]):
            if man == women_matches[preferred_woman]:
                current_partner_ranking = key
            elif man == proposing_man:
                proposing_man_ranking = key
            
        if proposing_man_ranking < current_partner_ranking:
            former_partner = women_matches[preferred_woman]
            women_matches[preferred_woman] = proposing_man
            assign_woman(former_partner, men, women_matches, women)
            break
    return


create_stable_pair(men)