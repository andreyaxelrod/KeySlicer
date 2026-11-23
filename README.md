# KeySlicer

KeySlicer is free to download and use on macOS. It turns existing screen recordings into screenshots, finds distinct screens automatically, and stitches scrolling footage into long screenshots. Refine the selection on a timeline, then save the screenshots, copy them to the clipboard, or paste them into Figma.

**[Download for free](https://github.com/andreyaxelrod/KeySlicer/releases/latest)** · macOS 15 or later

## Extract screenshots from a screen recording and paste them into Figma

For example, turn an MP4 or MOV recording of a product walkthrough into a set of screens for a design review.

1. Open the recording in KeySlicer. It detects distinct screens and places them on the timeline.
2. Review the results and check the screenshots you want to export.
3. Choose **Export → Copy to Figma**, then paste into your Figma file. The screenshots appear together in an Auto Layout frame.

## What you can do

- Open or drop one or several videos and automatically capture distinct screens. Adjust scan settings or add and remove keyframes on the timeline.
- Keep recent videos in a sidebar, resume the last opened video, and reuse locally cached analysis. Analysis continues when you switch videos. Stop a video's analysis from its ellipsis menu and keep the screenshots collected so far.
- Expand the timeline with **⌘T** to work with long recordings. Select multiple screenshots, scrub freely without changing your selection, delete them together, and undo up to 30 deletion actions.
- Stitch scrolling footage into a long screenshot. The gallery shows the start and end times of each stitch.
- Select a range with Shift-click or individual screenshots with Command-click. Start a selection rectangle in a gallery gap or blank space, including below a short gallery. Hold Command or Shift to add to the selection. Click outside the checked group to clear it. Double-click empty space in the gallery or below the video to exit multiselect. Drag near a gallery or expanded timeline edge to scroll to additional frames. Export only the checked cards to ZIP, clipboard, Figma or AirDrop.
- Delete selected screenshots with Backspace or the trash button beside Export, including immediately after rectangle selection. Deleting the final screenshot exits multiselect; undo restores the batch. Add new keyframes while selecting to include them in the checked group. Gallery controls stay aligned to the right.
- Start dragging a selection rectangle in the free area below the video or around the timeline to enter multiselect automatically and select keyframes without moving playback; hold Command or Shift to add to your selection. Dragging a marker to stitch shakes the markers instead: exit multiselect to stitch. Ruler, wheel and keyboard scrubbing keep your checks intact.
- See exactly how many screenshots will be exported in the Export menu, with a localized count above Copy to Figma.
- Drag a screenshot or a checked group out of the gallery as individual, full-resolution image files. The files use your export format, with PNG as the default.
- Right-click a screenshot to save that card or copy it to Figma. With multiple cards checked, the menu acts on the checked group.
- Copy screenshots into Figma as an Auto Layout frame, copy images to the clipboard, or export a ZIP. Command-C copies images by default; choose another clipboard export in General settings. Progress and a success checkmark appear without changing the Export button width.
- Use Command-A to select all screenshots, Command-Shift-A to clear the selection, Escape to leave multiselect, and Command-Z to undo deletion. Playback stays available during selection; shortcuts work across keyboard layouts.
- Adjust volume from a compact vertical control. Playback starts muted. Sidebars collapse as the window narrows.
- Automate imports and exports with watched folders. Optional deletion of app-owned working copies is available when both input and output are configured; originals are preserved.
- Choose Dark, Light, or System default appearance. Dark is the default.
- Choose from 33 interface languages with right-to-left (RTL) support.

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

Open the downloaded DMG and drag KeySlicer into Applications. To update an installed copy, choose **KeySlicer → Check for Updates…**.

By Andrey Axelrod  
Kudos to Aleksei Bogomolov

[License](LICENSE.md)
