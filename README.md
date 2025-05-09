# Cali Food Connect

A simple, interactive Streamlit application that helps users in California locate their nearest food-bank donation center. Using a 1-Nearest Neighbors model built on real food-bank locations, combined with Google Maps geocoding and embedded directions, the app routes donors to the closest center based on a free-text address or sample city selection.

## Features

* **Free-text or dropdown input**: Enter any California address or select from a list of major cities.
* **Real-world centers**: Nine established California food banks, each with exact street addresses.
* **KNN routing**: A 1‑NN model locates the nearest center based on latitude/longitude.
* **Distance calculation**: Displays the geodesic distance in kilometers.
* **Google Maps integration**: Geocoding of user input and embedded directions widget for visual routing.

## Demo

![Streamlit App Screenshot](images/screenshot.png)
*Example of the app in action.*

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/food-connect-application.git
   cd food-connect-application
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Google Maps API key**

   * Create or edit `.streamlit/secrets.toml` in the project root:

     ```toml
     GOOGLE_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
     ```
   * Ensure you have enabled the **Geocoding API** and **Maps Embed API** in your Google Cloud Console.

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Enter a California address or select a sample city from the dropdown.
* Click **Find Nearest Center** to view the closest food bank and the route.

## Project Structure

```
food-connect-application/
├── .streamlit/
│   └── secrets.toml      # Contains GOOGLE_API_KEY (ignored by Git)
├── images/
│   └── screenshot.png   # App screenshot for README
├── models.py            # KNN model and center data
├── app.py               # Streamlit application
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Contributing

Contributions are welcome! Please open an issue or PR to suggest improvements, new features, or fixes.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements

* [Streamlit](https://streamlit.io)
* [Scikit-learn](https://scikit-learn.org)
* [Geopy](https://geopy.readthedocs.io)
* [Google Maps Platform](https://cloud.google.com/maps-platform)
