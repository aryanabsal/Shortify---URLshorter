# Shortify - URL Shortener

Shortify shortens long URLs and acts as a bridge to your destination.

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/aryanabsal/Shortify---URLshorter.git
   cd Shortify---URLshorter
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Migrate database:
   ```bash
   python manage.py migrate
   ```
5. Run the server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Enter a URL to get a short link.
- Use the admin panel for management.

## License
**MIT License**
