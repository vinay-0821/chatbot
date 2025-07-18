﻿# Excel Chat Assistant

An AI-powered Streamlit application that allows users to interact with Excel datasets using natural language queries. It leverages OpenRouter's LLM APIs to analyze and respond to data-related questions and generates insightful visualizations using Altair.

---

## Features

- Upload Excel (.xlsx) files
- Ask questions about your dataset in plain English
- Automatically get intelligent answers from a Large Language Model (LLM)
- Generate visual charts (bar, line, histogram) from LLM-inferred instructions
- Modular structure with separate logic for data processing, chart rendering, and LLM interaction

---

## Tech Stack

- **Frontend & UI**: [Streamlit](https://streamlit.io/)
- **Data Analysis**: [Pandas](https://pandas.pydata.org/)
- **Charting**: [Altair](https://altair-viz.github.io/)
- **LLM Integration**: [OpenRouter](https://openrouter.ai/) API using OpenAI SDK
- **Excel Handling**: Pandas with `read_excel`

---

## Project Structure

```
excel-chat-assistant/
│
├── app.py                # Main Streamlit app logic
├── excel_parser.py       # Processes and cleans Excel data
├── llm_utils.py          # Interacts with OpenRouter LLM API
├── plot_utils.py         # Generates Altair charts from model instructions
├── .env                  # Stores your OpenRouter API key (not pushed to GitHub)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/excel-chat-assistant.git
   cd excel-chat-assistant
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your OpenRouter API Key**
   - Create a file named `.env`
   - Add the following:
     ```
     OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     ```

---

## Running the App

```bash
streamlit run app.py
```

---

## Example Usage

1. Upload your Excel file (e.g., `data.xlsx`)
2. Ask questions like:
   - “Show the average sales by region”
   - “Plot a bar chart of revenue by product”
3. Get instant answers and visualizations!

---

## Notes

- The model only analyzes a preview (first 100 rows) to reduce latency.
- Column names with special characters (e.g., spaces, colons) are automatically normalized for compatibility with Altair.
- Ensure your questions clearly specify chart requests for proper visualization.

---

## Acknowledgements

- OpenRouter for access to LLM APIs
- Streamlit for rapid UI development
- Altair for declarative charting
