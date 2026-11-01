# FlowForge viva study pack

Start with the [printable master guide](../../output/pdf/FlowForge-Viva-Master-Guide.pdf) or its [searchable Markdown edition](FlowForge-Master-Guide.md). It explains the project from beginner web concepts through architecture, actual implementation, OOP, syntax, libraries, alternatives, security, tests, and a 100-question viva bank.

Use the [complete line-by-line companion](FlowForge-Line-by-Line.md) to study the original numbered source and an explanation for every line across 71 application/test/configuration files. Its file fingerprints identify the snapshot. It deliberately excludes actual environment files, secrets, databases, dependency-generated source, and private logs.

For a short preparation window, read master chapters 2-7, 10-13, 17-20, then the demonstration and rapid revision in chapters 24-27. For source reading, start with Event, the three ABC contracts, runtime Workflow, engine, factories, service, and API routes before the frontend/integrations.

The report describes 31 October 2026 repository behavior. It distinguishes current code from older design/phase documents and does not claim current production health. No application behavior, authentication code, database schema, deployment, or secret configuration was changed.

Verification: 28 backend tests passed with one warning; the frontend build including TypeScript passed; lint completed with one React effect warning. Live browser/provider/deployment checks were not performed. PDF layout and source annotation coverage are validated as part of producing the study pack.

The documentation helper [build_study_materials.py](resources/build_study_materials.py) regenerates the appendix, coverage manifest, and PDF using Python with reportlab/pypdf and Windows Segoe UI/Consolas fonts. Critical-line notes describe this snapshot; review/update them if application lines change. [source-coverage.json](resources/source-coverage.json) records exact coverage; [build-results.json](resources/build-results.json) records generated sizes/counts.
