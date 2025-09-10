import json
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def generate_lab_report(data, filename="lab_report.docx"):
    # Create document
    doc = Document()

    # Set margins (Left=1.5, others=1)
    sections = doc.sections
    for section in sections:
        section.left_margin = Inches(1.5)
        section.right_margin = Inches(1)
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)

    # Helper function for formatting
    def add_header(text):
        p = doc.add_paragraph(text.upper())
        run = p.runs[0]
        run.font.size = Pt(16)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        return p

    def add_subheader(text):
        p = doc.add_paragraph(text)
        run = p.runs[0]
        run.font.size = Pt(14)
        run.bold = True
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        return p

    def add_paragraph(text):
        p = doc.add_paragraph(text)
        run = p.runs[0]
        run.font.size = Pt(12)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        return p

    def add_code(text):
        p = doc.add_paragraph(text)
        run = p.runs[0]
        run.font.size = Pt(12)
        run.italic = True
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        return p

    # --- Start Writing Report ---
    # Topic
    add_header(f"TOPIC: {data['topic']}")

    # Objective
    add_subheader("1. OBJECTIVE")
    for obj in data["objective"]:
        obj_para = doc.add_paragraph(style="List Bullet")
        run = obj_para.add_run(obj)
        run.font.size = Pt(12)

    # Theory
    add_subheader("2. THEORY")
    add_paragraph(data["theory"])

    # Implementation
    add_subheader("3. IMPLEMENTATION IN JAVA")
    add_code(data["implementation"])

    # Output (screenshot placeholder)
    add_subheader("4. OUTPUT")
    add_paragraph("[Screenshot will be added here]")

    # Conclusion
    add_subheader("5. CONCLUSION")
    add_paragraph(data["conclusion"])

    # Save document
    doc.save(filename)
    print(f"✅ Lab report saved as {filename}")


if __name__ == "__main__":
    # Example JSON input
    json_data = """
    {
        "topic": "Inheritance in Java",
        "objective": [
            "To understand the concept of inheritance in Java",
            "To implement single inheritance using classes"
        ],
        "theory": "Inheritance in Java allows a class to acquire properties and behavior of another class. It promotes code reusability and establishes a parent-child relationship among classes. The parent class is known as the superclass, while the child class is called the subclass. This mechanism enables developers to extend existing classes without rewriting code, making programs easier to manage and scale.",
        "implementation": "class Animal {\\n    void eat() { System.out.println(\\\"eating...\\\"); }\\n}\\nclass Dog extends Animal {\\n    void bark() { System.out.println(\\\"barking...\\\"); }\\n}\\nclass TestInheritance {\\n    public static void main(String args[]) {\\n        Dog d=new Dog();\\n        d.bark();\\n        d.eat();\\n    }\\n}",
        "conclusion": "Through this experiment, we learned how inheritance allows a class to reuse the fields and methods of another class. It provides a way to organize code in a hierarchical manner, reducing redundancy and improving maintainability. By implementing inheritance, Java programs become more modular and scalable."
    }
    """

    data = json.loads(json_data)
    generate_lab_report(data)
