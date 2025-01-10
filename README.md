# URL Shortening Application

This is a simple URL shortening service built with Flask. It allows users to shorten long URLs and redirect to the original URLs using a generated short key. The application uses in-memory data structures to store URL mappings.

## Features
- Shorten a long URL to a 6-character unique short URL.
- Redirect to the original URL when the shortened URL is accessed.
- Prevents duplication by checking if a URL has already been shortened.
  
## Installation
1. Clone the repository:
    ```bash
    git clone "https://github.com/havish7728/URL_SHORTENING"
    ```
2. Install required dependencies:
    ```bash
    pip install Flask
    ```
3. Run the application:
    ```bash
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000/` to use the URL shortening service.

## How It Works
1. **Home Page (`/`)**: Users input a long URL, and the app either generates or retrieves a shortened URL.
2. **Redirecting**: The app will redirect to the original URL when the shortened URL is visited.

## How to Use
- Enter the long URL in the input field on the homepage.
- The app will generate a shortened URL which can then be used to redirect to the original URL.
  
## Data Structures Used
- **`url_map`**: Maps shortened URLs (short keys) to their corresponding long URLs.
- **`reverse_map`**: Maps long URLs back to their corresponding shortened URLs for easy lookup.

## Files
- **`app.py`**: Contains the Python backend code using Flask.
- **`templates/index.html`**: HTML form for user input.
- **`templates/result.html`**: Displays the shortened URL after generation.