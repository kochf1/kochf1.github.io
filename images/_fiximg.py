from PIL import Image
import glob
import os

def main():
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Promo message
    print(f"🚀 Running at #{base_dir}")

    # Define resize tasks
    resize_tasks = [
        {"pattern": "*-banner.png", "size": (None, 300)},
        {"pattern": "*-headshot.png", "size": (None, 200)},  # Maintain aspect ratio
    ]

    # Process each task
    for task in resize_tasks:
        pattern_path = os.path.join(base_dir, '**', task["pattern"])
        image_files = glob.glob(pattern_path, recursive=True)

        for img_path in image_files:
            try:
                with Image.open(img_path) as img:
                    orig_width, orig_height = img.size
                    target_width, target_height = task["size"]

                    # Calculate missing dimension if None
                    if target_width is None and target_height is not None:
                        aspect_ratio = orig_width / orig_height
                        target_width = int(target_height * aspect_ratio)
                    elif target_height is None and target_width is not None:
                        aspect_ratio = orig_height / orig_width
                        target_height = int(target_width * aspect_ratio)

                    resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                    resized_img.save(img_path)
                    print(f"✅ Resized:  {os.path.basename(img_path)}→ {task['size']}")
            except Exception as e:
                print(f"❌ Failed: {img_path} — {e}")

if __name__ == "__main__":
    main()



