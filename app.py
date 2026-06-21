from dotenv import load_dotenv
load_dotenv()

from google import genai
import streamlit as st
import os
import sqlite3

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def get_response(input_text, prompt):
    response = client.models.generate_content(
    model="gemma-4-26b-a4b-it", #gemma-4-26b-a4b-it
    contents = (prompt[0], input_text)
    )
    return response.text

def read_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows= cur.fetchall()
    for row in rows:
        print(row)
    return rows

prompt = [
    """
You are an expert in converting English questions into SQL queries.

The SQL database contains a table named STUDENT with the following columns:
- NAME
- CLASS
- SECTION
- MARKS

Return only the SQL query as output.
Do not include explanations, markdown formatting, backticks, or the word 'sql'.

Example 1:
Question: How many records are present in the STUDENT table?
Answer:
SELECT COUNT(*) FROM STUDENT;

Example 2:
Question: Tell me all the students studying in the Data Science class.
Answer:
SELECT * FROM STUDENT WHERE CLASS = 'Data Science';

Example 3:
Question: Tell me the names of students whose marks are greater than 50 and are in Section A.
Answer:
SELECT NAME FROM STUDENT WHERE MARKS > 50 AND SECTION = 'A';
"""
]

st.set_page_config(page_title="Text To SQL APP")

st.header("Text to Sql Converter")
input_text = st.text_input("Input :", key="input")
submit = st.button("Ask a question")

if submit:
    response = get_response(input_text,prompt )
    print(response)
    response2 = read_query(response, "student.db")
    print(response2)
    st.subheader("The Retrieved data :")
    for row in response2:
        print(row)
        st.header(row)