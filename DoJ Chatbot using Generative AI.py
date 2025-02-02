import google.generativeai as genai
import streamlit as st

# Configure Generative AI with your API key
genai.configure(api_key="AIzaSyBfkcl6TUjyWLfsl5g0_v-Q_NAmjTmNiSE")
model = genai.GenerativeModel('gemini-1.5-flash')

# Set up the Streamlit UI with custom settings
st.set_page_config(page_title="PravdaGPT - Legal and DOJ Assistant", page_icon=":balance_scale:", layout="centered")

# Adding custom CSS for dark background and styling
st.markdown(
    """
    <style>
    .main {
        background-color: #1e1e2f;
        color: #e0e0e0;
    }
    .stTextInput>div>div>input {
        background-color: #333;
        color: #e0e0e0;
    }
    .stButton>button {
        background-color: #4a4a6a;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
    }
    .sidebar .sidebar-content {
        background-color: #2c2c3e;
        color: #e0e0e0;
    }
    .stMarkdown, .stAlert, .stSuccess, .stError, .stWarning {
        background-color: #333;
        color: #e0e0e0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description of the app
st.title('PravdaGPT - Legal and DOJ Specialist Assistant')
st.markdown("""
### Welcome to PravdaGPT - Your Legal and DOJ Specialist Assistant!
This AI assistant is tailored to answer questions specifically about the *Department of Justice* and legal codes, including penal codes and IPC sections. 
Whether you need help finding a specific legal section, understanding DOJ policies, or clarifying legal definitions, PravdaGPT is here to make the process easy.

*Please note*: The assistant is designed to respond to DOJ and legal-related questions. Any unrelated queries will not be processed.
""")

# Sidebar with suggested questions in English, Tamil, and Hindi
st.sidebar.header("Suggested Questions")

# English Suggestions
st.sidebar.markdown("*Find Penal Codes and Legal Sections (English):*")
english_questions = [
    "What is IPC Section 302?",
    "Can you help me find the penal code for theft?",
    "What does Section 420 of the IPC state?",
]
for question in english_questions:
    if st.sidebar.button(question):
        text = question

# Tamil Suggestions
st.sidebar.markdown("*சட்ட மற்றும் நீதி தொடர்பான கேள்விகள் (Tamil):*")
tamil_questions = [
    "IPC பிரிவு 302 என்ன?",
    "கள்வன் குறியீட்டை கண்டுபிடிக்க உதவ முடியுமா?",
    "IPC பிரிவு 420 என்ன சொல்கிறது?",
]
for question in tamil_questions:
    if st.sidebar.button(question):
        text = question

# Hindi Suggestions
st.sidebar.markdown("*कानूनी और न्याय विभाग से जुड़े प्रश्न (Hindi):*")
hindi_questions = [
    "IPC धारा 302 क्या है?",
    "कृपया चोरी के लिए दंड संहिता खोजने में मदद करें?",
    "IPC की धारा 420 क्या कहती है?",
]
for question in hindi_questions:
    if st.sidebar.button(question):
        text = question

# Input field for questions
user_input = st.text_input("Ask a legal or DOJ-related question", text if 'text' in locals() else "")

def is_legal_or_doj_related(question):
    # Check to ensure the question is related to legal or DOJ topics
    related_keywords = [
        'DOJ', 'Department of Justice', 'justice', 'legal', 'laws', 'attorney', 
        'federal', 'court', 'judge', 'policy', 'investigation', 'indictment',
        'IPC', 'penal code', 'section', 'law', 'criminal', 'penalty', 
        'சட்ட', 'நீதித் துறை', 'धारा', 'कानून'
    ]
    return any(keyword.lower() in question.lower() for keyword in related_keywords)

# Handling the input
if user_input:
    if is_legal_or_doj_related(user_input):
        try:
            response = model.generate_content(user_input)
            st.success(response.text)  # Display the answer from the AI
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Your question doesn't seem related to legal or DOJ topics. Please ask a relevant question.")
else:
    st.write("Please enter a legal or DOJ-related question.")