import pickle
import os

# Define the data seen in the ML_Models.ipynb notebook
skills_tools = [
    "python", "sql", "excel", "power bi", "tableau",
    "html", "css", "javascript", "react", "node",
    "photoshop", "figma", "illustrator", "canva",
    "marketing", "seo", "social media marketing", "content marketing",
    "communication", "recruitment", "management", "excel"
]

roles = [
    'Data Analytics Intern', 
    'Digital Marketing Intern',
    'Graphic Design Intern', 
    'HR Operations Intern',
    'Web Development Intern'
]

# Ensure output directory exists
output_dir = r"d:\Graphura\Resume_Matching_Project\Final\resume_data_ml_models\Models"
os.makedirs(output_dir, exist_ok=True)

# Save features.pkl (Unique skills only to match trained model columns)
unique_skills = []
for skill in skills_tools:
    if skill not in unique_skills:
        unique_skills.append(skill)

features_path = os.path.join(output_dir, "features.pkl")
with open(features_path, 'wb') as f:
    pickle.dump(unique_skills, f)
print(f"Generated {features_path} with {len(unique_skills)} unique features")

# Save encoder_classes.pkl
encoder_path = os.path.join(output_dir, "encoder_classes.pkl")
with open(encoder_path, 'wb') as f:
    pickle.dump(roles, f)
print(f"Generated {encoder_path}")
