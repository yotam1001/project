# Vacuuming and floor-washing robot project

High-school Electronics and Computers Engineering project: a **pair project, 5 units**, inspired by Dreame and similar cleaning robots.

## Start here

- [Proposal draft — PDF](resources/proposal/robot-project-proposal-draft.pdf)
- [Proposal draft — editable Word document](resources/proposal/robot-project-proposal-draft.docx)
- [Work plan](resources/context/proposal-plan.md)
- [Project context and requirements](resources/context/README.md)
- [Earlier working draft](resources/context/proposal-working-draft.md)
- [Functional block diagram](resources/proposal/robot-block-diagram.png)

The proposal is a working draft. Hardware choices, budget, test environment, commercial-product research, and the optional decision model still need to be finalized. The deadline given is around the 15th **for the proposal only**; the full date has not been confirmed.

## Resource folders

| Folder | Contents |
| --- | --- |
| `resources/originals/` | All four original uploaded documents, unchanged |
| `resources/extracted-text/` | Searchable text extracted from the documents |
| `resources/context/` | Requirements, project decisions, work plan, and working notes |
| `resources/proposal/` | Word/PDF draft, block diagram, previews, and generation script |

[Source manifest](resources/sources.json) records relative paths, file sizes, and checksums. The two uploaded proposal templates are identical; both are retained.

The current-year Ministry circular is for תשפ״ז; the shorter criteria document is for תשפ״ו. Document guidelines are project references and are distinct from the user's requests. The newer circular also requires a component list and an explanation of the block diagram.

## Access from another computer

Open this repository in GitHub to view or download individual files, or choose **Code → Download ZIP** to download all resources. To work with Git:

```sh
git clone https://github.com/yotam1001/project.git
cd project
```

## Regenerate the draft

Use Python 3 and install the dependencies in `resources/proposal/requirements.txt`. The script uses the bundled original template and writes outputs beside itself:

```sh
python -m pip install -r resources/proposal/requirements.txt
python resources/proposal/build_proposal.py
```

The diagram requires DejaVu Sans at `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf` and Pillow with right-to-left text rendering support. On another operating system, update that font path to an installed font supporting Hebrew. To export the Word file to PDF, use Word or LibreOffice. For LibreOffice:

```sh
soffice --headless --convert-to pdf --outdir resources/proposal resources/proposal/robot-project-proposal-draft.docx
```

Generated PDF and Word files are already included; regeneration is optional.
