def add(a, b):
    return a - b  # lỗi ở đây, đúng ra phải là `a + b`

if __name__ == "__main__":
    result = add(2, 3)
    print(f"Result: {result}")