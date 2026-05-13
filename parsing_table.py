def create_parsing_table(grammar, FIRST, FOLLOW, non_terminals):
    table = {nt: {} for nt in non_terminals}
    is_ll1 = True

    for nt in grammar:
        for production in grammar[nt]:
            symbols = production.split()
            first_set = set()

            if symbols[0] in non_terminals:
                first_set = FIRST[symbols[0]]
            else:
                first_set.add(symbols[0])

            # Fill using FIRST
            for terminal in first_set - {'ε'}:
                if terminal in table[nt]:
                    is_ll1 = False
                    table[nt][terminal] += " | " + production
                else:
                    table[nt][terminal] = production

            # Handle epsilon
            if 'ε' in first_set:
                for terminal in FOLLOW[nt]:
                    if terminal in table[nt]:
                        is_ll1 = False
                        table[nt][terminal] += " | " + production
                    else:
                        table[nt][terminal] = production

    return table, is_ll1