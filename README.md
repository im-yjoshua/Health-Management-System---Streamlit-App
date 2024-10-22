# Health Management System

Welcome to the Health Management System! This Streamlit application helps you manage your food intake and exercise routines effectively.

## Features

- **User Sign-up and Sign-in**: Users can sign up and sign in using their names.
- **Food Management**: Allows users to add and retrieve details about what they ate.
- **Exercise Management**: Allows users to add and retrieve details about their exercise routines.

## Installation

To run this application, you'll need to have Python installed along with the required libraries.

### Step-by-Step Guide:

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/im-yjoshua/Health-Management-System---Streamlit-App.git
   ```

2. **Navigate to the Project Directory:**

```
cd <Directory Name>
```

3. **Install Required Libraries:**

Make sure you have `pip` installed. Then, run:

```
pip install -r requirements.txt
```

## Running the Application

To run the Streamlit app, use the following command:

```
streamlit run main.py
```
## Usage
 
1. **Sign Up / Sign In:**  Enter your name to sign up or sign in.
2. **Food Management:**
- Select "Food Management" from the options.
- Add details about what you ate or retrieve previously entered data.
3. **Exercise Management:**
- Select "Exercise Management" from the options.
- Add details about the exercises you did or retrieve previously entered data.

## File Structure
- `app.py`: Main application file containing the Streamlit app code.
- `data/database.txt`: Stores user names for sign-in purposes.
- `<username>.food.txt`: Stores food intake data for the user.
- `<username>.workout.txt`: Stores exercise data for the user.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
 
## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the Streamlit community for providing excellent resources and support.