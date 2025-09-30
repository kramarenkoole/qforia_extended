import streamlit as st
import google.generativeai as genai
import pandas as pd
import json
import re

# Custom CSS for better visibility and styling
def load_custom_css():
    st.markdown("""
    <style>
    /* Main app styling */
    .main {
        background-color: #F5F7FA; /* Lighter main background */
        padding-top: 2rem;
    }
    
    /* Header styling */
    .main-header {
        /* New primary gradient */
        background: linear-gradient(135deg, #0D47A1 0%, #4285F4 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .main-header h1 {
        color: white !important;
        text-align: center;
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    .main-header p {
        color: #E3F2FD !important; /* Lighter text for better contrast */
        text-align: center;
        font-size: 1.2rem;
        margin: 0 !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #FFFFFF; /* Clean white sidebar */
    }
    
    .sidebar-header {
        /* New accent gradient for sidebar */
        background: linear-gradient(135deg, #00796B 0%, #009688 100%);
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    
    .sidebar-header h2 {
        color: white !important;
        margin: 0 !important;
        text-align: center;
    }
    
    /* Button styling */
    .stButton > button {
        /* Matching the new primary gradient */
        background: linear-gradient(135deg, #0D47A1 0%, #4285F4 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        filter: brightness(1.1); /* Add brightness on hover */
    }
    
    /* Input field styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border: 1px solid #DEE2E6; /* Softer border */
        border-radius: 8px;
        padding: 0.75rem;
        font-size: 1rem;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #4285F4; /* New focus color */
        box-shadow: 0 0 0 3px rgba(66, 133, 244, 0.15); /* Adjusted shadow */
    }
    
    /* Radio button styling */
    .stRadio > div {
        background-color: black;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e1e5e9;
    }
    
    /* Alert styling */
    .stSuccess, .stError, .stWarning {
        border-radius: 8px;
        padding: 1rem;
        border-width: 1px;
        border-style: solid;
    }
    .stSuccess { background-color: #E8F5E9; border-color: #A5D6A7; }
    .stError { background-color: #FFEBEE; border-color: #EF9A9A; }
    .stWarning { background-color: #FFFDE7; border-color: #FFF59D; }
    
    /* DataFrame styling */
    .stDataFrame {
        border: 1px solid #DEE2E6;
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Info boxes (Replaced old gradient with a cleaner look) */
    .info-box {
        background-color: #E3F2FD; /* Light blue background */
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: #0D47A1; /* Dark blue text */
        box-shadow: none;
        border-left: 5px solid #4285F4; /* Blue accent border */
    }
    
    .info-box h3 {
        margin-top: 0 !important;
        color: #0D47A1 !important; /* Dark blue header */
    }
    
    /* Generation details box (Replaced gradient for cleaner look) */
    .generation-details {
        background-color: #E0F2F1; /* Light teal background */
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #009688; /* Teal accent border */
    }
    
    /* Download button */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #28A745 0%, #20C997 100%); /* New green gradient */
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        filter: brightness(1.1);
    }
    
    /* Spinner styling */
    .stSpinner {
        text-align: center;
    }
    
    /* Hide Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom spacing */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# App config
st.set_page_config(
    page_title="Qforia - AI Query Gemini Fan-Out Simulator", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🔍"
)

# Load custom CSS
load_custom_css()

# Main header with custom styling
st.markdown("""
<div class="main-header">
    <h1>🔍 Qforia_Extended_Omer_EVREY</h1>
    <p>Advanced Query Fan-Out Simulator for Gemini AI Search Surfaces</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with enhanced styling
st.sidebar.markdown("""
<div class="sidebar-header">
    <h2>⚙️ Configuration</h2>
</div>
""", unsafe_allow_html=True)

# API key input with better styling
gemini_key = st.secrets.get("GEMINI_API_KEY") or st.sidebar.text_input(
    "🔑 Gemini API Key", 
    type="password",
    help="Enter your Google Gemini API key to enable AI query generation"
)
# Configure Gemini
if gemini_key:
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel("gemini-2.5-pro")
else:
    st.error("🔐 Please enter your Gemini API Key to proceed.")
    st.info("💡 You can get your API key from the Google AI Studio: https://makersuite.google.com/app/apikey  ")
    st.stop()
    
# Query input with enhanced styling
user_query = st.sidebar.text_area(
    "💭 Enter your query", 
    "What's the best electric SUV for driving up mt rainier?", 
    height=120,
    help="Enter the query you want to expand and analyze"
)

# Mode selection with better styling
mode = st.sidebar.radio(
    "🎯 Search Mode", 
    ["AI Overview (simple)", "AI Mode (complex)"],
    help="Choose the complexity level for query generation"
)

# Add some information about the modes
st.sidebar.markdown("""
<div style="background-color: #f0f2f6; color: #343A40; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
    <h4 style="margin-top: 0;">Mode Information:</h4>
    <p><strong>AI Overview:</strong> Generates 10+ focused queries for quick insights</p>
    <p><strong>AI Mode:</strong> Generates 20+ comprehensive queries for deep analysis</p>
</div>
""", unsafe_allow_html=True)

# Configure Gemini
if gemini_key:
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel("gemini-2.5-pro")
else:
    st.error("🔐 Please enter your Gemini API Key to proceed.")
    st.info("💡 You can get your API key from the Google AI Studio: https://makersuite.google.com/app/apikey")
    st.stop()

# Allowed routing formats (sent to the model)
ALLOWED_FORMATS = [
    "web_article",
    "faq_page",
    "how_to_steps",
    "comparison_table",
    "buyers_guide",
    "checklist",
    "product_spec_sheet",
    "glossary/definition",
    "pricing_page",
    "review_roundup",
    "tutorial_video/transcript",
    "podcast_transcript",
    "code_samples/docs",
    "api_reference",
    "calculator/tool",
    "dataset",
    "image_gallery",
    "map/local_pack",
    "forum/qna",
    "pdf_whitepaper",
    "case_study",
    "press_release",
    "interactive_widget"
]

# Prompt with detailed Chain-of-Thought logic
def QUERY_FANOUT_PROMPT(q, mode):
    min_queries_simple = 10
    min_queries_complex = 20

    if mode == "AI Overview (simple)":
        num_queries_instruction = (
            f"First, analyze the user's query: \"{q}\". Based on its complexity and the '{mode}' mode, "
            f"**you must decide on an optimal number of queries to generate.** "
            f"This number must be **at least {min_queries_simple}**. "
            f"For a straightforward query, generating around {min_queries_simple}-{min_queries_simple + 2} queries might be sufficient. "
            f"If the query has a few distinct aspects or common follow-up questions, aim for a slightly higher number, perhaps {min_queries_simple + 3}-{min_queries_simple + 5} queries. "
            f"Provide a brief reasoning for why you chose this specific number of queries. The queries themselves should be tightly scoped and highly relevant."
        )
    else:  # AI Mode (complex)
        num_queries_instruction = (
            f"First, analyze the user's query: \"{q}\". Based on its complexity and the '{mode}' mode, "
            f"**you must decide on an optimal number of queries to generate.** "
            f"This number must be **at least {min_queries_complex}**. "
            f"For multifaceted queries requiring exploration of various angles, sub-topics, comparisons, or deeper implications, "
            f"you should generate a more comprehensive set, potentially {min_queries_complex + 5}-{min_queries_complex + 10} queries, or even more if the query is exceptionally broad or deep. "
            f"Provide a brief reasoning for why you chose this specific number of queries. The queries should be diverse and in-depth."
        )
    routing_note = (
        "For EACH expanded query, also identify the most likely CONTENT TYPE / FORMAT the routing system would prefer "
        "for retrieval and synthesis (e.g., a how-to should route to 'how_to_steps' or a video transcript; comparisons to 'comparison_table' or 'buyers_guide'). "
        "Choose exactly ONE label from this fixed list:\n"
        + ", ".join(ALLOWED_FORMATS) +
        ".\nReturn it in a field named 'routing_format' and give a short 'format_reason' (1 sentence)."
    )
    return (
        f"You are simulating Google's AI Mode query fan-out process for generative search systems.\n"
        f"The user's original query is: \"{q}\". The selected mode is: \"{mode}\".\n\n"
        f"**Your first task is to determine the total number of queries to generate and the reasoning for this number, based on the instructions below:**\n"
        f"{num_queries_instruction}\n\n"
        f"**Once you have decided on the number and the reasoning, generate exactly that many unique synthetic queries.**\n"
        "Each of the following query transformation types MUST be represented at least once in the generated set, if the total number of queries you decide to generate allows for it (e.g., if you generate 12 queries, try to include all 6 types at least once, and then add more of the relevant types):\n"
        "1. Reformulations\n2. Related Queries\n3. Implicit Queries\n4. Comparative Queries\n5. Entity Expansions\n6. Personalized Queries\n\n"
        "The 'reasoning' field for each *individual query* should explain why that specific query was generated in relation to the original query, its type, and the overall user intent.\n"
        "Do NOT include queries dependent on real-time user history or geolocation.\n\n"
        f"{routing_note}\n\n"
        "**IMPORTANT: For each query, you must also provide a 'possible_usage_in_industry' field that suggests 2-3 specific industries or business contexts where this query would be particularly valuable. Be specific and practical.**\n\n"
        "**ВАЖНО: Все ответы, включая сгенерированные запросы, намерения, рассуждения и отраслевые применения, должны быть на русском языке.**\n\n"
        "Return only a valid JSON object. The JSON object should strictly follow this format:\n"
        "{\n"
        "  \"generation_details\": {\n"
        "    \"target_query_count\": 12, // This is an EXAMPLE number; you will DETERMINE the actual number based on your analysis.\n"
        "    \"reasoning_for_count\": \"The user query was moderately complex, so I chose to generate slightly more than the minimum for a simple overview to cover key aspects like X, Y, and Z.\" // This is an EXAMPLE reasoning; provide your own.\n"
        "  },\n"
        "  \"expanded_queries\": [\n"
        "    // Array of query objects. The length of this array MUST match your 'target_query_count'.\n"
        "    {\n"
        "      \"query\": \"Пример запроса 1...\",\n"
        "      \"type\": \"reformulation\",\n"
        "      \"user_intent\": \"Пример намерения...\",\n"
        "      \"reasoning\": \"Обоснование для этого запроса...\",\n"
        "      \"possible_usage_in_industry\": \"Автомобильная промышленность для исследований, Туризм для планирования приключений, Логистика для оптимизации маршрутов\",\n"
        "      \"routing_format\": \"article\",\n"
        "      \"format_reason\": \"Предпочтительно для формата статьи.\"\n"
        "    },\n"
        "    // ... more query objects ...\n"
        "  ]\n"
        "}"
    )

# Fan-out generation function
def generate_fanout(query, mode):
    prompt = QUERY_FANOUT_PROMPT(query, mode)
    try:
        response = model.generate_content(prompt)
        json_text = response.text.strip()
        
        # Clean potential markdown code block fences
        if json_text.startswith("```json"):
            json_text = json_text[7:]
        if json_text.endswith("```"):
            json_text = json_text[:-3]
        json_text = json_text.strip()

        data = json.loads(json_text)
        generation_details = data.get("generation_details", {})
        expanded_queries = data.get("expanded_queries", [])

        # Store details for display
        st.session_state.generation_details = generation_details

        return expanded_queries
    except json.JSONDecodeError as e:
        st.error(f"🔴 Failed to parse Gemini response as JSON: {e}")
        with st.expander("🔍 View Raw Response"):
            st.text(json_text if 'json_text' in locals() else "N/A (error before json_text assignment)")
        st.session_state.generation_details = None
        return None
    except Exception as e:
        st.error(f"🔴 An unexpected error occurred during generation: {e}")
        if hasattr(response, 'text'):
            with st.expander("🔍 View Raw Response"):
                st.text(response.text)
        st.session_state.generation_details = None
        return None

# Initialize session state for generation_details if not present
if 'generation_details' not in st.session_state:
    st.session_state.generation_details = None

# Generate and display results
if st.sidebar.button("🚀 Run Fan-Out Analysis"):
    # Clear previous details
    st.session_state.generation_details = None
    
    if not user_query.strip():
        st.warning("⚠️ Please enter a query to analyze.")
    else:
        with st.spinner("🤖 Generating query fan-out using Gemini AI... This may take a moment..."):
            results = generate_fanout(user_query, mode)

        if results:  # Check if results is not None and not empty
            st.success("✅ Query fan-out analysis complete!")

            # Display the reasoning for the count if available
            if st.session_state.generation_details:
                details = st.session_state.generation_details
                generated_count = len(results)
                target_count_model = details.get('target_query_count', 'N/A')
                reasoning_model = details.get('reasoning_for_count', 'Not provided by model.')

                st.markdown("---")
                st.markdown("""
                <div class="generation-details">
                    <h3>🧠 AI Model's Query Generation Strategy</h3>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("🎯 Target Queries", target_count_model)
                with col2:
                    st.metric("✅ Generated Queries", generated_count)
                with col3:
                    match_status = "✅ Perfect" if target_count_model == generated_count else "⚠️ Variance"
                    st.metric("📊 Match Status", match_status)
                
                st.markdown(f"**🤔 Model's Reasoning:** _{reasoning_model}_")
                
                if isinstance(target_count_model, int) and target_count_model != generated_count:
                    st.warning(f"⚠️ Note: Model aimed to generate {target_count_model} queries but actually produced {generated_count}.")
                
                st.markdown("---")
            else:
                st.info("ℹ️ Generation details (target count, reasoning) were not available from the model's response.")

            # Display results in a more visually appealing way
            st.subheader("📊 Generated Query Analysis")
            
            # Create tabs for different views
            tab1, tab2, tab3 = st.tabs(["📋 All Queries", "📈 Query Types", "💾 Export Data"])
            
            with tab1:
                df = pd.DataFrame(results)
                st.dataframe(
                    df, 
                    use_container_width=True, 
                    height=(min(len(df), 20) + 1) * 35 + 3,
                    column_config={
                        "query": st.column_config.TextColumn("Query", width="large"),
                        "type": st.column_config.TextColumn("Type", width="small"),
                        "user_intent": st.column_config.TextColumn("Intent", width="medium"),
                        "reasoning": st.column_config.TextColumn("Reasoning", width="large"),
                        "possible_usage_in_industry": st.column_config.TextColumn("Possible Usage in Industry", width="large")
                    }
                )
            
            with tab2:
                # Query type analysis
                type_counts = df['type'].value_counts()
                st.bar_chart(type_counts)
                
                # Show breakdown by type
                for query_type in type_counts.index:
                    with st.expander(f"📝 {query_type.title()} Queries ({type_counts[query_type]})"):
                        type_queries = df[df['type'] == query_type]
                        for _, row in type_queries.iterrows():
                            st.write(f"**Query:** {row['query']}")
                            st.write(f"**Intent:** {row['user_intent']}")
                            st.write(f"**Reasoning:** {row['reasoning']}")
                            st.write(f"**Industry Usage:** {row['possible_usage_in_industry']}")
                            st.write("---")
            
with tab3:
    # Create enhanced CSV with better column ordering
    csv_df = df[['query', 'type', 'user_intent', 'reasoning', 'possible_usage_in_industry', 'routing_format', 'format_reason']].copy()
    csv_df.columns = [
        'Query',
        'Type',
        'User Intent',
        'Reasoning',
        'Possible Usage in Your Industry',
        'Routing Format',
        'Format Reason'
    ]
    
    csv = csv_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Download Complete Analysis (CSV)", 
        data=csv, 
        file_name=f"qforia_analysis_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv", 
        mime="text/csv"
    )
    
    # Show preview of CSV data
    st.subheader("📋 CSV Preview")
    st.dataframe(csv_df.head(5), use_container_width=True)
    st.info(f"💡 The CSV file will contain all {len(csv_df)} queries with the 'Possible Usage in Your Industry' column included.")
    
    # JSON export option
    json_data = json.dumps(results, indent=2).encode("utf-8")
    st.download_button(
        "📥 Download Raw Data (JSON)", 
        data=json_data, 
        file_name=f"qforia_raw_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json", 
        mime="application/json"
    )
        
        elif results is None:  # Error occurred in generate_fanout
            # Error message is already displayed by generate_fanout
            pass
        else:  # Handle empty results list (empty list, not None)
            st.warning("⚠️ No queries were generated. The model returned an empty list, or there was an issue.")

# Add footer with app information
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🔍 <strong>Qforia</strong> - Advanced Query Fan-Out Simulator</p>
    <p>Powered by Google Gemini AI | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
