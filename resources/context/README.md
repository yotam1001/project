# Current project context: exploration rover

Updated 7 October 2026 after reading the live [Hebrew Google Docs proposal](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0). The live document is authoritative for proposal content; repository notes and exports are synchronized references. Read this file and engineering-plan.md before future project work, and fetch the latest repository and live document before editing.

## Current goal and scope

Pair project, 5 units, examination code 841589. The current document title is “רכב רובוטי לסריקה, מיפוי ותיעוד מפגעים באזורים מסוכנים”. It describes remote information collection for rescue and inspection, with an actual prototype demonstration restricted to a controlled test arena. The goal and problem statement have now been filled in the live document; do not restore earlier blank placeholders.

Initial milestone: autonomous planar driving, obstacle avoidance, initial 2D mapping, estimated rover position/path, and browser operation from phone or laptop. Event images are associated with estimated map locations and reviewed through advisory AI. There is no cleaning in the active project. Full SLAM, complete exploration, 3D reconstruction and elevation mapping are not current commitments. Edge sensing provides local stopping, not a height map or proof of real-cave suitability.

## Current hardware and ownership

- Motion ESP: motor feedback/control, encoder/IMU and side-distance measurements, immediate local stop, stale-command checks.
- Onboard Raspberry Pi: USB 2D LiDAR, position estimation, mapping/navigation, receiving and storing camera imagery, events, web backend and asynchronous AI requests.
- Separate ESP CAM S3: capture and WiFi image transfer to Pi. It is distinct from the motion ESP; the old generic camera-attached-to-Pi description is superseded.
- Core sensor plan: one 2D LiDAR, two ToF sensors at left and right, one IMU, two encoder motors, two front/rear bumper sensors and four edge sensors near chassis corners. LiDAR, right-side ToF, bumper and edge sensors are now core planned components, not optional.
- Operator laptop and phone: browsers for operation/testing. Laptop does not run rover mapping/navigation in the current plan.
- Home PC: local Cloudflare Clef-Flash Q8_0 image inference. Hardware suitability has been checked by the user; model integration, latency and project-image performance are not yet measured.
- Battery-voltage and motor-current monitoring remain optional.

## Data flow and AI

Motion ESP and Pi: UART over USB serial. Suitable sensors: I2C and digital inputs. LiDAR to Pi: USB. ESP CAM S3 to Pi: WiFi. Browser to Pi: WiFi/WebSocket. Pi sends images/event data over authenticated HTTPS through the internet to the home-PC inference service and receives decisions. Networking is planned and still requires implementation and testing; local phone access alone is not the IoT internet-exchange requirement.

AI returns scores for predefined choices, not free-form explanations or verified human-safety probabilities. Initial categories: blocked passage, obstacle in path, narrow opening, inadequate image. UI outcomes: possible hazard, no hazard detected, unknown; pending and failed requests stay distinct. Navigation and local stopping do not wait for AI. See ai-model.md and proposal-ai-section.md.

## Planned verification and open decisions

Current document targets: five collision-free trials, stop within one second of command loss, mean position error at most 30 cm in a small arena. These are planned acceptance targets, not achieved results. Models, calibration, budget, test-arena dimensions, capture triggers and network deployment details still need implementation decisions.

Supervisor acceptance of complete independently functioning school subsystems remains open; processor count alone does not establish compliance. Each needs input/display, appropriate sensors and outputs, and two accepted communication protocols. Both students must understand the whole project.

The live cover now includes school, student and supervisor names. Missing student IDs/coordinator details and the full proposal deadline still need checking against the template. Around the 15th means proposal submission only; no month/date confirmation is inferred.

## School requirements and history

The original uploaded school references and extracted text remain unchanged. Current circular: תשפ״ז, especially pp. 15–25. Pair projects require communicating subsystems and at least one controller's internet data exchange. Proposal requires cover, abstract, need, explained block diagram, component list and one PDF; the examiner submission date is 30 October of the school year. Prototype, measurements, logs, photographs/video, project book and documented AI assistance are required later.

The cleaning project is retained only in ../archive/cleaning-concept-2026-10-05/. Older dated reviews and diagrams are historical; consult the current live document before reusing them. The supplied Hebrew writing skill is in ../../skills/yotam-hebrew-writing/; its referenced style-evidence files were not supplied.

## Visual and export synchronization, 7 October 2026
The regenerated rover web app concept is embedded in the Google Doc with a Hebrew caption and example-data qualification. An old embedded diagram still referred to simulated cleaning; it was replaced with the current sensor/camera/home-PC architecture. Historical tldraw assets and the external board remain historical rather than silently altered. Word/PDF copies are exported directly from the live document.
