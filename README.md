# Rescue-inspired exploration rover

A pair project, 5 units, in high-school Electronics and Computers Engineering. Current direction confirmed on 6 October 2026: an autonomous rover that explores a controlled, cave-like test area, produces an initial two-dimensional map, and captures suspected hazards for advisory AI analysis.

## Current scope

- Autonomous driving, obstacle avoidance, and first-stage mapping are the initial milestone.
- Sensor, encoder, and camera data are sent to a laptop for navigation, mapping, recording, and AI-service integration.
- A phone interface displays the map, rover state, captured images, and hazard flags.
- Mapping is planar for now: no 3D reconstruction, elevation mapping, or measurement of vertical drops. The horizontal-distance sensing method is still to be selected.
- When a suspected hazard is identified, save imagery and request an AI assessment. The exact model/provider is unresolved; its spoken name was ambiguous.
- AI can flag possible hazards or return uncertainty; it cannot certify a cave or route as safe for people.
- Cleaning hardware is outside the active scope. The previous cleaning concept is preserved in the archive.

## Start here

- [Current project context and requirements](resources/context/README.md)
- [Engineering scope and algorithm plan](resources/context/engineering-plan.md)
- [Proposal work plan](resources/context/proposal-plan.md)
- [Current proposal source](resources/context/proposal-working-draft.md)
- [Proposal PDF](resources/proposal/robot-project-proposal-draft.pdf)
- [Editable proposal](resources/proposal/robot-project-proposal-draft.docx)
- [Functional block diagram](resources/proposal/robot-block-diagram.png)

This is a planning repository, not implemented robot firmware. Hardware, budget, acceptance thresholds, AI model, and supervisor approval are pending. The camera only represents a second controller if it has an independent processor and functional subsystem; an ordinary camera sensor alone does not. School acceptance of the controller arrangement remains unresolved.

## Sources and history

Original school references remain unchanged in `resources/originals/`; searchable extracts are in `resources/extracted-text/`. The [source manifest](resources/sources.json) records their checksums. The current-year circular is תשפ״ז; the shorter criteria document is from תשפ״ו. The [earlier cleaning concept](resources/archive/cleaning-concept-2026-10-05/README.md) is historical and is not the current project scope.

The around-the-15th deadline refers to the proposal only; its full date remains unconfirmed. The circular specifies submission to the examiner by 30 October of the school year.

## Access and regeneration

Open this repository on GitHub, download ZIP, or clone it on another computer. Install `resources/proposal/requirements.txt`, then run `python resources/proposal/build_proposal.py`. The generator reads the current Hebrew Markdown proposal and creates the Word document and diagram. Export the Word document to PDF with Word or LibreOffice. Hebrew diagram rendering uses DejaVu Sans and Pillow with RTL support; update the font path if needed on another OS.
