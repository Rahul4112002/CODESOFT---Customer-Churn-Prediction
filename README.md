

https://github.com/Rahul4112002/CODESOFT---Customer-Churn-Prediction/assets/124488758/a89db6b1-a8bf-4011-a004-2b3e5b49b45b
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

### Model Screenshots

I've included screenshots from my Jupyter Notebook to showcase various aspects of the model's performance and insights.
![2](https://github.com/Rahul4112002/CODESOFT---Customer-Churn-Prediction/assets/124488758/92c5f04a-d205-4cb8-8139-f4496468a606)


#### Feature Importance
![1 1](https://github.com/Rahul4112002/CODESOFT---Customer-Churn-Prediction/assets/124488758/17a18ffe-db48-44ed-83f3-3432b2ace379)
![1 2](https://github.com/Rahul4112002/CODESOFT---Customer-Churn-Prediction/assets/124488758/94777302-fbfd-4c58-8b39-4dc358cbf3e4)
![1 3](https://github.com/Rahul4112002/CODESOFT---Customer-Churn-Prediction/assets/124488758/dd558bef-8c3a-45a4-8575-5424f1d546f8)

This screenshot demonstrates the feature importance plot generated from the Random Forest model, highlighting the key factors influencing customer churn prediction.
![3 2](https://github.com/Rahul4112002/CODESOFT---Customer-Churn-Prediction/assets/124488758/6bfc08c1-9a44-411c-9a0f-26ead5fd82cc)
![3 1](https://github.com/Rahul4112002/CODESOFT---Customer-Churn-Prediction/assets/124488758/990f0c0b-955b-40b1-8fc0-fef9e684a5db)

#### Model Evaluation Metrics

Here's a snapshot showcasing the evaluation metrics such as accuracy of the trained model on the test dataset.
![3](https://github.com/Rahul4112002/CODESOFT---Customer-Churn-Prediction/assets/124488758/052c0cb1-e2cc-4638-9016-5b9b25eed276)

