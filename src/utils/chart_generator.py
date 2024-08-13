import matplotlib.pyplot as plt

def generate_pie_chart(data, title=""):
    labels = [item["name"] for item in data]
    sizes = [item["value"] for item in data]

    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(title)
    plt.show()

def generate_bar_chart(data, title="", x_label="", y_label=""):
    labels = [item["name"] for item in data]
    values = [item["value"] for item in data]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
