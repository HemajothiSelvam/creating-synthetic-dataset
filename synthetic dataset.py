#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install faker')


# In[3]:


import pandas as pd
import random
from faker import Faker

def generate_random_dataset(num_records=10):
    fake = Faker()
    data = []
    for _ in range(num_records):
        data.append([
            random.choice(["Python for Data Science", "Machine Learning Basics", "AI Fundamentals"]),
            f"C{random.randint(100,999)}",
            f"Attempt {random.randint(1,3)}",
            fake.name(),
            fake.email(),
            random.randint(50, 100),
            random.choice(["A+", "A", "B+", "B", "C", "D"])
        ])
    df = pd.DataFrame(data, columns=["Course Name (Required)", "Course ID", "Attempt ID", "Candidate Name", "Candidate Email", "Mark", "Grade"])
    return df

def create_manual_dataset():
    data = []
    while True:
        course_name = input("Enter Course Name (or type 'exit' to stop): ")
        if course_name.lower() == 'exit':
            break
        course_id = input("Enter Course ID: ")
        attempt_id = input("Enter Attempt ID (Attempt 1, 2, 3): ")
        candidate_name = input("Enter Candidate Name: ")
        candidate_email = input("Enter Candidate Email: ")
        mark = input("Enter Mark: ")
        grade = input("Enter Grade: ")
        data.append([course_name, course_id, attempt_id, candidate_name, candidate_email, mark, grade])
    
    df = pd.DataFrame(data, columns=["Course Name (Required)", "Course ID", "Attempt ID", "Candidate Name", "Candidate Email", "Mark", "Grade"])
    return df

def main():
    print("Choose an option:")
    print("1. Generate a Random Dataset")
    print("2. Create a Dataset Manually")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        num_records = int(input("Enter the number of records to generate: "))
        dataset = generate_random_dataset(num_records)
    elif choice == '2':
        dataset = create_manual_dataset()
    else:
        print("Invalid choice. Exiting...")
        return
    
    print("\nGenerated Dataset:")
    print(dataset)
    
    save_option = input("Do you want to save the dataset? (yes/no): ")
    if save_option.lower() == 'yes':
        filename = input("Enter filename (without extension): ")
        dataset.to_csv(f"{filename}.csv", index=False)
        print(f"Dataset saved as {filename}.csv")

if __name__ == "__main__":
    main()


# In[ ]:




