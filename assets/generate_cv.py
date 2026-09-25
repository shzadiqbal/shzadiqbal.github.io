#!/usr/bin/env python3
"""
Professional Academic CV Generator
Muhammad Shahzad Iqbal, PhD
Optimized for Assistant Professor (NGS / Genomics) positions
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable
)
import os

OUTPUT_FILE = "CV_Muhammad_Shahzad_Iqbal_Assistant_Professor.pdf"

# Colors
PRIMARY = HexColor("#0f172a")
ACCENT = HexColor("#0284c7")
TEXT = HexColor("#1e293b")
MUTED = HexColor("#64748b")
BORDER = HexColor("#e2e8f0")

def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(name='Name', fontSize=22, leading=26, textColor=PRIMARY,
                              fontName='Helvetica-Bold', spaceAfter=2))
    styles.add(ParagraphStyle(name='Headline', fontSize=11, leading=14, textColor=ACCENT,
                              fontName='Helvetica-Bold', spaceAfter=6))
    styles.add(ParagraphStyle(name='Contact', fontSize=9, leading=12, textColor=MUTED,
                              fontName='Helvetica', spaceAfter=8))
    styles.add(ParagraphStyle(name='SectionHeader', fontSize=12, leading=15, textColor=PRIMARY,
                              fontName='Helvetica-Bold', spaceBefore=13, spaceAfter=5))
    styles.add(ParagraphStyle(name='JobTitle', fontSize=10.5, leading=13, textColor=PRIMARY,
                              fontName='Helvetica-Bold', spaceBefore=7, spaceAfter=1))
    styles.add(ParagraphStyle(name='Meta', fontSize=9, leading=11, textColor=ACCENT,
                              fontName='Helvetica-Oblique', spaceAfter=3))
    styles.add(ParagraphStyle(name='Body', fontSize=9, leading=12, textColor=TEXT,
                              fontName='Helvetica', alignment=TA_JUSTIFY, spaceAfter=3))
    styles.add(ParagraphStyle(name='Pub', fontSize=8.5, leading=11, textColor=TEXT,
                              fontName='Helvetica', spaceAfter=4))
    styles.add(ParagraphStyle(name='Small', fontSize=8, leading=10, textColor=MUTED,
                              fontName='Helvetica'))
    return styles

def section_header(text, styles):
    return [
        Paragraph(text.upper(), styles['SectionHeader']),
        HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceBefore=0, spaceAfter=6)
    ]

def generate_cv():
    doc = SimpleDocTemplate(
        OUTPUT_FILE, pagesize=A4,
        rightMargin=1.6*cm, leftMargin=1.6*cm,
        topMargin=1.4*cm, bottomMargin=1.4*cm
    )
    styles = build_styles()
    story = []

    # ========== HEADER ==========
    story.append(Paragraph("MUHAMMAD SHAHZAD IQBAL, PhD", styles['Name']))
    story.append(Paragraph(
        "Assistant Professor Candidate  |  NGS Expert  |  Genomics & Bioinformatics",
        styles['Headline']
    ))
    story.append(Paragraph(
        "Email: shahzad.iqbal@uo.edu.pk  •  shzad@live.com  |  Phone: +92-334-7041004<br/>"
        "ORCID: 0000-0001-5145-3075  |  Open to relocation<br/>"
        "Portfolio: <link href='https://shzadiqbal.github.io/shzadiqbal.github.io/'>https://shzadiqbal.github.io/mshahzadiqbal.github.io/</link><br/>"
        "Google Scholar: 402 citations  |  h-index: 11",
        styles['Contact']
    ))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceBefore=2, spaceAfter=8))

    # ========== PROFESSIONAL SUMMARY ==========
    story.extend(section_header("Professional Summary", styles))
    story.append(Paragraph(
        "Molecular biologist and bioinformatician with deep hands-on expertise in "
        "<b>Next-Generation Sequencing (NGS)</b> and large-scale transcriptomic analysis. "
        "My PhD research involved comprehensive RNA-Seq analysis of a complex polyploid crop, "
        "including development of a novel computational pipeline to correct polyploidy effects — "
        "work that is now in final publishable form and scheduled for submission to "
        "<i>Plant Molecular Biology</i> (Springer Nature). "
        "I have independently analyzed 50+ NGS projects (WGS, WES, RNA-seq, smRNA-seq), "
        "trained over 50 researchers, and supervised 28 M.Phil. students. "
        "Seeking an Assistant Professor position to advance NGS-driven genomics research and teaching.",
        styles['Body']
    ))

    # ========== RESEARCH INTERESTS ==========
    story.extend(section_header("Research Interests", styles))
    story.append(Paragraph(
        "• Next-Generation Sequencing (NGS) data analysis & reproducible pipeline development<br/>"
        "• Transcriptomics and differential gene expression in complex genomes<br/>"
        "• Host–pathogen interactions and molecular virology<br/>"
        "• Computational prediction of host-derived microRNAs against viruses<br/>"
        "• Multi-omics data integration and functional genomics",
        styles['Body']
    ))

    # ========== EDUCATION ==========
    story.extend(section_header("Education", styles))

    story.append(Paragraph("PhD in Molecular Biology  <font color='#0284c7'>(Major NGS Project)</font>", styles['JobTitle']))
    story.append(Paragraph(
        "Centre of Excellence in Molecular Biology (CEMB), University of the Punjab, Pakistan  |  2021",
        styles['Meta']
    ))
    story.append(Paragraph(
        "<b>Thesis:</b> Transcriptomic expression behaviour of sugarcane cultivars against red rot disease.<br/>"
        "Conducted high-throughput RNA-Seq analysis of multiple sugarcane cultivars to identify "
        "pathogen-responsive genes and defense mechanisms in a highly polyploid genome. "
        "Developed a <b>novel bioinformatics pipeline</b> specifically designed to minimize the confounding "
        "effects of polyploidy on differential expression analysis. "
        "This work represents substantial original contribution to NGS methodology for complex plant genomes.<br/>"
        "<b>Current Status:</b> Manuscript submitted to <i>Plant Molecular Biology</i> (Springer Nature).",
        styles['Body']
    ))

    story.append(Paragraph("M.Phil. in Molecular Biology", styles['JobTitle']))
    story.append(Paragraph("CEMB, University of the Punjab, Pakistan  |  2013", styles['Meta']))
    story.append(Paragraph("Thesis: In Vitro knockdown of PVY through shRNA (RNA interference & molecular virology).", styles['Body']))

    story.append(Paragraph("BS (Hons) Biochemistry", styles['JobTitle']))
    story.append(Paragraph("The University of Lahore, Pakistan  |  2011", styles['Meta']))

    # ========== EXPERIENCE ==========
    story.extend(section_header("Professional Experience", styles))

    story.append(Paragraph("Lecturer (Biochemistry)", styles['JobTitle']))
    story.append(Paragraph("University of Okara, Pakistan  |  August 2022 – Present", styles['Meta']))
    story.append(Paragraph(
        "• Deputy Director, Office of Research, Innovation & Commercialization (ORIC)<br/>"
        "• In-Charge, Department of Food Sciences and Technology<br/>"
        "• Supervising 2 PhD + 28 completed M.Phil. + 40+ BS students<br/>"
        "• Teaching Biochemistry, Molecular Biology, Bioinformatics and NGS technologies<br/>"
        "• Trained 50+ researchers in NGS data analysis and computational biology",
        styles['Body']
    ))

    story.append(Paragraph("Assistant Professor (Biotechnology)", styles['JobTitle']))
    story.append(Paragraph("University of Central Punjab  |  Sep 2021 – Aug 2022", styles['Meta']))
    story.append(Paragraph("Research supervision and teaching in genetic engineering and molecular diagnostics.", styles['Body']))

    story.append(Paragraph("Senior Lecturer (Molecular Biology & Bioinformatics)", styles['JobTitle']))
    story.append(Paragraph("The University of Lahore  |  Mar 2020 – Sep 2021", styles['Meta']))
    story.append(Paragraph("Managed computational server for genomics research. Taught bioinformatics and NGS.", styles['Body']))

    story.append(Paragraph("NGS Application Scientist / Regional Manager", styles['JobTitle']))
    story.append(Paragraph("Molecular Products Co. (BGI Pakistan)  |  May 2018 – Feb 2020", styles['Meta']))
    story.append(Paragraph(
        "• Independently analyzed <b>50+ NGS projects</b> (WGS, WES, RNA-seq, smRNA-seq, lncRNA-seq)<br/>"
        "• Developed and optimized reproducible pipelines for variant calling and differential expression<br/>"
        "• Delivered technical training and project design support to university research groups",
        styles['Body']
    ))

    story.append(Paragraph("University Research Associate (IRSIP Fellow)", styles['JobTitle']))
    story.append(Paragraph("QAAFI, The University of Queensland, Australia  |  Jul 2017 – Jan 2018", styles['Meta']))
    story.append(Paragraph(
        "Supervisor: Prof. Robert Henry. Performed large-scale sugarcane RNA-Seq analysis (72+ samples) "
        "focused on red rot responsive genes — directly complementary to PhD research.",
        styles['Body']
    ))

    # ========== SELECTED PUBLICATIONS ==========
    story.extend(section_header("Selected Publications", styles))
    story.append(Paragraph("<i>Total Citations: 402  |  h-index: 11  |  Full list available on Google Scholar</i>", styles['Small']))
    story.append(Spacer(1, 4))

    pubs = [
        "<b>Iqbal MS</b>, Sharif MN, Ali T, Henry RJ, Nasir IA. Comparative Transcriptomics identifies red rot induced defense response in sugarcane. <i>Manuscript ready for submission to Plant Molecular Biology (Springer Nature)</i>.",
        "Sharif MN, <b>Iqbal MS</b>, et al. (2022). Silencing of multiple target genes via ingestion of dsRNA... in Helicoverpa armigera. <i>Scientific Reports</i>. Citations: 43",
        "<b>Iqbal MS</b>, et al. (2017). In Silico MCMV Silencing Concludes Potential Host-Derived miRNAs in Maize. <i>Frontiers in Plant Science</i>. Citations: 41",
        "Hassan M, <b>Iqbal MS</b>, et al. (2022). Prediction of Site Directed miRNAs... Against Influenza C Virus. <i>Frontiers in Molecular Biosciences</i>.",
        "Ashraf MA, et al. (including <b>Iqbal MS</b>) (2022). In silico identification of sugarcane genome encoded microRNAs targeting sugarcane bacilliform virus. <i>PLoS ONE</i>.",
        "Jabbar B, <b>Iqbal MS</b>, et al. (2019). Target prediction of candidate miRNAs from Oryza sativa for silencing the RYMV genome. <i>Computational Biology and Chemistry</i>."
    ]
    for p in pubs:
        story.append(Paragraph("• " + p, styles['Pub']))

    # ========== SUPERVISION ==========
    story.extend(section_header("Research Supervision", styles))
    story.append(Paragraph(
        "<b>PhD:</b> 2 (Ongoing) &nbsp;&nbsp;|&nbsp;&nbsp; <b>M.Phil.:</b> 28 (Completed) &nbsp;&nbsp;|&nbsp;&nbsp; <b>BS:</b> 40+<br/>"
        "Majority of postgraduate projects focused on computational viral bioinformatics and host-derived microRNA prediction.",
        styles['Body']
    ))

    # ========== TECHNICAL SKILLS ==========
    story.extend(section_header("Technical Skills", styles))
    story.append(Paragraph(
        "<b>NGS & Bioinformatics:</b> RNA-Seq (EdgeR, DESeq2), WGS, WES, Variant Calling, Differential Expression, "
        "Virus detection from RNA-seq, GO/KEGG Pathway Analysis, De novo Assembly, Custom pipeline development for polyploid genomes<br/><br/>"
        "<b>Programming & Computing:</b> R (Advanced), Python, Linux, High-Performance Computing (HPC), Reproducible workflows<br/><br/>"
        "<b>Molecular Biology:</b> qRT-PCR, advanced PCR, DNA/RNA extraction, Gene cloning & transformation, Sanger sequencing",
        styles['Body']
    ))

    # ========== AWARDS ==========
    story.extend(section_header("Awards & International Exposure", styles))
    story.append(Paragraph(
        "• IRSIP Training Fellowship – 6 months genomics research at The University of Queensland, Australia<br/>"
        "• British Council & HEC Study Visit to Scotland (Edinburgh, Glasgow, Dundee, Heriot-Watt)<br/>"
        "• HEC Indigenous PhD Scholarship (4-year full funding)",
        styles['Body']
    ))

    # ========== FOOTER ==========
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.8, color=BORDER, spaceBefore=4, spaceAfter=4))
    story.append(Paragraph(
        "References available upon request  •  Portfolio: https://shzadiqbal.github.io/mshahzadiqbal.github.io/  •  Google Scholar: https://scholar.google.com/citations?user=-gzVrr4AAAAJ",
        styles['Small']
    ))

    doc.build(story)
    print(f"✅ CV successfully generated: {OUTPUT_FILE}")
    return OUTPUT_FILE

if __name__ == "__main__":
    generate_cv()