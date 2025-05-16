<h1>🧠 CRM Django Project</h1>
<p>A fully-featured <strong>Customer Relationship Management (CRM)</strong> system built with <strong>Django</strong>, <strong>PostgreSQL</strong>, and <strong>Docker</strong>. This application helps businesses manage their <strong>contacts, leads, deals, tasks</strong>, and <strong>user accounts</strong> through an intuitive and responsive dashboard.</p>

  <hr>

  <h2>🚀 Live Demo</h2>
  <p>Deployed on <strong>AWS EC2</strong> using <strong>Docker</strong> and <strong>GitHub Actions CI/CD</strong> pipeline.</p>
  <p><a href="http://43.204.150.89:8000/" target="_blank">🔗 http://43.204.150.89:8000/</a></p>

  <hr>

  <h2>📦 Tech Stack</h2>
  <ul>
    <li><strong>Backend:</strong> Django 4.x</li>
    <li><strong>Frontend:</strong> HTML5, TailwindCSS, JavaScript</li>
    <li><strong>Database:</strong> PostgreSQL</li>
    <li><strong>DevOps:</strong> Docker, Docker Compose, GitHub Actions</li>
    <li><strong>Hosting:</strong> AWS EC2</li>
  </ul>

  <hr>

  <h2>📁 Project Structure</h2>
  <pre>
accounts/            - User registration, login, and profile management
contacts/            - Contact management (CRUD)
deals/               - Deal pipeline management
leads/               - Lead tracking functionality
dashboard/           - User-specific analytics and insights
tasks/               - Task assignment and tracking
templates/           - HTML templates styled with TailwindCSS
static/js/           - JavaScript scripts
crm_project/         - Main Django settings and URL routing
.github/workflows/   - GitHub Actions CI/CD configurations
Dockerfile           - Docker build instructions
docker-compose.yml   - Docker orchestration configuration
requirements.txt     - Python project dependencies
README.md            - Project documentation
  </pre>

  <hr>

  <h2>⚙️ Installation (Development)</h2>

  <h3>1. Clone the Repository</h3>
  <pre><code>git clone https://github.com/your-username/CRM-Django-project.git
cd CRM-Django-project</code></pre>

  <h3>2. Create and Activate Virtual Environment (optional)</h3>
  <pre><code>python3 -m venv .venv
source .venv/bin/activate</code></pre>

  <h3>3. Install Dependencies</h3>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>4. Run Migrations and Create Superuser</h3>
  <pre><code>python manage.py migrate
python manage.py createsuperuser</code></pre>

  <h3>5. Run the Development Server</h3>
  <pre><code>python manage.py runserver</code></pre>

  <hr>

  <h2>🐳 Docker Setup (Production Ready)</h2>

  <h3>1. Build and Run the Containers</h3>
  <pre><code>docker-compose up --build</code></pre>

  <h3>2. Open in Browser</h3>
  <p><a href="http://localhost:8000" target="_blank">http://localhost:8000</a></p>

  <hr>

  <h2>✅ Features</h2>
  <ul>
    <li>🔐 Secure user authentication (register, login, logout)</li>
    <li>📇 Full CRUD for contacts, leads, deals, and tasks</li>
    <li>📊 Dashboard with visual insights and analytics</li>
    <li>📨 Email notifications (coming soon)</li>
    <li>🧪 Unit test coverage setup (coming soon)</li>
    <li>🔁 CI/CD pipeline with GitHub Actions</li>
  </ul>

  <hr>

  <h2>🤝 Contributing</h2>
  <p>Contributions are welcome! Follow these steps:</p>
  <ol>
    <li>Fork this repository</li>
    <li>Create a new branch: <code>git checkout -b feature/YourFeature</code></li>
    <li>Commit your changes: <code>git commit -m "Add your message here"</code></li>
    <li>Push to the branch: <code>git push origin feature/YourFeature</code></li>
    <li>Open a pull request</li>
  </ol>
  <p>For major changes, please open an issue to discuss them first.</p>

  <hr>

  <h2>📜 License</h2>
  <p>This project is licensed under the <strong>MIT License</strong>.</p>

  <hr>

  <h2>📧 Contact</h2>
  <p><strong>Muhammadjon Merzaqulov</strong></p>
  <p>Email: <a href="mailto:merzaqulov1@gmail.com">merzaqulov1@gmail.com</a></p>
  <p>LinkedIn: <a href="https://www.linkedin.com/in/muhammadjon-merzaqulov/" target="_blank">muhammadjon-merzaqulov</a></p>
  <p>GitHub: <a href="https://github.com/muhammadjon-merzaqulov" target="_blank">github.com/muhammadjon-merzaqulov</a></p>
