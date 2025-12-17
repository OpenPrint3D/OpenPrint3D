# Contributing to OpenPrint3D

## Long-term Stewardship & Project Partners

OpenPrint3D is an ambitious standardization effort, and while I initiated the project, I don’t expect to carry it alone.

Due to limited bandwidth (especially during treatment), I’m actively looking for trusted partners and maintainers who can help drive the project forward and represent the community.

If you’re interested in helping shape the long-term governance of the project, please reach out or open a discussion thread.

## How to Contribute 

Thank you for your interest in contributing!  
OpenPrint3D is an early-stage, community-driven project that defines open, slicer-independent formats for:

- **Printer** profiles  
- **Filament** profiles  
- **Process** profiles  

To keep contributions consistent and interoperable, please follow the guidelines below.

---

## 📁 Repository Structure

```text
filament/          → Filament profile instances
printer/           → Printer profile instances
process/           → Process profile instances
profile-templates/ → Profile template files
schema/            → JSON Schema definitions (printer, filament, process)
tools/             → Validation and development helpers
```

✅ 1. Install Dependencies
You only need one Python package (if you don't use [`uv`](https://docs.astral.sh/uv/)):
```bash
pip install jsonschema
```

✅ 2. Validate Before Submitting
Use the provided tool:
```bash
python tools/validate_schema.py schema/<schema-file>.json <your-profile>.json
```

or if you use `uv`
```bash
uv run tools/validate_schema.py schema/<schema-file>.json <your-profile>.json
```

### Examples

Validate a filament profile:
```bash 
python tools/validate_schema.py schema/filament.schema.json filament/Polymaker/PolyLite-PLA.json
```

Validate a printer profile:
```bash
python tools/validate_schema.py schema/printer.schema.json printer/Elegoo/Centauri-Carbon.json
```

Validate a process profile:
```bash
python tools/validate_schema.py schema/process.schema.json process/Standard/0.20mm-quality.json
```

If valid, you’ll see:
```bash
[ OK ] path/to/your-file.json
```
📌 3. Naming and Organization

Please place files in the correct location and follow established naming conventions:

```text
Printer profiles → printer/<Manufacturer>/<Model>.json
Filament profiles → filament/<Brand>/<ProductName>.json
Process profiles → process/<Category>/<Profile>.json
```
Use simple, readable IDs, e.g.:

```text
Elegoo/Centauri-Carbon
Polymaker/PolyLite-PLA
Standard/0.20mm-quality
```

🧩 4. Schema Versioning
Each profile must include:
```text
"op3d_schema_version": "0.1.0"
```

#### Do not change this unless the schema itself is updated and a migration is planned.
Profiles must conform to the version indicated in the schema/ directory.

🏷️ 5. External IDs and Vendor Extensions
You may include external identifiers such as:

```json
"external_ids": {
  "open_print_tag": "opt:polymaker:polylite-pla:white",
  "gtin": "0000000000000"
}
```

Vendor- and slicer-specific extensions belong under dedicated namespaces:

```json
"x_cura": { },
"x_prusaslicer": { },
"x_bambu": { },
"x_orca": { }
```

Do not place slicer-specific fields at the top level.

🤝 6. Pull Request Guidelines
* Validate your JSON before submitting.
* Use consistent indentation (2 or 4 spaces).
* Include a brief PR description explaining your change.
* Validate each profile in multi-file PRs.
* If proposing schema changes, open an Issue first for discussion.

📣 7. Discussion & Collaboration

OpenPrint3D is still evolving.
If you have ideas or improvements for schemas, tooling, workflows, or structure:

➡️ Open an Issue and start a discussion!

We welcome suggestions, debate, and contributions from across the community.

Thank you for helping build an open, shared foundation for 3D-printing profiles!
