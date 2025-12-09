# OpenPrint3D Roadmap

#### A high-level view of planned milestones for delivering an open, vendor-neutral standard for 3D-printing profiles and interoperability.

## Phase 1 — Foundational Schema (Current Focus)

#### Objective: Publish the first stable OpenPrint3D schema for filament, printer, and slicer profiles.

### Miestones

 * Collect community and industry feedback on draft schema.
 * Finalize schema structure, field definitions, and validation rules.
 * Add examples for common printers, filaments, and slicers.
 * Publish complete schema documentation.
 * Tag v1.0 Specification Release.

#### Outcome: A stable foundation for tooling, API integrations, and certification processes.

## Phase 2 — Reference API (v1.x)

#### Objective: Provide a standardized way to access OP3D profiles programmatically.

### Milestones

 * Define the REST API specification aligned with the v1.0 schema.
 * Release an open-source reference server implementation.
 * Document API endpoints, versioning, and usage patterns.
 * Provide a public sandbox/test environment.

#### Outcome: A reliable mechanism for slicers, manufacturers, and tools to fetch OP3D profiles.

## Phase 3 — Example Implementations

#### Objective: Demonstrate how OP3D can be integrated into real workflows.

### Milestones

 * Create example slicer plugin(s) using the reference API.
 * Publish a sample manufacturer integration workflow.
 * Provide conversion tooling for turning existing profiles into OP3D-compliant JSON.
 * Release a simple “OP3D Updater” utility for power users.

#### Outcome: Practical, working integrations that lower friction for adopters.

## Phase 4 — Compatibility & Certification Program

#### Objective: Establish confidence, consistency, and long-term project sustainability.

### Certification Types

 * Profile Certification: Validates filament/printer/slicer profiles against objective criteria.
 * Software Certification: Ensures slicer/API clients follow the OP3D spec.
 * Manufacturer Certification: Confirms accuracy and consistency across published profile sets.

### Milestones

 * Define certification criteria and testing procedures.
 * Build automated validation tooling.
 * Publish certification documentation and workflow.
 * Launch a nominal, accessible fee structure to support OP3D development.
 * Fees go directly to project maintenance and compensating contributors for certification work.

#### Outcome: A trustworthy ecosystem with sustainable funding and high-quality metadata.

## Phase 5 — Long-Term Evolution (Community-Guided)

#### Objective: Enable OP3D to grow with new materials, technologies, and workflows.

### Potential Areas of Expansion
 
  * Resin and composite/fiber-reinforced materials.
  * Printer capability declarations (toolheads, MMUs, thermal envelope, sensors).
  * Profile performance benchmarking requirements.
  * User metadata for multi-material and hybrid manufacturing.
  * Governance processes and long-term maintainer structure.

#### Outcome: A living standard shaped by community, manufacturers, developers, and researchers.

## Guiding Principles

  - *Neutrality:* OpenPrint3D remains vendor-independent.
  - *Practicality:* Solve real-world fragmentation problems without excess complexity.
  - *Transparency:* Open documentation, open process, open governance.
  - *Sustainability:* Funds from certification go directly into project maintenance.
  - *Adoption-First:* Minimize friction for manufacturers, slicers, and community contributors.
