# Code Reviewer Project

A Flask-based web application that provides AI-powered code review and analysis using Google's Gemini AI.

## Features

- User authentication and registration
- Code submission and analysis
- AI-powered code review with Gemini
- Programming language detection
- Code quality scoring
- Plagiarism detection hints
- Submission history tracking

## Tech Stack

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Database**: PostgreSQL (production), SQLite (development)
- **AI**: Google Gemini AI
- **Deployment**: Railway
- **WSGI Server**: Gunicorn

## Local Development

### Prerequisites

- Python 3.11+
- pip
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd codereviewer-project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your actual values
   ```

5. **Initialize database**
   ```bash
   python manage.py init-db
   python manage.py migrate-db
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

The application will be available at `http://localhost:5000`

## Deployment to Railway

### Prerequisites

- Railway account
- GitHub repository with your code
- Google Gemini API key

### Deployment Steps

1. **Prepare your repository**
   - Ensure all files are committed to GitHub
   - Verify `requirements.txt`, `Procfile`, and `runtime.txt` are present

2. **Deploy to Railway**
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub repo"
   - Connect your GitHub account and select your repository
   - Railway will automatically detect it's a Python project

3. **Configure Environment Variables**
   In Railway dashboard, add these variables:
   ```
   SECRET_KEY=your-super-secret-key-here
   FLASK_ENV=production
   GEMINI_API_KEY=your-gemini-api-key-here
   ```

4. **Set up Database**
   - In Railway dashboard, click "New" → "Database" → "PostgreSQL"
   - Railway will automatically set `DATABASE_URL`

5. **Run Database Setup**
   - Go to your project's "Settings" → "Variables"
   - Add a custom domain if needed
   - The app will automatically create tables on first run

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Flask secret key for sessions | Yes |
| `FLASK_ENV` | Environment (production/development) | Yes |
| `DATABASE_URL` | PostgreSQL connection string | Auto-set by Railway |
| `GEMINI_API_KEY` | Google Gemini API key | Yes |
| `PORT` | Port for the application | Auto-set by Railway |

### Management Commands

```bash
# Initialize database
python manage.py init-db

# Run migrations
python manage.py migrate-db

# Create admin user
python manage.py create-admin

# Setup for deployment
python manage.py deploy-setup
```

## Project Structure

```
codereviewer-project/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── routes/              # Route blueprints
│   │   ├── auth.py          # Authentication routes
│   │   ├── dashboard.py     # Dashboard routes
│   │   └── code.py          # Code submission routes
│   ├── templates/           # HTML templates
│   └── utils/
│       └── ai_utils.py      # AI analysis utilities
├── instance/
│   └── config.py            # Configuration
├── migrations/              # Database migrations
├── requirements.txt         # Python dependencies
├── Procfile                # Railway deployment config
├── runtime.txt             # Python version
├── railway.json            # Railway configuration
├── manage.py               # Management commands
└── run.py                  # Application entry point
```

## API Endpoints

- `GET /` - Home page
- `GET /login` - Login page
- `POST /login` - Login form submission
- `GET /register` - Registration page
- `POST /register` - Registration form submission
- `GET /dashboard` - User dashboard
- `GET /submit` - Code submission page
- `POST /submit` - Submit code for analysis
- `GET /history` - Submission history
- `GET /feedback/<id>` - View specific feedback

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support, please open an issue in the GitHub repository. 