from fpdf import FPDF

def generate_pdf(name: str, conversation: list):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Psychometric Assessment Report", ln=True)
    pdf.cell(200, 10, txt=f"Patient: {name}", ln=True)
    pdf.ln(10)

    for speaker, message in conversation:
        prefix = "You: " if speaker == "user" else "Assistant: "
        pdf.multi_cell(0, 10, txt=prefix + message)

    pdf.output("psychometric_report.pdf")
    return "psychometric_report.pdf"
