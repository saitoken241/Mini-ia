# 🌳 Binary Decision Tree & DFS Traversals

This project is a Python implementation of a **Binary Decision Tree** used to simulate a simplified Medical Expert System. It demonstrates fundamental Computer Science concepts such as **Recursion**, **Hierarchical Data Structures**, and **Depth-First Search (DFS)** traversals.

## 🧠 Core Concepts

In this project, I explore how a non-linear data structure can be used to model complex decision-making logic. The tree is structured where:

* 
**Internal Nodes:** Represent clinical questions (decision points).


* **Edges:** Represent the "Yes" (Left) or "No" (Right) paths.
* 
**Leaf Nodes:** Represent the final diagnosis (result).



## 🚀 Algorithm Implementation

The project implements three types of **Depth-First Search (DFS)** traversals to explore the tree nodes:

1. **Pre-order (Root → Left → Right):** Useful for cloning trees or prefix expression evaluation.
2. **In-order (Left → Root → Right):** In a search tree, this would visit nodes in non-decreasing order.
3. **Post-order (Left → Right → Root):** Commonly used for deleting trees or postfix notation.

### Code Snippet: Recursive Traversal

```python
def preorder(node):
    if "diagnostico" in node:
        return [f"⇒ {node['diagnostico']}"]
    
    question = node.get("pergunta")
    current = [question] if question else []
    
    # Recursive calls following the Root -> Left -> Right pattern
    return current + preorder(node.get("sim")) + preorder(node.get("nao"))

```

## 🛠️ Project Structure

```text
.
└── mini_ia.py       # Main logic including the tree dictionary and DFS functions

```

## 📊 Technical Skills Demonstrated

As an Information Systems undergraduate, this project highlights my proficiency in:

* 
**Recursion:** Handling nested data structures without iterative loops.


* 
**Tree Traversals:** Deep understanding of how to navigate hierarchical data.


* 
**Data Modeling:** Using Python dictionaries to represent complex tree nodes.


* 
**Problem Solving:** Translating medical diagnostic logic into a computational model.



## 🔧 How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/saitoken241/binary-tree-python.git

```


2. **Run the script:**
```bash
python mini_ia.py

```



## 📄 License

This project is part of my personal portfolio for demonstrating Data Structures knowledge.

---

**ken** Information Systems Student | Backend Developer 

[LinkedIn]() | [GitHub](https://github.com/saitoken241)
