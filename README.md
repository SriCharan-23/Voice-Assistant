# Astra — Voice Assistant 🎤

Astra is a Python-based voice assistant that listens for a wake word, executes simple commands (opening websites, playing music), and falls back to Google's Gemini AI for open-ended questions it doesn't have a built-in command for.

## Features

- Wake word detection ("Astra") using `speech_recognition`
- Voice commands to open Google, YouTube, Instagram, Facebook, and LinkedIn
- Play songs from a local music library dictionary
- Fallback to Gemini AI for any question outside the built-in commands
- Text-to-speech responses using `pyttsx3`
- Markdown cleanup so Gemini's responses sound natural when spoken aloud

## Tech Stack

- Python 3
- `speech_recognition` — converts spoken audio to text
- `pyttsx3` — converts text responses to speech
- `google-genai` — connects to Google's Gemini models for general Q&A
- `python-dotenv` — keeps the Gemini API key out of source code

## Project Structure

```
Voice Assistant/
├── main.py              # Core assistant logic
├── musiclibrary.py       # Dictionary mapping song names to URLs
├── .env                  # Stores your Gemini API key (not committed to git)
└── requirements.txt       # Python dependencies
```

**Note:-** Create a new file with name musiclibrary.py and in that add music with any name and the link of music as a python dictionary(i.e., in key- value pair) and make sure you save that file.

## Setup

### 1. Clone or download the project

```
git clone <your-repo-url>
cd "Voice Assistant"
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

Or install manually:

```
pip install speechrecognition pyttsx3 google-genai python-dotenv
```

### 3. Add your Gemini API key

Get a free key from [Google AI Studio](https://aistudio.google.com/apikey).

Create a file named `.env` in the project folder:

```
GEMINI_API_KEY=your_actual_key_here
```

Never commit this file to GitHub. Add it to `.gitignore`:

```
.env
```

### 4. Run the assistant

```
python main.py
```

Say **"Astra"** to wake it up, then give a command such as:

- "Open YouTube"
- "Open Google"
- "Play `<song name>`"
- Any general question (e.g. "What's the capital of France?") — this gets answered by Gemini

## How It Works

1. `speech_recognition` continuously listens for the wake word "Astra".
2. Once triggered, it records your next spoken command.
3. `processcommand()` checks the command against known keywords (open google, open youtube, play, etc.).
4. If no match is found, the command is sent to Gemini via `ask_gemini()`.
5. Gemini's response is cleaned of markdown formatting (`clean_text()`) and spoken aloud using `pyttsx3`.

## Adding New Songs

Open `musiclibrary.py` and add entries to the dictionary:

```python
Music = {
    "song_name": "https://youtube.com/link-to-song"
}
```

## Roadmap / Future Enhancements

- [ ] More built-in commands (weather, reminders, system controls)
- [ ] Conversation memory so Gemini can handle follow-up questions

## Notes

- This project is a work in progress and intended primarily as a learning exercise in combining speech recognition, text-to-speech, and LLM APIs.
- Microphone access requires running on a machine with a working mic; it will not function on a headless server.

## License

This project is open for personal learning and modification. Add a license of your choice if publishing publicly.
