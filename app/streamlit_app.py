"""Thin Streamlit entry point for the waste sorting app."""

from pathlib import Path
import sys

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from waste_sorting_vision.class_names import load_class_names
from waste_sorting_vision.config import load_app_config
from waste_sorting_vision.detector import (
    ModelResolutionError,
    list_model_options,
    load_detector_cached,
    resolve_model_path,
)
from waste_sorting_vision.ui.image_panel import render_image_panel
from waste_sorting_vision.ui.video_panel import render_video_panel


def _resolve_default_model_index(model_options: dict[str, str], default_model_key: str) -> int:
    option_keys = list(model_options.keys())
    if not option_keys:
        raise ModelResolutionError("No model options are configured.")
    if default_model_key in model_options:
        return option_keys.index(default_model_key)
    return 0


def main() -> None:
    app_config = load_app_config()
    defaults = app_config["defaults"]
    ui = app_config["ui"]
    features = app_config["features"]
    video_config = app_config.get("video", {})

    st.set_page_config(
        page_title=ui["app_title"],
        page_icon="♻️",
        layout="wide",
    )
    st.title(ui["app_title"])
    st.caption(
        "Image and video waste detection app with configurable checkpoints and supporting project notes."
    )

    model_options = list_model_options()

    with st.sidebar:
        st.header("Inference Settings")
        default_model_index = _resolve_default_model_index(
            model_options=model_options,
            default_model_key=defaults["model_key"],
        )
        model_key = st.selectbox(
            "Checkpoint",
            options=list(model_options.keys()),
            index=default_model_index,
            format_func=lambda key: model_options[key],
        )
        confidence = float(
            st.slider(
                "Confidence threshold",
                min_value=0.10,
                max_value=0.95,
                value=float(defaults["confidence"]),
                step=0.05,
            )
        )

    try:
        model_path = resolve_model_path(model_key)
        detector = load_detector_cached(str(model_path))
        class_names = load_class_names(model_key)
    except (ModelResolutionError, ImportError, ModuleNotFoundError) as exc:
        st.error(
            "Unable to load the configured checkpoint. Add the model file under "
            "`models/` or point the matching environment variable to a valid path."
        )
        st.exception(exc)
        st.stop()
    except KeyError as exc:
        st.error("Unable to resolve the label mapping for the selected checkpoint.")
        st.exception(exc)
        st.stop()

    st.sidebar.caption(f"Resolved checkpoint: `{model_path}`")

    if features.get("enable_image_inference") and features.get("enable_video_inference"):
        image_tab, video_tab = st.tabs(["Image", "Video"])
        with image_tab:
            render_image_panel(
                detector=detector,
                class_names=class_names,
                confidence=confidence,
                enable_download=features.get("enable_download_annotated_image", True),
            )
        with video_tab:
            render_video_panel(
                detector=detector,
                class_names=class_names,
                confidence=confidence,
                frame_stride=int(video_config.get("frame_stride", 12)),
                max_frames=video_config.get("max_frames"),
            )
        return

    if features.get("enable_image_inference"):
        render_image_panel(
            detector=detector,
            class_names=class_names,
            confidence=confidence,
            enable_download=features.get("enable_download_annotated_image", True),
        )

    if features.get("enable_video_inference"):
        render_video_panel(
            detector=detector,
            class_names=class_names,
            confidence=confidence,
            frame_stride=int(video_config.get("frame_stride", 12)),
            max_frames=video_config.get("max_frames"),
        )


if __name__ == "__main__":
    main()
