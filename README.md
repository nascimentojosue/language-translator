# Real-Time Language Translator

This project is a real-time language translator that listens to spoken input, translates it into a specified language, and plays back the translated speech. It uses Google’s Speech-to-Text, Text-to-Speech, and translation services.

## Requirements

To run this project, you will need Python and the following libraries:
- `SpeechRecognition` for capturing audio input
- `googletrans` for language translation
- `gTTS` for converting translated text to speech
- `pyaudio` for capturing audio (needed for SpeechRecognition)

### Install Dependencies

Install the required libraries with:
```bash
pip install SpeechRecognition googletrans==4.0.0-rc1 gTTS pyaudio
