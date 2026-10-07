# Exploration rover — working project

A pair project, 5 units, in high-school Electronics and Computers Engineering. Current technical direction: autonomous driving, initial two-dimensional mapping, and image capture for advisory AI analysis. The live proposal now defines scanning, mapping and documenting possible hazards for rescue/inspection, demonstrated in a controlled test arena.

## Current scope

- Autonomous driving, obstacle avoidance, and first-stage mapping are the initial milestone.
- Current plan: ESP controls motors and local stopping; onboard Raspberry Pi handles camera capture, pose estimation, mapping, navigation, event storage, and the web interface. A laptop is used for operation, development and testing; the home PC hosts AI. The Raspberry Pi model and measured processing rate remain to be selected.
- A phone interface displays the map, rover state, captured images, and hazard flags.
- Mapping is planar for now: no 3D reconstruction, elevation mapping, or measurement of vertical drops. One USB 2D LiDAR is planned for range mapping, with left/right ToF, IMU, bumper/edge sensors and a separate ESP CAM S3 camera.
- When a suspected hazard is identified, save imagery and request an AI assessment. Preferred deployment: a locally hosted image-capable model on the user’s home PC, kept running when needed. The intended model is Cloudflare Clef-Flash, Q8_0, identified from its published model documentation. The user has checked home-PC hardware suitability; runtime integration, latency and project-image evaluation remain future work. See [AI model notes](resources/context/ai-model.md).
- AI can flag possible hazards or return uncertainty; it cannot certify a cave or route as safe for people.
- Cleaning hardware is outside the active scope. The previous cleaning concept is preserved in the archive.

## Editable proposal

The latest Hebrew proposal is an editable [Google Doc](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0). It follows the original school template, uses a redesigned RTL layout and block diagram, and contains the current team goal and problem statement. Repository Word/PDF exports are references; the native Google Doc is the editable source.

## Start here

- [Current project context and requirements](resources/context/README.md)
- [Engineering scope and algorithm plan](resources/context/engineering-plan.md)
- [Proposal work plan](resources/context/proposal-plan.md)
- [Synchronized proposal text](resources/context/proposal-working-draft.md)
- [Current proposal PDF export](resources/proposal/robot-project-proposal-draft.pdf)
- [Current Word proposal export](resources/proposal/robot-project-proposal-draft.docx)
- [Current architecture diagram and historical tldraw assets](resources/diagrams/README.md)
- [Generated web app concept](resources/design/webapp-rover-concept.png)
- [User supplied Hebrew writing skill](skills/yotam-hebrew-writing/README.md)

This is a planning repository, not implemented robot firmware. Hardware models, budget, acceptance thresholds, AI runtime integration and supervisor approval are pending. ESP and Raspberry Pi are the planned processing units. School acceptance still requires independently functioning subsystems and each subsystem’s complete input, display, sensors/actuators and communication requirements.

## Sources and history

Original school references remain unchanged in `resources/originals/`; searchable extracts are in `resources/extracted-text/`. The [source manifest](resources/sources.json) records their checksums. The current-year circular is תשפ״ז; the shorter criteria document is from תשפ״ו. The [earlier cleaning concept](resources/archive/cleaning-concept-2026-10-05/README.md) is historical and is not the current project scope.

The around-the-15th deadline refers to the proposal only; its full date remains unconfirmed. The circular specifies submission to the examiner by 30 October of the school year.

## Access and document updates

Open this repository on GitHub, download ZIP, or clone it on another computer. Edit the linked native Google Doc, then export it as Word/PDF to refresh the reference files. The Markdown is a synchronized text snapshot. The legacy generator is disabled to prevent stale architecture from replacing live edits.

To regenerate the current architecture diagram, install the dependencies in `resources/proposal/requirements.txt` and run `python resources/diagrams/build_current_diagram.py`. The script reuses the handwriting font embedded in the preserved tldraw SVG. The external tldraw board and historical exports remain preserved separately.
