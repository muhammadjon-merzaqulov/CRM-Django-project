# 🧠 CRM Django Project

A fully-featured CRM (Customer Relationship Management) system built with Django, Docker, and PostgreSQL. This project helps manage contacts, leads, deals, tasks, and user accounts through an intuitive dashboard.

## 🚀 Live Demo

Deployed on AWS EC2 with Docker & GitHub Actions CI/CD pipeline.

🔗 http://43.204.150.89:8000/

---

## 📦 Tech Stack

- **Backend**: Django 4.x
- **Frontend**: HTML5, TailwindCSS, JavaScript
- **Database**: PostgreSQL
- **DevOps**: Docker, Docker Compose, GitHub Actions
- **Hosting**: AWS EC2

---

## 📁 Project Structure

```text
├── accounts/          → User registration, login, profile management
├── contacts/          → Contact CRUD functionality
├── deals/             → Deal pipeline management
├── leads/             → Lead tracking module
├── dashboard/         → User-specific dashboard & charts
├── tasks/             → Task assignment and tracking
├── templates/         → HTML templates with TailwindCSS
├── static/js/         → JavaScript files
├── crm_project/       → Main Django settings and URL routing
├── .github/workflows/ → CI/CD configuration for GitHub Actions
├── Dockerfile         → Docker image build file
├── docker-compose.yml→ Multi-container orchestration
├── requirements.txt   → Python dependencies
└── README.md          → Project overview
```
⚙️ Installation (Development)
bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/your-username/CRM-Django-project.git
cd CRM-Django-project

# 2. Create and activate virtual environment (optional)
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations and create superuser
python manage.py migrate
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
🐳 Docker Setup (Production-Ready)
bash
Copy
Edit
# 1. Build and run the containers
docker-compose up --build

# 2. Open in browser
http://localhost:8000
🔐 Admin Access
After creating a superuser, access the admin panel via:

bash
Copy
Edit
http://localhost:8000/admin
✅ Features
🔐 Secure user authentication (registration, login, logout)

📇 Full CRUD for contacts, leads, deals, and tasks

📊 Dashboard with key insights and analytics

📨 Email notifications (coming soon)

🧪 Test coverage setup (coming soon)

🌐 CI/CD pipeline with GitHub Actions

🔧 Environment Variables
Create a .env file and configure:

env
Copy
Edit
DEBUG=True
SECRET_KEY=your_secret_key
POSTGRES_DB=crm_db
POSTGRES_USER=crm_user
POSTGRES_PASSWORD=crm_pass
🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📜 License
This project is licensed under the MIT License.

📧 Contact
Muhammadjon Merzaqulov
📧 merzaqulov1@gmail.com
🔗 [[LinkedIn/GitHub Profile]](https://www.linkedin.com/in/muhammadjon-merzaqulov/)
