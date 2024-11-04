
    import streamlit as st

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

    # Streamlit UI
    st.title("Simple Calculator")

    operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

    num1 = st.number_input("Enter first number", format="%.2f")
    num2 = st.number_input("Enter second number", format="%.2f")

    if st.button("Calculate"):
        if operation == "Add":
            st.write(f"The result is: {add(num1, num2)}")
        elif operation == "Subtract":
            st.write(f"The result is: {subtract(num1, num2)}")
        elif operation == "Multiply":
            st.write(f"The result is: {multiply(num1, num2)}")
        elif operation == "Divide":
            st.write(f"The result is: {divide(num1, num2)}")
    