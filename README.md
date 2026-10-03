# Algo Practice 🧠🐍

A personal collection of **Data Structures and Algorithms (DSA)** exercises implemented in Python — built while learning, one problem at a time.

---

## 🗂️ Project Structure

```text
algo-practice/
├── LICENSE
├── README.md
└── src/
    ├── __init__.py
    │
    ├── arrays/              # Array algorithms
    │   ├── advanced.py
    │   ├── basics.py
    │   ├── compare.py
    │   ├── intervals.py
    │   ├── matrix.py
    │   ├── rearrange.py
    │   ├── search.py
    │   └── unique.py
    │
    ├── games/               # Small games & interactive exercises
    │   ├── guess.py
    │   ├── rock_paper.py
    │   └── traffic_light.py
    │
    ├── math_ops/            # Math & number algorithms
    │   ├── arithmetic.py
    │   ├── calculator.py
    │   ├── comparison.py
    │   ├── digits.py
    │   ├── geometry.py
    │   ├── math_helpers.py
    │   ├── properties.py
    │   └── sequences.py
    │
    ├── patterns/            # Star / pyramid patterns
    │   └── pyramids.py
    │
    ├── searches/             # Searching algorithms
    │   └── binary.py
    │
    ├── sorts/                # Sorting algorithms
    │   └── merge.py
    │
    ├── string_ops/           # String algorithms
    │   ├── basics.py
    │   ├── letter.py
    │   ├── manipulation.py
    │   ├── permutations.py
    │   ├── string_patterns.py
    │   └── validation.py
    │
    ├── structures/           # Data structures
    │   ├── bst.py
    │   ├── linked_list.py
    │   ├── node.py
    │   ├── queue.py
    │   ├── stack.py
    │   ├── stack_helper.py
    │   ├── tree_advanced.py
    │   ├── tree_basics.py
    │   └── tree_traversal.py
    │
    └── utils/                # Small utilities
        ├── atm.py
        ├── bmi.py
        ├── grade.py
        ├── temperature.py
        └── time_utils.py
```

---

## ⚙️ Installation & Setup

### 📋 Prerequisites

- **Python 3.12+** — uses PEP 695 generics such as `class Stack[T]`
- **pip**

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nasir-ehsan-83/algo-practice.git
cd algo-practice
```

### 2️⃣ Create a Virtual Environment

**Linux / macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

Currently, no external dependencies are required.

To run tests once they are restored:

```bash
pip install pytest
```

---

## 📚 Learning Content

| Module | Topics |
|---|---|
| `arrays/` | Searching, sorting within arrays, matrix operations, intervals |
| `math_ops/` | Arithmetic, digit manipulation, number properties, sequences |
| `string_ops/` | Reversal, manipulation, validation, permutations, patterns |
| `structures/` | Stack, Queue, Linked List, Binary Tree, BST |
| `searches/` | Binary Search |
| `sorts/` | Merge Sort |
| `patterns/` | Pyramid & triangle patterns |
| `games/` | Number guessing, Rock-Paper-Scissors, Traffic Light |
| `utils/` | Temperature conversion, BMI, time, grade, ATM |

---

## 💻 Example Usage

### 🧱 Using a Data Structure

```python
from src.structures.stack import Stack

s = Stack[int]()

s.push(1)
s.push(2)
s.push(3)

print(s.pop())  # 3
print(s.top())  # 2
print(s.size())  # 2
```

### ➕ Using a Math Operation

```python
from src.math_ops.arithmetic import add_numbers

print(add_numbers(2, 3))  # 5
```

### 🔤 Using a String Operation

```python
from src.string_ops.basics import reverse_string

print(reverse_string("hello"))  # "olleh"
```

---

## 🧪 Running Tests

> **Note:** Tests are currently being rewritten to match the new `src/` layout. They will be added back soon.

Once restored, tests can be run with:

```bash
pytest
```

---

## 🛠️ Tools & Technologies

| Technology | Purpose |
|---|---|
| 🐍 **Python 3.12+** | Programming language |
| 🧪 **pytest** | Automated testing |
| 🔧 **Git** | Version control |
| 🐙 **GitHub** | Repository hosting |

---

## 🗺️ Roadmap

- [x] Reorganize modules under `src/`
- [x] Rename modules to avoid standard-library conflicts (`math_ops`, `string_ops`)
- [ ] Rewrite tests to match the new structure
- [ ] Add missing data structures (Heap, Graph, Hash Table, ...)
- [ ] Add CI workflow with GitHub Actions
- [ ] Add static type checking with mypy

---

## 🤝 Contributing

This is primarily a personal learning repository, but suggestions and feedback are welcome.

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/your-feature
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -m "feat: add your feature"
```

5. Push the branch:

```bash
git push origin feature/your-feature
```

6. Open a Pull Request.

---

## 📄 License

This project is released under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

---

## 👤 Author

**Nasir Ehsan**

- GitHub: [@nasir-ehsan-83](https://github.com/nasir-ehsan-83)

---

## ⭐ Support

If you find this project useful, consider giving it a **star** on GitHub.