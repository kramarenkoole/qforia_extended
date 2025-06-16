# qforia_extended
Qforia Best For specific Industry's Respect to wordlift and IPULL RANK

# Qforia - AI Query Fan-Out Simulator

A powerful Streamlit application that simulates Google's AI Mode query fan-out process for generative search systems using Google's Gemini AI.

## 🌟 Features

- **Advanced Query Expansion**: Generate 10-30+ related queries from a single input
- **Dual Mode Operation**: 
  - AI Overview (Simple): 10+ focused queries for quick insights
  - AI Mode (Complex): 20+ comprehensive queries for deep analysis
- **Beautiful UI**: Enhanced with custom CSS for better visibility and user experience
- **Query Analysis**: Categorizes queries by type (reformulations, related, implicit, comparative, entity expansions, personalized)
- **Export Options**: Download results as CSV or JSON
- **Real-time Processing**: Powered by Google Gemini AI

## 🚀 Live Demo

[Deploy your own instance on Streamlit Cloud](#deployment)

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

## 🛠️ Local Installation

1. Clone this repository:
```bash
git clone https://github.com/Pacamaraprogress/qforia_extended.git
cd qforia_extended
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 🔧 Configuration

1. Enter your Google Gemini API Key in the sidebar
2. Input your query in the text area
3. Select your preferred search mode
4. Click "Run Fan-Out Analysis" to generate expanded queries

## 📊 Query Types Generated

The application generates six types of queries:

1. **Reformulations**: Alternative ways to phrase the original query
2. **Related Queries**: Queries about related topics or concepts
3. **Implicit Queries**: Queries that address unstated but implied needs
4. **Comparative Queries**: Queries that compare options or alternatives
5. **Entity Expansions**: Queries that expand on specific entities mentioned
6. **Personalized Queries**: Queries tailored to different user contexts

## 🌐 Deployment on Streamlit Cloud

### Method 1: Direct GitHub Deployment

1. Fork this repository to your GitHub account
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Connect your GitHub account
5. Select your forked repository
6. Set the main file path to `app.py`
7. Click "Deploy"

### Method 2: Manual Upload

1. Download all files from this repository
2. Create a new repository on GitHub
3. Upload the files to your repository
4. Follow the steps in Method 1

## 🔐 Environment Variables

For production deployment, you can set the following environment variables:

- `GEMINI_API_KEY`: Your Google Gemini API key (optional, can be entered in the UI)

## 📁 Project Structure

```
qforia-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit configuration
└── README.md             # This file
```

## 🎨 Customization

The application includes extensive custom CSS for enhanced visual appeal. You can modify the styling by editing the `load_custom_css()` function in `app.py`.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for powering the query generation
- Streamlit for the amazing web app framework
- The open-source community for inspiration and tools

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Pacamaraprogress/qforia_extended/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the issue

---

**Made with ❤️ using Streamlit and Google Gemini AI**


