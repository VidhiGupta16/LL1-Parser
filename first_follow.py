def compute_first(grammar, non_terminals):
    FIRST = {nt: set() for nt in non_terminals}

    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for production in grammar[nt]:
                symbols = production.split()
                for symbol in symbols:
                    if symbol not in non_terminals:
                        if symbol not in FIRST[nt]:
                            FIRST[nt].add(symbol)
                            changed = True
                        break
                    else:
                        before = len(FIRST[nt])
                        FIRST[nt].update(FIRST[symbol] - {'ε'})
                        if 'ε' not in FIRST[symbol]:
                            break
                        if before != len(FIRST[nt]):
                            changed = True
                else:
                    FIRST[nt].add('ε')

    return FIRST


def compute_follow(grammar, non_terminals, FIRST, start_symbol):
    FOLLOW = {nt: set() for nt in non_terminals}
    FOLLOW[start_symbol].add('$')

    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for production in grammar[nt]:
                symbols = production.split()
                for i, symbol in enumerate(symbols):
                    if symbol in non_terminals:
                        next_symbols = symbols[i+1:]
                        if next_symbols:
                            next_symbol = next_symbols[0]
                            if next_symbol in non_terminals:
                                FOLLOW[symbol].update(FIRST[next_symbol] - {'ε'})
                                if 'ε' in FIRST[next_symbol]:
                                    FOLLOW[symbol].update(FOLLOW[nt])
                            else:
                                FOLLOW[symbol].add(next_symbol)
                        else:
                            FOLLOW[symbol].update(FOLLOW[nt])
    return FOLLOW
