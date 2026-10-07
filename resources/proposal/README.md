# Current editable proposal and synchronized exports

[Open the Hebrew Google Docs proposal](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0)

Google Docs remains authoritative. The Word/PDF files here are native exports updated on 7 October 2026, with the rover web app concept and corrected architecture diagram. They preserve the live cover, goal/problem, tables, algorithms, component allocation, tests and AI section.

Architecture: motion ESP; onboard Raspberry Pi; separate ESP CAM S3; one core USB 2D LiDAR; left/right ToF, encoders, IMU, two bumpers and four edge sensors. Operator phone/laptop access the Pi web app. Home PC runs Clef-Flash Q8_0 for asynchronous advisory image analysis via planned authenticated HTTPS internet exchange. Hardware models, integration and school acceptance remain open.

[Web app concept](../design/webapp-rover-concept.png) depicts the initial planar map/path, camera frame, map-linked events, pending AI review, manual/autonomous controls and sensor status. Example data are labelled; no implemented behavior or safety clearance is implied.

[Current block diagram](../diagrams/current-proposal-block-diagram.png) matches the live written allocation. It replaces an embedded historical diagram that still mentioned simulated cleaning. Historical tldraw exports and the board are preserved separately; they are not the current architecture reference.

The supplied [Hebrew writing skill](../../skills/yotam-hebrew-writing/SKILL.md) applies to captions and prose. Referenced style-evidence files were not supplied. The older generator is disabled so it cannot overwrite native exports with stale architecture. Export from Google Docs instead.
