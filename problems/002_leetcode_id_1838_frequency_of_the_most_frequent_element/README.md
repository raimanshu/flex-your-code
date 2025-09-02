# 🚀 1838: [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/)

🔗 [View on LeetCode](https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/)

---

## 🧠 Problem Statement

> The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

---

## 🤦‍♀️ Examples
Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:

Input: nums = [3,9,6], k = 2
Output: 1
 
---
<!-- ## ✅ Constraints

- Input: ...
- Output: ...
- Time Limit: ...
- Space Limit: ...

--- -->

## 🧩 Approaches

| Approach         | Description                       | Time Complexity | Space Complexity |
| ---------------- | --------------------------------- | --------------- | ---------------- |
| 1️⃣ Approach 1 | Using Precomputed Fibonacci Numbers | `O(1)`      | `O(1)`       |
| 2️⃣ Approach 2 | Recursive Approach     | `O(2ⁿ)`      | `O(n)`       |
| 1️⃣ Approach 3 | Dynamic Programming Approach | `O(n)`      | `O(n)`       |
| 2️⃣ Approach 4 | Dynamic Programming with Memoization     | `O(n)`      | `O(n)`       |
| 1️⃣ Approach 5 | Binet's Formula (Closed-form expression) | `O(log n)`      | `O(1)`       |

---

## 🐍 Python Solutions

| Approach | File                               |
| -------- | ---------------------------------- |
| 1    | [approach_1.py](python/approach_1.py) |
| 2    | [approach_2.py](python/approach_2.py) |
| 3    | [approach_3.py](python/approach_3.py) |
| 4    | - |
| 5    | [approach_5.py](python/approach_5.py) |


---

## 💻 JavaScript Solutions

| Approach | File                                   |
| -------- | -------------------------------------- |
| 1    | [approach_1.js](javascript/approach_1.js) |
| 2    | [approach_2.js](javascript/approach_2.js) |
| 3    | [approach_3.js](javascript/approach_3.js) |
| 4    | [approach_4.js](javascript/approach_4.js) |
| 5    | [approach_5.js](javascript/approach_5.js) |

---

## 📝 Notes

- Approach 2 is the most practical solution for this problem. 

---

## 📅 Day 01

_This solution is part of my [#FlexYourCode](https://www.instagram.com/yourpage/) series where I post daily coding challenges in Python & JavaScript._
