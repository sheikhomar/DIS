from pathlib import Path

import gdown

STANDARD_MODEL_URL = (
    "https://drive.google.com/open?id=1KyMpRjewZdyYfxHPYcd-ZbanIXtin0Sn"
)
GENERAL_MODEL_URL = (
    "https://drive.google.com/open?id=/1nV57qKuy--d5u1yvkng9aXW1KS4sOpOi"
)


def download_models() -> None:
    """Download pretrained models from Google Drive"""
    output_dir = Path("saved_models")
    output_dir.mkdir(exist_ok=True, parents=True)
    # Download official weights

    gdown.download(
        STANDARD_MODEL_URL, "saved_models/isnet2.pth", use_cookies=False, fuzzy=True
    )
    gdown.download(
        GENERAL_MODEL_URL,
        "saved_models/isnet-general-use2.pth",
        use_cookies=False,
        fuzzy=True,
    )


def main() -> None:
    """Main function"""
    download_models()


if __name__ == "__main__":
    main()
