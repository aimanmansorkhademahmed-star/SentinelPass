# SentinelPass: Smart Password Strength Analysis Tool

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)]()
[![Status](https://img.shields.io/badge/Status-V1.0%20(Initial)-orange.svg)]()

##  Executive Summary for Scholarship Applications

I developed **SentinelPass** as a dedicated security analysis tool written entirely in **Python** to address the critical risk posed by weak and compromised passwords. The project's core mission is to enable secure, local (on-premise) analysis of password lists, focusing on **detecting complex, predictable patterns** rather than just arbitrary length or character mix.

This project serves as tangible evidence of my ability to transition theoretical knowledge into practical, functional security tools, highlighting my passion and technical readiness for advanced studies in Cybersecurity and Computer Science.

##  Technical Structure and Key Features

### 1. Core Technology

The project is built using **Python 3.x** and relies on essential security and data-handling libraries:

* **hashlib:** Utilized for fast and secure hashing of passwords before analysis to ensure user privacy.
* **re (Regular Expressions):** Employed for advanced pattern matching to detect common, predictable sequences and weak structures.
* **collections:** Used for efficient processing of large lists of strings and optimizing the overall analysis speed.

### 2. Main Capabilities

* **Custom Pattern Detection:** Identifies complex, non-random patterns (e.g., repeating dates, keyboard sequences, common dictionary words).
* **Strength Scoring Algorithm:** Implements a logical algorithm to assign a measurable strength score, moving beyond simple character counts.
* **Command-Line Interface (CLI):** Designed for straightforward, efficient operation from the terminal.
* **Detailed Output:** Provides clear analysis reports indicating the specific weaknesses found in the submitted list.

---

##  Challenges and Learned Lessons (Crucial for Grant Committees)

Developing SentinelPass was a demanding and rewarding process. The challenges encountered were instrumental in shaping my current technical skill set.

### Key Challenges Faced:

1.  **Optimization for Large Datasets:** The primary challenge was optimizing the analysis algorithms to process very large lists of passwords without running into memory overflow issues or excessive execution time.
2.  **Algorithm Design Logic:** Structuring the custom strength-scoring algorithm to be fair and accurate—especially balancing long, complex-looking passwords that were still based on simple, predictable patterns.

### Technical and Personal Growth:

* **Mastering Data Structures:** This project forced me to practically implement **Hash Tables** to achieve significant performance improvements, directly lowering the overall **Time Complexity** of the analysis.
* **Code Efficiency:** I gained profound insight into the importance of writing clean, memory-efficient Python code suitable for security analysis applications.
* **Problem-Solving:** The iterative process of debugging and refining the pattern detection logic cemented my abilities in complex technical problem-solving.

---

##  Installation and Usage Guide

### 1. Prerequisites

* Python 3.x or later.

### 2. Setup

Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/Aiman-Khadem/SentinelPass](https://github.com/Aiman-Khadem/SentinelPass)
cd SentinelPass
pip install -r requirements.txt
