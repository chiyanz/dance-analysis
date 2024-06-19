from src.video_processor import load_video
from src.pose_estimator import estimate_pose
from src.movement_analyzer import analyze_movement
from src.synchronizer import compare_synchronization

def main():
    video_path = "path/to/your/video.mp4"
    frames = load_video(video_path)
    poses = [estimate_pose(frame) for frame in frames]
    movements = analyze_movement(poses)
    # Assuming synchronization needs to be compared within the same video for simplicity
    sync_score = compare_synchronization(movements, movements)
    print(f"Synchronization Score: {sync_score}")

if __name__ == "__main__":
    main()
