from langchain_core.prompts import PromptTemplate

#template

template = PromptTemplate(
    template = """
Please summarize the research paper titles "{paper_input}" with the following specifications:
Explanation style: {style_input}
Explanation length: {Length_input}
1.Mathematica details: 
     - Include relevant mathematical details and equations from the research papers to support the summary.
2. Analogies: 
     - Use relevant analogies to explain complex concepts in a more relatable manner.
If certain information is not available, respond with : " Insufficient information available to provide a summary" instead of guessing. Ensure the summary is clear, accurate, and aligned with the specified style and lenght mentioned above.
 """, 
input_variables = ['paper_input', 'style_input', 'Length_input'],
validate_template = True
)

template.save("template.json")
