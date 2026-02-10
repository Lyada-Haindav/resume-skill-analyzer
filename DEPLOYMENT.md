# Deployment Guide: AI Resume Skill Gap Analyzer

## Why Not Vercel?

This project is built with **Streamlit**, which requires persistent WebSocket connections and long-running processes. **Vercel** runs serverless functions with execution time limits and does not support Streamlit's architecture natively.

## Recommended: Streamlit Community Cloud (Free)

Streamlit Community Cloud is purpose-built for Streamlit apps and offers free hosting with automatic deployments from GitHub.

### Prerequisites

1. Push your code to a **GitHub** repository
2. Create an account at [share.streamlit.io](https://share.streamlit.io)

### Deployment Steps

1. **Push to GitHub** (if not already):
   ```bash
   cd /Users/haindavlyada/nlpp
   git init
   git add .
   git commit -m "Initial commit - Resume Skill Analyzer"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click **"New app"**
   - Select your repository, branch (`main`), and set:
     - **Main file path**: `resume_skill_analyzer/app.py`
   - Click **"Deploy!"**

3. **Wait for build** – The first deploy may take 2–5 minutes (NLTK downloads data automatically).

4. **Your app will be live** at `https://YOUR_APP_NAME.streamlit.app`

### Automatic Updates

Every push to your `main` branch will trigger a new deployment.

---

## Alternative Platforms

| Platform | Pros | Cons |
|----------|------|------|
| **Streamlit Cloud** | Free, native support, easy setup | Limited to Streamlit |
| **Railway** | Supports any Python app, easy deploy | Free tier has limits |
| **Render** | Free tier, supports Streamlit | Slower cold starts |
| **Hugging Face Spaces** | Free, ML-focused | Different workflow |

### Deploy on Railway

1. Connect your GitHub repo at [railway.app](https://railway.app)
2. Add a new project from repo
3. Set start command: `streamlit run resume_skill_analyzer/app.py --server.port $PORT`
4. Add a `Procfile` or configure in Railway dashboard

### Deploy on Render

1. Create a [render.com](https://render.com) account
2. New → Web Service → Connect repo
3. Build command: `pip install -r resume_skill_analyzer/requirements.txt`
4. Start command: `streamlit run resume_skill_analyzer/app.py --server.port $PORT --server.address 0.0.0.0`

---

## If You Need Vercel Specifically

To use Vercel, you would need to **rebuild the app**:

- **Frontend**: Next.js or React
- **Backend**: Python API routes (Vercel serverless functions) for skill extraction and analysis

This would be a substantial rewrite. For a Streamlit app, Streamlit Community Cloud is the simpler and more suitable option.
