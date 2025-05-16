from src.data_generation import generate_data
from src.preprocess import preprocess_data
from src.analysis import analyze_sentiments
from src.visualization import create_visualizations
    

def main():
    print('Generating random dataset...')
    generate_data(num_entries=200)

    print('Preprocessing data...')
    preprocess_data()

    print('Analyzing sentiments...')
    analyze_sentiments()

    print('Creating visualizations...')
    create_visualizations()

if __name__ == '__main__':
    main()
