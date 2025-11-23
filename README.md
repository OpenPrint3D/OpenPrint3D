# OpenPrint3D — An Open, Slicer-Independent Profile Format

OpenPrint3D is an open proposal for standardizing printer, filament, and process profiles in a simple, neutral JSON format.
It’s designed to make 3D-printing configurations easier to share, easier to maintain, and easier for tools or slicers to import — without replacing or competing with existing slicers.

This project began independently before the announcement of Prusa’s OpenPrintTag, but the two efforts are naturally complementary:
OpenPrintTag focuses on spool/tag metadata, while OpenPrint3D focuses on the configuration layer behind those materials.

The goal is a lightweight, community-driven framework that reduces fragmentation and provides a clean, consistent foundation for anyone building slicer tooling, print-farm systems, material libraries, or automation.

OpenPrint3D is currently an early-stage draft (schema v0.1). Feedback, discussion, and contributions are welcome.

# OpenPrint3D Profile Composition

Below is a high-level view of how OpenPrint3D structures configurations.

Each *complete* profile is assembled by combining:

   • A **Printer** definition  
   • A **Filament** definition  
   • A **Process** definition  

These three components map into a slicer's internal configuration model.


<img width="1000" height="900" alt="openprint3d_diagram_large" src="https://github.com/user-attachments/assets/0842e931-c80e-4230-ae13-283568df9497" />

**Key Idea:**  
OpenPrint3D does *not* replace slicers — it provides a clean, neutral, shared
format for describing the *intent* of a printer/filament/process combination.

Slicers can then map these fields into their own internal settings however they choose.
