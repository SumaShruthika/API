# OpenWeatherMap Weather Fetcher

This project fetches current weather data for a specified city using the OpenWeatherMap API and saves it to a CSV file.

## Features

- Fetches weather data for any city
- Saves results to `weather_data.csv`
- Uses a `.env` file for API keys and configuration
- Easy setup with a bootstrap script

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd API
```

### 2. Create a `.env` file

Copy `.env.example` to `.env` and fill in your details:

```env
API_KEY=your_openweathermap_api_key
CITY=your_city_name
```

### 3. Set up the environment

Run the bootstrap script to create a virtual environment and install dependencies:

```bash
source bootstrap.sh
```
> **Note:** Use `source` (not `bash`) so the virtual environment stays active in your shell.

### 4. Run the application

```bash
python open_weather_app.py
```

## Output

- Weather data is saved to `weather_data.csv` (ignored by git).

## Notes

- Do **not** commit your `.env` file. It is listed in `.gitignore` for your safety.
- To deactivate the virtual environment, run:
  ```bash
  deactivate
  ```

## Troubleshooting

- If you change the `.env` file, make sure to restart your terminal or VS Code session.
- If `weather_data.csv` is tracked by git, remove it with:
  ```bash
  git rm --cached weather_data.csv
  git commit -m "Stop tracking weather_data.csv"
  git push
  ```

