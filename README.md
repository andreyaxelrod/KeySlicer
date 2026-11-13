# KeySlicer

Turn a screen recording into a set of screenshots. KeySlicer finds keyframes automatically and lets you refine the selection on a timeline.

**[Download KeySlicer 1.0.33 (.dmg)](https://github.com/andreyaxelrod/KeySlicer/releases/download/v1.0.33/KeySlicer-1.0.33.dmg)** · macOS 15 or later · Apple Silicon and Intel

## Updating from 1.0.29

The automatic installer in 1.0.29 cannot start. Its update window now shows a download link instead. [Download 1.0.33](https://github.com/andreyaxelrod/KeySlicer/releases/download/v1.0.33/KeySlicer-1.0.33.dmg), quit KeySlicer, open the DMG, and drag KeySlicer to Applications, replacing the existing copy. This one-time manual update installs the corrected updater permissions. You do not need to uninstall KeySlicer first.

## What you can do

- Drop in a video and automatically capture distinct screens. Adjust scan settings or add and remove keyframes on the timeline.
- Keep recent videos in a sidebar, resume the last opened video, and reuse locally cached analysis. Analysis continues when you switch videos. Stop a video's analysis from its ellipsis menu and keep the screenshots collected so far.
- Expand the timeline with **⌘T** to work with long recordings. Select multiple screenshots, scrub freely without changing your selection, delete them together, and undo up to 40 deletion actions.
- Stitch scrolling footage into a long screenshot. The gallery shows the start and end times of each stitch.
- Select a range with Shift-click or individual screenshots with Command-click. Drag a rectangle across cards or blank gallery space, including galleries with one or two screenshots; hold Command or Shift to add to the selection. Export only the checked cards to ZIP, clipboard, Figma or AirDrop.
- Delete selected screenshots with the blue trash button beside Export. Gallery controls stay aligned to the right.
- See exactly how many screenshots will be exported in the Export menu, with a localized count above Copy to Figma.
- Right-click a screenshot to save that card or copy it to Figma. With multiple cards checked, the menu acts on the checked group.
- Copy screenshots into Figma as an Auto Layout frame, copy them to the clipboard, or export a ZIP.
- Choose Dark, Light, or System default appearance. Dark is the default.
- Choose from 21 interface languages, with right-to-left layout for Arabic, Hebrew, and Urdu.

Video analysis runs locally on your Mac.

Liquid Glass is available on macOS 26 and later. macOS 15 uses standard non-glass backgrounds and controls.

## Supported video formats

- MP4 (`.mp4`, `.mpg4`), QuickTime (`.mov`, `.qt`), and M4V (`.m4v`)
- AVI (`.avi`, `.vfw`) and DV (`.dv`, `.dif`)
- MPEG (`.mpg`, `.mpeg`, `.mpe`, `.m75`, `.m15`), MPEG-2 video (`.m2v`), and MPEG transport stream (`.ts`)
- 3GPP (`.3gp`, `.3gpp`, `.sdv`) and 3GPP2 (`.3g2`, `.3gp2`)
- WebM (`.webm`)

For formats handled by macOS, compatibility also depends on the codec inside the file.

## Install and update

1. Download the `.dmg` from the [latest release](https://github.com/andreyaxelrod/KeySlicer/releases/latest).
2. Open it and drag **KeySlicer** to **Applications**.
3. Open KeySlicer from Applications. If macOS blocks the first launch, follow the instructions in the disk image.

Already installed? Open **KeySlicer → Check for Updates…**.

## License

KeySlicer is free to install and use. See the [KeySlicer license](LICENSE.md).

KeySlicer bundles [FFmpeg](https://ffmpeg.org/) under the [GNU Lesser General Public License, version 2.1 or later](https://ffmpeg.org/legal.html). The corresponding source and build instructions are available in `FFmpeg-source.zip` on the [release page](https://github.com/andreyaxelrod/KeySlicer/releases/latest).

## Feedback

[Report a bug or suggest an improvement](https://github.com/andreyaxelrod/KeySlicer/issues). Include your macOS and KeySlicer versions and the steps to reproduce the issue.

Kudos to Aleksei Bogomolov
