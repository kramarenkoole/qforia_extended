# Qforia Deployment Guide

## Quick Deployment to Streamlit Cloud

### Step 1: Prepare Your GitHub Repository

1. **Create a new repository on GitHub:**
   - Go to [GitHub](https://github.com) and sign in
   - Click the "+" icon in the top right corner
   - Select "New repository"
   - Name it `qforia-app` (or any name you prefer)
   - Make it public (required for free Streamlit Cloud)
   - Click "Create repository"

2. **Upload your files:**
   - Download all files from this project
   - Upload them to your GitHub repository using GitHub's web interface, or
   - Use Git commands if you're familiar with them

### Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

2. **Create a new app:**
   - Click "New app"
   - Select your GitHub repository (`qforia-app`)
   - Set the main file path to `app.py`
   - Click "Deploy!"

3. **Wait for deployment:**
   - Streamlit Cloud will automatically install dependencies
   - Your app will be live in a few minutes

### Step 3: Configure Your App

1. **Get a Gemini API Key:**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key

2. **Use your app:**
   - Open your deployed Streamlit app
   - Enter your Gemini API key in the sidebar
   - Start generating query fan-outs!

## Alternative Deployment Methods

### Local Development

```bash
# Clone your repository
git clone https://github.com/yourusername/qforia-app.git
cd qforia-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:

```bash
docker build -t qforia-app .
docker run -p 8501:8501 qforia-app
```

## Troubleshooting

### Common Issues

1. **"Module not found" errors:**
   - Check that all dependencies are listed in `requirements.txt`
   - Ensure the versions are compatible

2. **API key issues:**
   - Verify your Gemini API key is correct
   - Check that the API is enabled in Google Cloud Console

3. **Deployment fails:**
   - Check the logs in Streamlit Cloud
   - Ensure your repository is public
   - Verify all files are uploaded correctly

### Getting Help

- Check the [Streamlit documentation](https://docs.streamlit.io)
- Visit the [Streamlit community forum](https://discuss.streamlit.io)
- Create an issue in your GitHub repository

## Security Notes

- Never commit API keys to your repository
- Use Streamlit's secrets management for production deployments
- Consider using environment variables for sensitive data

## Performance Tips

- The app works best with queries that are specific but not too narrow
- Complex queries may take longer to process
- Consider implementing caching for frequently used queries

---

**Happy deploying! 🚀**

