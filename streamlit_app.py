import streamlit as st
from app import check_spirit_animal  # Import the function from your Flask app

def main():
	st.title("Spirit Animal Checker")

	st.write("Enter your details to find out your spirit animal.")

	date = st.text_input("Enter your birth date (DD-MM-YYYY):")
	full_name = st.text_input("Enter your full name:")

	if st.button("Check Spirit Animal"):
		if date and full_name:
			spirit_animal = check_spirit_animal(date, full_name)
			st.success(f"{spirit_animal}")
		else:
			st.error("Please enter both your birth date and full name.")

if __name__ == "__main__":
	main()