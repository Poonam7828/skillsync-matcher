# Resume Matching Engine

A Django-based application designed to match candidate resumes with internship roles. The system uses a combination of rule-based skill matching and machine learning (Logistic Regression) to predict the best fit for each candidate.

## Key Features

- **Automated Text Extraction**: Supports extracting text from PDF and DOCX resume formats.
- **Rule-Based Matching**: Compares candidate skills against required role skills with a percentage-based fit analysis.
- **ML Role Prediction**: Utilizes a trained Logistic Regression model to predict the top 3 most suitable internship roles.
- **Candidate Management**: Stores candidate profiles, extracted skills, and match results in a local SQLite database.

## Prerequisites

Ensure you have Python installed. The project dependencies are listed in `requirements.txt`.

## Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Database Migrations**:
   Initialize the database schema:
   ```bash
   python manage.py migrate
   ```

3. **Populate Roles**:
   Load initial internship roles and required skills from the dataset:
   ```bash
   python populate_roles.py
   ```

4. **Generate ML Assets**:
   Prepare the model features and encoder classes for the matching engine:
   ```bash
   python generate_ml_assets.py
   ```

## Running the Application

1. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

2. **Test ML Predictions**:
   Run a standalone test script to verify ML functionality:
   ```bash
   python test_ml.py
   ```

## Project Structure

- `matching_engine/`: Main Django project configuration.
- `matching_app/`: Application logic, models, and utility functions for text extraction and matching.
- `resume_data_ml_models/`: Contains model binaries (`.pkl`), datasets, and asset generation scripts.
- `media/resumes/`: Default directory for uploaded resume files.
- `templates/`: HTML templates for the web interface.
