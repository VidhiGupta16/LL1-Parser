from flask import Flask, render_template, request, jsonify
from grammer import Grammar 
from first_follow import compute_first, compute_follow
from parsing_table import create_parsing_table
from parser_engine import parse_input

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process_page", methods=["POST"])
def process_page():
    grammar_text = request.form["grammar"]
    input_string = request.form["input"]

    grammar_obj = Grammar(grammar_text)
    grammar = grammar_obj.get_grammar()
    logs = grammar_obj.get_logs()
    FIRST = compute_first(grammar, grammar_obj.non_terminals)
    FOLLOW = compute_follow(grammar, grammar_obj.non_terminals, FIRST, grammar_obj.start_symbol)
    table, is_ll1 = create_parsing_table(grammar, FIRST, FOLLOW, grammar_obj.non_terminals)
    steps, result = parse_input(input_string, table, grammar_obj.start_symbol, grammar_obj.non_terminals)

    return render_template(
    "result.html",
    FIRST=FIRST,
    FOLLOW=FOLLOW,
    table=table,
    steps=steps,
    result=result,
    is_ll1=is_ll1,
    logs=logs   
)

if __name__ == "__main__":
    app.run(debug=True)
