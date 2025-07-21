# Project 03
## Description
This project is a Flask application that serves as a basic web service. It includes a simple route that returns a welcome message.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone    <repository-url>
   ```  
2. Navigate to the project directory:
   ```bash
    cd Project03
    ```
3. Create a virtual environment:
   ```bash  
    python -m venv venv
   ```
4. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
5. Install the required packages:
   ```bash  
    pip install -r requirements.txt
    ```
6. Set the environment variable for Flask:
   ```bash
   export FLASK_APP=run.py
   ```
   On Windows, use:
   ```bash
   set FLASK_APP=run.py
   ```
7. Run the application:
   ```bash      
    flask run
    ```
8. Open your web browser and go to `http:// 
