# Image-Based Expression Evaluation

## Project Overview
This project calculates the value of a mathematical expression based on an image that is drawn. Users can draw an expression, and the program processes the image to evaluate the mathematical result. The system is built using image processing techniques and mathematical expression parsing.

## Features
- **Image Input**: Draw or upload images containing mathematical expressions.
- **Image Processing**: Use image processing techniques to recognize and interpret the mathematical symbols and numbers in the image.
- **Expression Evaluation**: Evaluate the interpreted expression and return the calculated value.

## Technologies Used
# Python Libraries Overview

Below is an introduction to some essential Python libraries commonly used in machine learning, image processing, and data manipulation.

## 1. TensorFlow
**TensorFlow** is an open-source deep learning framework developed by Google. It enables fast and flexible development of machine learning models, especially deep neural networks, by providing a comprehensive suite of tools, such as Keras for high-level APIs, and TensorFlow Serving for model deployment. TensorFlow is widely used in areas such as computer vision, natural language processing, and reinforcement learning.

## 2. OpenCV (cv2)
**OpenCV (cv2)** is an open-source computer vision library that provides tools and functionalities for real-time image and video processing. It includes methods for image manipulation, feature detection, object tracking, and more. OpenCV is highly optimized and supports integration with deep learning frameworks, making it ideal for building image processing and computer vision applications.

## 3. os
The **os** module in Python provides a way to interact with the operating system. It allows users to perform operations such as file and directory manipulation, environment variable access, and path management. The os module is particularly useful for handling files and directories in a project, making it easier to manage data across different environments.

## 4. NumPy
**NumPy** is a fundamental library for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a comprehensive collection of mathematical functions to operate on these arrays. NumPy is a core dependency for many other scientific libraries, offering a high-performance tool for array-based data manipulation.

## 5. PIL (Pillow)
**Pillow (PIL)** is a Python Imaging Library that adds image processing capabilities to Python. It allows for opening, manipulating, and saving different image file formats. Pillow is often used for tasks such as resizing, cropping, filtering, and transforming images in a simple and efficient manner.

## 6. Scikit-Learn’s PCA
`sklearn.decomposition.PCA` is part of the **scikit-learn** library and is used for **Principal Component Analysis (PCA)**, a statistical method that reduces the dimensionality of datasets while retaining the most important features. PCA is frequently used for noise reduction, data visualization, and as a preprocessing step before training machine learning models.

## 7. pandas
**pandas** is a powerful data manipulation and analysis library for Python. It provides data structures, such as DataFrames, for handling tabular data. With pandas, you can perform operations like filtering, merging, grouping, and pivoting data, making it an essential tool for data cleaning and preprocessing.

## 8. Flask
**Flask** is a lightweight framework for web development, especially building RESTful APIs. Flask allows you to build simple web applications and can be extended with other utilities as needed.
## 9. Scikit-Learn Modules for Model Training and Evaluation
- **`sklearn.model_selection.train_test_split`**: A utility function for splitting datasets into training and testing sets. It ensures the model is trained and evaluated on separate data for reliable performance assessment.
  
- **`sklearn.ensemble.AdaBoostClassifier`**: An implementation of the **AdaBoost** algorithm, a popular ensemble learning method that combines multiple weak classifiers to form a strong classifier. It is used widely for binary and multiclass classification tasks.

- **`sklearn.preprocessing.LabelEncoder`**: This class is used to convert categorical labels into a numerical format that can be used by machine learning models, making it ideal for handling labeled datasets with non-numeric target labels.

- **`sklearn.metrics.accuracy_score` and `classification_report`**: These functions provide tools to evaluate model performance. `accuracy_score` computes the percentage of correct predictions, while `classification_report` provides detailed metrics like precision, recall, and F1-score for each class, giving insights into the model's strengths and weaknesses.


## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Install the required Python packages:
  ```bash
  pip install opencv-python numpy sympy
  python3 -m pip install tensorflow
  pip install pillow
  pip install flask
  pip install scikit-learn
  pip install pandas
### Run app
  ```bash
  git clone https://github.com/kocojo/image-computer/
  cd image-computer
  python app.py
  ```
Open web browser and connect to http://127.0.0.1:5000
## Data processing 
  ### Data sourse
  Image data is taken from https://www.kaggle.com/datasets/xainano/handwrittenmathsymbols and delete some unnecessary labels
  It has 220300 images and 29 labels 
  ### Data processing 
  The image is reduced from 45x45 to 10 dimensions using PCA and saved in the file outpur_csv.csv
## Model evaluation
   ### Confusion matrix
   ![output](https://github.com/user-attachments/assets/c261d217-12c9-4565-8e54-69622c05cea1)
   ### F1 score for each class
   ![output1](https://github.com/user-attachments/assets/fbe044e5-1c94-4cf2-8b94-4742e32905af)
   ### Recall for each class
   ![output2](https://github.com/user-attachments/assets/010d3a0e-4fbd-44ce-8e94-5fe5591942b6)
## Computer vision processing flow chart 

  ![output](https://github.com/user-attachments/assets/fa6fff38-709b-4d40-912a-1fc81f7ddbc9)
## Handle the position of each mathematical character
  ![Untitled drawio (1)](https://github.com/user-attachments/assets/a28f1520-d2b4-4582-8c1a-f46cff7cd129)



   
