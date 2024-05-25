# The Professor Bot

Welcome to **The Professor Bot**! This project is designed to create an AI tutor named **Professor Tublian** who can answer your questions, explain machine learning algorithms, and guide you through your learning journey.

## Introduction

The Professor Bot is a command-line chatbot built using Python. It leverages GroqCloud and Llama3 to provide detailed explanations and real-world examples related to Data Science, Machine Learning, and Artificial Intelligence. This project aims to provide a personal AI tutor to assist with learning and understanding complex topics in these fields.

## Tech Stack

- **Python**: The programming language used for developing the chatbot.
- **GroqCloud**: A platform to build GenAI applications.
- **Llama3**: An open-source Large Language Model used to generate responses.
- **python-dotenv**: A Python library to manage environment variables.

## Setting Up the Project

### Prerequisites

- Python 3.x
- Virtual Environment (optional but recommended)

### Creating a Virtual Environment

1. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```

2. **Activate the virtual environment:**
    - On Windows:
    ```bash
    .\env\Scripts\activate
    ```
    - On macOS/Linux:
    ```bash
    source env/bin/activate
    ```

### Installing the Required Libraries

1. Install the required libraries
```bash
pip install -r requirements.txt
```

### Setting Up the Groq API Key

1. Create a `.env` file in the root directory of the project, if not already exist
GROQ_API_KEY=your_groq_api_key_here

2. Replace `your_groq_api_key_here` with your actual Groq API key.

### Running the Program

1. Run the script:
```bash
python prof_tublian.py
```

2. Interact with the AI Tutor:

- Type your questions and get detailed explanations from Professor Tublian.
- To exit the program, type `exit`.

## Example Usage

```bash
====================================================================================================
Welcome!!!
I am Professor Tublian, your personal AI tutor.
Feel free to ask me any questions, and I will provide detailed explanations and real-world examples to help you understand.
To quit, type 'exit'.
Let's begin!
====================================================================================================

You: What is clustering?

Prof. Tublian: Clustering is an unsupervised machine learning technique used for grouping similar data points into clusters or categories. This technique is often used for exploratory data analysis, where the goal is to uncover underlying patterns in the data.

Imagine you are a marketing manager at a retail company, and you have a large dataset of customer information, including demographics, purchase history, and behavior. You want to segment your customer base into distinct groups, each with similar characteristics, interests, and behaviors. This is where clustering comes in.

Clustering algorithms work by identifying the distance or similarity between data points. In the marketing example, you might group customers based on their geographic location, age, and purchase history. The algorithm would then identify clusters or groups of customers with similar characteristics.

There are several types of clustering algorithms, including:

1. K-Means Clustering: This is a widely used algorithm that partitions the data into K clusters. The algorithm assigns each data point to the cluster with the closest centroid (a set of representative points).
2. Hierarchical Clustering: This algorithm builds a hierarchy of clusters by recursively merging or dividing them. It's useful for visualizing the structure of the data.
3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise): This algorithm groups data points based on density and proximity. It's useful for handling noise and outliers in the data.

Clustering has many real-world applications, including:

1. Customer segmentation: Grouping customers based on demographics, behavior, and preferences.
2. Fault detection: Identifying anomalies or exceptions in a system or process.
3. Image and text classification: Grouping images or documents into categories based on visual or textual features.
4. Recommendation systems: Suggesting products or services based on user behavior and preferences.

In summary, clustering is a powerful technique for identifying patterns and structures in data. By grouping similar data points together, clustering enables data analysts and business users to gain insights, uncover trends, and make informed decisions.

====================================================================================================

You: exit

Thank you, I am always here to help you on your learning journey. Goodbye!

```
