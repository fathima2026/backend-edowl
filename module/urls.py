from django.urls import path
from . import views
urlpatterns = [


    path('module/', views.ModuleList.as_view()),
    path('module/<int:pk>/', views.ModuleDetail.as_view()),

    path('teacher-module/<int:teacher_id>/', views.TeacherModuleList.as_view()),
   
   #course detail teacher
    path('teacher-module-detail/<int:pk>', views.TeacherModuleDetail.as_view()),

    path('topic/', views.TopicList.as_view()),
    
    path('topic/<int:pk>/', views.TopicDetailView.as_view()),

    path('module-topic/<int:module_id>/', views.ModuleTopicList.as_view()),

   


   #fetching course according to the code
   path('enroll/<str:module_code>/',views.Enrollment.as_view()),

   #enrolling into the course
    path('enrolled-module/', views.EnrollModule.as_view()),
 
    
    #fetch weather student enrolled into course already
    path('fetch-enroll-status/<int:student_id>/<int:course_id>',views.fetch_enroll_status),

    #fetch students courses
    path('student-module/<int:student_id>/', views.EnrolledModuleList.as_view()),

   #FETCH ENROLLED STUDENTS OF A SPECIFIC COURSE

     path('fetch-enroll-students/<int:course_id>',views.EnrolledStudentList.as_view()),

   #post new assignment    
    path('assignment/', views.AssignmentList.as_view()),

   #fetch all assignments for a module
    path('module-assignment/<int:module_id>/', views.ModuleAssignmentList.as_view()),
     
    #assignment detail
    path('assignment/<int:pk>/', views.AssignmentDetail.as_view()),

    path('teacher-assignment-detail/<int:pk>', views.AssignmentDetail.as_view()),

    #assignment fetch weather already submitted

    path('fetch-submission-status/<int:student_id>/<int:assignment_id>',views.fetch_submission_status),
    
    #submit assignment

    path('submit-assignment/', views.AssignmentSubmissionList.as_view()),

    #Fetch all submissions for an assignment
    path('assignment-submissions/<int:assignment_id>/', views.SubmissionAssignment.as_view()),

    #fetch individual submissions

    path('submissions/<int:pk>/', views.SubmissionDetail.as_view()),
   
    #path to show a student his/her submission details
   
    path('assignment-submissions/<int:student_id>/<int:assignment_id>',views.FetchSubmission.as_view()),

    #path to create a quiz and update the quiz details

    path('quiz/', views.QuizList.as_view()),

    #path to fetch quiz using module id

    path('module-quiz/<int:module_id>/', views.ModuleQuizList.as_view()),

    #quiz detail
    path('quiz/<int:pk>/', views.QuizDetail.as_view()),

    #Fetch all submissions for an quiz
    path('quiz-submissions/<int:quiz_id>/', views.SubmissionQuiz.as_view()),

    #path to submit quiz and update the quiz 

    path('submit-quiz/', views.QuizSubmissionList.as_view()),

    #path to fetch if quiz already submitted
    path('fetch-quiz-status/<int:student_id>/<int:quiz_id>',views.fetch_quiz_status),

    #path to show a student his/her quiz details //not implemented yet
   
    path('quiz-submissions/<int:student_id>/<int:quiz_id>',views.FetchSubmission.as_view()),

    #path to create a hangman and update the hangman details

    path('hangman/', views.HangmanList.as_view()),

    #path to fetch hangman using module id

    path('module-hangman/<int:module_id>/', views.ModuleHangmanList.as_view()),

    #hangman detail
    path('hangman/<int:pk>/', views.HangmanDetail.as_view()),

    #path to submit hangman and update the hangman 

    path('submit-hangman/', views.HangmanSubmissionList.as_view()),

    #path to fetch if hangman already submitted
    path('fetch-hangman-status/<int:student_id>/<int:hangman_id>',views.fetch_hangman_status),

    #Fetch all submissions for an hangman
    path('hangman-submissions/<int:hangman_id>/', views.SubmissionHangman.as_view()),

    #path to show a student his/her hangman details
   
    path('hangman-submissions/<int:student_id>/<int:hangman_id>',views.FetchSubmissionHangman.as_view()),

    path('hangman-rank/<int:hangman_id>',views.FetchHangmanRank),
    
    path('rank/<int:module_id>',views.FetchRank),
    path('remove-student-from-course/', views.remove_student_from_course, name='remove_student_from_course'),





]
