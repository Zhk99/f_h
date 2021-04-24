import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

with PdfPages(r'Charts.pdf') as export_pdf:
    plt.scatter(df1['Unemployment_Rate'], df1['Stock_Index_Price'], color='green')
    plt.title('Unemployment Rate Vs Stock Index Price', fontsize=10)
    plt.xlabel('Unemployment Rate', fontsize=8)
    plt.ylabel('Stock Index Price', fontsize=8)
    plt.grid(True)
    export_pdf.savefig()
    plt.close()

    plt.plot(df2['Year'], df2['Unemployment_Rate'], color='red', marker='o')
    plt.title('Unemployment Rate Vs Year', fontsize=10)
    plt.xlabel('Year', fontsize=8)
    plt.ylabel('Unemployment Rate', fontsize=8)
    plt.grid(True)
    export_pdf.savefig()
    plt.close()