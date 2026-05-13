# `README.md`

````md
# Predictive Parser Studio 🚀

An interactive **LL(1) Parser Generator** built using **Python** and **Flask** that helps users understand compiler design concepts practically through grammar validation, FIRST & FOLLOW computation, parsing table generation, parsing visualization, and parse tree construction.

---

## 📌 Project Overview

Predictive Parser Studio is a web-based compiler design project that allows users to:

- Enter context-free grammar
- Remove left recursion
- Apply left factoring
- Generate FIRST and FOLLOW sets
- Construct LL(1) parsing tables
- Validate input strings
- View step-by-step parsing
- Visualize parse trees
- Detect non-LL(1) grammars
- Suggest alternative parsing techniques

This project bridges the gap between compiler design theory and practical implementation.

---

## ✨ Features

✅ Grammar Parsing and Preprocessing  
✅ Left Recursion Removal  
✅ Left Factoring  
✅ FIRST Set Computation  
✅ FOLLOW Set Computation  
✅ LL(1) Parsing Table Generation  
✅ Input String Validation  
✅ Step-by-Step Parsing Visualization  
✅ Parse Tree Construction  
✅ Error Handling and Grammar Validation  
✅ Flask-based Interactive Web Interface  
✅ Recommendation for LR(0), SLR(1), CLR Parsing Techniques

---

## 🛠️ Tech Stack

### Backend
- Python

### Web Framework
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Compiler Design Concepts
- LL(1) Parsing
- FIRST and FOLLOW
- Parsing Table Generation
- Parse Tree Generation
- Grammar Optimization

---

## 📂 Project Structure

```bash
LL1_Parser/
│
├── app.py                  # Main Flask application
├── grammer.py              # Grammar preprocessing module
├── first_follow.py         # FIRST and FOLLOW computation
├── parsing_table.py        # LL(1) parsing table generation
├── parser_engine.py        # Parsing engine
├── parse_tree.py           # Parse tree generation
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ashmita67/LL1_Parser.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd LL1_Parser
```

### 3️⃣ Install Dependencies

```bash
pip install flask
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```bash
http://localhost:5000
```

---

## 🧠 How It Works

### Step 1: Enter Grammar
User provides grammar productions through the web interface.

### Step 2: Grammar Preprocessing
The system:
- Removes left recursion
- Applies left factoring

### Step 3: FIRST & FOLLOW Computation
FIRST and FOLLOW sets are generated for all non-terminals.

### Step 4: Parsing Table Generation
The LL(1) parsing table is created using FIRST and FOLLOW sets.

### Step 5: Input String Parsing
The parser validates whether the given string belongs to the grammar.

### Step 6: Parse Tree Visualization
A parse tree is generated to visualize derivation steps.

---

## 📸 Output Features

- FIRST Set Display
- FOLLOW Set Display
- LL(1) Parsing Table
- Parsing Steps
- Parse Tree Visualization
- Error Messages for Invalid Grammars/Input

---

## 🧪 Testing

The project has been tested using:

| Test Type | Status |
|-----------|--------|
| Unit Testing | ✅ Pass |
| Integration Testing | ✅ Pass |
| Sample Input Testing | ✅ Pass |
| Invalid Input Testing | ✅ Pass |

---

## 🚧 Challenges Faced

- Handling left recursion correctly
- Managing epsilon productions
- Avoiding LL(1) conflicts
- Parse tree synchronization
- Debugging parsing errors

---

## 🔮 Future Enhancements

- Advanced parse tree visualization
- Better UI/UX
- Support for LR(0), SLR(1), CLR parsers
- Grammar conflict highlighting
- Export parsing steps as PDF
- Dark mode support

---

## 👨‍💻 Team Members

### Syntax Squad

- Vidhi Gupta
- Ashmita Sohal
- Abinisha V
- Vansh Agarwal

---

## 📚 Learning Outcomes

This project helped in understanding:

- Compiler Design Fundamentals
- Predictive Parsing
- LL(1) Grammar Rules
- Flask Web Development
- Modular Programming
- Parsing Algorithms

---

## ⭐ Repository

GitHub Repository:

https://github.com/Ashmita67/LL1_Parser

---

## 📄 License

This project is created for educational and academic purposes.

---

## 💡 Sample Grammar Example

```text
E  -> T E'
E' -> + T E' | ε
T  -> F T'
T' -> * F T' | ε
F  -> ( E ) | id
```

### Sample Input

```text
id + id * id
```

---

## 🎯 Conclusion

Predictive Parser Studio provides an interactive and practical approach to learning LL(1) parsing and compiler design concepts. It combines theory with implementation, making compiler construction easier to understand for students and beginners.

---


