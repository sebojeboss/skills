# Edit and export media

## When to read

Read when preparing a local cut, timing change, composite or editable delivery. Use the user's existing editor, available agent media tools or FFmpeg as appropriate.

## Establish the edit

Inspect the source and decisive interval using [media inspection](media-inspection-contract.md). Mark the source in/out points, intended output duration, audio treatment and acceptance condition. Preserve camera originals and the last accepted version. A trim changes what is shown; a speed change alters performance and can make a physical action misleading.

Apply source-time cuts before reasoning about retimed duration. Expected output duration is `(source end − source start) / speed multiplier`. Treat this as a planning check, not proof of frame accuracy, natural speech or synchronization. For variable-frame-rate material, inspect actual boundary frames and audio alignment.

Use a native timeline for montage, captions, tracked masks, layered graphics, mixed audio and client-editable work. For a simple local trim or retime, use the installed editor or FFmpeg interface and verify its supported filters and codecs. If changing speed, decide whether audio should follow, be replaced, or remain untouched; avoid accidental pitch or sync changes.

## Export and verify

Choose dimensions, aspect ratio, frame rate, color handling, audio and file format for the actual destination. Preserve a color-managed pipeline for HDR or other special footage. A generic SDR transcode is not a universal mastering method. Write a new export, retain the source project when editability is required, and inspect the final rendered file rather than relying only on timeline playback.

Check the opening and ending, crop and safe areas, caption timing/readability, action continuity, voice, music and lip sync. Confirm that the file decodes and its duration is plausible. A playable file can still contain the wrong product, claim or take. Use the acceptance criteria for the creative itself.

If an export fails, identify the source, settings and partial output before retrying. Keep accepted work intact. Never interpret a queued job, command exit or output filename as approval. Record the useful edit decisions and output version.

## Worked decision

Illustrative: a three-second take contains idle lead-in, the action and a clean ending. Selecting source time 0.5–2.5 seconds and applying 2× speed produces roughly one second. Applying a one-second duration limit to the untrimmed source answers a different question. If the filmed action is wrong, a correctly timed cut does not repair its factual meaning.

## Deliver the work

Provide the requested export plus the source/timeline and selected assets needed for future edits. Identify any unsupported effect or unavailable tool precisely, with a usable editor handoff. Do not claim generation, upload, playback review or approval unless it occurred. Keep private media and paths within the user's approved tools and storage.
