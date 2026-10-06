# Intended AI model — Cloudflare Clef-Flash, Q8_0

Identified after the user’s spoken clarification on 6 October 2026. Intended deployment: locally on the user’s home PC; not installed or benchmarked yet. Camera/controller compliance remains unknown pending the user’s check next week.

## Verified model behavior

[Cloudflare’s model card](https://huggingface.co/Cloudflare/clef-flash) describes a 9B multimodal decision model supporting image/video inputs and a Jev/SystemOne-compatible interface. It scores predefined choices and returns probabilities rather than generating free-form explanations. This supports designing questions about visible blockage, narrow passages, and image adequacy. It is not documented as a cave-hazard detector; performance on our scenes must be evaluated.

## Quantized local distribution

[The GGUF publisher’s model card](https://huggingface.co/bartowski/Cloudflare_clef-flash-GGUF) lists `Cloudflare_clef-flash-Q8_0.gguf` at approximately 9.68 GB, plus a separate multimodal projector for image input. It documents a compatible llama.cpp runtime and the decision-specific `/v1/systemone` endpoint. These are distribution requirements, not proof of successful operation on the user’s PC. File size is not total runtime memory: allow for the projector, input processing, context, and runtime allocations.

## Project integration and pending checks

Use selected recorded frames as input and associate results with the event’s estimated map location. Define possible-hazard/no-hazard-detected/unknown options and separately assess image adequacy. Model probabilities need calibration on labelled test scenes; they are not demonstrated human-safety probabilities. Insufficient imagery, failure, or low-confidence results remain unknown. No output certifies structural stability, air quality, or cave safety.

Confirm the exact distribution/runtime versions, PC RAM and GPU/VRAM, image support, memory use, latency, and false/missed hazard rates before committing to performance targets. Keep AI requests asynchronous so driving and local stopping remain independent. This note records a model choice, not a deployed service.
