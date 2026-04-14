from __future__ import annotations

from .config import CONFIGS_DIR, load_yaml


def load_class_names() -> dict[int, str]:
    raw = load_yaml(CONFIGS_DIR / "class_names.yaml")
    return {int(k): str(v) for k, v in raw["class_names"].items()}


def get_class_name(class_id: int, class_names: dict[int, str] | None = None) -> str:
    mapping = class_names or load_class_names()
    return mapping.get(class_id, f"class_{class_id}")
