import pandas as pd

def analyze_data():
    try:
        # Load the CSV file
        df = pd.read_csv("sales.csv")
        
        print("--- Original Dataset ---")
        print(df)
        
        # Calculate Total Sales
        total_sales = df['Sales'].sum()
        print(f"\nTotal Overall Sales: ${total_sales}")
        
        # Group sales by Category
        summary = df.groupby('Category')['Sales'].sum()
        print("\n--- Sales Summary by Category ---")
        print(summary)
        
        # Export the summary to a new CSV file
        summary.to_csv("summary_report.csv")
        print("\nSuccess: 'summary_report.csv' has been generated!")
        
    except FileNotFoundError:
        print("Error: 'sales.csv' file not found. Please create it first.")

if __name__ == "__main__":
    analyze_data()