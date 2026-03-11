# CrewAI Job Application Assistant 🤖

An **AI-powered multi-agent system built with CrewAI** that analyzes job postings, profiles candidates, automatically tailors resumes, and generates interview preparation materials.

The system uses **autonomous agents collaborating together** to simulate a real job application preparation workflow.

---

# 🚀 Features

* 🔎 **Job Posting Analysis**
  Extracts required skills, experience, and qualifications from job listings.

* 👤 **Candidate Profiling**
  Builds a comprehensive profile using resume data, GitHub activity, and personal write-ups.

* 📄 **Automated Resume Tailoring**
  Optimizes the resume to align with the job requirements.

* 🎤 **Interview Preparation**
  Generates interview questions and talking points based on the job description and tailored resume.

* 🤖 **Multi-Agent Collaboration**
  Uses multiple specialized AI agents working together using **CrewAI orchestration**.

---

# 🧠 System Architecture

The system is composed of **four AI agents**:

1. **Tech Job Researcher**
   Extracts key job requirements from job postings.

2. **Personal Profiler**
   Analyzes the candidate’s resume, GitHub profile, and personal information.

3. **Resume Strategist**
   Tailors the resume to highlight relevant skills and experience.

4. **Interview Preparer**
   Generates interview questions and discussion points.

These agents collaborate using **CrewAI task orchestration**.

---

# 📂 Project Structure

```
crewai-job-application/
│
├── README.md
├── requirements.txt
├── .env.example
├── main.py
│
├── agents/
│   └── agents.py
│
├── tasks/
│   └── tasks.py
│
├── tools/
│   └── tools.py
│
├── crew/
│   └── crew_setup.py
│
├── data/
│   └── Krithi_resume_ETL.md
│
└── outputs/
    ├── tailored_resume.md
    └── interview_materials.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/crewai-job-application.git
cd crewai-job-application
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup environment variables

Create a `.env` file in the root directory.

```
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
OPENAI_MODEL_NAME=gpt-4o
```

---

# ▶️ Running the Project

Run the main script:

```bash
python main.py
```

---

# 📊 Inputs

The system accepts the following inputs:

* **Job Posting URL**
* **GitHub Profile URL**
* **Personal Write-up**
* **Resume (MD file)**

Example:

```python
inputs = {
    "job_posting_url": "LinkedIn job URL",
    "github_url": "https://github.com/username",
    "personal_writeup": "Candidate background description"
}
```

---

# 📁 Outputs

The system generates:

| File                     | Description                            |
| ------------------------ | -------------------------------------- |
| `tailored_resume.md`     | AI-optimized resume for the job        |
| `interview_materials.md` | Interview questions and talking points |

---

# 🛠 Technologies Used

* **Python**
* **CrewAI**
* **CrewAI Tools**
* **OpenAI GPT Models**
* **Serper API**
* **Web Scraping**

---

# 🔧 Tools Used by Agents

* **SerperDevTool** – Web search
* **ScrapeWebsiteTool** – Extract job posting content
* **FileReadTool** – Read resume data
* **MDXSearchTool** – Semantic search within resume

---

# 🎯 Use Cases

* Job application automation
* Resume optimization
* Interview preparation
* AI-powered career assistants

---

# 📌 Future Improvements

* Support for **multiple job applications**
* **Resume scoring system**
* **ATS compatibility checks**
* **LinkedIn profile analysis**
* **Streamlit UI dashboard**

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Submit a pull request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ⭐ Acknowledgements

* [CrewAI](https://github.com/joaomdmoura/crewai)
* OpenAI
* Serper API

---

⭐ If you found this project useful, consider **starring the repository**!
