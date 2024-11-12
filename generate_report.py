from fpdf import FPDF

# Create a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=1, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 12)

# Title
pdf.cell(0, 10, "Energy Drink FMCG Analysis Report", 0, 1, "C")
pdf.ln(10)

# Section 1
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, "1. Demographic Insights", 0, 1)
pdf.set_font("Arial", "", 10)
pdf.multi_cell(0, 10, "- Gender Distribution: A majority of respondents were male (60.38%), followed by females (34.55%) and a small percentage identifying as non-binary (5.07%).")
pdf.multi_cell(0, 10, "- Age Group Distribution: The most significant age group is 19-30 years, accounting for 5.52K respondents, followed by 31-45 years with 2.38K. The 15-18 age group had 1.49K respondents, while older groups, 46-65 and 65+, had considerably fewer.")
pdf.ln(5)

# Section 2
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, "2. Consumer Preferences and Competitor Analysis", 0, 1)
pdf.set_font("Arial", "", 10)
pdf.multi_cell(0, 10, "- Preferred Ingredients: Caffeine is the top preferred ingredient (39%), followed by vitamins (25%), sugar (20%), and guarana (16%).")
pdf.multi_cell(0, 10, "- Packaging Preferences: Compact and portable cans are the most favored packaging type (40%), followed by innovative bottle designs (30%). Collectible and eco-friendly designs had lesser preferences.")
pdf.multi_cell(0, 10, "- Competing Brands: Cola-Coka, Bepsi, Gangster, and Blue Bull are significant competitors, with factors like availability, brand reputation, and taste being the main reasons for consumer choices.")
pdf.ln(5)

# Section 3
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, "3. Marketing and Brand Awareness", 0, 1)
pdf.set_font("Arial", "", 10)
pdf.multi_cell(0, 10, "- Marketing Channel Effectiveness: Online ads were the most effective channel (40%), followed by TV commercials (27%). Outdoor billboards and print media were less impactful.")
pdf.multi_cell(0, 10, "- Brand Awareness: 55.53% of respondents have heard of CodeX, while 44.47% have not. Reasons for not trying the brand include local unavailability (24.3%), health concerns (22.6%), and lack of interest in energy drinks (21.9%).")
pdf.ln(5)

# Section 4
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, "4. Purchase Behavior", 0, 1)
pdf.set_font("Arial", "", 10)
pdf.multi_cell(0, 10, "- Purchase Locations: Supermarkets (45%) and online retailers (26%) are the most common purchase locations, followed by local stores (15%). Gyms and fitness centers had the least sales (8%).")
pdf.multi_cell(0, 10, "- Consumption Situations: Energy drinks are primarily consumed during sports/exercise (45%) and studying/working late (32%). Social outings/parties and commuting situations had lower consumption rates.")
pdf.ln(5)

# Section 5
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, "5. Product Development Insights", 0, 1)
pdf.set_font("Arial", "", 10)
pdf.multi_cell(0, 10, "- Suggested Improvements: The main improvements consumers want are reduced sugar content (29.95%) and more natural ingredients (24.98%). Expanding flavor variety and offering healthier alternatives were also notable suggestions.")
pdf.multi_cell(0, 10, "- Health Concerns: 60.45% of respondents expressed health concerns regarding energy drinks.")
pdf.multi_cell(0, 10, "- Limited Edition Packaging: Consumers are divided, with 40.2% preferring limited editions, 39.5% not interested, and 20.3% unsure.")
pdf.ln(5)

# Section 6
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, "6. City-Specific Insights", 0, 1)
pdf.set_font("Arial", "", 10)
pdf.multi_cell(0, 10, "- Taste Experience Rating: CodeX received varying ratings, with the highest in Lucknow (4.0) and the lowest in Hyderabad (3.0).")
pdf.multi_cell(0, 10, "- Brand Penetration: CodeX competes closely with other brands across major cities, holding significant market shares in cities like Mumbai, Bangalore, and Pune.")
pdf.ln(10)

# Save the PDF
output_path = "Energy_Drink_FMCG_Analysis_Report.pdf"
pdf.output(output_path)
print(f"Report saved as {output_path}")