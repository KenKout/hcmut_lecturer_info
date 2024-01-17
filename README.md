
# HCMUT Lecturer Information Crawler

This Python script allows you to scrape information about lecturers from the Ho Chi Minh City University of Technology (HCMUT) website and store it in a JSON file.

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/KenKout/hcmut_lecturer_info.git
   ```

2. Navigate to the repository's directory:

   ```bash
   cd hcmut_lecturer_info
   ```

3. Install the required Python packages if you haven't already. You can use `pip`:

   ```bash
   pip install requests
   ```

4. Run the `main.py` script:

   ```bash
   python main.py
   ```

   This will fetch lecturer information from the HCMUT website, process it, and save it in a JSON file named `data_lecturer.json` in the same directory.

## Script Explanation

- The script uses the `requests` library to make HTTP requests to the HCMUT website and `re` for regular expressions to parse the HTML data.

- It first fetches a list of department codes from the HCMUT website and then iterates through each department to obtain a list of lecturer IDs.

- For each lecturer ID, it fetches their information such as name, phone number, and email.

- The collected data is then stored in a JSON file (`data_lecturer.json`) in UTF-8 encoding and with proper indentation.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)

## License

This script is available under the [MIT License](LICENSE).

