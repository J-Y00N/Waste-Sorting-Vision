# Preprocessing Summary

## Positioning

This note gives a high-level overview of the preprocessing work that supported training.
For public release, the focus is on the workflow categories rather than publishing every utility script.

## Surviving Script Categories

### File and folder normalization

- zip extraction
- subfolder renaming
- filename-only normalization

### Format conversion

- JPG to PNG conversion
- JSON to TXT conversion
- JSON to YAML conversion
- YAML to TXT conversion

### Validation and matching

- bounding box inspection
- YOLO visualisation
- image/JSON matching
- image/label matching

### Label transformation

- class label remapping
- string-to-int conversion
- label dictionary mapping
- label removal
- class count checks

### Sampling and extraction

- random image and label extraction
- numeric filtering
- class-selective image extraction
- label extraction

## Recommended Public Framing

Recommended wording:

- `Preprocessing involved multiple ad hoc scripts for conversion, validation, remapping, and sampling.`
- `This repository summarises the preprocessing workflow at a high level and focuses on the final app and model results.`

## Documentation Choice

This summary is intentionally brief because the public repository is centred on the deployed app, experiment history, and modelling outputs rather than script-level implementation details.
