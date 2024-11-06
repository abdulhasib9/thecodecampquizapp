from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Exam, Quiz,Question,Option
from django.http import HttpResponse
import json
from django.core.paginator import Paginator


from django.contrib import messages


# View for submitting the quiz and showing the success page
def submit_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    total_questions = quiz.questions.count()
    correct_answers = 0
    
    # Calculate the number of correct answers
    for question in quiz.questions.all():
        selected_option_ids = request.POST.getlist(f"question{question.id}")
        correct_options = question.option_set.filter(is_correct=True).values_list('id', flat=True)

        if set(selected_option_ids) == set(correct_options):
            correct_answers += 1
    
    # Store the correct_answers and total_questions in session
    request.session['correct_answers'] = correct_answers
    request.session['total_questions'] = total_questions

    # Redirect to the success page
    return redirect('quiz_success')
# View for the success page (after quiz submission)
def quiz_success(request):
    # These values should come from the quiz attempt logic
    correct_answers = request.session.get('correct_answers', 0)
    total_questions = request.session.get('total_questions', 0)
    
    if correct_answers is None or total_questions is None:
        return HttpResponse("Quiz data not found. Please try again.", status=400)

    return render(request, 'success.html', {
        'correct_answers': correct_answers,
        'total_questions': total_questions
    })

def start_quiz(request, quiz_id, question_index=1):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    paginator = Paginator(questions, 1)  # Show one question per page
    page_obj = paginator.get_page(question_index)
    question = page_obj.object_list[0] if page_obj.object_list else None
    
    # Determine if the question has multiple correct options
    is_multiple = question.option_set.filter(is_correct=True).count() > 1 if question else False
    correct_options = question.option_set.filter(is_correct=True) if question else []
    
    return render(request, 'quiz.html', {
        'quiz': quiz,
        'question': question,
        'page_obj': page_obj,
        'is_multiple': is_multiple,
        'correct_options': correct_options,
    })



def dashboard(request):
    exams = Exam.objects.all()
    quizzes = Quiz.objects.all()
    questions = Question.objects.count()
    quiz_data = []
    for quiz in quizzes:
        quiz_data.append({
            'id': quiz.id,
            'name': quiz.name,
            'code': quiz.code,
            'exam_id': quiz.exam_id
        })

    context = {
        'exams': exams,
        'quizzes': quizzes,
        'quizzes_json': json.dumps(quiz_data),
        'questions': questions
    }
    return render(request, 'dashboard.html', context)
