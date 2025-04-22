import streamlit as st

def calculate_bmi(weight_kg, height_ft, height_in):
    # Convert height to meters
    total_inches = height_ft * 12 + height_in
    height_m = total_inches * 0.0254
    bmi = weight_kg / (height_m ** 2)
    return bmi

def main():
    st.title("🧮 BMI Calculator")

    st.write("Enter your height and weight to calculate your BMI.")

    # User inputs
    weight_kg = st.number_input("Weight (kg):", min_value=1.0, step=0.1)
    height_ft = st.number_input("Height (feet):", min_value=0, step=1)
    height_in = st.number_input("Height (inches):", min_value=0, step=1)

    if st.button("Calculate BMI"):
        try:
            bmi = calculate_bmi(weight_kg, height_ft, height_in)
            st.success(f"Your BMI is: {bmi:.2f}")

            # BMI Categories
            if bmi < 18.5:
                st.info("Category: Underweight")
            elif 18.5 <= bmi < 25:
                st.info("Category: Normal weight")
            elif 25 <= bmi < 30:
                st.info("Category: Overweight")
            else:
                st.info("Category: Obesity")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
