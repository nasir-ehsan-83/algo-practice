# Python DSA 🐍📚

A collection of **Data Structures and Algorithms (DSA)** exercises implemented in Python, with automated tests using **pytest**.

---

## 📁 Project Structure

```text
python-dsa/
├── algorithm/
│   ├── week1/                 # Week 1: Basics
│   ├── week2/                 # Week 2: Exercises 1–25
│   ├── week3/                 # Week 3: Exercises 1–30
│   └── week4/                 # Week 4: Exercises 1–25
│
├── data_structure/
│   ├── week5/                 # Week 5: Exercises 1–14
│   └── week6/                 # Week 6: Exercises 1–20
│
└── tests/
    ├── algorithm/
    │   ├── test_week1.py
    │   ├── test_week2_part1.py
    │   ├── test_week2_part2.py
    │   ├── test_week3_part1.py
    │   ├── test_week3_part2.py
    │   ├── test_week4_part1.py
    │   └── test_week4_part2.py
    │
    └── data_structure/
        ├── test_week1.py
        ├── test_week6_part1.py
        └── test_week6_part2.py
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10 or higher
- pip

### 1. Clone the repository

```bash
git clone https://github.com/nasir-ehsan-83/python-dsa.git
cd python-dsa
```

### 2. Create a virtual environment

**Linux / macOS:**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

If the repository contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install `pytest` directly:

```bash
pip install pytest
```

---

## 🧪 Running Tests

### Run all tests

```bash
pytest
```

### Run tests for a specific week

```bash
pytest tests/algorithm/test_week2_part1.py
```

```bash
pytest tests/data_structure/test_week6_part1.py
```

### Run tests with verbose output

```bash
pytest -v
```

---

## 🧠 Learning Content

| Section | Topic |
|---|---|
| `algorithm/week1` | Basics: addition, even/odd checks, string reversal, and more |
| `algorithm/week2` | Mixed algorithm exercises (1–25) |
| `algorithm/week3` | More advanced algorithm exercises (1–30) |
| `algorithm/week4` | Additional algorithm exercises (1–25) |
| `data_structure/week5` | Introduction to data structures (1–14) |
| `data_structure/week6` | Advanced data structure exercises (1–20) |

---

## 🧪 Example Exercise

### Implementation

```python
# algorithm/week1/is_even.py

def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0
```

### Corresponding Test

```python
# tests/algorithm/test_week1.py

from algorithm.week1.is_even import is_even


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
```

---

## 🛠 Tools & Technologies

- **Python 3** — Programming language
- **pytest** — Automated testing
- **Git & GitHub** — Version control

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Make your changes.
4. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```

5. Push the branch:

   ```bash
   git push origin feature/your-feature
   ```

6. Open a Pull Request.

---

## 📄 License

This project is released under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.

---

## 👤 Author

**Nasir Ehsan**

- GitHub: [@nasir-ehsan-83](https://github.com/nasir-ehsan-83)

---

⭐ If you find this project useful, consider giving it a star!