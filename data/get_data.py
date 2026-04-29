from pathlib import Path
import shutil

import kagglehub


def main() -> None:
	dataset_path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
	destination = Path.cwd()

	for item in Path(dataset_path).iterdir():
		target = destination / item.name
		if item.is_dir():
			shutil.copytree(item, target, dirs_exist_ok=True)
		else:
			shutil.copy2(item, target)

	print(f"Dataset copied to: {destination}")


if __name__ == "__main__":
	main()