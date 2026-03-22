from django.shortcuts import render, redirect, get_object_or_404
from .models import Candidate, Role, Match, Prediction
from .forms import ResumeUploadForm
from .ml_utils import extract_text_from_file, get_rule_based_matches, get_ml_predictions, extract_candidate_name
import os

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    roles = Role.objects.all()
    role_id = request.GET.get('role')
    sort_order = request.GET.get('sort', 'desc')
    
    context = {'roles': roles}
    
    if role_id:
        # Filter by role using the Match objects
        matches = Match.objects.filter(role_id=role_id)
        if sort_order == 'asc':
            matches = matches.order_by('match_percentage')
        else:
            matches = matches.order_by('-match_percentage')
        
        context['matches'] = matches
        context['selected_role'] = int(role_id)
        context['selected_sort'] = sort_order
    else:
        # Default view: all candidates
        candidates = Candidate.objects.all().order_by('-created_at')
        context['candidates'] = candidates
        
    return render(request, 'dashboard.html', context)

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.save()
            
            # Process Resume
            file_path = candidate.resume_file.path
            extracted_text = extract_text_from_file(file_path)
            candidate.extracted_text = extracted_text
            
            # AUTOMATED NAME EXTRACTION
            candidate.name = extract_candidate_name(extracted_text, os.path.basename(file_path))
            candidate.save()
            
            # Matching Logic (Stored in DB)
            roles = Role.objects.all()
            rule_matches = get_rule_based_matches(extracted_text, roles)
            
            for m in rule_matches:
                Match.objects.create(
                    candidate=candidate,
                    role=m['role'],
                    match_percentage=m['match_percentage'],
                    fit_category=m['fit_category']
                )
            
            # ML Predictions
            ml_results = get_ml_predictions(extracted_text)
            if ml_results:
                Prediction.objects.create(
                    candidate=candidate,
                    top_role_1=ml_results[0][0],
                    score_1=ml_results[0][1],
                    top_role_2=ml_results[1][0] if len(ml_results) > 1 else "",
                    score_2=ml_results[1][1] if len(ml_results) > 1 else 0,
                    top_role_3=ml_results[2][0] if len(ml_results) > 2 else "",
                    score_3=ml_results[2][1] if len(ml_results) > 2 else 0
                )
                
            return redirect('candidate_detail', pk=candidate.pk)
    else:
        form = ResumeUploadForm()
    return render(request, 'upload.html', {'form': form})

def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    roles = Role.objects.all()
    detailed_matches = get_rule_based_matches(candidate.extracted_text, roles)
    detailed_matches.sort(key=lambda x: x['match_percentage'], reverse=True)
    
    prediction = Prediction.objects.filter(candidate=candidate).first()
    
    return render(request, 'candidate_detail.html', {
        'candidate': candidate,
        'matches': detailed_matches,
        'prediction': prediction
    })

def rename_candidate(request, pk):
    if request.method == 'POST':
        candidate = get_object_or_404(Candidate, pk=pk)
        new_name = request.POST.get('name')
        if new_name:
            candidate.name = new_name
            candidate.save()
    return redirect('candidate_detail', pk=pk)

def delete_candidate(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if candidate.resume_file:
        if os.path.exists(candidate.resume_file.path):
            os.remove(candidate.resume_file.path)
    candidate.delete()
    return redirect('dashboard')
