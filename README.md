AI DDR Report Generation System

📌 Overview

This project builds an AI system that converts inspection and thermal reports into a structured Detailed Diagnostic Report (DDR).

The system processes:

- Inspection Report (site observations)
- Thermal Report (temperature & moisture analysis)

🚀 Features

- Extracts observations from PDFs
- Combines multi-source data (inspection + thermal)
- Removes duplicate issues
- Handles missing information
- Generates structured client-ready report
- Maps images to observations

📄 Final Output

👉 The generated DDR report is available here:
"outputs/final_ddr_report.html"

🧠 Approach

1. Extract text and images from PDFs
2. Identify key issues (dampness, leakage, cracks)
3. Merge and deduplicate observations
4. Analyze root causes using combined data
5. Generate structured DDR report

🛠 Tech Stack

- Python
- pdfplumber
- PyMuPDF
- Jinja2
- Basic NLP (rule-based)

▶️ How to Run

pip install -r requirements.txt
python main.py

✅ Output Structure

The DDR includes:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment
5. Recommended Actions
6. Additional Notes
7. Missing Information

---

💡 Note

This system demonstrates multi-document reasoning and real-world AI pipeline design for construction diagnostics.
