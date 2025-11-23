import re
import math

def calculate_entropy(password):
    """
    Calculates Shannon Entropy to measure password unpredictability.
    Formula: H = L * log2(N)
    """
    pool_size = 0
    if re.search(r'[a-z]', password): pool_size += 26
    if re.search(r'[A-Z]', password): pool_size += 26
    if re.search(r'[0-9]', password): pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password): pool_size += 32

    if pool_size == 0:
        return 0
    
    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Basic Length Check
    if len(password) < 8:
        feedback.append("[-] Password is too short (min 8 chars).")
    else:
        score += 1
        feedback.append("[+] Good length.")

    # Complexity Check
    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("[-] Add uppercase letters (A-Z).")
    
    if re.search(r"[0-9]", password): score += 1
    else: feedback.append("[-] Add numbers (0-9).")
    
    if re.search(r"[!@#$%^&*]", password): score += 1
    else: feedback.append("[-] Add special characters (!@#$%).")

    # Advanced Entropy Calculation
    entropy = calculate_entropy(password)
    
    print(f"\n--- Analysis Report for: {password} ---")
    print(f"Entropy Score: {entropy} bits")
    
    if entropy < 40:
        print(">> Result: WEAK 🔴 (Vulnerable to brute-force)")
    elif entropy < 60:
        print(">> Result: MODERATE 🟡")
    else:
        print(">> Result: STRONG 🟢 (High Resistance)")

    print("Details:")
    for item in feedback:
        print(item)

if __name__ == "__main__":
    print("Welcome to SentinelPass - Developed by Aiman Mansor")
    print("Type 'exit' to quit.")
    
    while True:
        user_pass = input("\nEnter password to analyze: ")
        if user_pass.lower() == 'exit':
            break
        check_password_strength(user_pass)
