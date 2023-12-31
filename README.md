Django Job Portal
Django job portal is a web application built using the Django web framework that allows employers to post job listings and job seekers to apply for jobs. The application typically includes user registration, job posting, job search, job application, employer dashboard, and job seeker dashboard

Key Features
 Key features for a Django job portal include:
1. User Authentication: Secure user registration ,login, and logout functionalities for both employers and employees
2. Job Posting: Employers can create and manage job postings, including job title, location, salary, and required qualifications.
3. Job Search: Job seekers can search for jobs using keywords and filters, such as job title, location, and industry.
4. Job Application: Employees can apply to job openings by submitting their resume and cover letter.
5. Employer Dashboard: A dashboard allows employers to view and manage their job postings and review and manage applicants.
6. Job Seeker Dashboard: A user dashboard allows job seekers to manage their job search and application process.
These features can be customized and expanded upon based on the specific requirements of the job portal.

Development Stack
Django Framework: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
Django ORM: An object-relational mapping system that simplifies database interactions.
Python: The primary programming language for the backend logic.
HTML/CSS/JavaScript/Bootstrap: For creating the frontend views and enhancing user interactivity.

Getting Started
To run the project locally, follow the instructions in the Installation section of the README file. The manage.py script provides essential commands for running the development server, applying migrations, and managing administrative tasks.

Why Django?
Django's batteries-included philosophy, coupled with its robust and well-documented features, makes it an ideal choice for developing scalable web applications. The project adheres to best practices in Django development, ensuring maintainability and readability of the codebase.

SYSTEM ARCHITECTURE
The system follows a standard Django architecture, including models, views, templates, and static files. Key components include:

Models:
1. JobPost: Represents a job listing.
2. CandidateApplications: Represents applications submitted by candidates.
3. SelectCandidateJob: Links selected candidates to specific jobs.
4. IsSortList: Records the date a user applied for a job.
5. Profile: User profile information including image, bio, qualifications, and job title.
6. Profilehr: HR profile information including image, phone number, company name, country, address, bio, and about.
7. MyApplyJobList: Records jobs applied to by candidates.


Views:
1. JobPostListView: Displays a list of available jobs.
2. applyJob: Handles job applications.
3. hrdash: HR dashboard for managing job applications.
4. acceptApplication and reject_application: Accepts or rejects job applications.
5. edit_profile: Allows users to edit their profiles.
6. edit_profilehr: Allows HR users to edit their profiles.
7. candidateHome: Displays the candidate dashboard.
8. myjoblist: Displays a list of jobs applied to by a candidate.
9. profilepage: Displays the candidate's profile.
10. edit_profile: Allows candidates to edit their profiles.
11. candidate_applications: Displays a list of job applications submitted by the candidate.
Templates:
HTML templates for rendering user interfaces.


Contribution
Contribution was mainly in groups in our group we split our selves in groups to be able to get things done faster as it was a different group that coded that handled documentation in order for everone to be useful we enforced that behaviour.


Installation
# Clone the repository
git clone https://github.com/zealizu/jobapp.git

# Navigate to the project directory
cd ecommerce-webapp

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate
Usage
Explain how users can run and interact with your eCommerce web app. Include information about starting the development server and accessing the application.

# Start the development server
python manage.py runserver
Visit http://localhost:8000 in your web browser to access the web app.

Contributing
Fork the project.
Create your feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Added some features').
Push to the branch (git push -u origin feature/YourFeature).
Open a pull request.

Testing
testing was done by users manually we had a group who searched for bugs manually it was slow but it worked.

