# grammar.py
epsilon = "eps"
class Grammar:
    def __init__(self, grammar_text):
        self.logs = []
        self.grammar = {}
        self.non_terminals = set()
        self.terminals = set()
        self.start_symbol = None
        self.parse_grammar(grammar_text)

        self.logs.append("\nChecking Left Recursion...")
        self.remove_left_recursion()

        self.logs.append("\nChecking Left Factoring...")
        self.left_factor()

    def parse_grammar(self, grammar_text):
        lines = grammar_text.strip().split('\n')

        for i, line in enumerate(lines):
            left, right = line.split("->")
            left = left.strip()
            productions = [p.strip() for p in right.split('|')]

            if i == 0:
                self.start_symbol = left

            self.non_terminals.add(left)
            self.grammar[left] = productions

        for left in self.grammar:
            for production in self.grammar[left]:
                for symbol in production.split():
                    if symbol not in self.non_terminals and symbol != 'ε':
                        self.terminals.add(symbol)

    # ✅ LEFT RECURSION (Direct Only – fixed logging)
    def remove_left_recursion(self):
        new_grammar = {}
        found = False

        for A in self.grammar:
            alpha = []
            beta = []

            for prod in self.grammar[A]:
                tokens = prod.split()
                if tokens and tokens[0] == A:
                    alpha.append(" ".join(tokens[1:]))
                else:
                    beta.append(prod)

            if alpha:
                found = True
                self.logs.append(f"Left Recursion Found in {A} → Fixed")

                A_dash = A + "'"
                self.non_terminals.add(A_dash)

                new_grammar[A] = [b + " " + A_dash for b in beta]
                new_grammar[A_dash] = [a + " " + A_dash for a in alpha] + ['ε']
            else:
                new_grammar[A] = self.grammar[A]

        if not found:
            self.logs.append("No Left Recursion Found")

        self.grammar = new_grammar

    # ✅ IMPROVED LEFT FACTORING
    def left_factor(self):
        new_grammar = {}
        found = False

        for A in self.grammar:
            prods = self.grammar[A]

            # Find longest common prefix
            prefix_map = {}
            for prod in prods:
                tokens = tuple(prod.split())
                if tokens:
                    prefix_map.setdefault(tokens[0], []).append(tokens)

            if any(len(v) > 1 for v in prefix_map.values()):
                found = True
                self.logs.append(f"Left Factoring Applied in {A}")

                A_dash = A + "F"
                self.non_terminals.add(A_dash)

                new_grammar[A] = []
                new_grammar[A_dash] = []

                for key in prefix_map:
                    group = prefix_map[key]

                    if len(group) > 1:
                        new_grammar[A].append(key + " " + A_dash)

                        for tokens in group:
                            rest = tokens[1:]
                            new_grammar[A_dash].append(" ".join(rest) if rest else "ε")
                    else:
                        new_grammar[A].append(" ".join(group[0]))
            else:
                new_grammar[A] = prods

        if not found:
            self.logs.append("No Left Factoring Needed")

        self.grammar = new_grammar

    def get_grammar(self):
        return self.grammar

    def get_logs(self):
        return self.logs