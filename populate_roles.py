import os
import pandas as pd
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_engine.settings')
django.setup()

from django.conf import settings

from matching_app.models import Role

def populate_roles():
    file_path = os.path.join(settings.BASE_DIR, 'resume_data_ml_models', 'dataset', 'role_skill_matrix.xlsx')
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        name = row['Role']
        skills = row['Required_Skills']
        role, created = Role.objects.get_or_create(name=name, defaults={'required_skills': skills})
        if not created:
            role.required_skills = skills
            role.save()
            print(f"Updated role: {name}")
        else:
            print(f"Created role: {name}")

if __name__ == "__main__":
    populate_roles()
