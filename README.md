# CV Generator 📄

An automated resume/CV generator that uses Selenium to interact with [Resumave](https://resumave.vercel.app/) to batch-generate PDF resumes from JSON data.

## Features ✨

- **Batch Processing**: Generate multiple resumes from a single JSON file
- **Automated PDF Generation**: Uses Selenium to automate the resume creation process
- **Custom Resume Data**: Store multiple resume configurations in JSON format
- **Firefox Integration**: Configured to automatically download generated PDFs

## Prerequisites 📋

- Python 3.11+
- Firefox browser installed
- GeckoDriver (Firefox WebDriver)

## Installation 🚀

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JethroNatividad/cv-gen.git
   cd cv-gen
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install GeckoDriver**:
   - Download from [Mozilla's GeckoDriver releases](https://github.com/mozilla/geckodriver/releases)
   - Add to your PATH or place in the project directory

## Usage 💡

1. **Prepare your resume data**: Edit `resumes.json` with your resume information. The file should contain an array of resume objects with the following structure:

   ```json
   [
     {
       "state": {
         "personalInfo": {
           "name": "Your Name",
           "email": "your.email@example.com",
           "phone": "+1 234 567 8900",
           "github": "https://github.com/yourusername",
           "linkedin": "https://www.linkedin.com/in/yourprofile",
           "website": "https://yourwebsite.com",
           "summary": "Your professional summary...",
           "jobTitle": "Your Job Title",
           "location": "Your Location"
         },
         "education": [...],
         "experience": [...],
         "skills": [...],
         "projects": [...]
       }
     }
   ]
   ```

2. **Run the generator**:
   ```bash
   python main.py
   ```

3. **Find your generated PDFs**: The script will automatically download PDF files named `{Name}_Resume.pdf` to your default download directory.

## How it Works 🔧

1. **Browser Automation**: Opens Firefox with PDF download preferences configured
2. **Data Injection**: Loads resume data from `resumes.json` and injects it into the Resumave web application's localStorage
3. **PDF Generation**: Triggers the download of each resume as a PDF file
4. **Batch Processing**: Processes all resumes in the JSON file sequentially

## Configuration ⚙️

The script is pre-configured for Firefox with the following settings:
- Automatic PDF downloads (no save dialog)
- Built-in PDF viewer disabled
- Implicit wait of 2 seconds for page elements

## File Structure 📁

```
cv-gen/
├── main.py              # Main automation script
├── requirements.txt     # Python dependencies
├── resumes.json        # Resume data (multiple resumes)
├── env/                # Virtual environment
└── README.md           # This file
```

## Dependencies 📦

- **selenium**: Web browser automation
- **Supporting packages**: Various dependencies for Selenium functionality

See `requirements.txt` for the complete list.

## Troubleshooting 🔍

### Common Issues:

1. **GeckoDriver not found**: Make sure GeckoDriver is installed and in your PATH
2. **Firefox not opening**: Ensure Firefox is installed on your system
3. **Download not working**: Check your Firefox download settings and permissions
4. **Element not found**: The web application might have changed - check if Resumave is accessible

### Debug Mode:

To see the browser automation in action, comment out or modify the headless options in `main.py`.

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License 📝

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments 🙏

- [Resumave](https://resumave.vercel.app/) - The resume builder web application
- [Selenium](https://selenium.dev/) - Web automation framework

---

**Note**: This tool is designed to work with the Resumave web application. If the application's interface changes, the script may need updates to maintain compatibility.
