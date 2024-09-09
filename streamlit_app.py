import streamlit as st # type: ignore

# Set the title and main header for the app
st.title("Pesarlanka Devendra Babu's Portfolio")
st.write("Welcome to my professional portfolio!")

# About Me Section
st.header("About Me")
st.write("""
I am a motivated and detail-oriented Computer Science and Engineering student with a strong foundation in programming, data analysis, 
and full-stack development. Proficient in Python and Java, with hands-on experience in machine learning, data visualization, 
and deep learning. I have a passion for continuous learning and professional growth.
""")

# Skills Section
st.header("Skills")
st.write("""
- **Programming Languages:** Python, Java
- **Frameworks:** HTML, CSS
- **Tools/Platforms:** MySQL, Power BI
- **Developer Tools:** Git, VS Code, PyCharm, IntelliJ, Eclipse, MS Office, Canva, Adobe Photoshop
""")

# Research & Projects Section
st.header("Research & Projects")

st.subheader("Research Experience")
st.write("""
**Skin Cancer Classification using CNN (March 2023 - Present)**
Developed a Convolutional Neural Network (CNN) model for skin cancer classification, achieving over 95% accuracy. 
This project aids in early detection and treatment of skin cancer.
- **Tech Stack:** Python, TensorFlow, Keras, CNN
""")

st.subheader("Projects")
st.write("""
**Exploratory Data Analysis on Insurance Claim System (October 2023)**
Performed EDA to analyze insurance claim data, identifying patterns and insights to enhance the efficiency of claims processing.
- **Domain:** Data Analysis
- **Tech:** Python

**Retail Management System (September 2023)**
Developed an e-commerce platform featuring seamless product selection and automated billing, enhancing user experience.
- **Domain:** Full Stack Development
- **Tech:** Tkinter
""")

# Publications & Certifications Section
st.header("Publications & Certifications")

st.subheader("Publications")
st.write("""
**Chapter Contribution:** 
"Security Aspects of Blockchain Technology" in the book "Driving Transformative Technology Trends with Cloud Computing" published by IGI Global (June 2024).
""")

st.subheader("Certifications")
st.write("""
- **Image Data Augmentation with Keras (Coursera)** - June 2024
- **Introduction to Statistics** - May 2023
- **Introduction to Hardware and Operating System** - April 2022
""")

# Achievements Section
st.header("Achievements")
st.write("""
**Best Leader Award** - AIESEC in India, January 2023
Recognized for outstanding contributions as Team Leader in Youth-for-Impact and Partnership Development.
""")

# Education Section
st.header("Education")
st.write("""
**Lovely Professional University, Punjab, India**
- Bachelor of Technology - Computer Science and Engineering
- CGPA: 7.49 (Since August 2021)

**Sri Chaitanya Junior College, Hyderabad, Telangana**
- Intermediate
- Percentage: 89% (July 2019 - March 2021)

**Sri Narayana Global High School, Hyderabad, Telangana**
- Matriculation
- Percentage: 93% (April 2018 - March 2019)
""")

# Contact Section
st.header("Contact")
st.write("Feel free to get in touch with me!")
st.write("[LinkedIn](https://www.linkedin.com/in/pesarlanka-devendrababu) | [GitHub](https://github.com/pesarlanka) | Email: devendrababu9666@gmail.com")

# Footer
st.write("© 2024 Pesarlanka Devendra Babu")

