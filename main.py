import streamlit as st
import datetime
import os

# Set page configuration
st.set_page_config(page_title="Health Management System")

def current_time():
    return datetime.datetime.now()

class HealthManagementSystem:
    def __init__(self, name):
        self.name = name
        self.database_path = 'data/database.txt'
        self.ensure_database_exists()

    def ensure_database_exists(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists(self.database_path):
            open(self.database_path, 'w').close()

    def sign_in(self):
        try:
            with open(self.database_path) as file:
                for line in file:
                    if self.name in line:
                        return True
            return False
        except FileNotFoundError:
            st.error("Database file not found.")
            return False

    def sign_up(self):
        if not self.sign_in():
            with open(self.database_path, 'a') as file:
                file.write(f"{self.name}\n")
            return True
        return False

    def food_management(self):
        st.subheader("Food Management")
        choice = st.radio("What do you want to do?", ("Add what you ate today", "Retrieve data"))
        if choice == "Add what you ate today":
            what_ate = st.text_input("Enter what you ate today:")
            if st.button("Submit"):
                with open(f"{self.name}.food.txt", "a") as file:
                    file.write(f"{self.name} ate {what_ate} at {current_time()}\n")
                st.success("Data added successfully!")
        elif choice == "Retrieve data":
            try:
                with open(f"{self.name}.food.txt", "r") as file:
                    data = file.read()
                st.text_area("Here's what you've added so far:", data)
            except FileNotFoundError:
                st.error("No data found.")

    def exercise_management(self):
        st.subheader("Exercise Management")
        choice = st.radio("What do you want to do?", ("Add what exercise you did", "Retrieve data"))
        if choice == "Add what exercise you did":
            what_exer = st.text_input("Enter what exercise you did:")
            if st.button("Submit"):
                with open(f"{self.name}.workout.txt", "a") as file:
                    file.write(f"{self.name} did {what_exer} at {current_time()}\n")
                st.success("Data added successfully!")
        elif choice == "Retrieve data":
            try:
                with open(f"{self.name}.workout.txt", "r") as file:
                    data = file.read()
                st.text_area("Here's what you've added so far:", data)
            except FileNotFoundError:
                st.error("No data found.")

# Streamlit interface
st.title("Health Management System")
st.write("Welcome to the Health Management System!")

name = st.text_input("Enter your name:")
if name:
    system = HealthManagementSystem(name)
    if system.sign_in() or system.sign_up():
        option = st.selectbox("What do you want to do today?", ["Food Management", "Exercise Management"])
        if option == "Food Management":
            system.food_management()
        elif option == "Exercise Management":
            system.exercise_management()
    else:
        st.error("Something went wrong with the sign-up process.")