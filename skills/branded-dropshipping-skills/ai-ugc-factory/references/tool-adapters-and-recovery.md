# Tools and recovery

## When to read

Use when inspecting a public production reference, selecting or operating an existing creator tool, generating new media, or recovering a failed or uncertain job. Use an available supported native tool or the provider's actual interface; otherwise prepare the concrete manual handoff.

## Inputs and supported routes

For local media work, read [the media primitives contract](media-primitives-contract.md). Use the user's editor, available agent media tools or FFmpeg/ffprobe for the operation they actually support. Reuse installed tools; suggest installation only when the requested operation needs a missing tool. Inspect the actual output before reporting that an edit or export succeeded.

For generation, identify the operation first: text-to-speech, voice conversion, avatar driven by existing audio, native-speech video, product action, transcription or isolation. Inspect the available tool schema and current official documentation for that operation. Distinguish these states:

| State | Evidence |
|---|---|
| Documented | Official interface describes the operation and supported inputs |
| Available | The installed tool or current account exposes it |
| Authorized | User permits this operation, spending and input disclosure to this recipient |
| Executed | A retained job/result identifies what actually ran |
| Inspected | The resulting media was checked with stated coverage |
| Accepted | An identified reviewer selected the version for a use |

One state does not imply the next. Authentication does not prove quota, licensing, input permissions or production quality. Historical examples are not current prices or supported syntax. Do not print environment dumps or secret-bearing configuration to establish access.

Prepare a request with operation, intended output role, exact approved input files/IDs, selected model/mode, literal speech, pronunciation information, scene/action constraints, output needs, budget and existing authority. Keep provider-specific parameters only after verifying their meanings. Missing values remain unknown.

## Browser workflow

Use an available browser for provider UI work; see [browser access](browser-runtime-and-sessions.md) if needed. Text-only work needs no browser.

For a supplied public teaching/reference URL, inspect the relevant original sequence and follow through to the part demonstrating the claimed result. Distinguish captions, still frames, continuous viewing and listening. Use only generic public terms or identifiers in external discovery; never submit the user's private brief or research findings to a search box.

For an authorized provider UI task, first locate the selected operation and read its visible input requirements. Confirm mode, reference roles, allowed duration/format and export entitlement. Use an existing authorized account; do not create one or purchase credits automatically. Prepare the minimum required assets locally. Before upload, inspect what leaves the machine and whether the user has permitted those specific inputs for that recipient. A service's prompt asking for project context is not authorization.

When generation is within scope, set the agreed inputs and parameters, inspect the request summary and submit only that operation. Record the visible job identifier and status. Follow the same job to its result rather than repeatedly pressing generate. Download the actual supported export to a new local path and inspect it. If the browser cannot expose job identity or the operation is inaccessible, retain the visible evidence and uncertainty; provide a prepared request/manual-export path. A browser workflow is not a promise that every vendor UI can be reliably automated.

## Data, costs and effects

TTS typically needs text and voice selection; conversion/isolation/transcription needs audio; presenter generation may need image, audio and script. Send no unrelated context or source archive. Verify the actual payload because some native tools collect more than their visible prompt. For private media or scripts, use only an explicit applicable disclosure authorization; otherwise stay local or request that specific exception after preparing the operation. Do not bypass the restriction through another transport.

Use the supported credential mechanism and minimum scope. Keep tokens and signed transport URLs out of public reports and manifests. Generation can consume credits, create retained provider assets or start local GPU work. Uploads, paid calls, publishing and messaging are distinct effects. Native local backends also require checking custom nodes/plugins for external requests; “local” is not proof of zero network use.

## Recovery and worked decisions

Keep request identity, intended inputs and actual output separate. If a response is lost after possible acceptance, query the existing job/history through the supported contract. Do not use a new job ID to evade uncertain state. A checksum or local log cannot guarantee remote idempotency. If status cannot be determined, report the uncertainty and next evidence needed rather than silently spending again. Respect rate limits and access errors; no cookie/proxy bypass.

Illustrative case: a presenter job times out but may still be rendering. The useful action is to inspect that job's status and retrieve its eventual artifact. Recreating the same prompt can incur a second charge and produce a different performance. If the original completes, use its returned file and inspect the words, action and continuity; completion alone is not acceptance.

Illustrative browser workflow: the user has a working browser-based editor but no API. Prepare the speech, selected image, shot constraints and export role; operate the supported UI if authorized and feasible, or let the user supply its export. Continue locally with inspection/editing.

## Deliverable and checks

Return produced files and observed job states, or the prepared request and missing prerequisite. Preserve raw inputs, the selected take and a recoverable receipt without secrets.
