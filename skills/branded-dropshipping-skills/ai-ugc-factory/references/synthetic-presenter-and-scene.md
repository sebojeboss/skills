# Synthetic presenter and scene

## When to read

Use to cast an original synthetic performer, use an approved real-person avatar, prepare a generator request or combine synthetic speech/presentation with real footage.

## How to do the work

Choose the production path from the required evidence and available inputs. Human footage is often the direct route for a precise real product operation. A synthetic presenter can carry an explanation; a real insert can carry the critical handling. Fully generated use footage requires close inspection of identity and physical action. None of these paths automatically supplies a genuine testimonial.

Separate appearance, performance and recording situation. An appearance reference describes the selected face, clothing and silhouette. A guide recording carries speech rhythm and emphasis. A scene specifies where the camera is, who could hold it, what the performer is doing and what the microphone could plausibly capture. Do not assume choosing a voice ID also chooses a reliable delivery or that matching a face also stabilizes a product.

Prepare the minimum sufficient references for the operation:

- Person: selected approved image or licensed/avatar input, appropriate framing, visible hands where needed and clean boundaries. Avoid embedded captions or reference grids unless the mode explicitly expects them.
- Product: actual views that expose the relevant geometry, label and operating parts. Record which characteristics must remain unchanged; “same product” is too vague to diagnose a changed hinge or cap.
- Scene: camera support and height, light direction, background, object positions and required continuity. A selfie frame cannot quietly become a two-handed overhead demonstration without a planned cut.
- Speech: final intended wording, pronunciation, selected exact audio when using an audio-driven mode, and whether translation is permitted.

Use the provider's supported input roles. A general reference can guide appearance without fixing frame zero. A first frame also fixes composition and may import unwanted hands, padding or text. An end frame constrains the destination, not necessarily the intervening motion. Refer to [action continuity](product-action-and-continuity.md) before selecting a mode to solve a handling problem.

For audio-first work, select and preserve the actual speech take before binding it to a presenter job. Re-synthesizing with the same voice ID can change timing and character. For native speech generation, inspect the actual words and pronunciation before adding captions or cleanup. Do not build a large continuation batch around an unselected anchor unless the existing authorization and creative plan expressly permit that variability.

Write a scene request around observable action: initial state, performer movement, camera behavior and ending. Keep fixed selections together. Avoid piling incompatible directions onto the same shot—handheld movement, both hands occupied and an unbroken frontal close-up may be physically inconsistent. A storyboard communicates coverage and order; it is not necessarily valid generator input or proof that the requested sequence was rendered.

Detectable and impossible are different defects. Some advertisers deliberately run presenters a careful viewer can tell are generated; whether that's acceptable for this brand and audience is the user's call, and sometimes a test's, not an automatic reject. A scene where nobody could be holding the camera, a microphone that vanishes between cuts, or a product that appears in a hand nobody reached with breaks the scene's own logic. Those are defects however real the face looks, and they're what viewers point at when they call a clip fake.

## Worked decisions

Illustrative scenario: an approved presenter explains a reusable bottle, but generated shots change its cap and drinking opening. More facial detail will not solve that defect. Compare a real bottle insert with a new generated handling shot. The real insert sacrifices a continuous synthetic scene but can preserve the actual SKU and action. If no real footage exists, narrow the shot's purpose to an accurate appearance illustration or leave the demonstration incomplete; do not claim success from the presenter alone.

Illustrative alternative: a character sheet contains three panels. Sending the entire sheet to a single-frame mode may reproduce the panel layout. Select the intended image and prepare its crop instead. That loses the simultaneous alternate views, so retain those as separate planning references if supported; inspect the rendered result rather than assuming the mode used them correctly.

## Deliverable and checks

Return a scene plan, approved-input list and tool-specific prepared request. Record installed/access/permission/cost status separately. Use [tools and recovery](tool-adapters-and-recovery.md) to execute only supported operations. Inspect appearance, exact speech, gesture meaning, camera logic and product action in the actual output. Keep a technically completed job separate from a selected take and an accepted deliverable.
