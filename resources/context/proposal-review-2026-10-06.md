# Proposal review after AI expansion

Reviewed the live Google Doc against the repository context, original proposal template, current-year school circular, and current model documentation. The editable Google Doc remains the authoritative proposal. User edits to component quantities were preserved.

The original AI mention was brief. A dedicated section now explains the model, local home-PC inference, predefined decisions rather than generated explanations, image-projector requirement, camera-event capture, selected-frame requests, map association, phone display, background processing, uncertainty/failure handling, and labelled-scene evaluation. The Hebrew section is also saved in `proposal-ai-section.md` for context.

Other gaps filled: WiFi data/command transport with timestamps and stale-command checks; a distinction between local phone access and a controller's actual internet exchange; filtering/invalid sensor readings; metric range measurement; and sourced TurtleBot3 teleoperation and planar SLAM examples. These examples are comparison references, not a commitment to buy TurtleBot3 or implement full SLAM.

Remaining team/supervisor decisions: exact goal and need, final title and cover details, two-controller/independent-subsystem compliance, hardware models and budget, protocol allocation, internet service, capture triggers/category definitions, test arena, numerical acceptance targets and full proposal deadline. Home-PC hardware suitability has already been checked by the user; project-specific integration and performance remain future implementation work.

The original tldraw Page 1 diagram remains exactly as requested. It still shows Raspberry Pi and simulated cleaning rather than the laptop/camera/AI architecture described by the current text. That mismatch is explicitly identified in the proposal's completion notes; the board has not been changed to resolve it. Final school submission also requires one PDF, while Google Docs remains the editable working format.

All six native-exported pages were rasterized and visually reviewed after the changes. The abstract and need sections still fit on their existing page, and the expanded AI section occupies the sixth page. No prototype operation or AI accuracy is claimed as tested.

Sources:

- https://huggingface.co/Cloudflare/clef-flash
- https://huggingface.co/bartowski/Cloudflare_clef-flash-GGUF
- https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_operation/
- https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/
- Original proposal DOCX and תשפ״ז circular in `resources/originals/`.
