# 1. Use the official Playwright image which has Python and Browsers pre-installed
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# 2. Set the directory inside the container where our code will live
WORKDIR /app

# 3. Copy our requirements file first (for better caching)
COPY requirements.txt .

# 4. Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your project code into the container
COPY . .

# 6. Set the default command to run your tests
# We use --base-url as an example of how to pass arguments
CMD ["pytest", "--browser", "chromium"]