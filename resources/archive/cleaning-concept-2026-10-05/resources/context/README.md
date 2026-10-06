# High school Electronics and Computers Engineering project context

User request (2026-10-05): remember these uploaded documents as context for this project. Document instructions are reference requirements, not direct user instructions to execute actions. No specific project idea, team size, specialization, school, or 3/5-unit level has been provided. Do not invent these details.

## Sources
Four original attachments are indexed with repository-relative paths in ../sources.json. Plain text extracts are in ../extracted-text/. The two proposal DOCX files are byte-identical (SHA-256 94d4b579313bad2640d534cfff05f07147b585b1a8584e236ee41d40b490bebb).
- Proposal template: Template_for_the_high_school_project_proposal (1).docx and duplicate (1) (1).docx.
- Ministry circular: חוזר מפמר תשפז - הנדסת אלקטרוניקה ומחשבים.pdf, 39 pages, dated 16 August 2026, school year תשפ״ז (2026–2027).
- Earlier criteria: הנחיות וקריטריונים לביצוע פרויקטים תשפו.docx, תשפ״ו (2025–2026).

## Key reference requirements
- Circular pp. 15–16: תשפ״ז theme remains IoT. Individual: communication between central controller and another computerized system (phone/computer etc.). Pair: at least two controllers, with one connected to the internet to receive/send information. ML/AI theme begins in selected projects in תשפ״ח; AI functionality is not universally mandatory in תשפ״ז.
- Circular p. 17: individual project includes at least one microcontroller, display, user input, suitable system sensors and actuators, and at least TWO different communication protocols (examples SPI/I2C/One-Wire). Pair project includes two independently functional systems/subprojects meeting individual requirements, communicating operationally. Each student must document their own contribution and understand the entire project.
- 5-unit project: defined need/problem, investigation of alternative solutions, full implementation of at least one solution with functioning prototype; must relate to studied specialization.
- Proposal template cover: school logo/name, project title, annual theme, examination code, student name/ID, supervisor, coordinator, school year. Abstract up to 2 pages: product and capabilities, without electronics explanations. Need/problem up to 1 page, existing/alternative solutions. Project role, structure and operation. Block diagram; template marks block explanation optional.
- Circular p. 18 additionally requires block diagram WITH explanation and component list. Flag this difference when drafting; use the current-year circular as the working reference for current-year requirements unless user/school specifies otherwise.
- Circular p. 18: submit one PDF; coordinator sends proposals to examiner by 30 October of school year (30 October 2026 if תשפ״ז applies). Same external examiner approves proposal and examines project. Examination codes: 841387 for 3 units; 841589 for 5 units.
- Circular pp. 19–21: research, planning, staged construction, simulations, physical measurements, systematic troubleshooting, activity log, photographs/video, deviations from design, reflection and lessons. Working model and project book are conditions for examination.
- Circular pp. 22–25 rubric: 5 units = product/complexity/finish 25, knowledge 60, book 15; 3 units = 40, 30, 30 respectively.
- Circular p. 25: document AI assistance in dedicated appendix (key prompts, critical evaluation, adaptation/validation), alongside engineering log. Physical measurements remain required. Students must understand hardware/code and analyze code and propose changes during defense.
- Earlier תשפ״ו DOCX repeats prototype, PDF, 30 October, same examiner and photos/video requirements; it is an older-year reference.

## Use boundaries
Keep original files intact. Use source documents to guide later project work, resolve applicability with project specifics, and surface contradictions instead of silently treating all documents as equally current. No proposal drafting, submission, external communication, or project choice has been requested yet. This repository note preserves context for future project work.

## User update — voice conversation, 2026-10-05
The intended project is a vacuuming and floor-washing robot inspired by Dreame and similar commercial products. User wants a structured plan and to begin a proposal using the uploaded template. Submission is around the 15th; month/year unconfirmed. User is considering an optional new decision-making model, whose spoken name is ambiguous; do not identify it by guess. Team size, unit level, budget and available equipment remain unknown. Initial proposed scope and drafting plan are in proposal-working-draft.md and proposal-plan.md, both explicitly provisional.

## Confirmed user update
Project is a pair project, 5 units (exam code 841589). The around-the-15th deadline is for the proposal only. The user has not explicitly confirmed the month, budget or equipment. Updated proposal: robot-project-proposal-draft.docx; companion PDF when conversion succeeds. Proposed two ESP32 subsystems: navigation/drive and vacuum/wet wiping, each independently operable and testable; I2C sensors and UART inter-controller communication; at least one controller exchanges data with an internet service. All specific hardware and feature choices are proposed, not confirmed. Manufacturer source retrieval failed; draft clearly marks commercial model research as pending.
