# Inspect local media

## When to read

Read when an edit or claim depends on duration, stream identity, frame timing, motion or sound. A successful decode establishes file readability; it does not mean anyone watched or listened.

## Inspect the decisive interval

Use the agent's available video/audio tools, an existing editor, or local FFmpeg/ffprobe. Check what the current host can actually expose to the model. Suggest installing a missing tool only when it is needed for the task. Keep originals intact and use a new location for derived files.

Start with file identity, duration, dimensions, orientation, frame rate and available audio streams. Variable frame rate requires actual timestamps; do not infer an exact time from a frame number divided by a nominal rate. Inspect a sparse overview when helpful, then the connected interval around the action, cut or pronunciation being judged. Record which frames and intervals were inspected. A still cannot establish contact over time, intelligibility, lip sync or an unseen ending.

Use native playback or supported continuous perception for motion and speech. If only captions and stills are available, limit conclusions accordingly. Clicking Play does not establish that the assistant received the audio/video. Compare the supplied version with the relevant accepted version before requesting a new take.

## Prepare evidence carefully

For repeated reviews, retain the source filename/version, relevant timestamps and, when identity matters, a locally computed hash. A hash identifies bytes, not rights or truth. Preserve subtitle timing and native orientation. Inspect adjacent frames around a decisive transition; coarse seeking can land away from the requested frame. Verify the extracted image against its source timestamp before treating it as exact evidence.

When an input is a URL, obtain authorized media through the supported source route first. Do not treat a remote URL as a local path or blindly pass playlists to a command that may fetch additional resources. Keep credentials and signed URLs out of shared diagnostics. After a failed extraction, distinguish usable derivatives from incomplete output and preserve completed inspection notes; do not overwrite originals to retry.

## Return what was observed

State the version, interval and inspection mode supporting each consequential judgment. Distinguish a decode check, sampled visual inspection, continuous viewing and listening. Local extraction does not authorize uploading media to another perception service. Screenshots are working material; original footage and accepted production assets follow the owner's retention policy.

Use the installed tool's help and official [ffprobe](https://ffmpeg.org/ffprobe.html) or [FFmpeg filter](https://ffmpeg.org/ffmpeg-filters.html) documentation for its current interface. Check the actual build, codec support and media rights before processing or exporting.
