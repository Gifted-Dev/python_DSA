Before beginning with data structure and algorithms, it is important to know what time complexity and space complexity is.

### 1. **What is Time Complexity?**

   - **Time Complexity** measures *how long an algorithm takes to run* as the size of the input grows.
   - We use it to predict the running time of an algorithm, especially with large data inputs.

#### Common Time Complexities:

| Notation   | Description                               | Example                     |
|------------|-------------------------------------------|-----------------------------|
| **O(1)**   | Constant Time - takes the same time no matter the input size. | Accessing a specific element in an array. |
| **O(n)**   | Linear Time - time grows linearly with input size. | Looping through an array. |
| **O(n²)**  | Quadratic Time - time grows with the square of the input size. | Nested loops (loop inside a loop). |
| **O(log n)** | Logarithmic Time - time grows slowly as input grows. | Binary search. |

#### Why It’s Important:
   - It helps us choose the fastest algorithm for a task, especially when we have large data. For example, **O(n)** is generally better than **O(n²)** because it grows slower as `n` increases.

---

### 2. **What is Space Complexity?**

   - **Space Complexity** measures *how much memory (space) an algorithm uses* as the input size grows.
   - We look at it to make sure our program doesn’t use more memory than is available or necessary.

#### Common Space Complexities:

| Notation   | Description                               | Example                     |
|------------|-------------------------------------------|-----------------------------|
| **O(1)**   | Constant Space - uses the same space regardless of input size. | Using a few variables. |
| **O(n)**   | Linear Space - space grows with input size. | Storing all items in a list. |
| **O(n²)**  | Quadratic Space - space grows with the square of input size. | 2D arrays (like a table of data). |

#### Why It’s Important:
   - It helps us avoid memory issues. Using excessive space can make a program run slower or even crash, especially if the input is large.

---

### 3. **Putting It Together**

   - In real-world coding, **time complexity** helps us know how fast an algorithm runs, while **space complexity** helps us manage memory use.
   - An efficient algorithm is one with low time complexity and low space complexity.

---

### 4. **An Example**

   - **Problem:** Find the largest number in a list.
   - **Solution:** Check each number and keep track of the largest.

#### Complexity Analysis:
   - **Time Complexity:** `O(n)` (because you check each item once).
   - **Space Complexity:** `O(1)` (because you only need one extra variable to store the largest number).

---

**Remember:** In general, the lower the time and space complexity, the more efficient the algorithm.