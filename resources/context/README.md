# Current project context — updated 6 October 2026

## Confirmed direction

The final objective is a functioning pair project at the 5-unit level (examination code 841589). The original vacuuming/wet-wiping concept has been replaced by a rescue-inspired exploration rover. Actual cleaning is excluded from the active scope.

The user wants autonomous driving and first signs of mapping first. The rover is intended to explore narrow, cave-like passages and show a scan/map on a phone. The current prototype will address a controlled planar environment, without 3D reconstruction or vertical terrain/drop assessment. A real cave deployment is not a demonstrated capability.

Data will be streamed to a laptop rather than relying on an onboard Raspberry Pi. The laptop performs higher-level processing. The robot retains local motor control and immediate stopping behavior.

Additional project goal: record imagery whenever a suspected hazard is identified, preserve it, and send it to an AI service for advisory hazard assessment. The exact AI/model name was unclear in speech and must not be guessed. Model outputs are possible-hazard, no-hazard-detected, or unknown assessments, not human safety clearance. Failure to detect a hazard does not establish safety.

## Architecture and compliance status

The user's intended arrangement treats the camera system and ESP controller as two computing subsystems. This is an intended design, not a verified statement of school compliance. A camera module without its own processor is a sensor, not a controller. Select a processor-equipped camera subsystem or another controller as needed and confirm the arrangement with the supervisor.

Proposed separation: ESP motion/encoder subsystem; processor-equipped camera/capture subsystem. Each needs independent test operation, sensor inputs, actuators/outputs, user input/display, and at least two communication protocols as required by the school. Camera capture alone may not meet the complete individual-subproject requirements. The laptop and phone support both systems. Actual operational inter-subsystem communication and at least one controller's internet data exchange must be demonstrated.

## Current-year school references

- Circular pp. 15–16: תשפ״ז theme is IoT. Pair projects need at least two controllers, one exchanging data with the internet. AI is not universally mandatory, though the rubric recommends it as a possible complexity contribution.
- Page 17: two independently functional, communicating systems/subprojects meeting individual requirements. Each includes a controller, display, user input, suitable sensors/actuators, and at least two different communication protocols. Both students must understand the entire project and document individual contributions.
- Page 18: cover, abstract, need/problem, explained block diagram, component list, and one PDF. The current circular requires diagram explanations even though the older template labels them optional. Coordinator submission deadline: 30 October of the school year.
- Pages 19–25: staged construction, measurements, troubleshooting, engineering log, photographs/video, project book, and working prototype. Five-unit grading: product/complexity/finish 25%, knowledge 60%, book 15%. Document AI assistance, evaluate it critically, and validate physical behavior.

## Unresolved details

Budget and equipment; camera hardware/processor; horizontal range sensor and placement; Wi-Fi operating conditions; exact AI provider/model; automatic hazard triggers and dataset; internet service; controller compliance; test arena and numerical acceptance targets; student/school details; full proposal deadline. The deadline around the 15th is for the proposal, not completion of the robot.

## Historical sources

Four originals and extracted texts are retained and indexed in `../sources.json`. The two template uploads are identical. Historical cleaning notes, generator, and outputs are preserved under `../archive/cleaning-concept-2026-10-05/`. They do not override this current context.
