# Crop Recommendation System

## Overview

The **Crop Recommendation System** is an innovative web application aimed at supporting farmers in making informed decisions about crop selection based on various agricultural parameters. By analyzing factors such as soil type, climate conditions, and land area, this system provides tailored recommendations to optimize crop yield and enhance agricultural productivity.

## Features

- **Dynamic District Selection**: The application fetches a list of districts from a dataset, allowing users to select their location effortlessly. This ensures that the recommendations are relevant to the user's specific agricultural context.

- **User-Friendly Interface**: Built with HTML, CSS, and JavaScript, the interface is designed to be intuitive and accessible, making it easy for users to input their data and receive recommendations.

- **Real-Time Crop Recommendations**: Once the user inputs their land area and selects a district, the system processes this information and provides immediate recommendations for suitable crops, along with predicted yields based on historical data.

- **Responsive Design**: The application is optimized for various devices, ensuring a seamless user experience whether accessed on a desktop, tablet, or mobile device.

## Technologies Used

- **Frontend**: 
  - HTML for structure
  - CSS for styling
  - JavaScript (with jQuery) for interactivity

- **Backend**: 
  - Flask (Python) for server-side processing and handling requests

- **Data Handling**: 
  - Pandas for data manipulation and analysis

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/crop-recommendation-system.git
   cd crop-recommendation-system
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```
   Access the application in your web browser at `http://127.0.0.1:5000`.

## Usage

After running the application, users can select their district from the dropdown menu and input the area of their land. Upon submission, the system will analyze the data and provide recommendations for the most suitable crops to plant, along with expected yields.

## Contribution

We welcome contributions from the community! If you would like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

We would like to thank our professors and peers for their support and guidance throughout this project. Your feedback has been invaluable in shaping this application.

