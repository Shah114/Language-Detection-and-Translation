## Language-Detection-and-Translation
This project is a web-based application that detects the language of a given text and translates it into the desired target language. The application is built using the Flask web framework and utilizes the googletrans module for language detection and translation. The user interface is crafted with HTML to ensure a smooth and user-friendly experience. The application provides two translation options: <br/>
* app.py: Uses the googletrans module.
* app_2.py: Uses the easygoogletranslate module. <br/>
<br/>

## Features
* Language Detection: Automatically detects the language of the input text.
* Text Translation: Translates the input text into the selected target language using either the googletrans or easygoogletranslate module.
* Simple Web Interface: User-friendly design with intuitive controls. <br/>
<br/>

## Installation

```python
git clone https://github.com/Shah114/language-detection-translation.git
cd language-detection-translation

pip install Flask googletrans==4.0.0-rc1
```
<br/>

## Usage
Navigate to the project directory. <br/>
* Option 1: Using googletrans (app.py) <br/>
Run the Flask application: <br/>
```bash
python app.py
```
<br/>
Open your web browser and go to http://localhost:5000/. <br/>

* Option 2: Using easygoogletranslate (app_2.py) <br/>
Run the Flask application: <br/>
```bash
python app_2.py
```
<br/>
Open your web browser and go to http://localhost:5000/. <br/>

Enter the text you want to analyze and select the target language for translation. <br/>
<br/>

## Contributing
Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change. <br/>
<br/>






