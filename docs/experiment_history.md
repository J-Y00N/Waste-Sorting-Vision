# Experiment History

## Source Note

This table condenses the main training iterations recorded in the project summary document.
It provides a compact view of how model size, image size, class design, and dataset scale changed across runs.

## Training Iterations

| Train | Model | Image Size | Dataset Volume | Classes | Note |
| --- | --- | ---: | ---: | ---: | --- |
| 1st | yolov8m | 640 | 9,000 | 15 | Initial dataset composition. |
| 2nd | yolov8m | 640 | 9,000 | 15 | Supplemented underrepresented `Vinyl with Contaminants` data. |
| 3rd | yolov8m | 640 | 9,000 | 11 | Dataset and class structure reorganised. |
| 4th | yolov8s | 640 | 9,000 | 11 | Switched model from `yolov8m` to `yolov8s`. |
| 5th | yolov8s | 640 | 9,000 | 8 | Focused class design on recyclable objects only. |
| 6th | yolov8s | 640 | 38,000 | 8 | Significantly increased dataset size. |
| 7th | yolov8s | 640 | 38,000 | 16 | Expanded classes from 8 to 16, including contaminants and bottle colours. |
| 8th | yolov8s | 1280 | 9,000 | 11 | Increased image size from 640 to 1280. |
| 9th | yolov8s | 1280 | 9,000 | 8 | Increased image size from 640 to 1280. |

## Metrics Summary

| Train | Precision (1.00 at) | Recall (at 0.00) | F1 Score | mAP@50 |
| --- | ---: | ---: | ---: | ---: |
| 1st | 1.000 | 0.95 | 0.74 | 0.791 |
| 2nd | 1.000 | 0.93 | 0.70 | 0.735 |
| 3rd | 0.991 | 0.96 | 0.81 | 0.868 |
| 4th | 0.993 | 0.95 | 0.80 | 0.867 |
| 5th | 0.984 | 0.96 | 0.84 | 0.888 |
| 6th | 0.979 | 0.99 | 0.91 | 0.957 |
| 7th | 0.988 | 0.96 | 0.79 | 0.841 |
| 8th | 0.993 | 0.97 | 0.82 | 0.882 |
| 9th | 0.992 | 0.97 | 0.86 | 0.911 |

Note:
These metrics were recorded as `100 Epochs` and `best.pt` in the original summary document.

## Interpretation

- The experiment history shows repeated iteration on class granularity, image size, and dataset scale.
- The highest `mAP@50` value in the summary table is `0.957` for the 6th training iteration.
- Later class expansion to 16 classes appears to have increased task difficulty relative to the 8-class setup.
