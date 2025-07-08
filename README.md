# Beyond Basics: Python

**Beyond Basics: Python** is a curated collection of Python code examples, exercises, and implementations aimed at developers who want to strengthen their grasp of intermediate to advanced Python concepts. This project is ideal for developers familiar with Python syntax and eager to understand _how_ things work behind the scenes — from functions and loops to decorators, object-oriented programming, and external integrations.

---

## 🔍 Key Features & Techniques

This repository uses a range of Python capabilities and standard library tools. Some notable implementations include:

- **Decorators** for caching, debugging, and timing functions ([MDN Explanation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#method_definitions))
- **Object-Oriented Programming (OOP)** concepts including inheritance and method overriding
- **[Mutable vs Immutable types](./muteableVsimmutable/)** in Python — a deep dive into behavior and memory implications
- **Python iteration internals** including [iterator protocol](https://docs.python.org/3/library/functions.html#iter) and generator workflows
- **Function closures and scope handling** ([MDN Scope Reference](https://developer.mozilla.org/en-US/docs/Glossary/Scope))
- **API integration** using [`requests`](https://pypi.org/project/requests/) and JSON manipulation
- **SQLite & MongoDB integration** to simulate lightweight data operations
- **Basic error handling** and control flow using `try-except` blocks

---

## 📦 Libraries and Technologies Used

In addition to the Python standard library, the repo uses:

- [`requests`](https://pypi.org/project/requests/): For handling external API calls
- [`pymongo`](https://pypi.org/project/pymongo/): To demonstrate MongoDB-based storage and retrieval
- [`sqlite3`](https://docs.python.org/3/library/sqlite3.html): For simple SQL-based data persistence
- [`functools`](https://docs.python.org/3/library/functools.html): Used in decorator examples
- [Open-source system fonts](https://fonts.google.com/) assumed by default; no custom font specified in code

---

## 📁 Project Structure

```bash
beyond-basics-python/
├── 01_basics/
├── 10_Conditionals/
├── 10_functions/
├── 10_loops/
├── Api_handling/
├── Decoraters/
├── Dictionary/
├── Error_handling/
├── List/
├── Numbers/
├── OOP/
├── String/
├── Tuples/
├── bts_in_loops/
├── inner-working/
├── muteableVsimmutable/
├── scope_and_clousers/
├── youtube_manager/
```

### 🔸 Directory Highlights

- **[`Api_handling/`](./Api_handling/)** – Demonstrates integration with a public API using `requests`
- **[`Decoraters/`](./Decoraters/)** – Includes performance and debug decorators
- **[`youtube_manager/`](./youtube_manager/)** – Uses both SQLite and MongoDB for CRUD-based data persistence
- **[`bts_in_loops/`](./bts_in_loops/)** – Explains what happens internally during iteration
- **[`scope_and_clousers/`](./scope_and_clousers/)** – Shows lexical scoping and closures in action
- **[`inner-working/`](./inner-working/)** – Contains memory management and execution flow examples

---

## 🛠️ Author

- **Wasim Akram** — [LinkedIn Profile](https://www.linkedin.com/in/wasim-akram-dev/)
- **Contact:** [malikwaseemshzad@gmail.com](mailto:malikwaseemshzad@gmail.com)
