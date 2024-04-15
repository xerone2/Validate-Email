# Email Address Validation Script

This Python script utilizes the Cloudmersive Validate API to validate email addresses. It checks whether an email address is valid, and if it is not disposable, it verifies if the root domain of the email is in a list of valid domains.

## Requirements

- Python 3.x
- Cloudmersive Validate API key (sign up at [Cloudmersive](https://cloudmersive.com/validate-api))

## Installation

1. Clone or download the repository to your local machine.
2. Install the required Python packages:

   ```bash
   pip install cloudmersive-validate-api-client
   ```

## Configuration

1. Obtain an API key from Cloudmersive.
2. Replace `'Your-api-key'` in the script with your actual API key.

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Enter the email address you want to verify when prompted.

## Output

The script will output the full validation response from the Cloudmersive Validate API, including whether the email address is disposable, and if not, additional information about the email address.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or bug fixes.
