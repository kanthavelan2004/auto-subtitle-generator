# Auto Subtitle Generator - User Guide

## System Requirements
- Windows 10/11 (64-bit)
- Java 21 or later
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space

---

## First-Time Setup

### Step 1: Install Java (if not already installed)
1. Download Java 21 from: https://www.oracle.com/java/technologies/downloads/
2. Run the installer
3. Restart your computer

### Step 2: Install Miniconda (if not already installed)
1. Download from: https://docs.conda.io/en/latest/miniconda.html
2. Run the installer
3. Use default settings

### Step 3: Setup Python Environment
1. Double-click `install_python.bat`
2. Wait for installation to complete (5-10 minutes)
3. Close the window when it says "Setup Complete!"

---

## Running the Application

Double-click `run.bat`

The application window will open automatically.

---

## How to Use

1. **Choose Video**: Click to select your video file (MP4, AVI, MKV, MOV)
2. **Select Model**: 
   - tiny: Fastest, good accuracy
   - base: Recommended for most videos
   - small: Better accuracy, slower
   - medium/large: Best accuracy, very slow
3. **Generate Subtitles**: Click the button and wait
4. **Find Your Subtitles**: They're saved next to your video file with .srt extension

---

## Tips

- First run downloads AI model (~150MB, one-time only)
- Processing time: approximately 30% of video length
- A 10-minute video takes about 3 minutes to process
- Subtitle file is saved with same name as video: `video.mp4` → `video.srt`

---

## Troubleshooting

### "Java is not installed" error
- Install Java 21 from the link above
- Restart your computer after installation

### "Python environment not found" error
- Run `install_python.bat` first
- Make sure it completes successfully

### Application doesn't start
- Right-click `run.bat` and "Run as Administrator"
- Check if Java is installed: Open Command Prompt and type `java -version`

### Subtitles have wrong timing
- Try a larger model (small or medium)
- Make sure audio quality is good

### "Out of memory" error
- Close other applications
- Use a smaller model (tiny or base)
- Process shorter video segments

---

## Support

For issues or questions:
- Check the log area in the application for detailed error messages
- Make sure all prerequisites are installed
- Try processing a short test video first

---

## File Structure

```
AutoSubtitleGenerator/
├── run.bat                    ← Double-click this to run
├── install_python.bat         ← Run this once for setup
├── AutoSubtitleApp-1.0-SNAPSHOT.jar
├── generate_subtitles.py
└── README.txt                 ← You are here
```

---

## Advanced: Command Line Usage

If you prefer command line:

```bash
conda activate subtitle
python generate_subtitles.py "video.mp4" "output.srt" base
```

---

Version 1.0
Created with Java, Python, and Faster-Whisper