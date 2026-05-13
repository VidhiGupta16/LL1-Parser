def parse_input(input_string, table, start_symbol, non_terminals):
    stack = ['$']
    stack.append(start_symbol)

    input_buffer = input_string.split() + ['$']
    pointer = 0
    steps = []

    while stack:
        top = stack.pop()
        current = input_buffer[pointer]

        steps.append({
            "stack": " ".join(stack),
            "input": " ".join(input_buffer[pointer:]),
            "action": ""
        })

        if top == current:
            pointer += 1
            steps[-1]["action"] = f"Match {current}"
        elif top in non_terminals:
            if current in table[top]:
                production = table[top][current]
                if "|" in production:
                    steps[-1]["action"]="COnflict in table->not LL(1)"
                steps[-1]["action"] = f"{top} -> {production}"
                if production != 'ε':
                    stack.extend(reversed(production.split()))
            else:
                return steps, False
        else:
            return steps, False

    return steps, True
