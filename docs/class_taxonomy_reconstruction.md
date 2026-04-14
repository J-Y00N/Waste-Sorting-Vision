# Checkpoint Label Sets

## Overview

This repository currently exposes two checkpoints with different label sets.
The default `best5.pt` checkpoint uses a 16-class label set for the public app.
The alternate `best.pt` checkpoint uses a 15-class label set stored directly in the checkpoint metadata.

## `best5.pt` Label Set

The table below is the 16-class label set used by the default app checkpoint.

| Class ID | English Label Used in This Repository |
| --- | --- |
| 0 | Paper |
| 1 | Paper Pack |
| 2 | Paper Cup |
| 3 | Vinyl |
| 4 | Vinyl with Contaminants |
| 5 | Plastic |
| 6 | Plastic with Contaminants |
| 7 | Reusable Glass |
| 8 | Brown Glass |
| 9 | Green Glass |
| 10 | White Glass |
| 11 | Other Glass |
| 12 | Can |
| 13 | PET |
| 14 | Styrofoam |
| 15 | Battery |

## `best.pt` Label Set

The alternate checkpoint stores the following 15 labels inside the model:

| Class ID | Embedded Label |
| --- | --- |
| 0 | `paper` |
| 1 | `can` |
| 2 | `glass` |
| 3 | `pet` |
| 4 | `plastic` |
| 5 | `vinyl` |
| 6 | `foam` |
| 7 | `battery` |
| 8 | `paper + f_s` |
| 9 | `can + f_s` |
| 10 | `o glass + f_s` |
| 11 | `pet + f_s + m-p_m` |
| 12 | `plastic + f_s` |
| 13 | `vinyl + f_s` |
| 14 | `foam + f_s` |

## Notes

- The app now switches label mappings with the selected checkpoint.
- Earlier training iterations also experimented with smaller class sets, which are summarised in [experiment_history.md](experiment_history.md).
- The best historical score in the experiment summary came from an 8-class run rather than from the bundled 15-class or 16-class app checkpoints.
