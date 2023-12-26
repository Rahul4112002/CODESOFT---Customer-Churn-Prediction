Customer Churn Prediction

## Overview
Machine learning project aimed at predicting customer churn in a bank using the Random Forest algorithm. The project employs a Flask-based web application to provide a user-friendly interface for predicting customer churn based on provided input data.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Installation
To use this project locally, follow these steps:
1. Clone the repository:
   ```
   git clone https://github.com/Rahul4112002/CODESOFT---Customer-Churn-Prediction.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```
   python app.py
   ```
4. Access the web application in your browser at `http://127.0.0.1:5000`.

## Usage
The web application allows users to input customer data (such as credit score, age, tenure, balance, etc.) and get predictions regarding customer churn. Users can input their data via the web interface and receive predictions in real-time.

To predict churn:
1. Fill in the required fields with customer information.
2. Click on the "Predict" button.
3. The application will generate a churn prediction based on the input data using the Random Forest algorithm.

## Project Structure
The project structure is organized as follows:
- `app.py`: Flask application handling web requests and model predictions.
- `templates/`: Contains HTML templates for the web interface.
- `static/`: Includes static files (CSS, images) for the web application.
- `model/`: Contains the trained Random Forest model for churn prediction.
- `data/`: Data used for training and testing the model.

## Dependencies
- Python 3.x
- Flask
- Pandas
- Scikit-learn
- ... (Other dependencies are listed in `requirements.txt`)

## Contributing
Contributions to improve the project are welcome! Here's how you can contribute:
- Fork the repository
- Create a new branch (`git checkout -b feature`)
- Make modifications and commit changes (`git commit -am 'Add new feature'`)
- Push changes to the branch (`git push origin feature`)
- Create a pull request

Feel free to modify this README file to include more specific instructions, additional details about the model, or any other relevant information about your project. Good luck with your project!
