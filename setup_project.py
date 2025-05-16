import os

def update_project_structure(base_dir=None):
    # Define the folder structure to add
    if base_dir is None:
        base_dir = os.getcwd()
    folders = [
        f"{base_dir}/data/raw",
        f"{base_dir}/data/processed",
        f"{base_dir}/data/logs",
        f"{base_dir}/notebooks",
        f"{base_dir}/src",
        f"{base_dir}/models",
        f"{base_dir}/outputs/graphs",
        f"{base_dir}/outputs/reports",
        f"{base_dir}/tests",
        f"{base_dir}/config"
    ]
    
    # Define base files to add (will not overwrite existing ones)
    files = {
        f"{base_dir}/README.md": "# Sentiment Analysis Project\n\nProject description and instructions.",
        f"{base_dir}/requirements.txt": "pymongo\nnumpy\npandas\ntextblob\nmatplotlib\nseaborn",
        f"{base_dir}/config/db_config.py": 'MONGO_URI = "mongodb://localhost:27017/"\nDATABASE_NAME = "cs_sentiment"\nCOLLECTION_NAME = "feedback"',
        f"{base_dir}/src/data_generation.py": "# Script to generate and insert random data into MongoDB\n",
        f"{base_dir}/src/preprocess.py": "# Script to preprocess data for sentiment analysis\n",
        f"{base_dir}/src/analysis.py": "# Script for performing sentiment analysis\n",
        f"{base_dir}/src/visualization.py": "# Script for visualizing sentiment analysis results\n",
        f"{base_dir}/main.py": """from src.data_generation import generate_data\nfrom src.preprocess import preprocess_data\nfrom src.analysis import analyze_sentiments\nfrom src.visualization import create_visualizations\n\ndef main():\n    print('Generating random dataset...')\n    generate_data(num_entries=200)\n\n    print('Preprocessing data...')\n    preprocess_data()\n\n    print('Analyzing sentiments...')\n    analyze_sentiments()\n\n    print('Creating visualizations...')\n    create_visualizations()\n\nif __name__ == '__main__':\n    main()\n"""
    }
    
    # Add folders if missing
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Checked or created folder: {folder}")
    
    # Add files if missing
    for file_path, content in files.items():
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write(content)
            print(f"Created file: {file_path}")
        else:
            print(f"File already exists: {file_path}")

# Execute the function
update_project_structure()
