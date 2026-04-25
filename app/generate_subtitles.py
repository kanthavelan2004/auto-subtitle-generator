import sys
import os
from faster_whisper import WhisperModel

def format_time(seconds):
    """Convert seconds to SRT timestamp format (HH:MM:SS,mmm)"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def generate_subtitles(video_path, output_path, model_size="base"):
    """
    Generate subtitles for a video file
    
    Args:
        video_path: Path to the video/audio file
        output_path: Path where to save the .srt subtitle file
        model_size: Whisper model size (tiny, base, small, medium, large)
    """
    try:
        print(f"Loading Whisper model ({model_size})...")
        print(f"Video path: {video_path}")
        print(f"Video exists: {os.path.exists(video_path)}")
        
        # Load the model (CPU version - works on any computer)
        # For GPU: device="cuda", compute_type="float16"
        print("Initializing model (this downloads ~150MB on first run)...")
        
        # Try with local_files_only first (if model already exists)
        try:
            model = WhisperModel(model_size, device="cpu", compute_type="int8", local_files_only=True)
            print("Model loaded from cache!")
        except Exception:
            # If not cached, download it (might need SSL fix)
            print("Downloading model from Hugging Face...")
            os.environ['CURL_CA_BUNDLE'] = ''
            os.environ['REQUESTS_CA_BUNDLE'] = ''
            model = WhisperModel(model_size, device="cpu", compute_type="int8", local_files_only=False)
            print("Model downloaded and loaded successfully!")
        
        print(f"Transcribing: {video_path}")
        print("This may take a few minutes depending on video length...")
        
        # Transcribe the video
        segments, info = model.transcribe(video_path, beam_size=5)
        
        print(f"Detected language: {info.language} (probability: {info.language_probability:.2f})")
        
        # Generate SRT file
        with open(output_path, 'w', encoding='utf-8') as f:
            segment_number = 1
            for segment in segments:
                # Write subtitle number
                f.write(f"{segment_number}\n")
                
                # Write timestamp
                start_time = format_time(segment.start)
                end_time = format_time(segment.end)
                f.write(f"{start_time} --> {end_time}\n")
                
                # Write text
                f.write(f"{segment.text.strip()}\n\n")
                
                segment_number += 1
                
                # Print progress
                print(f"[{format_time(segment.start)}] {segment.text.strip()}")
        
        print(f"\nSubtitles saved to: {output_path}")
        return True
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_subtitles.py <video_path> <output_path> [model_size]")
        print("Example: python generate_subtitles.py video.mp4 subtitles.srt base")
        sys.exit(1)
    
    video_path = sys.argv[1]
    output_path = sys.argv[2]
    model_size = sys.argv[3] if len(sys.argv) > 3 else "base"
    
    # Validate video file exists
    if not os.path.exists(video_path):
        print(f"ERROR: Video file not found: {video_path}")
        sys.exit(1)
    
    # Generate subtitles
    success = generate_subtitles(video_path, output_path, model_size)
    
    sys.exit(0 if success else 1)