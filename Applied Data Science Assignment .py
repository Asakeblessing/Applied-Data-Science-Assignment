import pandas as pd
import matplotlib.pyplot as plt

""" Data Source:  https://www.kaggle.com/datasets/teamincribo/glaucoma-detection-dataset """

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('glaucoma_dataset.csv')

def plot_line_chart():
    """ plot the line chart"""
    # Filter the data to select patients with Glaucoma Diagnosis
    glaucoma_patients = df[df['Diagnosis'] == 'No Glaucoma']

    # Group the data by 'Age' and count the number of Glaucoma patients for each age
    age_counts = glaucoma_patients['Age'].value_counts().sort_index()

    # Create a line chart to visualize the number of Glaucoma patients by age
    plt.figure(figsize=(10, 6))
    plt.plot(age_counts.index, age_counts.values, marker='o', linestyle='-')
    plt.title('Patients without Glaucoma by Age')
    plt.xlabel('Age')
    plt.ylabel('Number of Patients')
    plt.grid(True)

    # Display the chart
    return plt.show()

def plot_bar_chart():
    """ plot the bar chart"""
    # Count the occurrences of each age
    age_counts = df['Age'].value_counts().sort_index()

    # Plotting the bar chart with labels, legends, title, and colors
    colors = plt.cm.viridis(age_counts.index.astype(float) / max(age_counts.index))

    # Uncomment the next line to increase the size of the chart
    plt.figure(figsize=(12, 10))

    plt.bar(age_counts.index, age_counts.values, color=colors)

    # Adding labels and title
    plt.xlabel('Age')
    plt.ylabel('Age Count')
    plt.title('Distribution of Ages in the Dataset')

    # Add chart  legend
    plt.legend(['Count per Age'], loc='upper right')

    # Display the chart
    return plt.show()

def plot_pie_chart():
    """ plot the pie chart"""
    # Filter the df to select Glaucoma patients with 'Family History' equal to 'YES'
    glaucoma_with_family_history = df[(df['Diagnosis'] == 'Glaucoma') & (df['Family History'] == 'Yes')]

    # Count the number of patients with family history
    count_yes = len(glaucoma_with_family_history)

    # Count the number of Glaucoma patients without family history
    count_no = len(df[df['Diagnosis'] == 'Glaucoma']) - count_yes

    # Create data for the pie chart
    labels = ['With Family History', 'Without Family History']
    sizes = [count_yes, count_no]
    # Define custom colors

    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)

    # Create a pie chart with legends, title, and custom colors
    plt.figure(figsize=(12, 10))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140,)
    plt.title('Distribution of Glaucoma Patients by Family History')
    plt.legend(labels, title='Legend', loc='upper right')

    # Show the pie chart
    plt.axis('equal')
    return plt.show()

def main():
    print('Starting the program')
    plot_line_chart()
    plot_pie_chart()
    plot_bar_chart()


main()


