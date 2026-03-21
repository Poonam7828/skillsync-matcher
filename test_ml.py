import os
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_engine.settings')
django.setup()

from matching_app.ml_utils import get_ml_predictions

# Sample text for testing
sample_text = "Experienced in python, sql, and machine learning. Familiar with excel and power bi."

print("Testing ML Predictions...")
predictions = get_ml_predictions(sample_text)

if predictions:
    print("Predictions found:")
    for role, score in predictions:
        print(f"- {role}: {score:.2f}%")
else:
    print("No predictions found or error occurred.")
